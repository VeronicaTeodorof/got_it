# got it?

## Goals
### Developer Goals:
- to apply lessons learned from previous projects: improve commit messages,
- to develop an application with an intuitive design, never assuming users will know what to do

## User Stories

- **Workflow Theme**
1. As a student, I want a reminder to be selective when writing a reference note, so that I can evaluate whether an idea is worth capturing.
2. As a student I want to be asked whether I understood a reference note after saving it, so that I can immediately link it to an own words note, a question note, or defer the decision for later.
3. As a student I want the option to defer the comprehension check on a reference note when I'm not ready to evaluate my understanding, so that I can return to it later without pressure.
4. As a student, I want to link my own-words and question notes to the reference note they stem from, so that I can trace ideas back to their source and evaluate how well I understood them.
5. As a student, I want to be prompted to explain an idea in simple terms when writing an own-words note, so that I am reminded to avoid jargon and test my real understanding.
6. As a student, I want to easily notice which question notes are still unanswered, so that I can prioritize them during revision.
7. As a student I want to be able to check questions as answered after linking them to own words notes, so that I make a conscious decision that the respective idea is understood.
8. As a student I want to be able to differentiate between linked and unlinked reference notes, so that I make the unlinked ones a priority.
9. As a student I want to be able to turn my question notes into own words notes when I find the answers, so that I can work through my understanding.
10. As a student I want to be able to create an own-words note, optionally linked to a reference note, so that I can either process a source or capture my own thinking independently.
11. As a student, I want to create a question note optionally linked to a reference note or an own-words note, so that I can track gaps in my understanding whether they arise from a source or my own thinking.

- **UI/UX Theme**
<details>
<summary>12 As a user I want a consistent, responsive navigation bar with links relevant to my authentication state so that I can easily move between key pages and understand at a glance whether I'm signed in.</summary>

**Acceptance Criteria:**
- AC1: Navbar displays the app logo, linking to the home page - see MNAV-MT-01
- AC2: Navbar shows Home, and either (Dashboard, Logout) or (Sign In, Sign Up) depending on authentication state - see MNAV-MT-02, MNAV-MT-03, MNAV-MT-04, MNAV-MT-06, MNAV-MT-07, MNAV-MT-09, MNAV-MT10
- AC3: Navbar remains usable and readable across mobile and desktop breakpoints
- AC4: Navbar container switches between full-width and constrained-width layout at the medium breakpoint - see MNAV-MT-02
- AC5: All navbar links are keyboard-navigable with visible focus indicators
</details>
<details>
<summary>13 As a user, I want an intuitive way to move between levels of my content, so that I can navigate through it without clutter or confusion.</summary>

**Acceptance Criteria:**
- AC1: Secondary nav displays a back-link to the level above, with a short label describing the destination - see SNAV-MT-01
- AC2: All links navigate to the correct page - see SNAV-MT-02
- AC3: Secondary nav shows a hamburger menu opening an offcanvas nav where there is sufficient content to move more than one level up or down
- AC4: On desktop, navigation options are shown directly in the sidebar
- AC5: Sidebar and offcanvas share identical navigation content, switching presentation at the large breakpoint
</details>
<details>
<summary>14 As a new or returning user I want to see a home page that presents the app's value and gives me clear options to sign up or log in so that I can understand what the app offers and easily get started.</summary>

Acceptance Criteria:
- AC1: Home page displays the app's value proposition (tagline/headline) - see  HP-MT-01
- AC2: Home page displays a "How it works" explanation of the note-taking flow - see HP-MT-02
- AC3: Home page displays a primary "Get started" CTA - see HP-MT-03
- AC4: Clicking 'Get started' link navigates to Sign up page - see HP-MT-04
- AC5: Home page footer displays attribution and relevant links - see HP-MT-05, HP-MT-06 and HP-MT-07
</details>
<details>
<summary>15. As a user I want a dashboard so that I have a central place to access and manage my content</summary>

Acceptance Criteria:
- AC1: Page only accessible to logged-in users — unauthenticated users redirected to login -see DP-AT-01 and DP-AT-02;
- AC2: Page shows a list of sources belonging to the logged in user - see DP-MT-03;

</details>

16. As a student I want a quick capture option for own words and question notes directly from the dashboard, so that I don't lose a thought while navigating the app.
17. As a student I want to see my most recent activity from the dashboard, so that I can quickly pick up where I left off.
18. As a new user I want to trigger a walkthrough from the home page so that I can understand how the app works before signing up.
<details>
<summary>19. As a user, I want the app to work on mobile, tablet and desktop, so that I can take notes on any device.</summary>

Acceptance Criteria:
**Home Page**:
- AC1: Home page content reflows correctly on mobile viewports (single-column stack: headline, CTA, diagram, text, footer all stack vertically) -see RES-MT-08
- AC2: Home page content displays as a two-column layout on tablet/desktop viewports (≥768px) for the "How it works" diagram and explanation -see RES-MT-09
- AC3: Navigation bar remains usable and readable at all tested breakpoints (no overlapping or cut-off links) - see RES-MT-10
- AC4: Footer remains pinned to the bottom of the viewport when content is shorter than the screen, on all tested breakpoints -see RES-MT-11
- AC5: Images/diagrams scale appropriately without distortion or overflow at each breakpoint - see RES-MT-12

