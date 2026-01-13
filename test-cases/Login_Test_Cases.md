# 📋 Login Feature - Test Cases

## Test Plan Information
- **Test Plan Name:** Login Feature Test Plan
- **Area Path:** Azure-Test-Plans-Demo
- **Iteration:** Sprint 1
- **Created Date:** January 13, 2026

---

## Test Suite: Valid Login Scenarios

### TC-001: Verify login with valid credentials

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-001 |
| **Title** | Verify login with valid credentials |
| **Priority** | 1 - High |
| **Test Type** | Functional |
| **Automation Status** | Automated |
| **Assigned To** | QA Team |
| **Tags** | login, positive, smoke |

#### Test Steps

| Step | Action | Expected Result | Status |
|------|--------|----------------|---------|
| 1 | Navigate to application URL | Login page loads successfully | |
| 2 | Enter valid username: "admin" | Username is entered in the field | |
| 3 | Enter valid password: "admin123" | Password is entered and masked | |
| 4 | Click on "Login" button | User is redirected to Dashboard | |
| 5 | Verify Dashboard page | Dashboard displays with welcome message "Welcome, admin!" | |
| 6 | Verify page title | Page title shows "Dashboard - Azure Test Plans Demo" | |

#### Pre-conditions
- Application is deployed and accessible
- Test user credentials are available

#### Post-conditions
- User is logged in successfully
- Session is created

---

## Test Suite: Invalid Login Scenarios

### TC-002: Verify login with invalid credentials

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-002 |
| **Title** | Verify login with invalid credentials |
| **Priority** | 1 - High |
| **Test Type** | Functional |
| **Automation Status** | Automated |
| **Assigned To** | QA Team |
| **Tags** | login, negative, security |

#### Test Steps

| Step | Action | Expected Result | Status |
|------|--------|----------------|---------|
| 1 | Navigate to application URL | Login page loads successfully | |
| 2 | Enter invalid username: "user" | Username is entered in the field | |
| 3 | Enter invalid password: "wrongpass" | Password is entered and masked | |
| 4 | Click on "Login" button | Login fails, error message displayed | |
| 5 | Verify error message | "Invalid username or password" message is shown | |
| 6 | Verify page state | User remains on login page | |

#### Pre-conditions
- Application is deployed and accessible

#### Post-conditions
- User is not logged in
- No session is created

---

### TC-003: Verify login with empty username

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-003 |
| **Title** | Verify login with empty username |
| **Priority** | 2 - Medium |
| **Test Type** | Functional |
| **Automation Status** | Automated |
| **Assigned To** | QA Team |
| **Tags** | login, negative, validation |

#### Test Steps

| Step | Action | Expected Result | Status |
|------|--------|----------------|---------|
| 1 | Navigate to application URL | Login page loads successfully | |
| 2 | Leave username field empty | Username field is empty | |
| 3 | Enter valid password: "admin123" | Password is entered and masked | |
| 4 | Click on "Login" button | Browser validation prevents form submission | |
| 5 | Verify validation message | "Please fill out this field" or similar message appears | |

#### Pre-conditions
- Application is deployed and accessible

#### Post-conditions
- Form validation prevents submission
- User remains on login page

---

### TC-004: Verify login with empty password

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-004 |
| **Title** | Verify login with empty password |
| **Priority** | 2 - Medium |
| **Test Type** | Functional |
| **Automation Status** | Automated |
| **Assigned To** | QA Team |
| **Tags** | login, negative, validation |

#### Test Steps

| Step | Action | Expected Result | Status |
|------|--------|----------------|---------|
| 1 | Navigate to application URL | Login page loads successfully | |
| 2 | Enter valid username: "admin" | Username is entered in the field | |
| 3 | Leave password field empty | Password field is empty | |
| 4 | Click on "Login" button | Browser validation prevents form submission | |
| 5 | Verify validation message | "Please fill out this field" or similar message appears | |

#### Pre-conditions
- Application is deployed and accessible

#### Post-conditions
- Form validation prevents submission
- User remains on login page

---

### TC-005: Verify login with both fields empty

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-005 |
| **Title** | Verify login with both fields empty |
| **Priority** | 2 - Medium |
| **Test Type** | Functional |
| **Automation Status** | Automated |
| **Assigned To** | QA Team |
| **Tags** | login, negative, validation |

#### Test Steps

| Step | Action | Expected Result | Status |
|------|--------|----------------|---------|
| 1 | Navigate to application URL | Login page loads successfully | |
| 2 | Leave username field empty | Username field is empty | |
| 3 | Leave password field empty | Password field is empty | |
| 4 | Click on "Login" button | Browser validation prevents form submission | |
| 5 | Verify validation message | Validation message appears for username field | |

---

## Test Suite: Logout Scenarios

### TC-006: Verify logout functionality

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-006 |
| **Title** | Verify logout functionality |
| **Priority** | 1 - High |
| **Test Type** | Functional |
| **Automation Status** | Automated |
| **Assigned To** | QA Team |
| **Tags** | logout, positive |

#### Test Steps

