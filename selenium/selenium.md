# 🔹 Selenium Basics (Python)

## 1️⃣ Install Selenium

```bash
pip install selenium
```

Download **ChromeDriver** (match your Chrome version)
➡️ [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
Keep it in PATH or same folder as script.

---

## 2️⃣ First Selenium Script (Open Browser)

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("chromedriver")   # path if needed
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
time.sleep(5)

driver.quit()
```

👉 **Practice:**

* Change URL to `https://example.com`
* Increase/decrease sleep time

---

## 3️⃣ Locate Elements (MOST IMPORTANT)

### 🔹 By ID

```python
driver.find_element(By.ID, "username")
```

### 🔹 By Name

```python
driver.find_element(By.NAME, "q")
```

### 🔹 By XPath

```python
driver.find_element(By.XPATH, "//input[@name='q']")
```

### 🔹 By CSS Selector

```python
driver.find_element(By.CSS_SELECTOR, "input[name='q']")
```

---

## 4️⃣ Send Keys & Click

### 🔹 Google Search Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

search = driver.find_element(By.NAME, "q")
search.send_keys("Selenium Python")
search.submit()

time.sleep(5)
driver.quit()
```

👉 **Practice:**

* Change search text
* Replace `submit()` with Enter key

---

## 5️⃣ Click Button / Link

```python
driver.find_element(By.LINK_TEXT, "Images").click()
```

OR

```python
driver.find_element(By.XPATH, "//a[text()='Images']").click()
```

---

## 6️⃣ Get Page Title & URL

```python
print(driver.title)
print(driver.current_url)
```

---

## 7️⃣ Handle Waits (IMPORTANT)

### 🔹 Implicit Wait (Global)

```python
driver.implicitly_wait(10)
```

### 🔹 Explicit Wait

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
```

---

## 8️⃣ Handle Input Form (Login Example)

```python
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
```

---

## 9️⃣ Handle Alerts

```python
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
```

---

## 🔟 Handle Dropdown

```python
from selenium.webdriver.support.ui import Select

dropdown = Select(driver.find_element(By.ID, "dropdown"))
dropdown.select_by_visible_text("Option 1")
```

---

# 🧪 PRACTICE TASKS (DO THESE)

### ✅ Task 1

Open Google → Search **"Azure DevOps Selenium"**

---

### ✅ Task 2

Open:

```
https://the-internet.herokuapp.com/
```

Click:

* Form Authentication
* Login using valid credentials

---

### ✅ Task 3

Open:

```
https://the-internet.herokuapp.com/dropdown
```

Select **Option 2**

---

### ✅ Task 4

Open:

```
https://the-internet.herokuapp.com/javascript_alerts
```

* Click JS Alert
* Accept alert
* Print alert text

---

### ✅ Task 5

Print:

* Page title
* Current URL

---

# 🔹 Interview-Ready Points (Remember)

* Selenium automates **real browsers**
* Needs **browser driver**
* XPath is most powerful locator
* Prefer **explicit waits**
* Selenium ≠ performance testing
* Mostly used with **pytest / unittest / CI**

---