- Sidebar is visible by default on desktop → RES-MT-02
- Sidebar is hidden by default on mobile and can be opened via the toggler → RES-MT-03, RES-MT-05
- Toggler is visible on mobile and hidden on desktop → RES-MT-04
- Sidebar sits below the navbar on all screen sizes → RES-MT-07
- No horizontal scrolling on any screen size → RES-MT-01
</details>
20. As a student with learning difficulties, I want the app to meet accessibility standards, so that I can use it without barriers.

- **CRUD Functionality Theme**

- **Sources**
<details>
<summary>21. As a student, I want to see all my sources in a list, so that I can navigate to the one I want to work on.</summary>

Acceptance Criteria:

- AC1: Only shows sources belonging to the logged-in user - see DP-AT-03 and DP-AT-04
- AC2: Sources listed in reverse chronological order — most recent first - see DP-MT-05
- AC3: Each source shows name,type, author, and date created - see DP-MT-04
- AC4: Each source links to its unit list page
- AC5: Empty state shown when no sources exist, encouraging user to create one - see DP-MT-06
</details>
<details>
<summary>22. As a student I want to be able to create a source, so that I can organise my notes around a single book, course, or subject.
</summary>
Acceptance Criteria:

- AC1: User can enter a source name and a source author - see DP-MT-07;
- AC2: User should select a source type from the available options - see DP-MT-08;
- AC3: Name field cannot be empty — error shown if submitted blank - see DP-MT-09;
- AC4: Source type has to be selected - error shown if not selected - see DP-MT-10;
- AC5: On successful creation user is redirected to the new source detail page - see DP-MT-11
- AC6: A user cannot create two sources with the same name, an error is shown if they try - see DP-MT-12 and DP-AT-06
</details>

23. As a student, I want to be able to view all my sources filtered by type, so that I can quickly find material of a specific kind such as all my books or all my lectures.
<details>
<summary>24. As a student I want to be able to edit a source name, author, or type, so that I can keep it accurate.</summary>

Acceptance Criteria:

- AC1: Only accessible to logged-in users - see DP-MT-14
- AC2: Only accessible to the source owner — another logged-in user gets a 404 - see DP-MT-15 and DP-AT-07
- AC3: User can edit source name, author, and type - see DP-MT-16
- AC4: Name field cannot be empty — error shown if submitted blank - see DP-MT-17
- AC5: On successful edit user is redirected back to the dashboard page - see DP-MT-18
- AC6: One type choice has to be selected - error shown if no choice is selected - see DP-MT-19
</details>
<details>
<summary>25. As a student I want to be able to delete a source with confirmation step when I no longer need it, so that my dashboard stays uncluttered.</summary>

- AC1: Only accessible to logged-in users; unauthenticated user is redirected to login page - see DP-MT-26, DP-MT-27, DP-AT-09
- AC2: Only accessible to the source owner — another logged-in user gets a 404 see DP-MT-25 and DP-MT-26
- AC3: Deleting a source removes it from the sources list - see DP-MT-28
- AC4: User is redirected to the sources page after deletion - see DP-MT-28
- AC5: A confirmation step is required before deletion - see DP-MT-29
- AC6: Source name and author appear in confirmation step to avoid confusions - DP-MT-30
- AC7: A confimation message appears after successful deletion - DP-MT-31
- AC8: When a source is deleted, all its units and notes are deleted as well
</details>

 - **Units**

<details>
<summary>26. As a student, I want to see all the units within a specific source, so that I can navigate to the unit I want to work on</summary>

Acceptance Criteria:


- AC1: Page only accessible to logged-in users — unauthenticated users redirected to login - see SDP-AT-01, SDP-AT-02, SDP-MT-01, SDP-MT-02
- AC2: Page only accessible to the source owner — another logged-in user gets a 404 - see SDP-AT-03 and SDP-MT-03
- AC3: If source does not exist, return 404 - see SDP-AT-04
- AC4: Source name and author displayed - see SDP-AT-05
- AC5: Units listed in most recent edited order
- AC6: Each unit shows name and note count
- AC7: Each unit links to its three-column unit page
- AC8: Sidebar shows Sources link - see SDP-MT-06
- AC9: Edit and delete unit actions accessible for each unit on this page
- AC10: Only and all units belonging to current source are displayed in the list of units - see SDP-AT-05, SDP-AT-06, SDP-MT-08, and SDP-MT-09
- AC11: Empty state shown when no unitss exist, encouraging user to create one - see SDP-MT-07

</details>
<details>
<summary>27. As a student I want to be able to create a unit within a source, so that I can organise my notes by topic.</summary>

Acceptance Criteria:

- AC1: Create unit button is present on source detail page - see SDP-MT-10
- AC2: Clicking create unit button will expand the create unit form - see SDP-MT-11
- AC3: Save and Cancel buttons are present on create unit form - see SDP-MT-12
- AC4: Cancel button collapses the form - see SDP-MT-13
- AC5: Cancel button resets the form - see SDP-MT-14
- AC6: User can enter a unit name - see SDP-MT-15
- AC7: Name field cannot be empty — error shown if submitted blank - see SDP-MT-16
- AC8: On successful creation user is redirected to the new unit detail page
- AC9: A user cannot create duplicate name units within a source -  an error is shown if they try - see SDP-MT-18 and SDP-AT-07
- AC10: When there are errors on the form, page loads with expanded form so feedback is immediately visible - see SDP-MT-19
</details>
<details>
<summary>28. As a student I want to be able to rename a unit, so that I can keep it aligned with my source structure.</summary>

