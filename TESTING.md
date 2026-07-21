## Manual Testing (MT)

### Base

| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| BASE-MT-01 | Favicon and static assets load correctly | Favicon displays in browser tab; no 404s in console for static files | As expected | Pass | |
| BASE-MT-02 | Navbar remains fixed at top of viewport when scrolling | Navbar stays visible/sticky at top of page as user scrolls down | Fails — navbar scrolls with content instead of pinning. Confirmed on mobile and desktop, Chrome/Edge, devtools emulation. See Known Bugs: Sticky top bug | Fail | |


### Navigation

#### Main Navigation

| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| MNAV-MT-01 | Logo image loads and links to home page | Logo displays correctly in navbar; clicking logo navigates to home page | As expected | Pass | |
| MNAV-MT-02 | "Home" nav link navigates to home page | Home page | As expected | Pass | |
| MNAV-MT-03 | Dashboard link visible for authenticated user | Dashboard link appears in navbar when user is logged in | As expected | Pass | |
| MNAV-MT-04 | Dashboard link hidden for unauthenticated user | Dashboard link does not appear in navbar when user is logged out | As expected | Pass | |
| MNAV-MT-05 | Clicking "Dashboard" link navigates to dashboard page | Dashboard page loads | As expected | Pass | |
| MNAV-MT-06 | Logout button visible for authenticated user | Logout button appears in navbar when user is logged in | As expected | Pass | |
| MNAV-MT-07 | Logout button hidden for unauthenticated user | Logout button does not appear in navbar when user is logged out | As expected | Pass | |
| MNAV-MT-08 | Clicking Logout redirects to home page | User is redirected to home page after logging out | As expected | Pass | |
| MNAV-MT-09 | Sign In and Sign Up links visible for unauthenticated user | Sign In and Sign Up links appear in navbar when user is logged out | As expected | Pass | |
| MNAV-MT-10 | Sign In and Sign Up links hidden for authenticated user | Sign In and Sign Up links do not appear in navbar when user is logged in | As expected | Pass | |
| MNAV-MT-11 | Clicking "Sign In" link navigates to sign in page | Sign in page loads | As expected | Pass | |
| MNAV-MT-12 | Clicking "Sign Up" link navigates to sign up page | Sign up page loads | As expected | Pass | |


#### Secondary/Content Navigation


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| SNAV-MT-01 | Back link displays with icon and 'Change or add source' on source detail page | Back link appears with icon and appropriate descriptive text | As expected | Pass | |
| SNAV-MT-02 | Tapping icon or 'Change or add source' link | Navigates to dashboard | As expected | Pass | |


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
| AUTH-MT-33 | Logged in success message | Message does not appear after successful log in | As expected | Pass | |
| AUTH-MT-34 | Logged out success message | Message does not appear after successful log out | As expected | Pass | |


### Actions Menu

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|-------|-------|------------|
| AM-MT-01 | Click dropdown button | Expands dropdown menu | As expected | Pass |

### Home Page


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| HP-MT-01 | Tagline present on home page | Tagline present on home page | As expected | Pass | |
| HP-MT-02 | How it works diagram and text | Diagram and text present on home page | As expected | Pass | |
| HP-MT-03 | Primary CTA | Get started button present on home page | As expected | Pass | |
| HP-MT-04 | Click 'Get started' link | Navigates to Sign up page | As expected | Pass | |
| HP-MT-05 | Footer attribution and links | Attribution and links present on page footer | As expected | Pass | |
| HP-MT-06 | Click GitHub link | Opens correct GitHub page in a new tab | As expected | Pass | |
| HP-MT-07 | Click LinkedIn link | Opens correct LinkedIn page in a new tab | As expected | Pass | |


### Dashboard Page

### Access Control


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| DP-MT-01 | Unauthenticated user visits /dashboard/ | Redirected to login page | As expected | Pass | |
| DP-MT-02 | Authenticated user visits /dashboard/ | Dashboard page loads | As expected | Pass | |


### Sources List


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| DP-MT-03 | Sources list or empty state present on dashboard | Page shows a list of sources belonging to the logged in user or empty state | As expected | Pass | |
| DP-MT-04 | Each source displays name, type, author and date created | All four fields visible for each source | As expected |Pass | |
| DP-MT-05 | Sources are displayed in reverse chronological order | Sources are displayed in reverse chronological order | As expected | Pass | |
| DP-MT-06 | Empty state shown when no sources exist | Empty state shown when no sources exist | As expected | Pass | |


