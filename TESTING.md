# Testing

## How this document is organised, and why

Testing here is done in two passes, because a single approach — either reading the code or clicking through the app — would each miss things the other one catches.

**Pass 1 audits the code itself, file by file** (models, forms, views), checking whether everything defined in the backend actually reaches the user: every field surfaces somewhere, every piece of business logic has a visible effect, nothing was built and then silently left disconnected from the interface. This pass has two parts per file: an automated part, testing the code's logic in isolation (constraints, custom validation, business rules) with no browser involved, and a manual part, confirming that logic actually renders correctly once it reaches a template.

**Pass 2 tests the app the way a real user would — action by action**, rather than file by file. Anything that recurs across multiple pages (access control, authentication, navigation) is tested once, as its own category, rather than repeated per page. Anything unique to a single feature (creating a Source, linking a note) is tested where it happens.

Together, the two passes cover what neither one does alone: Pass 1 catches things invisible from clicking around — a field that exists but never displays, logic with no visible effect. Pass 2 catches things invisible from reading code — a view that works in isolation but the wrong template renders, or a flow that works from one entry point but not another.

Note: The two-pass testing methodology (code-to-UI audit, then user-perspective testing) and its categorisation are my own; AI articulated these ideas into accurate wording (file intro, names of the two passes, and some other category names), drafted the skeleton  and sanity checked the idea and structure. I reread and edited the draft where necessary.

# Table of Contents

