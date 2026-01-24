# Azure Test Plans Setup Guide

## Current Status
✅ Automated tests running successfully via Azure Pipelines  
✅ Test results being published (Run IDs: 12, 13, 14, 15)  
❌ No Test Plan created yet

## Step 1: View Your Test Runs

Navigate to: `https://dev.azure.com/atul-kamble/project/_TestManagement/Runs`

You should see your recent test runs from the pipeline.

## Step 2: Create a Test Plan

### Option A: Via Azure DevOps Web UI

1. Go to `https://dev.azure.com/atul-kamble/project/_testPlans`

2. Click **"+ New Test Plan"**

3. Fill in details:
   - **Name**: `Selenium Automation Test Plan`
   - **Area Path**: `project`
   - **Iteration**: `project`

4. Click **Create**

### Option B: Create Test Plan with Test Suites

1. Navigate to Test Plans: `https://dev.azure.com/atul-kamble/project/_testPlans`

2. Create New Test Plan:
   - Name: `Selenium Web Tests`
   - Description: `Automated Selenium tests for Google homepage validation`

3. Add Test Suite:
   - Click on your test plan
   - Click **"+ New Suite"** → **"Static suite"**
   - Name: `Smoke Tests`

4. Add Test Cases:
   - Click **"+ New Test Case"**
   - Title: `Verify Google Homepage Title`
   - Steps:
     1. Navigate to https://www.google.com
     2. Verify page title contains "Google"
   - Save

   - Click **"+ New Test Case"**
   - Title: `Verify Google Homepage Loads`
   - Steps:
     1. Navigate to https://www.google.com
     2. Verify URL is https://www.google.com/
   - Save

## Step 3: Link Automated Tests to Test Cases

1. Open each test case

2. Go to **"Associated Automation"** tab

3. Click **"Add Automated Test"**

4. Search for:
   - `test_google_homepage_title` (for first test case)
   - `test_google_homepage_loaded` (for second test case)

## Step 4: View Progress Reports

After linking, you can view progress at:
- Progress Report: `https://dev.azure.com/atul-kamble/project/_testManagement/analytics/progressreport`
- Test Runs: `https://dev.azure.com/atul-kamble/project/_TestManagement/Runs`

## Step 5: Run Tests via Test Plan (Optional)

You can trigger pipeline runs from Test Plans:

1. Go to your Test Plan
2. Select test cases
3. Click **"Run for web application"**
4. This can trigger your pipeline

## Understanding Test Plans vs Test Runs

### Test Runs (What you have now)
- Automatic execution of tests via pipeline
- Published results appear in Runs section
- Shows pass/fail status and execution time
- Not organized into test plans

### Test Plans (What you need to create)
- Manual organization of test cases
- Groups tests into suites
- Provides progress tracking
- Links manual and automated tests
- Shows test coverage and trends

## Quick Commands for CI/CD

Your current pipeline already publishes results correctly:

```yaml
- task: PublishTestResults@2
  inputs:
    testResultsFormat: 'JUnit'
    testResultsFiles: '**/results.xml'
    testRunTitle: 'Selenium Tests - Build $(Build.BuildNumber)'
    mergeTestResults: true
    failTaskOnFailedTests: true
```

## Viewing Results

### Test Runs Page
Direct link to your runs:
```
https://dev.azure.com/atul-kamble/project/_TestManagement/Runs?runId=15&_a=runCharts
```

Replace `runId=15` with the latest run number from your pipeline logs.

### Tests Tab in Pipeline
```
https://dev.azure.com/atul-kamble/project/_build/results?buildId=255&view=ms.vss-test-web.build-test-results-tab
```

Replace `buildId=255` with your current build ID.

## Creating Test Plans via REST API (Advanced)

```bash
# Set variables
ORG="atul-kamble"
PROJECT="project"
PAT="your-personal-access-token"

# Create Test Plan
curl -X POST \
  "https://dev.azure.com/${ORG}/${PROJECT}/_apis/testplan/plans?api-version=7.1-preview.1" \
  -H "Content-Type: application/json" \
  -H "Authorization: Basic $(echo -n :${PAT} | base64)" \
  -d '{
    "name": "Selenium Automation Tests",
    "areaPath": "project",
    "iteration": "project"
  }'
```

## Troubleshooting

### Issue: "No test plans found"
**Solution**: You need to manually create a Test Plan first (Step 2 above)

### Issue: Test runs not showing
**Solution**: Check the correct URL with capital letters:
- ❌ Wrong: `/_testManagement/runs`
- ✅ Correct: `/_TestManagement/Runs`

### Issue: Cannot associate automated tests
**Solution**: Ensure:
1. Test has `@pytest.mark` decorators
2. Pipeline publishes test results
3. Build agent can access test assemblies

## Next Steps

1. ✅ Create a Test Plan named "Selenium Automation Tests"
2. ✅ Add Test Suites for organizing tests (Smoke, Regression, etc.)
3. ✅ Create Test Cases matching your automated tests
4. ✅ Link automated tests to test cases
5. ✅ Run pipeline and verify results appear in Test Plan
6. ✅ Set up Test Plans dashboards and charts

## Resources

- [Azure Test Plans Documentation](https://learn.microsoft.com/en-us/azure/devops/test/overview)
- [Associate Automated Tests](https://learn.microsoft.com/en-us/azure/devops/test/associate-automated-test-with-test-case)
- [Test Plans REST API](https://learn.microsoft.com/en-us/rest/api/azure/devops/testplan)