### Create Source


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| DP-MT-07 | User can enter a source name and a source author | User can enter a source name and a source author | As expected | Pass | |
| DP-MT-08 | User should select a source type from the available options | User should select a source type from the available options | Pass | |
| DP-MT-09 | Name field cannot be empty — error shown if submitted blank | Name field cannot be empty — error shown if submitted blank | As expected | Pass | |
| DP-MT-10 | Source type has to be selected - error shown if not selected | Source type has to be selected - error shown if not selected | As expected | Pass | |
| DP-MT-11 | On successful creation user is redirected to the new source detail page | On successful creation user is redirected to the new source detail page | Pass | |
| DP-MT-12 | Duplicate name error | Submitting a source with an already existing name returns a form error | Raises Integrity Error | Pass | |
| DP-MT-13 | Expandable form | When create source button is clicked, form expands/collapses | As expected | Pass| |


### Edit Source

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| DP-MT-14 | Unauthenticated user navigates directly to edit URL | Visiting /sources/9/edit/ redirects to login page | As expected | Pass | |
| DP-MT-15 | Authenticated user navigates directly to edit URL for another user's source | 404 returned | As expected | Pass | |
| DP-MT-16 | Owner edits source name, author, and type and submits | Changes saved and visible on dashboard page | As expected | Pass | |
| DP-MT-17 | Owner submits edit form with name field empty | Form rejected, error shown | As expected | Pass | |
| DP-MT-18 | Owner submits valid edit form | Redirected to source dashboard page | As expected | Pass | |
| DP-MT-19 | Owner submits edit form with no type selected | Form rejected, error shown | As expected | Pass | |
| DP-MT-20 | Edit button correctly displayed in the dropdown when clicked | Dropdown button displays the edit button when clicked | As expected | Pass |
| DP-MT-21 | Clicking edit button expands edit form | Edit form correctly displayed under source when edit button is clicked | As expected | Pass | |
| DP-MT-22 | Clicking edit button expands only corresponding form, not all forms | Only the form under the targeted source is expanded when edit button is clicked |As expected | Pass | |
| DP-MT-23 | Edit form correctly prepopulated with corresponding data | Edit form displays the correct data in all its fields | As expected | Pass |
| DP-MT-24 | Cancel button on form correctly collapses the form | Form collapses when cancel is clicked | As expected | Pass | |


### Delete Source


| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| DP-MT-25 | Authenticated user visis`sources/<non-existing-source>/delete/`| Authenticated user visits sources/800/delete/ gets 404| As expected | Pass | |
| DP-MT-26 | Authenticated user visits `sources/<existing-source>/delete/` | Authenticated user visits `sources/<existing-source>/delete` is redirected to dashboard | Authenticated user visits existing `sources/22/delete/` is redirected to dashboard | Pass | |
| DP-MT-27 | Unauthenticated user visits `sources/<existing-source>/delete/` | Unauthenticated user visiting `sources/<existing-source>/delete/`is redirected to login page | As expected | Pass | |
| DP-MT-28 | Deleting a source removes it from sources list | Source is removed from sources list after deletion | As expected | Pass | |
| DP-MT-29 | Confirmation is required before deleting | Clicking delete button opens a modal asking user to confirm or cancel deletion | As expected | Pass | |
| DP-MT-30 | Confirmatiion message includes source name and author if present | Confirmation message includes source name and message if present | Pass | |
| DP-MT-31 | Successful deletion message on dashboard after delete | Message present on dashboard after delete | As expected | Pass | |

### Sign Up Page


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| SUP-MT-01 | Home link navigates to home page | Home page loads | As expected | Pass | Pass |
| SUP-MT-02 | Sign In link navigates to Sing In page | Sign In page loads | As expected | Pass | Pass|
| SUP-MT-03 | Sign Up link reloads Sing Up page | Sign Up page reloads | As expected | Pass | Pass |
| SUP-MT-04 | Sign In link in paragraph navigates to Sing In page | Sign In page loads | As expected | Pass | Pass |