1. [Pass 1 - Code Audit](#pass-1--code-audit)
   - [Automated tests](#automated-tests)
     - [notes app - models.py](#notes-app-models)
     - [notes app - forms.py](#notes-app-forms)
     - [notes app - views.py](#notes-app-views)
   - [Manual tests - code reflection in UI](#manual-tests--code-reflection-in-ui)
     - [notes app - models.py](#manual-notes-app-models)
     - [notes app - forms.py](#manual-notes-app-forms)
     - [notes app - views.py](#manual-notes-app-views)
     - [notes app - notes.js](#manual-notes-app-notesjs)
     - [notes app - templates](#manual-notes-app-templates)
2. [Pass 2 - User-Perspective Testing](#pass-2--user-perspective-testing)
   - [Repeating categories](#repeating-categories)
     - [Main Navbar (MNAV)](#main-navbar-mnav)
     - [Content Navigation (TREE)](#content-navigation-sourceunitnotes-tree)
     - [NAV-OFFCANVAS](#nav-offcanvas-offcanvas-for-mobile)
     - [NAV-BACK](#nav-back-back-link-for-mobile)
     - [Breadcrumbs (BNAV)](#breadcrumbs-bnav)
     - [Pagination (PAG)](#pagination-pag)
     - [A11Y](#a11y-accessibility)
     - [Responsiveness](#responsiveness)
     - [Minimalist UI](#minimalist-ui)
   - [Per-feature tests](#per-feature-tests)
     - [Authentication (AUTH)](#authentication-auth)
     - [Authorization (AUTHZ)](#authorization-authz)
     - [External navigation (EXT)](#external-navigation-ext)
     - [Actions partial](#actions-partial)
     - [Source CRUD](#source-crud)
     - [Unit CRUD](#unit-crud)
     - [Note CRUD](#note-crud)
     - [Workflow Theme](#workflow-theme)
     - [UI/UX Theme](#uiux-theme)
3. [Story-to-Test Mapping](#story-to-test-mapping)
4. [Solved Bugs](#solved-bugs)
5. [Known Bugs / Limitations](#known-bugs--limitations)
6. [Validation](#validation)
---

## Pass 1 — Code Audit

### Automated tests

#### notes app models

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| ANM-01 | test_duplicate_source_name_per_user_raises_error | A user cannot have two sources with identical names, error is raised | Pass |
| ANM-02 | test_duplicate_source_name_enforced_per_user_not_globally | Two different users can have identical named sources, uniqueness enforced per user | Pass |
| ANM-03 | test_valid_source_type_saves_without_errors | A source can be saved with no problems given it has a valid type | Pass |
| ANM-04 | test_invalid_source_type_raises_error | Trying to save a source with an invalid type raises error | Pass |
| ANM-05 | test_duplicate_unit_name_raises_error | Creating a new unit with a duplicate name within a source raises error | Pass |
| ANM-06 | test_same_unit_name_in_different_sources_saves | Test two distinct sources can have units with same name | Pass |
| ANM-07 | deleting_reference_does_not_delete_linked_questions | Tests that deleting the reference note set as foreign key on a question note does not delete the question as well | Pass |
| ANM-08 | test_deleting_reference_sets_question_reference_to_null | Tests that deleting a reference note sets reference field to
null on linked questions | Pass |
| ANM-09 | deleting_reference_does_not_delete_linked_mywords | Tests that deleting the reference note set as foreign key on a mywords note does not delete mywords note as well | Pass |
| ANM-10| test_deleting_reference_sets_mywords_reference_to_null | Tests that deleting a reference note sets reference field to
null on linked mywords | Pass |
| ANM-11 | deleting_question_does_not_delete_linked_mywords | Tests that deleting the question note set as foreign key on a mywords note does not delete mywords note as well | Pass |
| ANM-12| test_deleting_question_sets_mywords_reference_to_null | Tests that deleting a question note sets question field to
null on linked mywords | Pass |


#### notes app forms
| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| ANF-01 | test_empty_source_author_saved_as_none | Empty source_author saved as None, not empty string | Pass |
| ANF-02 | test_white_spaces_only_for_author_saved_as_none | Whitespace-only source_author saved as None | Pass |
| ANF-03 | test_author_field_value_is_returned_correctly | Valid source_author value passes through unchanged | Pass |
| ANF-04 | test_duplicate_source_name_same_user_raises_error | Same user creating a duplicate name source raises error | Pass |
| ANF-05 | test_other_user_same_source_name_submits_without_error | Source name uniqueness is enforced per user, not globally | Pass |
| ANF-06 | test_editing_source_with_same_name_submits_correctly | Editing a source with unchanged name doesn't raise error | Pass |
| ANF-07 | test_duplicate_unit_name_same_source_raises_error | Creating a duplicate name unit within the same source raises error | Pass |
| ANF-08 | test_same_unit_name_different_source_is_valid | Unit name uniqueness is enforced per source, not globally | Pass |
| ANF-09 | test_editing_unit_with_unchanged_name_is_valid | Editing a unit with its own unchanged name is valid | Pass |

#### notes app views

**Dashboard view**

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| ANV-01 | test_authenticated_user_sees_own_sources | User's own sources appear in the context | Pass |
| ANV-02 | test_authenticated_user_cannot_see_another_user_sources | Authenticated user cannot see another user's sources | Pass |
| ANV-03 | test_source_saved_with_correct_user | Source is saved with the correct user | Pass |
| ANV-04 | test_valid_submission_creates_source | Valid submission creates source and redirects to source detail page | Pass |
| ANV-05 | test_unauthenticated_user_is_redirected | `@login_required` redirects anonymous users to the login page | Pass |
| ANV-06 | test_authenticated_user_gets_200 | Authenticated user can access the dashboard page | Pass |
| ANV-07 | test_invalid_submission_rerenders_dashboard | Invalid submission re-renders dashboard instead of redirecting | Pass |


**Delete source view**
| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| ANV-08 | test_unauthenticated_user_visits_source_delete_url_redirects | Unauthenticated user requests delete url of an existing source and gets redirected to login page | Pass |
| ANV-09 | test_authenticated_user_gets_404_for_missing_source | Authenticated user trying to delete a source that doesn't exist gets 404 | Pass |
| ANV-10 | test_owner_can_delete_own_source | Authenticated user can delete their source and is redirected to dashboard | Pass |


**Source detail view**

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| ANV-11 | test_all_units_in_source_fetched_in_list | Tests that all units belonging to a source are filtered in the queryset | Pass |
| ANV-12 | test_units_only_show_on_source_they_belong_to | Tests that units are only displayed in the list of units belonging to their parent source | Pass |
| ANV-13 | test_edit_mode_false_by_default | Tests that source details are not editable by default | Pass |
| ANV-14 | test_valid_edit_source_submission_saves_and_redirects |  Tests that valid edit source submission updates the source and redirects to source detail page | Pass |
| ANV-15 | test_edit_mode_true_on_invalid_edit_source_submission | Tests that invalid submission triggers page rerender in edit mode | Pass |
| ANV-16 | test_valid_add_unit_submission_creates_unit_and_redirects | Valid add_unit submission creates a unit linked to the source and redirects to source detail page | Pass |
| ANV-17 | test_invalid_add_unit_submission_does_not_create_unit | Invalid add_unit submission re-renders the page and does not create a unit | Pass |

**Delete unit view**

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| ANV-18 | test_owner_can_delete_unit | Authenticated user can delete a unit and is redirected to source detail page | Pass |
| ANV-19 | test_unit_belonging_to_different_source_returns_404 | Unit exists but isn't linked to the given source_pk -  confirms the second get_object_or_404's source filter works | Pass |
| ANV-20 | test_unauthenticated_user_visits_unit_delete_url_redirects | Unauthenticated user requests delete url of an existing unit and gets redirected | Pass |

**Unit detail view**

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| ANV-21 | test_authenticated_owner_accessing_unit_detail_page_gets_200 | Authenticated owner gets 200 status code when requesting detail page of a unit | Pass |
| ANV-22 | test_unauthenticated_user_redirected | Any unauthenticated user is redirected when trying to access a unit detail page | Pass |
| ANV-23 | test_authenticated_user_gets_404_for_another_user_unit | Authenticated user trying to access another user's unit detail page gets 404 response | Pass |
| ANV-24 | test_authenticated_user_gets_404_for_inexistent_unit | Authenticated user requesting a unit that doesn't exists gets 404 | Pass |


### Manual tests — code reflection in UI

#### manual notes app models
Tests how code written at model level reflects in UI

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| MNM-01 | Source type choices display correctly | Confirms all 8 SourceType values render as selectable options in the create-source form | Pass |
| MNM-02 | Add source form does not submit without a source type selected | source_type's blank=False default correctly enforced — form rejects submission with no type chosen | Pass |
| MNM-03 | Add source form does not submit without a source name filled in | souce_name's blank=False default correctly enforced -form rejects submission with blank field | Pass |
| MNM-04* | Source name has a character limit imposed | source_name's max_length=255 correctly enforced - input stops accepting characters once the limit is reached | Pass |
| MNM-05 | Source_author has a character limit imposed | source_author's max_length=100 correctly enforced - input stops accepting characters once the limit is reached | Pass |
| MNM-06 | Add source form with blank author field submits without error | source_author's blank=True enforced - form submits with blank author field without error | Pass |
| MNM-07 | Unit name has a character limit imposed | unit_name's max_length=255 correctly enforced - input stops accepting characters once the limit is reached | Pass |
| MNM-08 | All types of notes correctly submit without title | abstract base title with blank=True | Pass |
| MNM-09 | All types of notes titles have a character limit imposed | title max_length=100 correctly enforced - input stops accepting characters once limit is reached | Pass |
| MNM-10 | Reference notes submit correctly without location | location's blank=True enforced - form submits with blank location field without error | Pass |
* Note: while testing MNM-04 at the max-length boundary, found that unbroken long strings (e.g. URLs) in source_name cause horizontal scroll rather than wrapping. Logged as a bug — see Solved Bugs.

#### manual notes app forms

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| MNF-01 | Test 'type' and not '----' is displayed first in source type choices | for loop in SourceForm correctly reaches UI | Pass |
| MNF-02 | Test error message for duplicate source name | Error message for duplicate source name correctly displays in UI | Pass |
| MNF-03 | Test in edit mode rewriting the same source name doesn't raise error | Submits with name unchanged or cleared and typed again | Pass |
| MNF-04 | Test error message for duplicate unit name | Error message for duplicate unit name within a source correctly displays in UI | Pass |
| MNF-05 | Test in edit mode rerwiting the same unit name doesn't raise error | Submits with name unchanged or cleared and typed again | Pass |


#### manual notes app views

**All Views**

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| MNV-01 | Log in, view a page in notes, log out, click browser back button; repeat for all pages in notes | @never_cache, pageshow reload, and @login_required together prevent cached authenticated content from being shown after logout, redirecting to Sign In instead | Pass |
| MNV-02 | Anonymous user typing correctly formated url gets redirected to sign in | Verified all @login_required views redirect anonymous users to login rather than exposing content or returning a 404, confirming no route bypasses authentication | Pass |
| AUTHZ-20 | Ownership check implementation | All Source/Unit/Note views use the documented ownership helper consistently — confirmed by code inspection, not just behavioural testing | | | |
| AUTHZ-20a | Helper function itself | Correctly returns 404 for both non-owned and nonexistent PKs, with no distinguishable difference in response | | | |
| AUTHZ-20b | Grep/audit: any view manually querying Source/Unit/Note by PK without going through the helper | None found — confirms no view bypasses the pattern | | | | | Ownership check implementation | All Source/Unit/Note views use the documented ownership helper consistently — confirmed by code inspection, not just behavioural testing | | | |


**Dashboard view**

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| MNV-03 | With more than 8 sources, load Dashboard | Pagination controls appear | Pass |
| MNV-04 | Count sources on page 1 | Exactly 8 shown | Pass |
| MNV-05 | Feedback message after successful add source save | 'Source added' message appears in Dashboard | Pass |

**Delete source view**

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| MNV-06 | Feedback message after successful delete source action | 'Source deleted' message appears in Dashboard | Pass |

**Source detail view**

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| MNV-07 | Feedback message after successful source edit | 'Edit saved' message appears in source detail page | Pass |
| MNV-08 | Feedback message after successful unit creation | 'Unit added' message appears in source detail page | Pass |

**Delete unit view**

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| MNV-09 | Feedback message after successful unit deletion | 'Unit deleted' message appears in source detail page | Pass |


#### manual notes app notes.js


| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| MNJS-01 | Log in, view a page in notes, log out, click browser back button; repeat for all pages in notes | @never_cache, pageshow reload, and @login_required together prevent cached authenticated content from being shown after logout, redirecting to Sign In instead | Pass |

#### manual notes app templates

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| MPT-01 | Verify external link security attributes | Verify external link security attributes | Inspect page source code or elements to confirm all external anchor tags contain `target="_blank"` and `rel="noopener"` to ensure cross-origin browser security | |

---

## Pass 2 — User-Perspective Testing

### Repeating categories

#### Main Navbar (MNAV)

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|-------|-------|------------|
| MNAV-01 | Anonymous state desktop | Navbar displays: logo, home, how it works, give feedback, sign in, sign up links | | | |
| MNAV-02 | Authenticated user view desktop | Navbar displays: logo, home, how it works, give feedback, dashboard, log out | | |
| MNAV-03 | Click logo link | Home page loads | | | |
| MNAV-04 | Click home link | Home page loads | | | |
| MNAV-05 | Click How it works link | How it works page loads | | | |
| MNAV-06 | Click Give feedback link / test target="_blank" behaviour | Google form loads in a separate tab | | | |
| MNAV-07 | Click sign in link | Sign in page loads | | | |
| MNAV-08 | Click sign up link | Sign up page loads | | | |
| MNAV-09 | Click Dashboard link | Dashboard page loads | | | |
| MNAV-10 | Click Log out link | Redirects to Home page anonymous state | | | |
| MNAV-11 | Anonymous state mobile | Navbar displays: logo, icons for home, how it works, give feedback, and again linkds for sign in and sign up | | | |
| MNAV-12 | Authenticated user view mobile | Navbar displays: logo and icons for home, how it works, give feedback, dashboard and log out | | | |
| MNAV-13 | Click all icon links on mobile view | Icons link to correct pages | | | |


#### Content Navigation (source/unit/notes tree)

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|-------|-------|------------|
| TREE-01 | Click Add source link | Navigates to Dashboard with Add Source form expanded | | | |
| TREE-02 | Click Sources link | Navigates to Dashboard with Add Source form collapsed | | | |
| TREE-03 | Click Chevron right | Expands the sources list tree | | | |
| TREE-04 | Sources count | Present in tree and accurate | | | |
| TREE-05 | Scrollable list | List of sources is scrollable | | | |
| TREE-06 | Click an individual source in the list | Navigates to that specific source detail page | | | |
| TREE-07 | Individual chevron icon per source | Chevron icon present to the right of every source | | | |
| TREE-08 | Long sources name display | Long sources names are truncated with ellipsis, while tooltips display the entire name | | | |
| TREE-09 | Click individual source chevron | Expands a list of units belonging to that source | | | |
| TREE-10 | Units count | Present in tree when units list expanded and accurate | | | |
| TREE-11 | Plus icon | Plus icon present in Tree when units list is expanded and tooltip reads 'Add unit' | | | |
| TREE-12 | Click + icon | Navigates to unit detail page, unit form expanded | | | |
| TREE-13 | Click an individual unit | Navigates to that specific unit detail page | | | |
| TREE-14 | Long units name display | Long units names are truncated with ellipsis, while tooltips display the entire name | | | |
| TREE-15 | Notes pages tree content | Lower part of tree content shows links to reference notes, mywords notes, and question notes , and + icons associated with each link | | | |
| TREE-16 | Click Reference link | Navigates to Unit detail page with Reference panel active | | | |
| TREE-17 | Click My Words link | Navigates to Unit detail page with My Words panel active | | | |
| TREE-18 | Click Question link | Navigates to Unit detail page with Question panel active | | | |
| TREE-19 | Plus icons tooltips | All plus icons show descriptive tooltips | | | |
| TREE-20 | Click plus icon | Navigates to the specific note type create page | | | |
| TREE-21 | Empty tree | Newly registered account dashboard tree shows 0 sources | | | |
#### NAV-OFFCANVAS (offcanvas for mobile)
#### NAV-BACK (back link for mobile)
#### Breadcrumbs (BNAV)

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|-------|-------|------------|
| BNAV-01 | Page presence | Present in Unit detail page and in Notes pages | | | |
| BNAV-02 | Trail | Starts with parent source name link and ends with last parent | | | |
| BNAV-03 | Content | Updates dynamically dependent on page and item | | | |
| BNAV-04 | Click breadcrumb link | Navigates cleanly to the specific parent item's detail view page | | | |
| BNAV-05 | Long names display | Long names are truncated with ellipsis | | | |
#### Pagination (PAG)

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|-------|-------|------------|
| PAG-01 | Number of items per page | Each page correctly displays 8 items per page unless it is an incomplete last page | | | |
| PAG-02 | Click Next | Navigates to next page | | | |
| PAG-03 | Click Previous | Navigates to previous page | | | |
| PAG-04 | 8 or less items | Pagination is not displayed | | |
| PAG-05 | First page | Previous link is not displayed | | | |
| PAG-06 | Last page | Next link is not displayed | | | |


#### A11Y (accessibility)
**Story 28 - Accessibility**

*Automated testing with Lighthouse*

A11Y-01
- Lighthouse accessibility audit run per page, both mobile and desktop viewport, in Chrome DevTools.
- Covers colour contrast, alt text, accessible-name checks, list structure validity, heading order, basic form-label association, across all 16 pages (Home, How it works, Sign In, Sign Up, Dashboard, Source detail, Unit detail, and Create/Detail/Edit for each of the three note types)
- 100/100 on both desktop and mobile for every page. Several issues were flagged and corrected during this test cycle: some contrast failures, invalid list markup

*Manual Accessibility Review*

- Semantic HTML and structure

A11Y-02 — Use real `<button>`, `<nav>`, `<main>`, `<header>`, `<footer>` instead of styled `<div>`s.** Checked all .html files. Result: Pass.

A11Y-03 — One `<h1>` per page; headings nest in order (no skipping h2 → h4).** Checked all .html files. Result: Pass.

- Forms

A11Y-04 — Every input has a `<label for="id">`.** Checked all custom forms in the notes app. All inputs in all forms have labels using Bootstrap's `visually-hidden` class, so they conform to accessibility criteria while remaining aligned with the app's aesthetics. Result: Pass.

A11Y-05 — Required fields marked with the `required` attribute and indicated visually. All forms checked. While the `required` attribute is passed down from model to form to template and reliably announced by screen readers, sighted users had no way of knowing which fields were required. Added "required" to placeholders for required inputs, giving parity between sighted and visually impaired users: when a field has content, "required" is not announced since the condition is satisfied; when a field is empty, "required" is announced for both types of users. Final result after changes: Pass.

A11Y-06 — Feedback messages made available to screen readers via `role="status"` for CRUD operations and via `aria-live="polite"` for form errors.** Added everywhere relevant. Result: Pass.


#### Responsiveness
**Story 29 - Responsive design**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| RESP-01 | Layout at mobile breakpoint (e.g. 375px) | No broken/overlapping elements, content readable without zoom | | | |
| RESP-02 | Layout at tablet breakpoint (e.g. 768px) | No broken/overlapping elements | | | |
| RESP-03 | Layout at desktop breakpoint | No broken/overlapping elements, no excessive whitespace/stretching | | | |
| RESP-04 | Long unbroken string (source/unit/note title) on mobile | No horizontal scroll — regression check on earlier fix | | | |
| RESP-05 | Long unbroken string on tablet/desktop | No horizontal scroll | | | |
| RESP-06 | Navigation collapses to offcanvas on mobile | Hamburger/offcanvas pattern activates at appropriate breakpoint | | | |
| RESP-07 | Offcanvas nav opens/closes correctly on mobile | Tap opens, tap outside or close icon dismisses | | | |
| RESP-08 | Sidebar behaviour on desktop | Sidebar expandable/collapsable | | | |
| RESP-09 | Touch target sizing on mobile | Buttons/links/icons meet minimum touch target size not cramped together | | | |
| RESP-10 | Forms usable on mobile | Input fields, dropdowns, and buttons on Create/Edit forms remain usable without horizontal scroll or overlap | | | |
| RESP-11 | Tables/lists (Sources, Units, Notes) on mobile | Content reflows appropriately rather than forcing horizontal scroll | | | |


#### Minimalist UI
**Story 30 - Minimalist UI**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| UX-01 | Pages avoid unnecessary visual clutter | No decorative elements that don't support the task | | | |
| UX-02 | Consistent, restrained color and typography | Same palette/type system used throughout, no inconsistent one-off styling | | | |
| UX-03 | CTAs visually clear without excessive decoration | Primary actions stand out through hierarchy/contrast, not ornamentation | | | |

### Per-feature tests

#### Authentication (AUTH)

**Sign up page**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|-------|-------|------------|
| AUTH-01 | Sign up form fields | Sign up form displays all fields correctly | | | |
| AUTH-02 | Placeholders on sign up form |  All fields display descriptive placeholders instead of raw visible labels to achieve a clean layout | | | |
| AUTH-03 | Communicating required fields to users on sign up form | Required fields include 'required' in the placeholder. Matching `label` elements are present in the DOM using Bootstrap's `visually-hidden` class to ensure full screen-reader accessibility| | | |
| AUTH-04 | Submit button | Get started button present | | | |
| AUTH-05 | Sign in alternative | Sign in alternative present for already registered users | | | |
| AUTH-06 | Valid submission | Creates account and redirects to dashboard | | | |
| AUTH-07 | Submission with blank fields | Form rejected errors shown | | | |
| AUTH-08 | Submission with blank email field | Form rejected, error shown | | | |
| AUTH-09 | Submission with wrong email format | Form rejected, error shown | | | |
| AUTH-10 | Submission with already used email | Form rejected, error shown | | | |
| AUTH-11 | Submission with blank username field | Form rejected, error shown | | | |
| AUTH-12 | Submission with already used username | Form rejected, error shown | | | |
| AUTH-13 | Submission with blank password field | Form rejected, error shown | | | |
| AUTH-14 | Submission with blank password again field | Form rejected, error shown | | | |
| AUTH-15 | Submission with duplicate password not matching | From rejected, error shown | | | |
| AUTH-16 | Click sign in link | Navigates to sign in page | | | |

**Sign in page**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|-------|-------|------------|
| AUTH-17 | Sign in form fields | Sign in form displays all fields correctly | | | |
| AUTH-18 | Placeholders on sign in form |  All fields display descriptive placeholders instead of raw visible labels to achieve a clean layout | | | |
| AUTH-19 | Communicating required fields to users on sign in form | Required fields include 'required' in the placeholder. Matching `label` elements are present in the DOM using Bootstrap's `visually-hidden` class to ensure full screen-reader accessibility| | | |
| AUTH-20 | Sign in button  | Present on page | | | |
| AUTH-21 | Remember me option | Checkbox and text present on page | | | |
| AUTH-22 | Sign up alternative | Present for unregistered users | | | |
| AUTH-23 | Valid credentials submission | User is redirected to dashboard | | | |
| AUTH-24 | Submission with blank fields | Form rejected, error shown | | | |
| AUTH-25 | Submission with invalid credentials | Form rejected, error shown | | | |
| AUTH-26 | Submission with blank email field | Form rejected, error shown | | | |
| AUTH-27 | Submission with incorrectly formatted email | Form rejected, error shown | | | |
| AUTH-28 | Submission with invalid password | Form rejected, error shown | | | |
| AUTH-29 | Remember me unchecked | Upon closing and reopening browser user is not logged in, regardless of whether they actually previously logged out or not | | | |
| AUTH-30 | Remember me checked, user does not log out at the end of session | Upon closing without logging out and reopening it, user is logged in, unless more than 2 weeks have passed since their last sign in | | | |
| AUTH-31 | Remember me checked, user logs out at the end of session | Upon reopening browser user is asked to log in to access their account | | | |


#### Authorization (AUTHZ)


| Test ID | View accessed while logged out | Expected | Actual | Local | Deployment |
|---------|-------------------------------|----------|-------|-------|------------|
| AUTHZ-01 | Source: list, detail, create, edit, delete URLs | All redirect to login | | | |
| AUTHZ-02 | Unit: list, detail, create, edit, delete URLs | All redirect to login | | | |
| AUTHZ-03 | Note (Reference/MyWords/Question): detail, create, edit, delete URLs | All redirect to login | | | |
| AUTHZ-04 | Dashboard / sidebar context data | Redirects to login | | | |
| AUTHZ-05 | User A requests detail URL for User B's Source | 404 | | | |
| AUTHZ-06 | User A requests detail URL for User B's Unit | 404 | | | |
| AUTHZ-07 | User A requests detail URL for User B's Note (each type) | 404 | | | |
| AUTHZ-08 | User A requests edit URL for User B's Source/Unit/Note (GET) | 404 | | | |


#### External navigation: (EXT)

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|-------|-------|------------|
| EXT-01 | Give feedback link | Opens Google form in a separate tab | | | |
| EXT-02 | GitHub link | Opens GitHub page in a separate tab | | | |
| EXT-03 | Linked in link | Opens Linked in page in a separate tab | | | |


#### Actions partial

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|-------|-------|------------|
| ACT-01 | Display | Displays as a 3 dot icon whenever edit and delete actions are needed | | | |
| ACT-02 | Click 3 dots icon | Opens a dropdown with edit and delete actions selectable | | | |
| ACT-03 | Click edit | Displays source/unit forms in edit mode or navigates to the specific note's edit page | | | |
| ACT-04 | Click delete | Opens a delete modal | | | |


#### Source CRUD

**Create source**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|-------|-------|------------|
| SCRUD-01 | Click Add source button | Expands Add source form | | | |
| SCRUD-02 | Add source form fields | Add source form correctly displays name, author and source type fields | | | |
| SCRUD-03 | Save and Cancel buttons | Present on form | | | |
| SCRUD-04 | Placeholders | All fields display descriptive placeholders instead of raw visible labels to achieve a clean layout | | | |
| SCRUD-05 | Communicating required fields to users on add source form | Required fields include 'required' in the placeholder. Matching `label` elements are present in the DOM using Bootstrap's `visually-hidden` class to ensure full screen-reader accessibility | | | |
| SCRUD-06 | Click type select | Opens a dropdown with choices | | | |
| SCRUD-07 | Selection | Only one choice can be selected at one time | | | |
| SCRUD-08 | Valid submission | Creates source, reloads dashboard with sources list updated to include the newly created source, shown first in list, and "Source added" message displayed | | | |
| SCRUD-09 | Blank fields | Form rejected, errors shown | | | |
| SCRUD-10 | Blank name field | Form rejected, error shown | | | |
| SCRUD-11 | Blank author | Form submits | | | |
| SCRUD-12 | Duplicate name | Form rejected, error shown | | | |
| SCRUD-13 | Blank type | Form rejected, error shown | | | |
| SCRUD-14 | Click save button | Saves form if valid | | | |
| SCRUD-15 | Click cancel button | Collapses and clears the form | | | |
| SCRUD-16 | Click cancel after invalid submission with errors showing on form | Collapses and clears the form | | | |

**Read Source**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|-------|-------|------------|
| SCRUD-17 | Individual source display | Each source in the list of sources displays name, author if present, and type badge | | | |
| SCRUD-18 | Click an individual source | Navigates to the the specific source detail page | | | |
| SCRUD-19 | Empty state message | Displayed when no source has been created | | | |
| SCRUD-19 | Source header in source detail page | Shows source name, author if present and type badge and a 3 dots icon as header | | | |
| SCRUD-20 | Source detail page | Shows Add unit button and list of its units | | | |
| SCRUD-21 | Empty state message for units | Displayed when no units have been created in that source | | | |
| SCRUD-22 | Sources list filtering | Only sources belonging to the logged-in user appear in the list — create sources as two different users, confirm each user's list shows only their own | | | |
| SCRUD-23 | Sources list ordering | Most recently created source appears first, oldest last (reverse chronological) | | | |
| SCRUD-24 | Date created displayed per source | Each source in the list shows its creation date | | | |
| SCRUD-25 | Date created displayed per source (desktop viewport) | Each source in the list shows its creation date | | | |

**Edit Source**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|-------|-------|------------|
| SCRUD-26 | Edit mode: title field pre-populated with current source title | Field shows existing title, editable | | | |
| SCRUD-27 | Edit mode: author field pre-populated with current author (or placeholder if blank) | Shows existing author, or "add author" placeholder if none set | | | |
| SCRUD-28 | Edit mode: type dropdown pre-selected to current source type | Dropdown shows current type (e.g. "Website") selected | | | |
| SCRUD-29 | Submit valid title change via checkmark icon | Source title updates, redirects/re-renders without `?edit=1`, new title displayed | | | |
| SCRUD-30 | Submit empty/whitespace-only title | Form rejected with validation error, remains in edit mode | | | |
| SCRUD-31 | Submit extremely long title (test truncation/scroll bug regression) | No horizontal scroll introduced, long-string fix holds | | | |
| SCRUD-32 | Leave author field blank and submit | Accepted — author is optional, saves with blank author | | | |
| SCRUD-33 | Change type dropdown to a different value and submit | Source type updates correctly, reflected on next page load | | | |
| SCRUD-34 | Click cross (cancel) icon without changing anything | Returns to display mode, no changes saved, `?edit=1` removed from URL | | | |
| SCRUD-35 | Make changes, then click cross (cancel) icon | Returns to display mode, no changes saved, `?edit=1` removed from URL | | | |
| SCRUD-37 | Submit valid author change | Author updates and persists on reload | | | |
| SCRUD-38 | Success message on edit | "Edit saved" message displayed after valid submission | | | |
| SCRUD-39 | Submit edit with no type selected | Form rejected, error shown, edit not saved | | | |


**Delete Source**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| SCRUD-40 | Click delete option | Confirmation step/modal appears before any deletion occurs | | | |
| SCRUD-41 | Confirmation step content | Source name and author are displayed in the confirmation step, so the user can verify they're deleting the right one | | | |
| SCRUD-42 | Confirmation step — author blank | If source has no author, confirmation step displays sensibly (no "None" or blank gap) rather than breaking the layout | | | |
| SCRUD-43 | Cancel from confirmation step | Deletion aborted, source remains in list unchanged | | | |
| SCRUD-44 | Confirm deletion | Source is removed from the sources list on dashboard | | | |
| SCRUD-45 | Redirect after deletion | User is redirected to dashboard | | | |
| SCRUD-46 | Success message after deletion | Confirmation message displayed after successful deletion | | | |
| SCRUD-47 | Cascade: note pk of a unit belonging to the source before deletion, delete the source, then navigate directly to that unit's URL | 404 — unit no longer exists | | | |
| SCRUD-48 | Cascade: note pk of a note (Reference/MyWords/Question) belonging to a unit under the source before deletion, delete the source, then navigate directly to that note's URL | 404 — note no longer exists | | | |


#### Unit CRUD

**Read Unit (list within source)**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| UCRUD-01 | Source name displayed on source detail page | Source name shown correctly | | | |
| UCRUD-02 | Source author displayed on source detail page | Author shown if present | | | |
| UCRUD-03 | Units listed in most-recently-edited order | Most recently edited unit appears first, oldest edit last | | | |
| UCRUD-04 | Each unit in the list displays its name | Name shown for every unit | | | |
| UCRUD-05 | Click a unit in the list | Navigates to that unit's detail page (three-tabs view) | | | |
| UCRUD-06 | List only shows units belonging to the current source | No units from other sources (even the same user's other sources) appear in this list | | | |
| UCRUD-07 | Empty state message | Displayed when no units exist yet in this source, encouraging user to create one | | | |

**Create Unit**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| UCRUD-08 | Create unit button present on source detail page | Button visible | | | |
| UCRUD-09 | Click Create unit button | Expands the create unit form | | | |
| UCRUD-10 | Save and Cancel buttons | Present on form | | | |
| UCRUD-11 | Click cancel button | Collapses and resets the form | | | |
| UCRUD-12 | Name field | User can enter a unit name | | | |
| UCRUD-13 | Blank name field submitted | Form rejected, error shown | | | |
| UCRUD-14 | Valid submission | Unit appears in units list and success message shown | | | |
| UCRUD-15 | Duplicate unit name within same source | Form rejected, error shown | | | |
| UCRUD-16 | Duplicate unit name across different sources (same user) | Accepted — uniqueness is scoped per-source, not global | | | |
| UCRUD-17 | Submit form with errors | Page reloads with form already expanded, so validation feedback is immediately visible without needing to click Create unit again | | | |

**Edit Unit**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| UCRUD-18 | Edit form pre-populated with correct unit name | Existing name shown, editable | | | |
| UCRUD-19 | User can edit the name field | Field accepts new input | | | |
| UCRUD-20 | Save and Cancel icons present on edit form | Both visible | | | |
| UCRUD-21 | Submit empty name field | Form re-rendered with error, not saved | | | |
| UCRUD-22 | Submit valid name change | Form saves, page reloads in non-editable (display) mode showing updated name | | | |
| UCRUD-23 | Submit duplicate name (matching another unit in same source) | Form re-rendered with error, not saved | | | |


**Delete Unit**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| UCRUD-24 | Confirmation modal content | Source name and unit name both included, along with a risk/warning message, so user can verify they're deleting the right unit | | | |
| UCRUD-25 | Delete and Cancel buttons present on modal | Both visible | | | |
| UCRUD-26 | Click Cancel on modal | Modal closes, unit not deleted, list unchanged | | | |
| UCRUD-27 | Click Delete on modal | Unit deleted, modal closes, page re-renders with updated units list (deleted unit no longer present) | | | |
| UCRUD-28 | Cascade: note pk/URL of a note belonging to this unit before deletion, delete the unit, then navigate directly to that note's URL | 404 — note no longer exists (cascade deletion confirmed, same technique used for Source cascade in SCRUD-47/48) | | | |


#### Note CRUD

**Read Notes (unit detail — three-tab view)**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| NCRUD-01 | Three tabs present on unit detail page | Reference, My Words, Question tabs all visible | | | |
| NCRUD-02 | Each tab shows only notes of its own type | Reference tab shows only Reference notes, My Words only MyWords notes, Question only Question notes | | | |
| NCRUD-03 | Notes shown belong only to the current unit | No notes from other units (even within the same source) appear in any tab | | | |
| NCRUD-04 | Active tab persists via URL hash on refresh | Refreshing the page keeps the same tab active (e.g. `#question` stays on Question tab) | | | |
| NCRUD-05 | Active tab persists via URL hash on shared link | Opening a URL with a tab hash (e.g. pasted into a new browser session while logged in) opens directly to that tab | | | |
| NCRUD-06 | Pagination is independent per tab | Paginating Reference notes doesn't affect page position in My Words or Question tabs | | | |
| NCRUD-07 | Empty state per tab | Each tab shows its own empty-state message when no notes of that type exist, encouraging creation | | | |
| NCRUD-08 | Empty state doesn't leak across tabs | A tab with notes doesn't show empty state, and a genuinely empty tab doesn't inherit content from another tab type | | | |


**Read Note (individual detail page)**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| NCRUD-09 | Reference note detail page displays all relevant fields | Title, content and location | | | |
| NCRUD-10 | MyWords note detail page displays all relevant fields | My Words title and content | | | |
| NCRUD-11 | Question note detail page displays all relevant fields | Question title and content| | | |
| NCRUD-12 | Breadcrumb navigation on note detail page | Shows correct chain: Source → Unit → Note type, matching the note's actual parent hierarchy | | | |
| NCRUD-13 | Breadcrumb links are functional | Clicking Source or Unit in the breadcrumb navigates to the correct respective page (the *actual* parent, not just any source/unit) | | | |

**Edit Note**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| NCRUD-14 | Edit option accessible from note detail page (Reference/MyWords/Question) | Edit link/button present for all three note types | | | |
| NCRUD-15 | Any type of note edit form pre-populated with current content | Existing title, content (and location for Reference) shown, editable | | | |
| NCRUD-16 | Submit any type of note with empty required content field | Form rejected, error shown | | | |
| NCRUD-17 | Submit valid content change (each note type) | Updated content displayed on detail page, confirmation message shown | | | |
| NCRUD-18 | Cancel button on edit form | Returns to note detail page, no changes saved, original content still displayed | | | |


**Delete Note**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| NCRUD-19 | Click delete option | Confirmation step appears before any deletion occurs | | | |
| NCRUD-20 | Confirmation step content | Note title and parent unit name present so user can verify they're deleting the right note | | | |
| NCRUD-21 | Confirm and Cancel options present | Both visible on confirmation step | | | |
| NCRUD-22 | Click Cancel | Deletion aborted, note remains, no redirect | | | |
| NCRUD-23 | Confirm deletion | Note removed, user redirected to the unit's note list (correct tab active) | | | |
| NCRUD-24 | Success message after deletion | Confirmation message displayed | | | |

#### Workflow Theme

**Story 18 — Create Reference note**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| WORKFLOW-01 | "Create reference note" option from Unit detail page | Opens create form | | | |
| WORKFLOW-02 | "Create reference note" option from sidebar | Opens create form, correctly attached to the right unit via context | | | |
| WORKFLOW-03 | Create form displays required content field | Field present and clearly required | | | |
| WORKFLOW-04 | Submit valid content | Note saved, user taken to new note's detail page | | | |
| WORKFLOW-05 | Newly created note appears in Reference panel on Unit detail page | Note visible, correctly under its parent unit | | | |
| WORKFLOW-06 | Newly created note shows "Unlinked" status badge | Badge displayed correctly at creation | | | |
| WORKFLOW-07 | Submit empty/invalid content | Clear error message shown, note not created | | | |
| WORKFLOW-08 | Click Cancel on create form | Returns to previous page via `?next=`, no note created | | | |


**Story 19 — Create MyWords note (linked or standalone)**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| WORKFLOW-09 | Create linked MyWords note from Reference detail view | Create My Words page loads | | | |
| WORKFLOW-10 | Reference note shown collapsed on linked-creation page | Reference content collapsed/expandable | | | |
| WORKFLOW-11 | Create standalone MyWords note from Unit detail page | Create My Words page loads, no Reference association | | | |
| WORKFLOW-12 | Create standalone MyWords note from sidebar | Create My Words page loads correctly attached to the right unit via context, no Reference association | | | |
| WORKFLOW-13 | Submit valid form | Note created, user taken to new note's detail page | | | |
| WORKFLOW-14 | Newly created MyWords note appears in Unit detail page, MyWords panel | Note visible, correctly under its parent unit | | | |
| WORKFLOW-15 | Origin badge on newly created MyWords note | Badge correctly indicates origin - "From Reference" vs "Standalone" - matching how it was created | | | |
| WORKFLOW-16 | Reference note's status updates after a linked MyWords note is created from it | Reference badge changes from "Unlinked" to "Linked" on Unit detail page and Reference detail page | | | |
| WORKFLOW-17 | Submit invalid/empty content (both linked and standalone) | Clear error message shown, note not created | | | |
| WORKFLOW-18 | Click Cancel on create form (both linked and standalone) | Returns to previous page via `?next=`, no note created | | | |


**Story 20 — Create Question note (linked or standalone)**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| WORKFLOW-19 | Create linked Question note from Reference detail view | Create Question page loads | | | |
| WORKFLOW-20 | Reference note shown collapsed on linked-creation page | Reference content collapsed/expandable | | | |
| WORKFLOW-21 | Create standalone Question note from Unit detail page | Create Question page loads, no Reference association | | | |
| WORKFLOW-22 | Create standalone Question note from sidebar | Create Question page loads correctly attached to the right unit via context, no Reference association | | | |
| WORKFLOW-23 | Submit valid form | Note created, user taken to new note's detail page | | | |
| WORKFLOW-24 | Newly created Question note appears in Unit detail page, Question panel, with "Unanswered" status badge | Note visible under correct unit, badge shows Unanswered by default | | | |
| WORKFLOW-25 | Reference note's status updates after a linked Question note is created from it | Reference badge changes from "Unlinked" to "Linked" on Unit detail page and Reference detail page | | | |
| WORKFLOW-26 | Submit invalid/empty content (both linked and standalone) | Clear error message shown, note not created | | | |
| WORKFLOW-27 | Click Cancel on create form (both linked and standalone) | Returns to previous page via `?next=`, no note created | | | |


**Story 21 — Answer a Question via linked MyWords note**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| WORKFLOW-28 | "Answer in My Words" option present on Question detail view | Option visible, leads to MyWords create form linked to that Question | | | |
| WORKFLOW-29 | Both parent Reference and the Question shown collapsed on MyWords create page (when Question is itself linked to a Reference) | Both notes shown collapsed/expandable for context while answering | | | |
| WORKFLOW-30 | MyWords create page when Question is standalone (no parent Reference) | Only the Question shown collapsed | | | |
| WORKFLOW-31 | Submit valid answer | MyWords note created and linked to the Question, user taken to new note's detail page | | | |
| WORKFLOW-32 | Question's status badge updates after linked MyWords note created | Badge changes from "Unanswered" to "Answered" on Unit detail page and Question detail page | | | |
| WORKFLOW-33 | New MyWords note's origin badge | Displays "From Question" | | | |


**Story 22 — View notes linked from a Reference note**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| WORKFLOW-34 | Reference detail page displays linked MyWords notes | List shown when one or more MyWords notes are linked to this Reference | | | |
| WORKFLOW-35 | Reference detail page displays linked Question notes | List shown when one or more Question notes are linked to this Reference | | | |
| WORKFLOW-36 | Reference with no linked notes of a given type | Section for that type not shown| | | |
| WORKFLOW-37 | Each linked note shows identifying info (title and content preview) in correct category | User can tell what the note is without opening it | | | |
| WORKFLOW-38 | Click a linked MyWords note in the list | Navigates to that note's detail page | | | |
| WORKFLOW-39 | Click a linked Question note in the list | Navigates to that note's detail page | | | |


**Story 23 — View notes linked to a Question note**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| WORKFLOW-40 | Question detail page displays linked MyWords notes | List shown when one or more MyWords notes are linked as answers | | | |
| WORKFLOW-41 | Question with no linked MyWords note (Unanswered) | Section not shown | | | |
| WORKFLOW-42 | Each linked MyWords note shows identifying info (title and content preview) | User can tell what the note is without opening it | | | |
| WORKFLOW-43 | Click a linked MyWords note in the list | Navigates to that note's detail page | | | |

##### UI/UX Theme
**Story 24 - Home page**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| HOME-01 | Value proposition displayed | Tagline/headline clearly visible on home page | | | |
| HOME-02 | "How it works" explanation present | Note-taking flow explained on home page | | | |
| HOME-03 | Primary "Get started" CTA present | Visible, clearly the primary action on the page | | | |
| HOME-04 | Click "Get started" | Navigates to Sign up page | | | |
| HOME-05 | Footer attribution and links | Footer displays attribution and relevant links | | | |

**Story 25 - Walkthrough**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| HIW-01 | Walkthrough explains Source → Unit → Note hierarchy | Clear explanation present | | | |
| HIW-02 | Walkthrough explains three note types and their purpose | Reference, MyWords, Question each explained | | | |
| HIW-03 | Walkthrough accessible from main nav at any time | Link present in nav regardless of logged-in state or current page | | | |
| HIW-04 | Empty states explain role of structure/workflow | Empty states (Sources, Units, per-tab Notes) include explanatory text, not just "nothing here" | | | |

**Story 26 - External feedback form**

| Test ID | Test | Expected | Actual | Local | Deployment |
|---------|------|----------|--------|-------|------------|
| GF-01 | Feedback link visible from key pages | Present in footer/nav consistently | | | |
| GF-02 | Feedback link opens Google Form in new tab | Opens `target="_blank"` (with `rel="noopener"`), user's place in app preserved | | | |


---

## Story-to-Test Mapping

## Solved Bugs

*Flat list — bug, cause, fix.*
**Bug: Long source_name without white spaces causes horizontal scroll / layout break**
Found via: Pass 1 model-to-UI audit — specifically while testing source_name at its model-defined max_length=255 boundary (MNM-04).
What happens: A long, unbroken string (no spaces) in source_name doesn't wrap — it pushes the container wider, forcing horizontal scroll instead of wrapping to a new line.
Severity/threshold: Worse than initially assumed to be an "edge case" —

- Breaks around ~117 characters on desktop
- Breaks around ~27 characters on the smallest mobile breakpoint
This is a realistic scenario, not just an edge case: source_type includes WEBSITE as one of its 8 choices, and a natural way to name a website source is to paste its URL directly into source_name — which is exactly the kind of unbroken string that triggers this bug.
Fix: add word-break: break-word to source-name class.

**Dashboard accessible via browser back button after logout**

Description:After logging out and being redirected to the home page, pressing the browser's back button displays the dashboard as if the user is still logged in. This is caused by the browser serving a cached version of the page without re-validating with the server, bypassing Django's session authentication check.
Fix: Add cache-control headers to the dashboard view to prevent the browser from caching the page.

Commit: `c9dd47c`

**Follow-up: other authenticated pages had the same issue, plus bfcache bypass**

During final Pass 1 testing I discovered that all pages that require authentication except for Dashboard did not have this security system in place and were accessible to logged out user via browser back button. I added @never_cache to all views in notes, except delete views which only have a POST branch. Still some content was shown after logout via browser back button due to bfcache mechanism.

Fix: add pageshow reload in notes.js
Commit: `a61023b`


**Sticky top bug**
*Description:* Sticky-top not sticking in Chrome/Edge despite correct computed CSS (`position: sticky`, `top: 0`); confirmed broken on both mobile and desktop viewports, independent of pagination changes. `getBoundingClientRect` confirms nav moves with scroll instead of pinning.

*Ruled out:*
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

*Further complication with scroll behaviour*

On create_reference.html specifically, triggering a scroll (by increasing the content textarea beyond 5 rows) caused the fixed navbar and sidebar to briefly visually separate — a gap opening between them for the duration of the scroll. Reducing the textarea back to 5 rows keeps the page short enough that no scroll ever occurs, avoiding the issue entirely rather than resolving its underlying cause.
Later on the same bug was seen in dashboard when source form was expanded. I devised a wordaround solution by givine the sidebar a height of 120vh and a z-index of 98, while for nav a z-index of 99. Now the two at least scroll together as below, avoiding the awkward white gap. Since sidebar only appears on desktop, this device cannot affect mobile or tablet views.

By contrast, create_question.html and create_mywords.html scroll regardless of how many textarea rows are set — even at 5 rows or fewer, the page still triggers a scrollbar. On these two pages, however, the navbar and sidebar scroll away together, moving as a consistent unit rather than separating from each other, so no gap appears. Since the specific issue being guarded against (a visible gap between navbar and sidebar) doesn't occur here, no row-count workaround was applied to these two pages, and their scrolling behavior was left as-is.

*Fix: always remember your tutor's fixes*
Finally, after going through all that trouble, both on my own and with Claude AI, I remembered I had a similar problem in my first project, and the fix was given by my tutor: put sticky on parent element. I put class 'sticky-top' on header instead of nav, and it works! It seems the olden days remedies still work in the age of AI. Thank you, Kevin!


**test_duplicate_source_name_raises_error fails**
*Description:* Automated test fails and raises Integrity Error at database level, instead of returning a 200 status code wit a form error.

*Verified manually:* Confirmed in browser — submitting a duplicate source name at `/dashboard/` raised an unhandled `IntegrityError` before the fix.
[Unhandled Integrity Error](testing_screenshots/dp-mt-08.png)

*Cause:* Missing form-level validation — duplicate data passed `form.is_valid()` and reached the database, which rejected it with an `Integrity Error`.

*Fix:* Added `__init__` to `SourceForm` to accept `user` as a keyword argument; updated dashboard view to pass `user=request.user` to the form; added `clean()` to validate duplicate source names per user before saving.


**Visiting sources/800/delete/ returns Value Error instead of 404**
*Description* Authenticated user types sources/800/delete/ in local environment and gets ValueError.

*Evidence*

[DP-MT-25 Value Error](testing_screenshots/dp-mt-25.png)

*Automated test*

Confirmed by `test_authenticated_user_gets_404_for_missing_source` - DP-AT-08 failing with `AssertionError: 301 != 404`
Initial automated test returned 301 (redirect) due to missing trailing slash in test URL. Once corrected, test confirmed the same ValueError seen in the browser.

*Root cause*
The view had no return for GET requests which were falling through and getting a None.

*Fix*
Add return for GET requests. Both manual and automated tests now passing.

*Commit:* `1b4bcdd`


**Error not shown after login attempt with incorrect credentials**

After removing crispy forms from sign in template and adding custom form for styling purposes, error message would not show on login attempt with invalid credentials. Fixed with Claude AI by adding `{{form.non_field_errors}}` to form.



## Known Bugs / Limitations

*Flat list — bug, and explanation of why it remains unfixed.*

## Validation

### HTML — W3C validator

The following pages have been validated with [W3C](https://validator.w3.org/):
- [index.html](docs/readme-assets/home-validation.png) - no errors or warnings to show
- [how_it_works.html](docs/readme-assets/how-it-works-validation.png) - no errors or warnings to show
- [signup.html](docs/readme-assets/sign-up-validation.png) - no errors or warnings to show
- [login.html](docs/readme-assets/sign-in-validation.png) - no errors or warnings to show
- [dashboard.html](docs/readme-assets/dashboard-validation.png) - no errors or warnings to show
- [source_detail.html](docs/readme-assets/source-detail-validation.png) - no errors or warnings to show
- [unit_detail.html](docs/readme-assets/unit-detail-validation.png) - no errors or warnings to show
- [create_reference.html](docs/readme-assets/create-reference-validation.png) - no errors or warnings to show
- [reference_detail.html](docs/readme-assets/reference-detail.png) - no errors or warnings to show
- [edit_reference.html](docs/readme-assets/edit-reference-validation.png) - no errors or warnings to show
- [create_mywords](docs/readme-assets/create-mywords-validation.png) - no errors or warnings to show
- [edit_mywords](docs/readme-assets/edit-mywords-validation.png) - no errors or warnings to show
- [create_question.html](docs/readme-assets/create-question-validation.png) - no errors or warnings to show
- [question_detail.html](docs/readme-assets/question-detail-validation.png) - no errors or warnings to show
- [edit_question.html](docs/readme-assets/edit-question-validation.png) -no errors or warnings to show
-
### CSS — Jigsaw validator

The following pages have been validated with [W3C Jigsaw validator](https://jigsaw.w3.org/css-validator/):
- [notes.css](docs/readme-assets/css-validation.png) - no error found
- [style.css](docs/readme-assets/) - no error found
- **JavaScript** — JSLint
### Python — PEP8

The following pages have been validated with [Code Institute CI Python Linter](https://pep8ci.herokuapp.com/#):
- [notes/models.py](docs/readme-assets/notes_models_validation.png) - no errors found
- [notes/tests/test_models.py](docs/readme-assets/notes_test_models_validation.png) - no errors found
- [notes/forms.py](docs/readme-assets/notes_forms_validation.png) - no errors found
- [notes/tests/test_forms.py](docs/readme-assets/notes_test_forms_validation.png) - no errors found
- [notes/context_processors.py](docs/readme-assets/notes-context-processor-validation.png) - no errors found
- [notes/urls.py](docs/readme-assets/notes_urls_validation.png) - no errors found
- [notes/views.py](docs/readme-assets/notes_views.png) - no errors found
- [notes/tests_views.py](docs/readme-assets/notes_tests_views_validation.png) - not errors fourd.
- [notes/admin.py](docs/readme-assets/notes_admin_validation.png) - no errors found
- [pages/urls.py](docs/readme-assets/pages_urls_validation.png) - no errors found
- [pages/views.py](docs/readme-assets/pages_views_validation.png) - no errors found
- [forms.py](docs/readme-assets/forms_validation.png) - no errors found
- [urls.py](docs/readme-assets/urls_validation.png) - no errors found

 **Lighthouse** — performance, accessibility, best practices, SEO
