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
