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

| Test ID | Test | Covers | Result |
|---------|------|--------|--------|
| MNV-01 | Log in, view a page in notes, log out, click browser back button; repeat for all pages in notes | @never_cache, pageshow reload, and @login_required together prevent cached authenticated content from being shown after logout, redirecting to Sign In instead | Pass |
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

#### PERM (access control)
#### AUTH (sign up / log in / log out / session)
#### NAV-MAIN (navbar)
#### NAV-EXT (external links)
#### NAV-SIDEBAR (source/unit tree)
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