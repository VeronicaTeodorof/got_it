## Manual Testing (MT)


### Authentication 


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| AUTH-MT-01 | Visit /accounts/signup/ | Signup form loads | Signup form loads | Pass | Pass |
| AUTH-MT-02 | Visit /accounts/signin/ | Signin form loads | Signin form loads | Pass | Pass |
| AUTH-MT-03 | Submit signup form without email | Form not submitted, error shown | Form not submitted, prompts to fill out email field | Pass | Pass |
| AUTH-MT-04 | Submit signup form without username | Form not submitted, error shown | Form not submitted, prompts to fill out username field | Pass | Pass |
| AUTH-MT-05 |Submit signup form without password 1 | Form not submitted, error shown | Form not submitted, prompts to fill out password 1 field | Pass | Pass |
| AUTH-MT-06 | Submit signup form without password 2 | Form not sumbitted, error shown | Form not submitted, prompts to fill out password 2 field | Pass | Pass |
| AUTH-MT-07 | Submit signup form with mismatched passwords | Form rejected, error shown | Form rejected, prompts to fill out the same password | Pass | Pass | 
| AUTH-MT-08 | Submit signup form with all valid fields | Account created, redirected to dashboard page | Account created, redirected to dashboard page | Pass | Pass |  
| AUTH-MT-09 | Submit signup form with invalid email format (notanemail) | Form rejected, error shown | Form rejected, user prompted to include "@" | Pass | Pass |  
| AUTH-MT-10 | Submit signup form with password similar to other personal information | Form rejected, error shown | Form rejected, "Password too similar to username" shown | Pass | Pass |
| AUTH-MT-11 | Submit signup form with password too short | Form rejected, error shown | Form rejected, "This password is too short. It must contain at least 8 characters." shown | Pass | Pass |
| AUTH-MT-12 | Submit signup form with password too common | Form rejected, error shown | Form rejected, "This password is too common." shown | Pass | Pass |
| AUTH-MT-13 | Submit signup form with password entirely numeric | Form rejected, error shown | Form rejected, "This password is entirely numeric." shown. | Pass | Pass |
| AUTH-MT-14 | Submit signup form with already registered email address | Form rejected, feedback message shown | Form rejected, "A user with that email already exists" shown | Pass | Pass |
| AUTH-MT-15 | Submit signup form with already registered username | Form rejected, feedback message shown | Form rejected, "A user with that username already exists" shown | Pass | Pass |
| AUTH-MT-16 | Submit signin form with valid credentials | Signed in, redirect to dashboard page | Signed in, redirect to dashboard page | Pass | Pass |
| AUTH-MT-17| Submit signin form with incorrect password | Form rejected, error shown | Form rejected, "The username and/or password you specified are not correct." shown | Pass | Pass |
| AUTH-MT-18 | Submit signin form with unregistered email | Form rejected, error shown | Form rejected, "The username and/or password you specified are not correct." shown | Pass | Pass |
| AUTH-MT-19 | Submit signin form without email | Form rejected, error shown | Form rejected, user prompted to fill out email field | Pass | Pass |
| AUTH-MT-20 | Submit signin form without password | Form rejected, error shown | Form rejected, user prompted to fill out password field | Pass | Pass |
| AUTH-MT-21 | Clicking logout ends the session | Session_id cookie in dev tools application is cleared after clicking logout | Session_id cookie in dev tools application is cleared after clicking logout | Pass | Pass | 
| AUTH-MT-22 | Unlogged users cannot access dashboard page | Writing '/dashboard/' suffix in the url bar redirects to login | Writing '/dashboard/' suffix in the url bar redirects to login| Pass | Pass | 
| AUTH-MT-23 | "Remember me" checkbox is visible on login page | "Remember me" checkbox is visible on login page | "Remember me" checkbox is visible on login page | Pass | Pass |
| AUTH-MT-24 | Remembered users stay logged in between sessions | Closing and reopening the browser loads the dashboard without prompting login | Closing and reopening the browser loads the dashboard without prompting login | Pass | Pass | 
| AUTH-MT-25 | Remembered users are redirected away from login page | Visiting /accounts/login/ with an active remembered session redirects to dashboard | Visiting /accounts/login/ with an active remembered session redirects to dashboard | Pass | Pass |
| AUTH-MT-26 | Non-remembered users are logged out when browser closes | Closing and reopening the browser redirects to login | Closing and reopening the browser redirects to login | Pass | Pass |
| AUTH-MT-27 | Session expires after inactivity even with Remember Me checked | User is redirected to login after session duration expires | Not tested - relies on Django default session expiry behaviour (SESSION_COOKIE_AGE = 1209600) | - | - |
| AUTH-MT-28 | User can manually log out ends session regardless of Remember Me | Clicking logout with Remember Me checked ends the session, redirects to login, and attempting to access /dashboard/ redirects to login | Clicking logout with Remember Me checked ends the session, redirects to login, and attempting to access /dashboard/ redirects to login | Pass | Pass |
| AUTH-MT-29 |  After signing out and being redirected to signin page, visit /dashboard/ | Login form loads with empty fields and no reference to previous user | Flash message reveals who was signed in | Pass | Pass |
| AUTH-MT-30 | Successful signup redirects to dashboard page | User is redirected to dashboard page after successful signup | As expected | Pass | Pass |
| AUTH-MT-31 | Clicking logout redirects to home page | User is redirected to home page after clicking logout | As expected | Pass | Pass |
| AUTH-MT-32 | After logout, pressing browser back button does not show dashboard | Login page or home page loads (not dashboard) | Browser displays cached dashboard page | Pass | Pass |

