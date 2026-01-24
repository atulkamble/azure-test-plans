## 🧪 **Azure Test Plans – Quick, Clear Guide**

Azure Test Plans is a **test management service inside Azure DevOps** that helps teams **plan, track, and execute manual & exploratory testing**—all tightly integrated with work items and CI/CD.

---

### 🔹 What it’s used for

* **Manual testing** (step-by-step test cases)
* **Exploratory testing** (find issues while using the app)
* **End-to-end test management** linked to requirements & bugs
* **Release readiness** with traceability and reporting

---

### 🔹 Core Components

* **Test Plans** → High-level container for testing a feature/release
* **Test Suites** → Organize test cases (static, requirement-based, query-based)
* **Test Cases** → Steps, expected results, parameters
* **Test Runs** → Execution results (Pass/Fail/Blocked)
* **Bugs** → Auto-created and linked during testing

---

### 🔹 Typical Workflow

1. Create **User Stories / Requirements**
2. Create a **Test Plan**
3. Add **Test Suites**
4. Write **Test Cases**
5. Execute tests → record outcomes
6. Log **Bugs** (linked automatically)
7. Track **Reports & Progress**

---

### 🔹 Key Features

* ✅ Rich **manual test cases** with steps & parameters
* 🧭 **Exploratory testing** with browser extension
* 🔗 **Traceability** (Requirement ↔ Test ↔ Bug)
* 📊 **Dashboards & reports**
* 🤝 Integrates with **Azure Boards, Pipelines, GitHub**

---

### 🔹 Where it fits in DevOps

| Phase      | Tool                 |
| ---------- | -------------------- |
| Planning   | Azure Boards         |
| Code       | Git / GitHub         |
| Build & CI | Azure Pipelines      |
| **Test**   | **Azure Test Plans** |
| Release    | Pipelines / Releases |

---

### 💰 Licensing (important)

* **Not free by default**
* Requires **Azure Test Plans license** or **Visual Studio Enterprise**
* Stakeholders get limited access (no full test execution)

---

### 📌 When to choose Azure Test Plans

* Manual/regression testing heavy projects
* Enterprises needing **audit & traceability**
* Teams already on **Azure DevOps**

---
## ✅ 1️⃣ BASIC **MANUAL TEST CASE** (as written in Azure Test Plan)

```
Test Case: Open Google Homepage

Step 1: Open browser
Expected: Browser opens successfully

Step 2: Go to https://www.google.com
Expected: Google homepage is displayed
```

That’s it. ✔️
(This is exactly how beginners start in Azure Test Plans.)

---

## ✅ 2️⃣ BASIC **AUTOMATION CODE** (Python + Selenium)

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

print("Google opened successfully")

driver.quit()
```

👉 This script:

* Opens Chrome
* Opens Google
* Closes browser

---

## ✅ 3️⃣ **PASS / FAIL LOGIC**

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

if "Google" in driver.title:
    print("TEST PASSED")
else:
    print("TEST FAILED")

driver.quit()
```

---
Below is a **Azure Pipeline** that runs the **same test** and publishes results so you can see them in **Test Plans → Runs → Progress Report**.

---

## 🔹 Azure Pipeline 

### 📄 `azure-pipelines.yml`

```yaml
trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:
- script: |
    pip install selenium pytest
  displayName: Install dependencies

- script: |
    echo "from selenium import webdriver" > test_google.py
    echo "def test_google():" >> test_google.py
    echo "    driver = webdriver.Chrome()" >> test_google.py
    echo "    driver.get('https://www.google.com')" >> test_google.py
    echo "    assert 'Google' in driver.title" >> test_google.py
    echo "    driver.quit()" >> test_google.py
  displayName: Create test

- script: |
    pytest test_google.py --junitxml=results.xml
  displayName: Run test

- task: PublishTestResults@2
  inputs:
    testResultsFiles: results.xml
    testRunTitle: Basic Google Test
```

---

## 🔹 How this shows in **Azure Test Plans**

### ✅ Test Plans

* Create **Test Plan**
* Add **Test Case** (manual)
* Link this pipeline to the test case (optional but recommended)

---

### 📊 Runs

After pipeline runs:

* Go to **Azure DevOps → Test Plans → Runs**
* You will see:

  * **Run Name:** `Basic Google Test`
  * Status: **Passed / Failed**
  * Execution time

---

### 📈 Progress Report

* Go to **Test Plans → Progress Report**
* You’ll see:

  * Total tests
  * Passed / Failed count
  * Execution trend from pipeline runs

---

## 🔹 Flow (ONE LINE)

```
Azure Pipeline → Run Test → Publish Results → Test Plans → Runs → Progress Report
```

---

## 🔹 Interview-friendly explanation (VERY SHORT)

> Azure Pipeline executes automated tests and publishes results, which are tracked in Azure Test Plans under Runs and Progress Reports.

---