Acceptance Criteria:
- AC1: Edit button present in list element dropdown - see SDP-MT-20
- AC2: Clicking Edit button expands inline form - see SDP-MT-21
- AC3: Edit form is prepopulated with correct data - see SDP-MT-22 and SDP-AT-08
- AC4: User can edit unit name in form - see SDP-MT-23
- AC5: Save and Cancel buttons present on the form - see SDP-MT-24
- AC6: Submitting empty unit name field rerenders the form with errors - see SDP-MT-25
- AC7: Submitting form with valid data saves the form and reloads source detail page with edited unit - see SDP-MT-26
- AC8: Cancel button collapses the form - see SDP-MT-27
- AC9: Cancel button resets the form -see SDP-MT-28
- AC10: Submitting the form with duplicate name rerenders the form with error - see SDP-MT-29
</details>
<details>
<summary>29. As a student I want to be able to delete a unit with a confirmation step when I no longer need it, so that I can keep my source structure tidy.</summary>

Acceptance Criteria:
- AC1: Delete button present on inline dropdown - see SDP-MT-30
- AC2: Clicking delete button opens a confirmation modal - see SDP-MT-31
- AC3: Confirmation modal has source and unit names included along with risks warnings, so that user does not accidentaly delete wrong unit - see SDP-MT-32
- AC4: Delete and Cancel buttons present on modal - see SDP-MT-33
- AC5: Delete button deletes unit, closes modal and rerenders page with updated units list - see SDP-MT-34
- AC6: Cancel button closes modal - see SDP-MT-35
- AC7: Page accessible to logged in owners, unauthenticated users are redirected to login - see SDP-MT-36 and SDP-MT-38
- AC8: Trying to access an inexisting unit gives 404 - see SDP-MT-37
</details>


- **Notes**
<details>
<summary>30. As a student I want to be able to see a list of all my notes in a specific unit, organized by type, so that I have an ensemble view of what's done and what's left and easily access the ones I need.</summary>

Acceptance Criteria:


- AC1: Page only accessible to logged-in users — unauthenticated users redirected to login - see UDP-AT-01, UDP-AT-02, UDP-MT-01 and UDP-MT-02
- AC2: Page only accessible to the source owner — another logged-in user gets a 404 - see UDP-AT-03 and UDP-MT-03
- AC3: If unit does not exist, return 404 - see UDP-AT-04 and UDP-MT-04
- AC4: Unit name is displayed - see UDP-AT-05 and UDP-MT-05
- AC5: Notes are organized by type
- AC6: Sidebar shows Sources and Units links
</details>

**Reference Notes**
<details>
<summary>31. As a user, I want to view the full content of a reference note, see its location, add linked notes, and view any notes already linked to it, so that I can engage with the material and build on my understanding.</summary>

Acceptance Criteria:

- AC1: Page only accessible to logged-in users — unauthenticated users redirected to login -see RDP-MT-01, RDP-MT-02 and RDP-AT-01
- AC2: Page only accessible to the source owner — another logged-in user gets a 404 -see RDP-MT-03
- AC3: If reference note does not exist, return 404 - see RDP-MT-04
- AC4: Title, content and location show on the page - see RDP-MT-05
- AC5: Add dropdown visible on the page
- AC6: A button to show/hide notes linked to this reference is visible on the page
- AC7: Clicking the links button expands a list of linked notes
- AC8: Empty state message is shown when no links exist and 'got it?' logo appears above the add button
</details>
<details>
<summary>32. As a student, I can create a reference note, so that I can track where my information comes from and return to the source when needed.</summary>

Acceptance Criteria:

- AC1: Page only accessible to logged-in users — unauthenticated users redirected to login - see CRP-MT-03 and CRP-MT-06
- AC2: `New` link visible below Reference tab - see CRP-MT-04
- AC3: `+` link visible in sidebar near Reference link - see CRP-MT-05
- AC4: Clicking either create reference buttons links to create_reference.html - see CRP-MT-01, CRP-MT-02
- AC5: User can enter title, content and location - see CRP-MT-07
- AC6: Saving note without content prompts error message - see CRP-MT-08
- AC7: Save button present on the page - see CRP-MT-09
- AC8: Submitting form with valid data redirects to unit-detail page with new note displaying first in grid see CRP-MT-10
- AC9: Success message displayed on unit detail page after valid reference note save - see CRP-MT-11

</details>
<details>
<summary>33. As a student I can edit a reference note, so that I can keep my source information accurate</summary>

Acceptance Criteria:

- AC1: Page only accessible to logged-in users — unauthenticated users redirected to login
- AC2: Page only accessible to the source owner — another logged-in user gets a 404
- AC3: If reference note does not exist, return 404
- AC4: Edit icon present on reference note detail page - see RDP-MT-06
- AC5: Tooltip appears on hover - see RDP-MT-07
- AC6: Clicking edit icon loads edit reference page - see RDP-MT-08
- AC7: Form is preloaded with data from requested reference note - see ERP-MT-03
- AC8: Saving edited note redirects to reference detail page with edited note shown - see ERP-MT-04
- AC9: Saving note with blank body prompts error - see ERP-MT-05
- AC10: Cancel button present on edit page - see ERP-MT-01
- AC11: Clicking cancel button loads reference detail page - see ERP-MT-02
</details>

34. As a student I want to be able to delete any of my notes with a confirmation step, so that I can declutter my notes without accidentally losing them.
35. As a student I want to be able to search for a specific note, so that I can easily find one when I need it.