### Home Page 


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| HP-MT-01 | Logged-out user visits home page | Sign In and Sign Up links visible in navbar, no Dashboard link or Logout button | As expected | Pass | |
| HP-MT-02 | Sign Up link navigates to signup page | Sign Up form loads | As expected | Pass | Pass | 
| HP-MT-03 | Sign In link navigates to signin page | Sign In form loads | As expected | Pass | Pass |
| HP-MT-04 | Logged-in user visits home page | Dashboard link and Logout button visible in navbar, no Sign In and Sign Up links| As expected | Pass | Pass |


### Dashboard Page


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| DP-MT-01 | Dashboard page displays correctly with Logout link | Logout link present on dashboard page | Logout link present on dashboard page | Pass | Pass |


### Sign Up Page 


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
|SUP-MT-01 | Home link navigates to home page | Home page loads | As expected | Pass | Pass |
|SUP-MT-02 | Sign In link navigates to Sing In page | Sign In page loads | As expected | Pass | Pass|
|SUP-MT-03 | Sign Up link reloads Sing Up page | Sign Up page reloads | As expected | Pass | Pass |
|SUP-MT-04 | Sign In link in paragraph navigates to Sing In page | Sign In page loads | As expected | Pass | Pass |


### Sign In Page 


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
|SIN-MT-01 | Home link navigates to home page | Home page loads | As expected | Pass | Pass|
|SIN-MT-02 | Sign Up link navigates to Sing Up page | Sign Up page loads | As expected | Pass | Pass|
|SIN-MT-03 | Sign In link reloads Sing In page | Sign In page reloads | As expected | Pass | Pass |
|SIN-MT-04 | Sign Up link in paragraph navigates to Sing Up page | Sign Up page loads | As expected | Pass | Pass |


### Responsiveness

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| RES-MT-01 | Navbar on mobile | Burger menu shows, links hidden | As expected | Pass | Pass |
| RES-MT-02 | Clicking burger on mobile | Links expand below navbar | As expected | Pass | Pass |
| RES-MT-03 | Navbar on desktop | All links visible, no burger | As expected | Pass | Pass |
| RES-MT-04 | No horizontal scrolling on any screen size | Page fits within screen width on all devices | As expected | Pass | Pass |


## Automated Testing (AT)


### Home Page


| Test ID | Test | Covers | Result |
|---------|------|----------|-------|
| HP-AT-01 | test_home_page_loads | Home page returns 200 | Pass |


### Sign Up Page

| Test ID | Test | Covers | Result |
|---------|------|----------|-------|
| SUP-AT-01 | test_signup_page_loads | Signup page returns 200 | Pass |
| SUP-AT-02 | test_signup_page_contains_signin_link | Signup page contains link to signin | Pass |


### Sign In Page

| Test ID | Test | Covers | Result |
|---------|------|----------|-------|
| SIN-AT-01 | test_signin_page_loads | Signin page returns 200 | Pass |
| SIN-AT-02 | test_signin_page_contains_signin_link | Signin page contains link to signin | Pass |


## Known Bugs


## Solved Bugs
### AUTH - Dashboard accessible via browser back button after logout (AUTH-MT-32)

**Description:** After logging out and being redirected to the home page, pressing the browser's back button displays the dashboard as if the user is still logged in. This is caused by the browser serving a cached version of the page without re-validating with the server, bypassing Django's session authentication check.  

**Fix:** Add cache-control headers to the dashboard view to prevent the browser from caching the page.  

**Commit:** `c9dd47c`


### AUTH - Username disclosed after signout (AUTH-MT-29)

**Description:** After signing out and visiting `/dashboard/`, the login page displayed a flash message revealing the previous user's username("Successfully signed in as vteodorof"). The email field also appeared pre-filled, however testing in an incognito window confirmed this was browser autofill, not a backend issue. The flash message persisted in incognito, confirming it originates from Django/allauth.  
**Also observed:** The same flash message leak occurs when navigating back after logout via the browser back button (AUTH-MT-32). Fixing AUTH-MT-32 with `@never_cache` exposed this behaviour on back navigation as well.

**Evidence:** 
[MT31 - Username disclosed after signout](testing_screenshots/auth-mt-29.png)

**Fix:** Tests on deplyed version didn't show the above bug.

**Commit:** `abc1234`
