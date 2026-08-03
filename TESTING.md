# Testing

## How this document is organised, and why

Testing here is done in two passes, because a single approach — either reading the code or clicking through the app — would each miss things the other one catches.

**Pass 1 audits the code itself, file by file** (models, forms, views), checking whether everything defined in the backend actually reaches the user: every field surfaces somewhere, every piece of business logic has a visible effect, nothing was built and then silently left disconnected from the interface. This pass has two parts per file: an automated part, testing the code's logic in isolation (constraints, custom validation, business rules) with no browser involved, and a manual part, confirming that logic actually renders correctly once it reaches a template.

**Pass 2 tests the app the way a real user would — action by action**, rather than file by file. Anything that recurs across multiple pages (access control, authentication, navigation) is tested once, as its own category, rather than repeated per page. Anything unique to a single feature (creating a Source, linking a note) is tested where it happens.

Together, the two passes cover what neither one does alone: Pass 1 catches things invisible from clicking around — a field that exists but never displays, logic with no visible effect. Pass 2 catches things invisible from reading code — a view that works in isolation but the wrong template renders, or a flow that works from one entry point but not another.

Note: The two-pass testing methodology (code-to-UI audit, then user-perspective testing) and its categorisation are my own; AI articulated these ideas into accurate wording (file intro, names of the two passes, and some other category names), drafted the skeleton  and sanity checked the idea and structure. I reread and edited the draft where necessary.

## Contents

1. [Pass 1 — Code Audit](#pass-1--code-audit)
      - [Automated tests](#automated-tests)
      - [Manual tests - code reflection in UI](#manual-tests--code-reflection-in-ui)
2. [Pass 2 — User-Perspective Testing](#pass-2--user-perspective-testing)
3. [Solved Bugs](#solved-bugs)
4. [Known Bugs / Limitations](#known-bugs--limitations)
5. [Validation](#validation)
---

## Pass 1 — Code Audit

### Automated tests

#### notes app
##### models.py

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


##### forms.py
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

##### views.py

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



##### urls.py

#### pages app
##### views.py
##### urls.py

#### got_it project
##### urls.py (root — confirms each app is correctly included)
##### settings.py

### Manual tests — code reflection in UI

#### notes app
##### models.py
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

##### forms.py

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| MNF-01 | Test 'type' and not '----' is displayed first in source type choices | for loop in SourceForm correctly reaches UI | Pass |
| MNF-02 | Test error message for duplicate source name | Error message for duplicate source name correctly displays in UI | Pass |
| MNF-03 | Test in edit mode rewriting the same source name doesn't raise error | Submits with name unchanged or cleared and typed again | Pass |
| MNF-04 | Test error message for duplicate unit name | Error message for duplicate unit name within a source correctly displays in UI | Pass |
| MNF-05 | Test in edit mode rerwiting the same unit name doesn't raise error | Submits with name unchanged or cleared and typed again | Pass |


##### views.py

**All Views**

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| MNV-01 | Log in, view a page in notes, log out, click browser back button; repeat for all pages in notes | @never_cache, pageshow reload, and @login_required together prevent cached authenticated content from being shown after logout, redirecting to Sign In instead | Pass |
| MNV-02 | Anonymous user typing correctly formated url gets redirected to sign in | Verified all @login_required views redirect anonymous users to login rather than exposing content or returning a 404, confirming no route bypasses authentication | Pass |

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




##### urls.py

##### notes.js


| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| MNJS-01 | Log in, view a page in notes, log out, click browser back button; repeat for all pages in notes | @never_cache, pageshow reload, and @login_required together prevent cached authenticated content from being shown after logout, redirecting to Sign In instead | Pass |


##### templates
#### pages app
##### views.py
##### urls.py
##### templates

#### got_it project
##### urls.py
##### settings.py
##### context processors / shared templates

---

## Pass 2 — User-Perspective Testing

### Repeating categories

#### Authentication: sign up / log in / session (AUTH)

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
#### NAV-EXT (external links)
#### NAV-SIDEBAR (source/unit tree)
#### NAV-OFFCANVAS (offcanvas for mobile)
#### NAV-BACK (back link for mobile)
#### NAV-BREAD (breadcrumbs)
#### NAV-PAGE (pagination)
#### NAV-LINK (note-to-note linking)
#### A11Y (accessibility)
#### RESPONSIVE (responsiveness across breakpoints)

Each category tested against:
- **Local**
- **Deployed**
### Per-feature tests

#### Source CRUD
#### Unit CRUD
#### Reference note CRUD
#### MyWords note CRUD
#### Question note CRUD
#### Home Page
#### How it Works Page
#### Other per-page features

Each tested against:
- **Local**
- **Deployed**
---

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


## Known Bugs / Limitations

*Flat list — bug, and explanation of why it remains unfixed.*

## Validation

- **HTML** — W3C validator
- **CSS** — Jigsaw validator
- **JavaScript** — JSLint
### Python — PEP8

The following pages have been validated with [Code Institute CI Python Linter](https://pep8ci.herokuapp.com/#):
- [notes/models.py](docs/readme-assets/notes_models_validation.png) - no errors found
- [notes/tests/test_models.py](docs/readme-assets/notes_test_models_validation.png) - no errors found
- [notes/forms.py](docs/readme-assets/notes_forms_validation.png) - no errors found
- [notes/tests/test_forms.py](docs/readme-assets/notes_test_forms_validation.png) - no errors found

- **Lighthouse** — performance, accessibility, best practices, SEO
  (cross-references A11Y and RESPONSIVE categories in Pass 2 — a mechanical
  complement to those manual checks, not a replacement)