- **Tags**
36. As a student I want to be able to assign one or more tags to a note, so that I can connect related notes across different sources.
37. As a student I want to be prompted with a list of already used tags when tagging a note, so that I keep my tags consistent and avoid duplicates.
38. As a student I want to be able to remove a tag from a note, so that I can correct mistakes or update connections.
39. As a student I want to be able to see all notes associated with a tag in one view, so that I can explore connections between ideas across sources.

- **Authentication Theme**
<details>
<summary>40. As a new user I want to be able to create a new account, to start using the app.</summary>
Acceptance criteria:

- AC1: User can access the signup page - see AUTH-MT-01

- AC2: User must provide a username and password - see AUTH-MT-03 and AUTH-MT-04

- AC3: Error messages are shown for invalid or missing fields - see AUTH-MT-03 to AUTH-MT-07 and AUTH-MT-09

- AC4: User is redirected to dashboard page after successful signup - see AUTH-MT-30

- AC5: Password must meet minimum security requirements (length, complexity) - see  AUTH-MT-10 to AUTH-MT-13
</details>
<details>
<summary>41. As a user I want to be able to sign into my account, to be able to access my notes and create new ones.</summary>
Acceptance criteria:

- AC1: User can access the signin page - see AUTH-MT-02

- AC2: User can sign in with valid credentials - see AUTH-MT-16

- AC3: Error shown for incorrect password - see AUTH-MT-17

- AC4: Error shown for unregistered email/username - see AUTH-MT-18

- AC5: Error shown for missing fields - see AUTH-MT-19 and AUTH-MT-20

- AC6: User is redirected to dashboard on successful signin - see AUTH-MT-16

- AC7: User remains on signin page if login fails - see AUTH-MT-17 to AUTH-MT-20
</details>
<details>
<summary>42. As a user, I want to log out of my account so that I can securely end my session.</summary>
Acceptance criteria:

- AC1: User can see a logout link on the dashboard - see DP-MT-01

- AC2: Clicking logout ends the user's session - see AUTH-MT-21

- AC3: User is redirected to the home page after logging out - see AUTH-MT-31

- AC4: User cannot access the dashboard after logging out - see AUTH-MT-22 and AUTH-MT-32
</details>
43. As a user I want to be able to reset my password, so as not to lose access to my account when I forget it.
<details>
<summary>44. As a user I want to stay logged in between sessions, so that I don't have to sign in every time.</summary>
Acceptance criteria:

- AC 1: User sees a "Remember Me" checkbox on sign in page - see AUTH-MT-23

- AC 2: When a user logs in with "Remember me" checked, their session persists after closing and reopening the browser - see AUTH-MT-24

- AC 3: When a user logs in without "Remember me" checked, their session ends when the browser is closed - see AUTH-MT-26

- AC4: After a defined period of inactivity, the session expires and the user is prompted to log in again, even if "Remember me" was checked - see AUTH-MT-27

- AC5: The user can manually log out at any time, which ends the session immediately regardless of "Remember me" - see AUTH-MT-28
</details>
45. As a user I want to be able to delete my account with confirmation step when I consider I don't need it anymore, so that I can be in control of my information.
46. As a new user I want to verify my email address after registering, so that my account is secure and recoverable.


## ERD
Entity Relationship Diagram showing the core data structure: User, Source, Source Type, Unit, Note, Tags, Note Tags, Reference, Own-Words and Questions.

![ERD](docs/readme-assets/got_it_erd.png)


## Development Process (Agile Workflow)

1. Check the user story;
2. Write acceptance criteria and tasks if not already in issue;
3. Move to respective iteration if not already there;
4. Move to In Progress in Project Board;
5. Write acceptance criteria in README user story;
6. Plan the code;
7. Write code;
8. Write automated tests;
9. Run automated tests, fix if failing, and document in TESTING.md;
10. Write manual tests in TESTING.md;
11. Link tests with acceptance criteria in README;
12. Update README if any decisions were made;
13. Move issue to done on project board;
14. Commit;

## Design Decisions

### Onboarding through empty states

Empty states are treated as onboarding moments rather than placeholders — each one teaches the user what to do next and why, instead of just indicating that content is missing, reinforcing the app's structure and pedagogy at the exact moment it's relevant.

- **Sidebar reflects data existence** — the sidebar stays empty on first interaction, since the dashboard's primary call-to-action is the sole entry point for a new user; showing sidebar content with nothing to navigate would compete with that and add confusion rather than help.


### Navigation Architecture
**Problem**
The original mobile layout used a single unlabeled forward arrow to open the offcanvas navigation. This created a real usability gap: nothing on the page told users how to get back to the sources list. The arrow itself pointed forward, so even users who tried it for that purpose were working against its visual meaning, and there was no separate, correctly-oriented control for returning to a previous page at all. Users had no reliable way to navigate back.

**Goals:**

- Make every navigation control state where it leads.
- Avoid redundant navigation paths (the same destination reachable two different visible ways on the same screen).
- Reflect the app's actual hierarchy (Source → Unit → Note) rather than imposing a flat menu that implies destinations aren't really reachable.
- Scale gracefully from mobile to desktop without maintaining two unrelated navigation systems.

**Approach considered and rejected: persistent icon rail**
An early option was a slim, always-visible sidebar with single-letter abbreviations (S / U / N) for Sources, Units, Notes. This was rejected because:

