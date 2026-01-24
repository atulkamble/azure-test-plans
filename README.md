# 🧪 Azure Test Plans - Selenium Test Automation

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://dev.azure.com)
[![Tests](https://img.shields.io/badge/tests-automated-blue.svg)](https://dev.azure.com)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)

Automated Selenium testing with Azure DevOps Pipelines integrated with **Azure Test Plans** for comprehensive test management, reporting, and tracking.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [Pipeline Configuration](#pipeline-configuration)
- [Azure Test Plans Integration](#azure-test-plans-integration)
- [Test Management](#test-management)
- [Progress Reports & Runs](#progress-reports--runs)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

This project demonstrates:
- **Automated Selenium tests** running in Azure Pipelines
- **Headless Chrome** execution in CI/CD environment
- **Azure Test Plans integration** for test result tracking
- **HTML and JUnit reports** generation
- **Screenshot capture** on test failures
- **pytest fixtures and markers** for organized test execution

### What is Azure Test Plans?

Azure Test Plans is a **test management service inside Azure DevOps** that helps teams **plan, track, and execute both manual & automated testing**—all tightly integrated with work items and CI/CD.

#### Key Uses:
* ✅ **Manual testing** (step-by-step test cases)
* 🧭 **Exploratory testing** (find issues while using the app)
* 🤖 **Automated test tracking** (CI/CD integration)
* 🔗 **End-to-end test management** linked to requirements & bugs
* 📊 **Release readiness** with traceability and reporting

---

## ✨ Features

### Pipeline Features
- ✅ Headless Chrome with Selenium WebDriver
- ✅ pytest framework with fixtures and markers
- ✅ Automatic screenshot capture on test failure
- ✅ HTML and XML test reports
- ✅ Azure Test Plans integration
- ✅ Build artifact publishing

### Test Management Features
- 📊 **Test Plans** → High-level container for testing a feature/release
- 📁 **Test Suites** → Organize test cases (static, requirement-based, query-based)
- 📝 **Test Cases** → Steps, expected results, parameters
- ▶️ **Test Runs** → Execution results (Pass/Fail/Blocked)
- 🐛 **Bugs** → Auto-created and linked during testing

---

## 🚀 Quick Start

### Prerequisites

- Azure DevOps account and project
- GitHub repository connected to Azure Pipelines
- Basic understanding of pytest and Selenium

### Local Development Setup

```bash
# Clone the repository

git clone https://github.com/atulkamble/Azure-Test-Plans.git
cd Azure-Test-Plans

# Install dependencies
pip install selenium pytest pytest-html pytest-metadata

# Install ChromeDriver (macOS)
brew install chromedriver

# Run tests locally
pytest test_google.py -v --html=report.html --self-contained-html
```

---

## ⚙️ Pipeline Configuration

### Pipeline Structure

```yaml
trigger:
- main

pool:
  vmImage: ubuntu-latest

variables:
  testRunTitle: 'Selenium Tests - Build $(Build.BuildNumber)'
  pythonVersion: '3.12'

steps:
  - Python version setup
  - Install dependencies (selenium, pytest, pytest-html)
  - Install Chrome & ChromeDriver
  - Create enhanced test suite
  - Run tests with JUnit and HTML reporting
  - Publish test results to Azure Test Plans
  - Publish HTML report as build artifact
```

### Key Pipeline Tasks

#### 1. **Test Execution**
```yaml
- script: |
    pytest test_google.py \
      --junitxml=results.xml \
      --html=test-report.html \
      --self-contained-html \
      -v \
      --tb=short \
      --maxfail=3
  displayName: 'Run Selenium Tests'
```

#### 2. **Publish to Azure Test Plans**
```yaml
- task: PublishTestResults@2
  inputs:
    testResultsFormat: 'JUnit'
    testResultsFiles: '**/results.xml'
    testRunTitle: '$(testRunTitle)'
    failTaskOnFailedTests: true
    publishRunAttachments: true
```

#### 3. **Publish HTML Report**
```yaml
- task: PublishBuildArtifacts@1
  inputs:
    PathtoPublish: 'test-report.html'
    ArtifactName: 'test-html-report'
```

---

## 📊 Azure Test Plans Integration

### Accessing Test Results

Your test results are automatically published to Azure Test Plans:

```
https://dev.azure.com/{organization}/{project}/_TestManagement/Runs
```

### Test Run Details

Each pipeline execution creates a Test Run containing:
- **Summary**: Pass/fail statistics, duration
- **Test Results**: Individual test case results
- **Attachments**: XML results, HTML reports
- **Build Info**: Associated build, commit, branch
- **Timeline**: Execution timestamps

### Viewing Test Runs

1. Navigate to **Azure DevOps** → Your Project
2. Click **Test Plans** in the left sidebar
3. Select **Runs** tab
4. Click on your test run (e.g., "Selenium Tests - Build 12")

You'll see:
- ✅ **Passed tests** with duration
- ❌ **Failed tests** with error details
- 📎 **Attachments** (screenshots, logs)
- 🔗 **Associated work items**

---

## 📈 Test Management

### Creating Test Plans

#### Step 1: Create a Test Plan
```
Test Plans → + New Test Plan
  Name: "Selenium Automated Tests"
  Area Path: YourProject
  Iteration: Sprint 1
```

#### Step 2: Add Test Suites
```
Select Test Plan → + New Suite
  Types:
    - Static Suite: Manual collection
    - Requirement-based: Linked to user stories
    - Query-based: Dynamic based on queries
```

#### Step 3: Link Automated Tests
Your automated tests are automatically linked when published via the pipeline.

### Test Case Management

#### Manual Test Cases
```
Select Test Suite → + New Test Case
  Title: "Verify Google Homepage Title"
  Steps:
    1. Navigate to https://www.google.com
    2. Verify page loads successfully
    3. Verify title contains "Google"
  Expected Result: Title should contain "Google"
  Priority: 1 - High
  Tags: smoke, regression
```

#### Automated Test Metadata

The pipeline creates tests with markers:
```python
@pytest.mark.smoke
@pytest.mark.priority_high
def test_google_homepage_title(driver):
    """Verify Google homepage title contains 'Google'"""
    driver.get('https://www.google.com')
    assert 'Google' in driver.title
```

---

## 📊 Progress Reports & Runs

### Built-in Reports

#### 1. Test Result Trend
- **Path**: Test Plans → Runs → Analytics
- **Shows**: Pass/fail trends over time
- **Useful for**: Identifying test stability

#### 2. Test Execution Chart
- **Path**: Test Plans → Charts
- **Shows**: Execution progress
- **Metrics**:
  - Total tests
  - Passed (%)
  - Failed (%)
  - Blocked
  - Not Run

#### 3. Test Status Report
- **Custom charts** showing:
  - Pass rate percentage
  - Test duration trends
  - Failure categories

### Creating Custom Charts

```
Test Plans → Charts → + New Chart
  Chart Type: Line, Bar, Pie, etc.
  Group By: Outcome, Priority, Test Suite
  Filters: Date range, Build
  OK
```

### Test Run Metrics

| Metric | Description | Location |
|--------|-------------|----------|
| **Pass Rate** | % of tests passing | Runs → Summary |
| **Test Duration** | Time per test | Test Results tab |
| **Flaky Tests** | Inconsistent results | Runs → Analytics |
| **Trend Analysis** | Historical pass/fail | Charts |
| **Bug Discovery** | Bugs found per run | Work Items |

### Accessing Your Test Runs

**Direct URL Format:**
```
https://dev.azure.com/{organization}/{project}/_TestManagement/Runs?runId={runId}&_a=runCharts
```

**Example from your pipeline:**
```
https://dev.azure.com/atul-kamble/project/_TestManagement/Runs?runId=12&_a=runCharts
```

---

## 🎯 Best Practices

### 1. Test Organization
```python
# Use pytest markers for categorization
@pytest.mark.smoke      # Quick smoke tests
@pytest.mark.regression # Full regression suite
@pytest.mark.priority_high
@pytest.mark.priority_medium
```

### 2. Fixture Management
```python
@pytest.fixture
def driver(request):
    # Setup
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    # Teardown with screenshot on failure
    if request.node.rep_call.failed:
        driver.save_screenshot(f"{request.node.name}.png")
    driver.quit()
```

### 3. Descriptive Test Names
```python
# Good: Descriptive and clear
def test_google_homepage_loads_successfully():
    pass

# Bad: Vague
def test_1():
    pass
```

### 4. Pipeline Optimization
- Run smoke tests on every commit
- Run full regression suite nightly
- Use parallel execution for large test suites
- Cache dependencies to speed up builds

### 5. Test Data Management
- Use pytest parametrize for multiple test data
- Store test data in separate files
- Use environment variables for sensitive data

---

## 🔍 Troubleshooting

### Common Issues

#### Chrome Session Failed
**Error**: `SessionNotCreatedException: Chrome instance exited`

**Solution**: Ensure all Chrome options are set:
```python
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
```

#### Tests Not Appearing in Test Plans
**Solution**: Verify PublishTestResults@2 task is configured:
```yaml
- task: PublishTestResults@2
  inputs:
    testResultsFormat: 'JUnit'
    testResultsFiles: '**/results.xml'
    testRunTitle: 'Your Test Run Title'
```

#### Screenshots Not Captured
**Solution**: Ensure directory permissions and use absolute paths:
```python
screenshot_path = os.path.abspath(f"screenshot_{timestamp}.png")
driver.save_screenshot(screenshot_path)
```

#### HTML Report Not Generated
**Solution**: Install pytest-html plugin:
```bash
pip install pytest-html
pytest --html=report.html --self-contained-html
```

---

## 📱 Dashboard & Notifications

### Setting Up Dashboards

```
Overview → Dashboards → + New Dashboard
  Add Widgets:
    - Test Results Trend
    - Test Runs
    - Requirements Quality
    - Build History
    - Query Tile (for custom queries)
```

### Email Notifications

```
Project Settings → Notifications → + New Subscription
  Select: "A test run is completed"
  Recipients: Team members or groups
  Filter: All runs or Failed runs only
  Delivery: Email or Service hooks
```

---

## 🔗 Integration with Azure Boards

### Linking Tests to Work Items

1. Tests automatically link to builds
2. Failed tests can create bugs
3. Bugs link back to test runs
4. Traceability: Requirement → Test → Bug

### Bug Creation from Failed Tests

```
Test Plans → Runs → Select Failed Test → Create Bug
  Auto-filled:
    - Test name
    - Error details
    - Build number
    - Commit SHA
    - Screenshots (if attached)
```

### Workflow Integration

1. **Plan**: Create User Stories in Azure Boards
2. **Develop**: Write code and tests
3. **Build**: Pipeline runs automatically
4. **Test**: Results published to Test Plans
5. **Track**: Monitor via dashboards
6. **Fix**: Create bugs for failures
7. **Verify**: Re-run tests to validate fixes

---

## 📚 Additional Resources

### Documentation
- [Azure Test Plans Documentation](https://learn.microsoft.com/en-us/azure/devops/test/)
- [Azure Pipelines Documentation](https://learn.microsoft.com/en-us/azure/devops/pipelines/)
- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
- [pytest Documentation](https://docs.pytest.org/)

### Useful Links
- [Azure DevOps REST API](https://learn.microsoft.com/en-us/rest/api/azure/devops/)
- [pytest Plugins](https://docs.pytest.org/en/stable/reference/plugin_list.html)
- [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)
- [Selenium WebDriver Best Practices](https://www.selenium.dev/documentation/test_practices/)

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Add tests for new features
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Atul Kamble**
- GitHub: [@atulkamble](https://github.com/atulkamble)
- Azure DevOps: [Project Link](https://dev.azure.com/atul-kamble/project)

---

## 🎓 Complete Testing Workflow

### 1. Planning Phase
```
Azure Boards:
  - Create User Story: "User can search Google"
  - Add Acceptance Criteria
  - Assign to Sprint
```

### 2. Development Phase
```
Code:
  - Write test cases (TDD approach)
  - Implement functionality
  - Run tests locally
  
Git:
  - Commit changes
  - Push to feature branch
  - Create pull request
```

### 3. Build & Test Phase
```
Azure Pipelines:
  - Triggers automatically on PR
  - Runs all tests
  - Publishes results to Test Plans
  - Generates HTML reports
```

### 4. Review Phase
```
Azure Test Plans:
  - Review test results
  - Check pass/fail trends
  - Analyze failures
  - Create bugs if needed
```

### 5. Monitoring Phase
```
Dashboards:
  - Track test metrics
  - Monitor build health
  - Review code coverage
  - Identify flaky tests
```

---

## 🔹 DevOps Integration Overview

| Phase | Tool | Purpose |
|-------|------|---------|
| **Plan** | Azure Boards | User stories, backlog |
| **Develop** | GitHub/Azure Repos | Source control |
| **Build** | Azure Pipelines | CI/CD automation |
| **Test** | Azure Test Plans | Test management |
| **Monitor** | Azure Dashboards | Metrics & insights |
| **Deploy** | Azure Pipelines | Release management |

---

## 📊 Key Metrics to Track

### Quality Metrics
- **Test Pass Rate**: Target >95%
- **Code Coverage**: Target >80%
- **Mean Time to Detection (MTTD)**: Time to find bugs
- **Mean Time to Resolution (MTTR)**: Time to fix bugs

### Performance Metrics
- **Build Duration**: Pipeline execution time
- **Test Duration**: Individual test execution time
- **Deployment Frequency**: How often code is deployed
- **Failure Rate**: % of failed deployments

---

## ⚡ Quick Reference

### Pipeline Commands
```bash
# Trigger pipeline manually
az pipelines run --name "Azure-Test-Plans-CI"

# List recent runs
az pipelines runs list --pipeline-ids <id>

# Download test results
az pipelines runs artifact download --run-id <id>
```

### pytest Commands
```bash
# Run all tests
pytest

# Run with markers
pytest -m smoke

# Run specific test
pytest test_google.py::test_google_homepage_title

# Generate HTML report
pytest --html=report.html --self-contained-html

# Run with verbose output
pytest -v -s

# Stop after first failure
pytest -x
```

---

**Last Updated**: January 2026 | **Version**: 1.0.0
