# Testing

## How this document is organised, and why

Testing here is done in two passes, because a single approach — either reading the code or clicking through the app — would each miss things the other one catches.

**Pass 1 audits the code itself, file by file** (models, forms, views), checking whether everything defined in the backend actually reaches the user: every field surfaces somewhere, every piece of business logic has a visible effect, nothing was built and then silently left disconnected from the interface. This pass has two parts per file: an automated part, testing the code's logic in isolation (constraints, custom validation, business rules) with no browser involved, and a manual part, confirming that logic actually renders correctly once it reaches a template.

**Pass 2 tests the app the way a real user would — action by action**, rather than file by file. Anything that recurs across multiple pages (access control, authentication, navigation) is tested once, as its own category, rather than repeated per page. Anything unique to a single feature (creating a Source, linking a note) is tested where it happens.

Together, the two passes cover what neither one does alone: Pass 1 catches things invisible from clicking around — a field that exists but never displays, logic with no visible effect. Pass 2 catches things invisible from reading code — a view that works in isolation but the wrong template renders, or a flow that works from one entry point but not another.

Note: The two-pass testing methodology (code-to-UI audit, then user-perspective testing) and its categorisation are my own; AI articulated these ideas into accurate wording (file intro, names of the two passes, and some other category names), drafted the skeleton  and sanity checked the idea and structure. I reread and edited the draft where necessary.

## Contents

1. [Pass 1 — Code Audit](#pass-1--code-audit)
2. [Pass 2 — User-Perspective Testing](#pass-2--user-perspective-testing)
3. [Solved Bugs](#solved-bugs)
4. [Known Bugs / Limitations](#known-bugs--limitations)
5. [Validation](#validation)
---

## Pass 1 — Code Audit

### Automated tests

#### notes app
##### models.py
##### forms.py
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
##### forms.py
##### views.py
##### urls.py
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

## Known Bugs / Limitations

*Flat list — bug, and explanation of why it remains unfixed.*

## Validation

- **HTML** — W3C validator
- **CSS** — Jigsaw validator
- **JavaScript** — JSLint
- **Python** — PEP8
- **Lighthouse** — performance, accessibility, best practices, SEO
  (cross-references A11Y and RESPONSIVE categories in Pass 2 — a mechanical
  complement to those manual checks, not a replacement)