Notes aren't reachable without first selecting a Unit, so a flat S/U/N rail would need disabled/dimmed states at shallower depths, which adds complexity without adding real navigation.
The rail's contents would need to change shape depending on the current page (dashboard vs. source detail vs. unit detail), undermining the consistency it was meant to provide.

**Final approach: two-tier navigation + depth-aware menu**
Top navbar (unchanged): brand mark, Home, Dashboard, Log out. Persistent across all pages and breakpoints.
Mobile: second nav bar, directly below the top navbar, contextual per page:

Left: a single labelled back-link combining "go up" and "go to creation" into one destination, since both land on the same list/index page (e.g. "Change source or add one", "Change unit or add one", "Change note or add a new one"). On the new-note page specifically, this becomes "View all notes", since there's nothing yet to "change."
Right (only on pages with more than one add-action or a multi-level jump need): "Menu" + hamburger icon, opening a Bootstrap offcanvas.

Offcanvas menu appears only from Unit detail downward, since that's the point where a single inline button can no longer represent all available content types. It groups:

Navigation shortcuts to jump more than one level up (Sources, Units).
Add-actions per content type (Sources, Units, Reference, Own words, Questions).

Source detail and Dashboard don't need the menu. For Source detail its only one-level-up path is inline, as are all available actions (single "Create unit" button, three-dot dropdown for edit/delete).
Inline actions (three-dot dropdown for edit/delete) are used consistently at every depth next to the relevant title (source title, unit title), rather than living in the menu, since edit/delete apply to "the thing I'm looking at," not "something I want to navigate to."
Desktop: the second nav bar and offcanvas are replaced by a permanent sidebar, occupying the space already implied by the app's existing vertical accent border. The sidebar shows the same depth-appropriate actions as the offcanvas/back-link combination would on mobile, but always visible, with no back-link duplicate, since showing the same destination two different ways on one screen was judged to be redundant rather than helpful.

**Rule of thumb**
Show exactly what's reachable from the current page, once. A menu (offcanvas or sidebar) is only introduced where a page needs more than one add-action or a jump of more than one level; everything else stays inline.

**Semantic structure**
Decision: the back-link, the burger, and the sidebar link list are all the same category of thing — navigation — just different affordances for it at different screen sizes (a single "up one level" link vs. a menu of destinations). They all live inside one <nav> landmark.

**Page-by-page behavior matrix**

| Page | Back-link (mobile/tablet) | Burger + offcanvas (mobile/tablet) | Sidebar frame (desktop, lg+) |
|------|---------------------------|------------------------------------|------------------------------|
| dashboard | - | - | Always present |
| source_detail | present -> dashboard | - | Always present |
| unit_detail | present -> source_detail | Present | Always present |
| note pages (reference/words/question) | present -> unit_detail | Present | Always present |

Key principle: the sidebar frame itself is unconditional from dashboard upwards — it always renders on desktop, whether or not the current page has populated it with links. This is what makes the coral divider line read as a deliberate, permanent part of the app's chrome rather than something that flickers in and out per page.

The back-link and burger are the only genuinely conditional pieces, and they're controlled entirely by which Django template blocks a page chooses to override

**Template hierarchy**
Two separate layout lineages, split by whether a page needs the app frame (sidebar + secondary nav) or not.

- base.html — head, main nav, footer (unchanged)

  - index.html — home, stays on base.html directly, no sidebar
  - account/login.html
  - account/signup.html
  - app_base.html (NEW — adds secondary nav + sidebar shell)

    - dashboard.html
    - source_detail.html
    - unit_detail.html
    - note_base.html (EXISTING — extends app_base.html, not base.html)

      - create_reference.html
      - edit_reference.html
      - reference_detail.html

**Open item**

Whether the new-note page needs any menu/sidebar at all, deferred until the create-note form is built and its actual length/complexity is known.

### Nested Tree Content Navigation

**Origin**

The nested tree content navigation was proposed by my tutor as an enhancement to site navigation, allowing users to browse their Source → Unit hierarchy without leaving the current page. My tutor's main justification was that users are already familiar with this pattern from file explorer systems. The interaction design, state management approach, and information architecture below were worked out building on my tutor's initial idea and visual example.

**Architecture**

**Implementation across breakpoints**

- For **small** and **medium** screens, an offcanvas for content navigation was already in place; the nested tree would be housed here.
- For **large** screens, horizontal space has to be taken advantage of, so there's no reason the nested tree and main content should be mutually exclusive, which the offcanvas enforces via its backdrop — the two need to live side by side and be accessible at any point. A narrow sidebar for content navigation was already in place for this reason, also carrying the homepage's notebook aesthetic into content pages via its vertical divider. But this was too narrow to house a nested tree, while a permanent wider one would have no justification eating up content space. So the solution was a sliding sidebar: narrow in its default state when navigation content is collapsed, and wider when the tree is expanded.

**Conclusion:** The nested tree navigation needed to be handled on two dimensions:
- **Vertical** — expanding/collapsing the tree content itself.
- **Horizontal** — expanding/collapsing the navigation container: a sliding drawer on sm/md screens, and an expandable sidebar on lg.

**Controlling the two dimensions:**

**Vertical** — Controlling the vertical dimension is handled primarily by the `sidebar-node-toggle` class, attached to a button with an animated right-to-down chevron — a standard, recognizable UX pattern. At the first level it expands Sources; at the second level it expands a Source into its Units. For logical simplicity, and for a default-collapsed consistency site-wide, it was decided that the first-level (master) chevron button would also reset the state of any nested ones beneath it.

