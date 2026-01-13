## 🚀 Azure Test Plans – End-to-End Project

![Image](https://learn.microsoft.com/en-us/azure/devops/test/media/overview/test-authoring.png?view=azure-devops)

![Image](https://learn.microsoft.com/en-us/azure/devops/test/media/overview/intro-test-plans.png?view=azure-devops)

![Image](https://www.c-sharpcorner.com/article/how-to-create-and-execute-test-plan-test-suite-in-azure-devops/Images/Picture7.png)

![Image](https://www.c-sharpcorner.com/article/how-to-create-and-execute-test-plan-test-suite-in-azure-devops/Images/Picture1.png)

---

## 🧩 Project Overview

**Project Name:** `azure-test-plans-demo`
**Tool:** Azure DevOps
**Service Used:** Azure Test Plans (Manual + Exploratory Testing)
**Application Under Test (AUT):** Sample Web App (Login + Dashboard)

---

## 🎯 Project Objectives

* Create **Test Plans, Test Suites & Test Cases**
* Execute **Manual Tests**
* Track **Bugs & Test Results**
* Integrate **Automation (Selenium + Azure Pipelines)**
* Generate **Test Reports**

---

## 🏗️ Architecture Flow

```
Developer Code
     ↓
Azure Repos / GitHub
     ↓
Azure Pipelines (CI)
     ↓
Build & Deploy App
     ↓
Azure Test Plans
     ↓
Manual / Automated Tests
     ↓
Bugs + Reports
```

---

## 📁 Repository Structure

```
azure-test-plans-demo/
│
├── app/
│   └── index.html
│
├── test-automation/
│   ├── selenium-login-test.py
│   └── requirements.txt
│
├── pipelines/
│   └── azure-pipelines.yml
│
├── test-cases/
│   └── Login_Test_Cases.md
│
└── README.md
```

---

## 🔧 Step-by-Step Implementation

---

## 1️⃣ Create Azure DevOps Project

```text
Organization  → New Project
Project Name  → Azure-Test-Plans-Demo
Visibility    → Private
```

---

## 2️⃣ Enable Azure Test Plans

```
Project Settings → Billing → Select Test Plans
```

> 💡 **Azure Test Plans requires a paid extension or trial**

---

## 3️⃣ Create Test Plan

```
Test Plans → New Test Plan
```

| Field     | Value                   |
| --------- | ----------------------- |
| Name      | Login Feature Test Plan |
| Area Path | Azure-Test-Plans-Demo   |
| Iteration | Sprint 1                |

---

## 4️⃣ Create Test Suites

```
Test Plan
 ├── Requirement-based Suite
 ├── Static Test Suite
 └── Query-based Suite
```

### Example

```
Login Test Suite
 ├── Valid Login
 ├── Invalid Login
 └── Edge Cases
```

---

## 5️⃣ Create Manual Test Cases

### 📄 Sample Test Case

| Field             | Value                               |
| ----------------- | ----------------------------------- |
| Title             | Verify login with valid credentials |
| Priority          | 1                                   |
| Assigned To       | Tester                              |
| Automation Status | Not Automated                       |

### 🔹 Test Steps

| Step | Action               | Expected Result     |
| ---- | -------------------- | ------------------- |
| 1    | Open login page      | Page loads          |
| 2    | Enter valid username | Username accepted   |
| 3    | Enter valid password | Password accepted   |
| 4    | Click Login          | Dashboard displayed |

---

## 6️⃣ Execute Test Cases

```
Test Plans → Execute → Run Tests
```

| Status  | Meaning          |
| ------- | ---------------- |
| Pass    | Test succeeded   |
| Fail    | Bug created      |
| Blocked | Dependency issue |

> 🐞 **Fail → Automatically create Bug Work Item**

---

## 7️⃣ Bug Linking (Auto)

Bug is linked with:

* Test Case
* Test Step
* Build
* Assigned Tester

---

## 🤖 Automation Integration (Selenium)

### 📌 Selenium Test (Python)

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:8080")

driver.find_element("id","username").send_keys("admin")
driver.find_element("id","password").send_keys("admin123")
driver.find_element("id","login").click()

assert "Dashboard" in driver.title
driver.quit()
```

---

## ⚙️ Azure Pipeline (Automation + Reporting)

```yaml
trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '3.x'

- script: |
    pip install selenium pytest
    pytest test-automation/
  displayName: 'Run Selenium Tests'

- task: PublishTestResults@2
  inputs:
    testResultsFiles: '**/TEST-*.xml'
    testRunTitle: 'Automated UI Tests'
```

---

## 📊 Test Reporting

| Report          | Location          |
| --------------- | ----------------- |
| Test Runs       | Test Plans → Runs |
| Pass/Fail Trend | Dashboards        |
| Bug Metrics     | Boards → Queries  |

---

## 🧪 Exploratory Testing (Optional)

```
Azure Test & Feedback Extension
 → Record session
 → Capture screenshots
 → File bugs instantly
```

---

## 🔐 Best Practices

✅ Use **Requirement-Based Suites**
✅ Link **Test Cases ↔ User Stories**
✅ Combine **Manual + Automated**
✅ Run tests **per Sprint**
✅ Track **Defect Leakage**

---

## 🎓 Real-World Use Cases

| Scenario       | Why Azure Test Plans |
| -------------- | -------------------- |
| Agile Teams    | Sprint-wise testing  |
| Regulated Apps | Test traceability    |
| Enterprise QA  | Manual + Automation  |
| DevOps CI/CD   | Pipeline integration |

---

## 📌 Ready-to-Use Repo Names

* `azure-test-plans-demo`
* `azure-devops-test-management`
* `manual-testing-azure-test-plans`
* `selenium-azure-test-plans`

---