| Step | Action | Expected Result | Status |
|------|--------|----------------|---------|
| 1 | Login with valid credentials | User is logged in and on Dashboard | |
| 2 | Click on "Logout" button | User is redirected to login page | |
| 3 | Verify login page | Login page is displayed | |
| 4 | Verify form fields | Username and password fields are empty | |
| 5 | Verify page title | Page title shows "Login - Azure Test Plans Demo" | |
| 6 | Try to access dashboard directly | User is not able to access without login | |

#### Pre-conditions
- User is logged in

#### Post-conditions
- User is logged out
- Session is destroyed
- Form fields are cleared

---

## Test Suite: UI/UX Scenarios

### TC-007: Verify login page UI elements

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-007 |
| **Title** | Verify login page UI elements |
| **Priority** | 3 - Low |
| **Test Type** | UI/UX |
| **Automation Status** | Manual |
| **Assigned To** | QA Team |
| **Tags** | ui, visual |

#### Test Steps

| Step | Action | Expected Result | Status |
|------|--------|----------------|---------|
| 1 | Navigate to application URL | Login page loads successfully | |
| 2 | Verify page header | "🚀 Azure Test Plans" and "Demo Application" are visible | |
| 3 | Verify username field | Field is visible with label "Username" | |
| 4 | Verify password field | Field is visible with label "Password" and input is masked | |
| 5 | Verify login button | Button is visible with text "Login" | |
| 6 | Verify test credentials section | Test credentials box is visible with sample credentials | |
| 7 | Verify visual design | Page has gradient background and styled form | |

---

### TC-008: Verify dashboard UI elements

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-008 |
| **Title** | Verify dashboard UI elements |
| **Priority** | 3 - Low |
| **Test Type** | UI/UX |
| **Automation Status** | Manual |
| **Assigned To** | QA Team |
| **Tags** | ui, visual, dashboard |

#### Test Steps

| Step | Action | Expected Result | Status |
|------|--------|----------------|---------|
| 1 | Login with valid credentials | Dashboard page loads | |
| 2 | Verify page header | "📊 Dashboard" is visible | |
| 3 | Verify welcome message | "Welcome, admin!" is displayed | |
| 4 | Verify Test Plans card | Card shows "Test Plans" with count "12" | |
| 5 | Verify Test Cases card | Card shows "Test Cases" with count "48" | |
| 6 | Verify Passed card | Card shows "Passed" with count "42" | |
| 7 | Verify Failed card | Card shows "Failed" with count "6" | |
| 8 | Verify logout button | Logout button is visible and clickable | |

---

## Test Suite: Security Scenarios

### TC-009: Verify password masking

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-009 |
| **Title** | Verify password masking |
| **Priority** | 1 - High |
| **Test Type** | Security |
| **Automation Status** | Manual |
| **Assigned To** | Security Team |
| **Tags** | security, password |

#### Test Steps

| Step | Action | Expected Result | Status |
|------|--------|----------------|---------|
| 1 | Navigate to login page | Login page loads | |
| 2 | Enter text in password field | Text is displayed as dots/asterisks | |
| 3 | Inspect password field in browser | Password field type is "password" | |
| 4 | Check if password is visible in source | Password is not visible in page source | |

---

## Test Suite: Responsive Design

### TC-010: Verify responsive design on mobile

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-010 |
| **Title** | Verify responsive design on mobile |
| **Priority** | 2 - Medium |
| **Test Type** | UI/UX |
| **Automation Status** | Manual |
| **Assigned To** | QA Team |
| **Tags** | responsive, mobile |

#### Test Steps

| Step | Action | Expected Result | Status |
|------|--------|----------------|---------|
| 1 | Open application on mobile device | Page loads properly | |
| 2 | Verify form container | Form is centered and properly sized | |
| 3 | Verify input fields | Fields are properly sized for touch input | |
| 4 | Verify buttons | Buttons are large enough for touch | |
| 5 | Test login functionality | Login works on mobile | |
| 6 | Verify dashboard on mobile | Dashboard cards display properly | |

---

## Test Execution Summary Template

| Metric | Value |
|--------|-------|
| **Total Test Cases** | 10 |
| **Automated** | 6 |
| **Manual** | 4 |
| **High Priority** | 4 |
| **Medium Priority** | 4 |
| **Low Priority** | 2 |

---

## Bug Report Template

### Bug: [Bug Title]

| Field | Value |
|-------|-------|
| **Bug ID** | BUG-XXX |
| **Severity** | Critical / High / Medium / Low |
| **Priority** | 1 / 2 / 3 / 4 |
| **Status** | New / Active / Resolved / Closed |
| **Found In** | Test Case ID |
| **Environment** | Browser, OS, Version |
| **Assigned To** | Developer Name |

#### Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

#### Expected Result
[What should happen]

#### Actual Result
[What actually happened]

#### Screenshots/Logs
[Attach evidence]

---

## Notes for Testers

### Test Data
- **Valid Username:** admin
- **Valid Password:** admin123
- **Invalid Username:** user
- **Invalid Password:** wrongpass

### Test Environment
- **Local:** http://localhost:8080
- **Test Server:** [To be configured]

### Browser Compatibility
- ✅ Chrome (Latest)
- ✅ Firefox (Latest)
- ✅ Safari (Latest)
- ✅ Edge (Latest)

### Test Execution Schedule
- **Sprint 1:** Week 1-2
- **Regression Testing:** Every Sprint
- **Smoke Testing:** After each deployment

---