**Horizontal** — Controlling the horizontal dimension is handled differently across breakpoints. A default X button closes the offcanvas drawer on small and medium screens. On large screens, the Sources chevron button also toggles the horizontal dimension, since expanding horizontally is only ever justified by expanding vertically as well. However, with a wider sidebar, users may also look for an X button to collapse it back to default, rather than assuming the chevron handles both jobs. So a second X button was added on lg, initially given only its primary task — collapsing horizontally. This created an async between the two dimensions: the possibility of expanded navigation content partially showing inside a sidebar that had returned to its default width. So the X needed to synchronize with the vertical dimension too, and therefore needed to reset it as well.

**Conclusion:** On all breakpoints, animated chevron icon buttons toggle the vertical dimension, with the master Sources toggle also resetting nested ones. On sm/md breakpoints, container dimensions are controlled by the burger menu and offcanvas X button; on lg screens, both the chevron master toggle and a dedicated X button control both dimensions.

**Question:** Should the offcanvas X button also reset the tree?

The answer was yes — both for symmetry with the lg X button, and for consistency with the site-wide default-collapsed policy.

**Result:** There are now two X buttons for the nested tree sidebar, each with separate jobs and code for controlling the horizontal dimension, but sharing common functionality — and duplicate code — for controlling the vertical dimension.

**Question:** To merge or not to merge the two buttons?

**Pros and cons**

*One shared button:*
- **Pro:** the vertical-reset logic (find every open node, close it) is written once and used on every breakpoint, rather than duplicated across two buttons — removing the exact risk that caused the original bug, where one X reset state and the other didn't.
- **Pro:** one element to maintain and test instead of two; a future change to reset behaviour only needs to happen in one place.
- **Pro:** more accurately models the underlying intent — conceptually there is one job ("close/reset whatever is open"), even though the mechanism differs by breakpoint.
- **Con:** the single element now carries logic for two distinct concerns (drawer-dismiss, width-reset) that never fire together, which is less immediately legible from the markup alone than one button per job.
- **Con:** visibility depends on two independent conditions (`.offcanvas.show` OR `.expanded-sidebar`) rather than one, adding a small amount of surface area for a visibility bug if either class falls out of sync with the actual UI state (e.g. resizing across the breakpoint mid-interaction).

*Two separate buttons:*
- **Pro:** each button has exactly one job, which is easier to reason about in isolation and requires no cross-breakpoint visibility logic.
- **Pro:** matches Bootstrap's own default offcanvas structure without needing to repurpose it.
- **Con:** the shared vertical-reset logic still has to live somewhere reachable by both — either duplicated in two listeners, or extracted into one shared function called by two separate buttons. The latter keeps the logic unified but still carries two DOM elements for no functional gain, since the actual fix (unifying the reset logic) has already happened in the JS layer regardless.
- **Con:** duplication (or near-duplication) of listener setup is exactly the category of drift that produced the original bug.

**Result:** One shared button was chosen. Since the vertical-reset requirement is genuinely shared across both breakpoints, and a real bug had already demonstrated what happens when that logic isn't unified, merging was the stronger engineering choice rather than a stylistic preference. A single `.sidebar-close` button carries `data-bs-dismiss="offcanvas"` (Bootstrap's own dismiss hook, functionally relevant only on sm/md) alongside a custom click listener that resets any open `.collapse` elements (functionally relevant on every breakpoint). Visibility is handled entirely in CSS and scoped per context, so the two states never overlap.

X's visibility rule mirrors its reset job symmetrically at each breakpoint: it only ever appears when there is something active for it to close — never as a permanent fixture. On sm/md it appears only while the drawer is open; on lg it appears only while the sidebar is expanded. Had the two breakpoints shared no functionality at all, merging would have been arbitrary consolidation rather than a justified design choice — the shared vertical dimension is what makes one button the right call here.


**Structure**

- **Upper section**: expandable tree — Sources → Units (two levels, hard stop)
- **Lower section** present on note-detail/note-create pages: fixed panel — note-type summary (Reference, My Words, Questions), always visible on individual note pages regardless of sidebar width

**Expand/collapse behavior**

- Sidebar defaults to collapsed (narrow) on every page load — no persisted state, no localStorage
- A single master toggler controls width; expanding any row widens the whole sidebar (one shared width state, not per-level)
- Collapsing (via master toggler or an explicit close) resets all nested expansion — the sidebar always returns to a single known state rather than accumulating stale expand state across navigations
- Each row's name/label navigates; a separate toggler (where present) expands — click targets are never shared between the two actions, to avoid ambiguous clicks

**Why a single "expanded path" instead of per-row booleans**