### Sign In Page


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| SIN-MT-01 | Home link navigates to home page | Home page loads | As expected | Pass | Pass|
| SIN-MT-02 | Sign Up link navigates to Sing Up page | Sign Up page loads | As expected | Pass | Pass|
| SIN-MT-03 | Sign In link reloads Sing In page | Sign In page reloads | As expected | Pass | Pass |
| SIN-MT-04 | Sign Up link in paragraph navigates to Sing Up page | Sign Up page loads | As expected | Pass | Pass |


### Sources Detail Page


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| SDP-MT-01 | Page accessible to logged in user | Logged in user can access the page showing details of a selected source | As expected | Pass | |
| SDP-MT-02 | Page unavailable to unauthenticated users; redirects to login page | User not logged in trying to access a source_detail page by writing the url in the browser is redirected to login page | As expected | Pass |
| SDP-MT-03 | Page only accessible to the source owner — another logged-in user gets a 404 | User with no sources created visits /sources/10/ gets 404 page | As expected | Pass | |
| SDP-MT-04 | If source does not exist, return 404  | User with ten sources created visits /sources/11/ gets 404 | As expected | Pass | |
| SDP-MT-05 | Source name, author and type displayed | Source name and author displayed | As expected | Pass | |
| SDP-MT-06 | Sources link present in sidebar | Sidebar correctly displays sources link | As expected | Pass | |
| SDP-MT-07 | Empty state | Empty state shown when no unitss exist, encouraging user to create one | As expected | Pass | |
| SDP-MT-08 | All units of a source displayed in list | All units of a source appear in the list | As expected | Pass | |
| SDP-MT-09 | One source does not display another source's units | Only units belonging to current source show in list | As expected | Pass | |


### Create Unit


| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|-------|-------|------------|
| SDP-MT-10 | Create unit button present | Create unit button is present on the page | As expected | Pass | |
| SDP-MT-11 | Clicking create unit button expands form | Create unit form is expanded by clicking Create unit button | As expected | Pass | |
| SDP-MT-12 | Save and cancel buttons present on form | Save and Cancel buttons present on form | As expected | Pass | |
| SDP-MT-13 | Cancel button on Create unit form collapses the form | Cancel button collapses the form | As expected | Pass | |
| SDP-MT-14 | Cancel button on Create unit form resets the form | Cancel button resets the form | As expected | Pass | |
| SDP-MT-15 | User can enter name for a unit | Form has a unit name input and label | As expected | Pass | |
| SDP-MT-16 | Submitting form with blank unit name | Form rejected, error shown | As expected | Pass | |
| SDP-MT-17 | On successful creation user is redirected to unit detail page | On successful creation user is redirected to unit detail page | As expected | Pass | |
| SDP-MT-18 | Duplicate unit names within a source | Form rejected, error shown | As expected | Pass | |
| SDP-MT-19 | Form loaded expanded when errors shown | On page load, form is expanded when it includes error feedback | As expected | Pass | |


### Edit Unit


| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|-------|-------|------------|
| SDP-MT-20 | Edit button present in dropdown on each element in list | Edit button present in dropdown on each element in list | As expected | Pass | |
| SDP-MT-21 | Clicking edit button expands the inline form | Form is expanded when edit button is clicked | As expected | Pass | |
| SDP-MT-22 | Each form is prepopulated with correct data | Form has correct data | As expected | Pass | |
| SDP-MT-23 | User can edit name in form | User can edit name in form | As expected | Pass | |
| SDP-MT-24 | Save and Cancel buttons present on the form | Save and Cancel buttons present on the form | As expected | Pass | |
| SDP-MT-25 | Submitting empty unit name rerenders form with errors | Form rejected, error shown | As expected | Pass | |
| SDP-MT-26 | Valid submission saves edited unit and loads updated list | Valid submission saves edited unit and loads updated list | As expected | Pass | |
| SDP-MT-27 | Cancel button collapses the form | Cancel button collapses the form | As expected | Pass | |
| SDP-MT-28 | Cancel button resets the form | Cancel button resets the form | Reset does not work after invalid submission | Fail | |
| SDP-MT-29 | Submitting the form with duplicate name rerenders form with errors | Form rejected, error shown | As expected | Pass | |


### Delete Unit


| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|-------|-------|------------|
| SDP-MT-30 | Delete button present in dropdown on each element in list | Delete button present in dropdown on each element in list | As expected | Pass | |
| SDP-MT-31 | Clicking delete button opens a confirmation modal | Clicking delete button opens a confirmation modal | As expected | Pass | |
| SDP-MT-32 | Source and unit names included in confirmation modal | Source and unit names included in confirmation modal | As expected | Pass | |
| SDP-MT-33 | Delete and Cancel buttons present on modal | Delete and Cancel buttons present on modal | As expected | Pass | |
| SDP-MT-34 | Delete button rerenders page with deleted unit removed from list | Delete button rerenders page with deleted unit removed from list | As expected | Pass | |
| SDP-MT-35 | Cancel button closes modal | Canncel button closes modal | As expected | Pass | |
| SDP-MT-36 | Authenticated owner typing `sources/<existent_source>/units/<inexistent_unit>/delete/ gets 404 | Authinticated owner typing `sources/<existent_source>/units/<inexistent_unit>/delete gets 404 | As expected | Pass | |
| SDP-MT-37 | Unauthenticated user typing Authinticated owner typing `sources/<existent_source>/units/<existent_unit>/delete/ is redirected to login |
| SDP-MT-38 | Authenticated owner typing `sources/<exostent_source>/units/<existent_unit>/delete/ gets to 'source_detail.html' page | Authenticated owner typing `sources/<exostent_source>/units/<existent_unit>/delete/ gets to 'source_detail.html' page | As expected | Pass | |


### Unit Detail Page


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| UDP-MT-01 | Unit detail page loads with no error | Unit detail page loads with no error for authenticated owner | As expected | Pass | |
| UDP-MT-02 | Unauthenticated user is redirected | Unauthenticated user is redirected when trying to access a unit detail page | As expected | Pass | |
| UDP-MT-03 | Authenticated user cannot access another user's unit detail page | Authenticated user trying to access another user's unit detail page gets 404 | As expected | Pass | |
| UDP-MT-04 | Authenticated user gets 404 for inexistent unit detail page | Authenticated user gets 404 for inexistent unit detail page | As expected | Pass | |
| UDP-MT-05 | Unit name displayed in unit detail page | Unit name correctly appears on unit detail page | As expected | Pass | |
| UDP-MT-06 | Reference, My Words and Questions tabs present on the page | Reference, My Words and Questions tabs present on the page | As expected | Pass | |
| UDP-MT-07 | Clicking Reference tab correctly displays reference notes list | Clicking Reference tab correctly displays reference notes list | As expected | Pass | |
| UDP-MT-08 | Reference note cards correctly display title, content preview and timestamp | Reference note cards correctly display title, content preview and timestamp | As expected | Pass | |
| UDP-MT-09 | Sidebar correctly shows links to the three note types | Sidebar correctly shows links to the three note types | As expected | Pass | |
| UDP-MT-10 | "No reference notes yet" message for empty state | Message appears correctly | As expected | Pass | |


### Reference Detail Page


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| RDP-MT-01 | Reference detail page loads with no error | For authenticated owner reference detail page loads with no error | As expected | Pass | |
| RDP-MT-02 | Page not accessible for unauthenticated users | Unauthenticated user visits 'sources/<existant source>/units/<existant unit>/reference/<existant reference>' - redirected to login | As expected | Pass | |
| RDP-MT-03 | Authenticated user tries to access another user's reference note | Gets 404 | As expected | Pass | |
| RDP-MT-04 | Authenticated user tries to access inexistent reference note | Gets 404 | As expected | Pass | |
| RDP-MT-05 | Title, content and location shown on page | Title, content and location shown on page | As expected | Pass | |
| RDP-MT-06 | Edit icon displayed on page | Edit icon present | As expected | Pass | |
| RDP-MT-07 | Tooltip display | Tooltip displays on hover | As expected | Pass | |
| RDP-MT-08 | Click edit icon | Loads edit detail page | As expected | Pass | |


### Create Reference Page


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| CRP-MT-01 | User clicks `+` Add reference in sidebar | Create Reference Page loads | As expected | Pass | |
| CRP-MT-02 | User clicks `New` link under Reference tab | Create Reference Page loads | As expected | Pass |
| CRP-MT-03 | Unauthenticated user visits `/sources/<existent source>/units/<existent unit>/reference/create/` | Redirected to login | As expected | Pass | |
| CRP-MT-04 | `New` link visible under Reference tab | Link visible | As expected | Pass | |
| CRP-MT-05 | `+` link visible near Reference link in sidebar | Link visible | As expected | Pass | |
| CRP-MT-06 | Authenticated user visits `/sources/<existent source>/units/<existent unit>/reference/create/`  Create Reference Page loads | As expected | Pass | |
| CRP-MT-07 | User can enter title, note and location | Title, note and location fields present on the page | As expected | Pass | |
| CRP-MT-08 | Save form with blank body | Form rejected, error shown | As expected | Pass | |
| CRP-MT-09 | Save button present on page | Save button presetn on page | As expected | Pass | |
| CRP-MT-10 | Form submitted with valid data | Redirects to unit detail page with new reference note showing first in grid | As expected | Pass | |
| CRP-MT-11 | Success message on unit detail page | Successful reference note save prompts success message on unit detail page | As expected | Pass | |


### Edit Reference Page

| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| ERP-MT-01 | Cancel button present on page | Cancel button present on page | As expected | Pass | |
| ERP-MT-02 | Cancel button click | Loads reference detail page | As expected | Pass | |
| ERP-MT-03 | Form is preloaded with correct data | Form is preloaded with correct data | As expected |Pass | |
| ERP-MT-04 | Save with valid data | Redirects to reference detail page | As expected | Pass | |
| ERP-MT-05 | Save with empty content | Form rejected, error shown | As expected | Pass | |




### Responsiveness

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| RES-MT-01 | No horizontal scrolling on any screen size | Page fits within screen width on all devices | As expected | Pass | Pass |


#### Navigation


| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| RES-MT-02 | Navbar container switches from full-width to constrained width at breakpoint | Navbar spans full viewport width on mobile (container-fluid); switches to a constrained, centered container at medium breakpoint and above (container-md) | As expected | Pass | |
| RES-MT-03 | Navbar remains usable at all tested breakpoints | All nav links visible, no overlap or cut-off | As expected | Pass | |
| RES-MT-04 | Sidebar visible by default on desktop | Sidebar displayed as a permanent fixture in the layout | As expected | Pass | |
| RES-MT-05 | Sidebar hidden by default on mobile | Sidebar hidden by default on mobile | As expected | Pass | |
| RES-MT-06 | Toggler visible on mobile, hidden on desktop | Toggler visible on mobile, hidden on desktop | As expected | Pass | |
| RES-MT-07 | On mobile, toggler opens sidebar | Toggler opens sidebar on mobile | As expected | Pass | |
| RES-MT-08 | On mobile, close arrow closes sidebar | Close arrow closes sidebar on mobile | As expected | Pass | |
| RES-MT-09 | Sidebar sits below navbar | Sidebar top edge aligns with bottom of navbar | As expected | Pass | |

#### Home Page


| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| RES-MT-10 | Home page content stacks in single column on mobile | Headline, CTA, diagram, text, and footer stack vertically | As expected | Pass | |
| RES-MT-11 | "How it works" diagram and text display side by side on tablet/desktop | Two-column layout from md breakpoint up | As expected | Pass | |
| RES-MT-12 | "How it works" heading display across breakpoints | Visible above diagram on small sreens (> 768px) and above text on all other screen sizes; no duplicates | As expected | |
| RES-MT-13 | Footer sits at bottom of viewport when content is shorter than screen | Footer pinned to bottom, no gap below it | As expected | Pass | |
| RES-MT-14 | Images/diagram scale without distortion across breakpoints | Diagram resizes proportionally, no overflow or stretching | as expected | Pass | |


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


### Dashboard Page

### Access Control

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| DP-AT-01 | test_authenticated_user_gets_200 | Authenticated user can access sources page | Pass |
| DP-AT-02 | test_unauthenticated_user_is_redirected | Unauthenticated user is redirected to login | Pass |

### Sources List

| DP-AT-03 | test_user_sees_own_sources | User's own sources appear in context | Pass |
| DP-AT-04 | test_user_cannot_see_another_users_sources | Another user's sources do not appear in context | Pass |

### Create Source

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| DP-AT-05 | test_valid_submission_creates_source | Valid submission creates source and redirects to source detail page |Pass |
| DP-AT-06 | test_duplicate_source_name_raises_error | duplicate name for same user returns 200 and raises error | Pass |


### Edit Source

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| DP-AT-07 | test_authenticated_user_gets_404_for_another_user_source | Authenticated user cannot access another user's source | Pass |


### Delete Source

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| DP-AT-08 | test_authenticated_user_gets_404_for_missing_source | Authenticated user gets 404 for inexisting source | Pass |
| DP-AT-09 | test_unauthenticated_user_visits_source_delete_url_redirects | Unauthenticated user gets redirected to login for trying to access delete view of an existent source | Pass |


### Source Detail Page

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| SDP-AT-01 | test_unauthenticated_user_is_redirected | Unauthenticated user is redirected to login | Pass |
| SDP-AT-02 | test_authenticated_user_can_see_own_source | Page loads with correct template and context | Pass |
| SDP-AT-03 | test_user_cannot_access_another_users_source | Another user's source returns 404 | Pass |
| SDP-AT-04 | test_nonexistent_source_returns_404 | Nonexistent source returns 404 | Pass |
| SDP-AT-05 | test_units_only_show_on_source_they_belong_to | A source does not display units of another source | Pass |
| SDP-AT-06 | test_all_units_in_source_fetched_in_list | A source displays all units that belong to it | Pass |


### Create Unit

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| SDP-AT-07 | test_duplicate_unit_name_raises_error | Duplicate unit names whithin a source reloads the form with error | Pass |


### Edit Unit

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| SDP-AT-08 | test_get_request_for_edit_unit | 200 status code, right template, and right context for edit unit get request | Pass | |



### Unit Detail Page


| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| UDP-AT-01 | test_authenticated_owner_accessing_unit_detail_page_gets_200 | Authenticated owner can access unit detail page | Pass |
| UDP-AT-02 | test_unauthenticated_user_redirected | Any unauthenticated user trying to access a unit detail page is redirected | Pass |
| UDP-AT-03 | test_authenticated_user_gets_404_for_another_user_unit | Authenticated user trying to access another user's unit detail page gets 404 | Pass |
| UDP-AT-04 | test_authenticated_user_gets_404_for_inexistent_unit | Authenticated user trying to access a unit detail page for a unit that doesn't exist gets 404 | Pass |
| UDP-AT-05 | test_unit_name_is_correctly_displayed | Unit name appears on the unit detail page | Pass |


### Reference Detail Page


| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| RDP-AT-01 | test_authenticated_owner_gets_200 | Authenticated owner can access existing reference note |



## Known Bugs
### No user feedback on incorrect login credentials
When a user submits the login form with an incorrect username/password combination, no error message is displayed to the user.

### Sticky top bug
**Description:** Sticky-top not sticking in Chrome/Edge despite correct computed CSS (`position: sticky`, `top: 0`); confirmed broken on both mobile and desktop viewports, independent of pagination changes. `getBoundingClientRect` confirms nav moves with scroll instead of pinning.

**Ruled out:**
- Overflow on ancestors (checked via computed style loop)
- Inline style overrides
- Body/html overflow-x (removed entirely, no effect)
- `display: flex` on body (removed temporarily, no effect)
- CSS specificity/override — `.sticky-top` rule confirmed winning in Styles panel,
  no strikethroughs on position/top/z-index
- `<header>` structure/sizing — confirmed normal display:block, reasonable height,
  DOM matches source exactly, no injected wrappers
- Browser extensions — still fails in Incognito with extensions disabled
- Bootstrap CDN loading correctly (200 status, not a stale/cached version)
- Zoom level (confirmed 100%)
- Isolated minimal reproduction (bare Bootstrap navbar, zero project CSS) —
  still fails, ruling out project code entirely
- Firefox — still fails, ruling out Chrome/Edge-specific rendering
- Hardware acceleration toggle — still fails

**Further complication with scroll behaviour**

On create_reference.html specifically, triggering a scroll (by increasing the content textarea beyond 5 rows) caused the fixed navbar and sidebar to briefly visually separate — a gap opening between them for the duration of the scroll. Reducing the textarea back to 5 rows keeps the page short enough that no scroll ever occurs, avoiding the issue entirely rather than resolving its underlying cause.
Later on the same bug was seen in dashboard when source form was expanded. I devised a wordaround solution by givine the sidebar a height of 120vh and a z-index of 98, while for nav a z-index of 99. Now the two at least scroll together as below, avoiding the awkward white gap. Since sidebar only appears on desktop, this device cannot affect mobile or tablet views.

By contrast, create_question.html and create_mywords.html scroll regardless of how many textarea rows are set — even at 5 rows or fewer, the page still triggers a scrollbar. On these two pages, however, the navbar and sidebar scroll away together, moving as a consistent unit rather than separating from each other, so no gap appears. Since the specific issue being guarded against (a visible gap between navbar and sidebar) doesn't occur here, no row-count workaround was applied to these two pages, and their scrolling behavior was left as-is.

**Fix: always remember your tutor's fixes**
Finally, after going through all that trouble, both on my own and with Claude AI, I remembered I had a similar problem in my first project, and the fix was given by my tutor: put sticky on parent element. I put class 'sticky-top' on header instead of nav, and it works! It seems the olden days remedies still work in the age of AI. Thank you, Kevin!


### Edit cancel button preserves state in DOM
**Description** After editing a source and then clicking cancel button, form state is preserved in the DOM, and a new click on edit brings the form as last edited, not with the initial prepopulated data. This is a known limitation of the button collapse approach.


### Unauthenticated user visits `sources/<existing-source>/delete/` (DP-MT-27)
**Description** Unauthenticated user visiting `sources/<existing-source>/delete/` (actual url `sources/22/delete`) gets TypeError instead of being redirected to login.

**Evidence**
[DP-MT-27 Value Error](testing_screenshots/dp-mt-27.png)

**Automated test**

Confirmed by `test_unauthenticated_user_visits_source_delete_url_redirects` (DP-AT-09) failing with TypeError.

**Fix**
`login_required` decorator was added, initially omitted.


### Cancel button does not reset unit edit form after invalid submission (SDP-MT-28)

**Description** After invalid submission clicking cancel button does not reset the form. Clicking edit again will expand the form with previous errors and edits still present. This is a known limmitation to be revisited.



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

**Commit:** `1c35a47`


### DP - User with no sources created sees another user's sources instead of empty state (DP-MT-06)

**Description:** When manually testing whether a user with no sources sees the empty page with a message encouraging them to create one, another user's sources were visible instead.

**Automated Test:** Confirmed by `test_authenticated_user_cannot_see_another_user_sources` (SP-AT-04) — failing.

**Root Cause:** The `order_by('-source_creation_date')` line in `sources_list`was written as a separate queryset instead of being chained onto
`.filter(user=request.user)`, overwriting the user filter and returning all sources:

<pre>
@login_required
def sources_list(request):
    sources = Source.objects.filter(user=request.user)
    sources = Source.objects.order_by('-source_creation_date')
    return render(request, 'notes/sources.html', {'sources': sources})
</pre>

**Fix:** Chained `.filter(user=request.user)` with `.order_by()` in the queryset.


### DP test_duplicate_source_name_raises_error fails (DP-AT-06)
**Description:** Automated test fails and raises Integrity Error at database level, instead of returning a 200 status code wit a form error.

**Verified manually:** Confirmed in browser — submitting a duplicate source name at `/dashboard/` raised an unhandled `IntegrityError` before the fix.
[Unhandled Integrity Error](testing_screenshots/dp-mt-08.png)

**Cause:** Missing form-level validation — duplicate data passed `form.is_valid()` and reached the database, which rejected it with an `Integrity Error`.

**Fix:** Added `__init__` to `SourceForm` to accept `user` as a keyword argument; updated dashboard view to pass `user=request.user` to the form; added `clean()` to validate duplicate source names per user before saving.


### Visiting sources/800/delete/ returns Value Error instead of 404
**Description** Authenticated user types sources/800/delete/ in local environment and gets ValueError.

**Evidence**

[DP-MT-25 Value Error](testing_screenshots/dp-mt-25.png)

**Automated test**

Confirmed by `test_authenticated_user_gets_404_for_missing_source` - DP-AT-08 failing with `AssertionError: 301 != 404`
Initial automated test returned 301 (redirect) due to missing trailing slash in test URL. Once corrected, test confirmed the same ValueError seen in the browser.

**Root cause**
The view had no return for GET requests which were falling through and getting a None.

**Fix**
Add return for GET requests. Both manual and automated tests now passing.

**Commit:** `1b4bcdd`


## Biases in Testing

Test `SDP-MT-22: Each form is prepopulated with correct data` was a false positive in commit `8a61774` because of a confirmation bias, or because of the fact that unit name visible above form masked the fact that the corresponding field was not actually prepopulated.