Only one branch of the tree can be open at a time (e.g. one Source's Units), so state is modeled as a single current path (e.g. `{ sourceId }`) rather than independent flags per row. This means expanding a new Source implicitly closes whatever was previously open, and collapsing is a single reset rather than walking every row.

**Why the tree stops at two levels**

Units don't expand further into individual notes. Instead of a third nesting level, each Unit row surfaces the information that would motivate drilling in: total note count, unlinked Reference count, and unanswered Question count. This gives an at-a-glance view of where attention is needed across *all* Units without requiring navigation into each one — directly supporting the app's active-recall goal (spotting gaps, not just inventory).

**Why the lower panel is separate and non-expanding**

The lower panel shows the same category of information (counts, gap-metrics, create actions) but scoped to the *current* Unit rather than across all Units. Keeping it structurally separate from the tree — and always visible rather than behind a toggle — avoids showing the same fact twice in two places: the tree answers "which Unit needs attention," the panel answers "what's the state of the Unit I'm in now."

**Consistency principle**

Every destination is shown exactly once, in exactly one place. Where duplication risk was identified during design (e.g. note-type counts appearing both in an expanded tree and in the lower panel), the information was deliberately scoped differently (cross-Unit vs current-Unit) rather than shown twice at the same specificity.

**Implementation Phases**

1. **Master toggler** — CSS transition + JS class toggle on sidebar container, `aria-expanded` wiring
2. **Sources section** — add-source link (rendered first) + queryset with annotated Unit counts, per-row toggler
3. **Units section** — add-unit link (rendered first) + queryset with annotated total/unlinked-reference/unanswered-question counts, no further expansion
4. **Lower panel** — note-type counts + gap-metrics + create links, richer detail on note-detail pages, always visible independent of sidebar width


**Sidebar visible on Dashboard**
Dashboard will render the same Sources sidebar as other authenticated pages, rather than excluding it.
Rationale: Sidebar and Dashboard's Source list serve different purposes, not duplicate ones.

Dashboard Source list — record/detail view: full name, author, type, date created, pagination, add-form. Answers "what is this source, and what do I need to manage?"
Sidebar Sources tree — navigation view: condensed, drill-down into Units/Notes. Answers "where do I want to go?"

New users with zero Sources get a distinct empty-state partial (sidebar-empty.html) instead of an empty tree, so first-run dashboard doesn't show two dead panels.
Guardrail: if Dashboard's list ever grows inline expand-into-Units behavior, it starts encroaching on the sidebar's job — at that point re-evaluate

### Naming: Dashboard vs. Sources

The same page is labelled "Dashboard" in the main nav and "Sources" in the sidebar. This is intentional, not inconsistent — the main nav names the page's role relative to the whole site (entry point/overview), while the sidebar names its content relative to the Source→Unit hierarchy (top-level list of sources). Breadcrumbs start at Source level and don't reference this page, so no further reconciliation is needed there.

### Breadcrumbs

 Breadcrumbs omit Dashboard/Sources because the sidebar already provides persistent Source→Unit navigation and orientation across all authenticated views. Including them in the breadcrumb would duplicate that information; the breadcrumb instead acts as a local context label (Source > Unit) rather than a full site trail.

### Source Detail: Inline Edit — Design Decisions

**Architecture: single form, not per-field inline-edit** Source name/author/type are edited together via one Django `<form>` and one POST, not as independent fields with their own save actions (as seen in tools like Jira/GitHub). This is a deliberate simplification: per-field
editing would require JSON endpoints, manual CSRF handling, and JS-driven partial saves — a much larger scope than this page needs right now.Documented tradeoff: this diverges from Atlassian's inline-edit guidance (don't nest inline-edit inside a `<form>`), accepted knowingly.

**Edit mode: server-rendered, not JS-toggled**
Readonly state renders plain text (`<span>`); edit state renders real form controls (`<input>`, `<select>`). Because these are different elements chosen via `{% if edit_mode %}`, entering/leaving edit mode requires a real request — done via a `?edit=1` query param on GET, followed by Edit/Cancel as plain `<a>` links rather than JS-toggled attributes. Chosen to preserve a boxless, text-like readonly look (no border/underline at rest) that a pure attribute-toggle approach couldn't achieve.

**Input styling: underline, not bordered box**
Matches the existing convention from Add Source and auth pages (underline-only inputs, no boxed card). Considered a bordered-box style
(GitHub-style) after feedback that inputs need a clearer edit affordance, but chose to strengthen the underline instead (thicker on focus) to keep one consistent input language across the app, rather than introducing a second visual style for form fields.

**Save/Cancel: icon-only, not text buttons**
Kept as compact check/x icons rather than matching Add Source's full green Save/Cancel buttons. Reasoning: Source Detail's edit row is a
small in-place action within a larger page, not a standalone form — full buttons would compete visually with page content and risk breaking
the single-row layout. Consistency is preserved through color (icons recolored to the same dark green, `#085041`) rather than shape.

**Empty author displays as blank, not "None"**
`source_author` can be stored as `None`/empty. Templates must guard with `|default:''` wherever it's rendered directly, since `{{ value }}`
would otherwise print the literal string "None". Bug caught during manual testing (2026-07-03) on source_detail specifically — dashboard
already had this guard via a truthiness check.

**Long source names: accepted to clip/scroll, not wrap**
`.inline-field` capped at `max-width: 100%` so a very long title can't overflow the viewport. Text scrolls within the input rather than the
box growing or the row wrapping. Considered a tradeoff worth accepting given how rare genuinely long titles are expected to be.


### Visual Hierarchy: Headings, Accents, and Action Color

**Three-tier hierarchy, app-wide**
Every page follows the same visual order:
- muted grey for context (breadcrumbs), matching the introductory part of the tagline in home page,
- dark green + terracota accent for the page heading (most important content),
- solid terracotta for the single primary action on the entire site,
- dark green for all other primaty action buttons.

**Heading accent: fixed-width underline, not full-width**
A short (48px), thick, terracotta bar sits below each page heading, offset by a few pixels rather than hugging the text baseline. Considered a   `full-width `text-decoration: underline` first, but rejected: an underline scaling with text length reads as a link affordance, and grows awkwardly under long titles (e.g. unit or source names). A fixed-width accent, decoupled from text length, keeps the decorative intent unambiguous regardless of heading length, and never suggests the heading itself is clickable.

**Heading font: sans, not italic serif, for in-app pages**
Page headings use the same sans-serif as body text, distinguished by size and weight rather than a decorative typeface. Italic serif was trialled first (echoing the logo's handwritten style) but rejected for in-app headings that wrap user-generated content — italics degrade in legibility as line length grows, and several in-app headings (unit titles, source titles) can't be guaranteed to stay short. The italic serif treatment is reserved for the home page hero section (tagline), where the heading is fixed copy the developer wrote, not user data.

**Terracotta reserved for exactly one action per site**
Actionwise, terracotta (`#bb6f6f`) is used only for the home page's "Get started" CTA — the single most important action across the entire app. Sign in/sign up submit buttons and every create/save action inside the app (Add source, Add unit, Save note, etc.) use dark green instead. Considered scoping terracota to "primary CTA per page" first, but rejected for accessibility reasons.

**Breadcrumbs: muted, not heading-adjacent styling**
Breadcrumb trail (e.g. "Source name > Unit name") uses the same muted grey as the home page's supporting copy, sitting above the heading with tighter spacing to the heading than the heading has to the content below — grouping breadcrumb-and-heading visually as "where am I, then what am I looking at."

### Notes Display

- Unit detail uses Bootstrap tabs (Reference, My Words, Questions) with full-width content area per tab
- Reference notes displayed as Bootstrap card grid (3 columns, h-100 for equal height)
- Cards show title and truncated content preview only
- Evaluated/Pending distinction: green border = evaluated, blue border = pending
- Filter on Reference and Questions tabs: All / Evaluated / Pending (References), All / Answered / Unanswered (Questions)

### Note Relationships

- Reference notes have one-to-many relationship with My Words and Question notes
- Foreign key to parent reference note is nullable — My Words and Question notes can exist independently within a unit (linked to source and unit but not to a specific reference note)
- Answered questions link to one or more My Words notes

### Modals vs Full Pages

- Modals: create/edit source, create/edit unit, delete confirmations
- Full pages: create, read, edit individual notes
- Rationale: notes deserve space and focus; modals suit quick transactional actions

### Terminology

- Consistent naming throughout: Reference, My Words, Questions
- Evaluated/Pending for reference note status
- Answered/Unanswered for question status

### Visual Identity

- Single green accent colour throughout
- "got it?" logo as branding in navbar
- "got it?" logo reused as pending/unanswered indicator on note detail pages
- Bootstrap defaults otherwise — minimal additional styling


### Internationalisation (i18n)
While overriding allauth templates, I came across the i18n library and had to decide whether to implement it across all my templates or remove it from the authentication ones for consistency. Although a note-taking app would benefit from it, this being my first Django project, I considered internationalisation an unnecessary overhead at this stage and added it to the future features list instead.


## Accessibility
- The offcanvas sidebar includes a visually hidden heading so screen readers can identify the region when it opens.
- The sidebar's top offset and height are calculated at runtime via JavaScript rather than hardcoded, so the layout remains correct if a user increases their font size or zoom level.


### Pagination

- Pagination controls are wrapped in a `<nav>` element with a descriptive `aria-label` ("Source list pagination"), distinct from the site's main navigation, so screen reader users can identify and jump to the pagination landmark independently.
- Previous/Next links use `rel="prev"` and `rel="next"` to provide anadditional semantic hint for assistive technology and browsers.
- Previous/Next links are only rendered when a previous or next page actually exists — rather than rendering a disabled or non-functional link, avoiding confusing "dead" links being announced to screen readers.
- Interactive elements inherit the site-wide `:focus-visible` styling (WCAG 2.4.7), ensuring pagination links remain keyboard-navigable with
a visible focus indicator.

## Features
### Security and Data Protection Features:
- Rate limiting (control of how many requests a user/IP can make to an app within a certain time period) provided by Django allauth;
- Account enumeration prevention (stops attackers from figuring out which email addresses/usernames are registered in an app by giving intentionally vague error messages) provided by Django allauth;


### Future features
- Social authentication (Google, GitHub) planned as a future enhancement using django-allauth's built-in social providers
- Internationalisation (i18n) support for multi-language translations using Django's built-in i18n framework

## Future Improvements
- Extend source uniqueness constraint to include 'source_author' and 'source_type' to handle edge cases where same title exists across different authors or formats




## Deployment
### Prerequisites
- Heroku account
- GitHub accout
- Git installed locally
- gunicorn latest version installed locally and added to requirements.txt

### Files Required
- Procfile in the root directory of your project containing the command that Heroku will use to start the server:
 web: gunicorn your-project.wsgi

### Steps
1. Create the Heroku app: sign into your Heroku account, navigate to your dashboard and create a  new app with a unique name;
2. In your app click on the Deploy tab;
3. In the Deployment method section enable GitHub integration by clicking on Connect to GitHub. You may be asked to authenticate with GitHub if this is the first project you deploy with GitHub;
4. In the Search box start typing the name of your project and choose it from the list displayed;
5. Scroll to the bottom of the page and click Deploy Branch to start a manual deployment of the main branch.
6. Click on Open App to view your deployed project;


## Technologies Used
- SVG icons from Bootstrap icons were used inline rather than an icon font library, for reliability and to avoid an additional dependen