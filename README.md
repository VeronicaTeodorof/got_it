# got it?

## Goals
### Developer Goals:
- to apply lessons learned from previous projects: improve commit messages, 
- to develop an application with an intuitive design, never assuming users will know what to do

## User Stories

- **Workflow Theme**
1. As a student, I want a reminder to be selective when writing a reference note, so that I can evaluate whether an idea is worth capturing.
2. As a student, I can create a reference note, so that I can track where my information comes from and return to the source when needed.
3. As a student I want to be asked whether I understood a reference note after saving it, so that I can immediately link it to an own words note, a question note, or defer the decision for later.
4. As a student I want the option to defer the comprehension check on a reference note when I'm not ready to evaluate my understanding, so that I can return to it later without pressure.
5. As a student, I want to link my own-words and question notes to the reference note they stem from, so that I can trace ideas back to their source and evaluate how well I understood them.
6. As a student, I want to be prompted to explain an idea in simple terms when writing an own-words note, so that I am reminded to avoid jargon and test my real understanding.
7. As a student, I want to easily notice which question notes are still unanswered, so that I can prioritize them during revision.
8. As a student I want to be able to check questions as answered after linking them to own words notes, so that I make a conscious decision that the respective idea is understood.
9. As a student I want to be able to differentiate between linked and unlinked reference notes, so that I make the unlinked ones a priority.
10. As a student I want to be able to turn my question notes into own words notes when I find the answers, so that I can work through my understanding.
11. As a student I want to be able to create an own-words note, optionally linked to a reference note, so that I can either process a source or capture my own thinking independently.
12. As a student, I want to create a question note optionally linked to a reference note or an own-words note, so that I can track gaps in my understanding whether they arise from a source or my own thinking.  

- **UI/UX Theme**
<details>
<summary>13. As a new or returning user I want to see a home page that presents the app's value and gives me clear options to sign up or log in so that I can understand what the app offers and easily get started.</summary>


Acceptance Criteria:   
- AC1: Home page loads without errors - see AT-HP-01  
- AC2: User can see a navigation bar with a signup and login link - see MT-HP-01
- AC3: Clicking signup takes the user to the signup page - see MT-HP-02
- AC4: Clicking login takes the user to the login page - see MT-HP-03
</details>

14. As a user I want a dashboard so that I have a central place to access and manage my content
15. As a student I want to be able to see a list of all the reference notes, own words notes and question notes related to a particular source, so that I have an ensemble view of what's done and what's left.
16. As a student I want a quick capture option for own words and question notes directly from the dashboard, so that I don't lose a thought while navigating the app.
17. As a student I want to see my most recent activity from the dashboard, so that I can quickly pick up where I left off. 
18. As a new user I want to trigger a walkthrough from the home page so that I can understand how the app works before signing up.
19. As a user, I want the app to work on mobile, tablet and desktop, so that I can take notes on any device.
20. As a student with learning difficulties, I want the app to meet accessibility standards, so that I can use it without barriers.  

- **CRUD Functionality Theme**  

- **Notes**
21. As a student I want to be able to modify any note, so that I keep my notes up to date with my understanding.
22. As a student I want to be able to delete any of my notes with a confirmation step, so that I can declutter my notes without accidentally losing them.
23. As a student I want to be able to search for a specific note, so that I can easily find one when I need it.  

- **Sources**
24. As a student I want to be able to create a source, so that I can organise my notes around a single book, course, or subject.
25. As a user, I want to create my own source types, so that I can organise my sources in a way that makes sense to me.
26. As a student, I want to be able to view all my sources filtered by type, so that I can quickly find material of a specific kind such as all my books or all my lectures.
27. As a student I want to be able to edit a source name or type, so that I can keep it accurate.
28. As a student I want to be able to delete a source with confirmation step when I no longer need it, so that my dashboard stays uncluttered.  

- **Units**
29. As a student I want to be able to create a unit within a source, so that I can organise my notes by topic.
30. As a student I want to be able to rename a unit, so that I can keep it aligned with my source structure.
31. As a student I want to be able to delete a unit with a confirmation step when I no longer need it, so that I can keep my source structure tidy.  

- **Tags**
32. As a student I want to be able to assign one or more tags to a note, so that I can connect related notes across different sources.
33. As a student I want to be prompted with a list of already used tags when tagging a note, so that I keep my tags consistent and avoid duplicates.
34. As a student I want to be able to remove a tag from a note, so that I can correct mistakes or update connections.
35. As a student I want to be able to see all notes associated with a tag in one view, so that I can explore connections between ideas across sources.   

- **Authentication Theme**
<details>
<summary>36. As a new user I want to be able to create a new account, to start using the app.</summary>   
Acceptance criteria:  

- AC1: User can access the signup page  

- AC2: User must provide a username and password  

- AC3: Error messages are shown for invalid or missing fields  

- AC4: User is redirected to the homepage after successful signup   

- AC5: Password must meet minimum security requirements (length, complexity)
</details>
<details>
<summary>37. As a user I want to be able to sign into my account, to be able to access my notes and create new ones.</summary> 
Acceptance criteria:  

- AC1: User can access the signin page  

- AC2: User can sign in with valid credential  

- AC3: Error shown for incorrect password  

- AC4: Error shown for unregistered email/username  

- AC5: Error shown for missing fields  

- AC6: User is redirected to homepage on successful signin  

- AC7: User remains on signin page if login fails
</details>
<details>
<summary>38. As a user, I want to log out of my account so that I can securely end my session.</summary>
Acceptance criteria:  

- AC1: User can see a logout link on the dashboard;  

- AC2: Clicking logout ends the user's session;  

- AC3: User is redirected to the index page after logging out;  

- AC4: User cannot access the dashboard after logging out; 
</details>
39. As a user I want to be able to reset my password, so as not to lose access to my account when I forget it.
<details>
<summary>40. As a user I want to stay logged in between sessions, so that I don't have to sign in every time.</summary>
Acceptance criteria: 

- AC 1: User sees a "Remember Me" checkbox on sign in page;  

- AC 2: When a user logs in with "Remember me" checked, their session persists after closing and reopening the browser.  

- AC 3: When a user logs in without "Remember me" checked, their session ends when the browser is closed.  

- AC4: After a defined period of inactivity, the session expires and the user is prompted to log in again, even if "Remember me" was checked.  

- AC5: The user can manually log out at any time, which ends the session immediately regardless of "Remember me".
</details>
41. As a user I want to be able to delete my account with confirmation step when I consider I don't need it anymore, so that I can be in control of my information.
42. As a new user I want to verify my email address after registering, so that my account is secure and recoverable.


## ERD
Entity Relationship Diagram showing the core data structure: User, Source, Source Type, Unit, Note, Tags, Note Tags, Reference, Own-Words and Questions.

![ERD](docs/readme-assets/got_it_erd.png)


## Features 
### Security and Data Protection Features: 
- Rate limiting (control of how many requests a user/IP can make to an app within a certain time period) provided by Django allauth;
- Account enumeration prevention (stops attackers from figuring out which email addresses/usernames are registered in an app by giving intentionally vague error messages) provided by Django allauth;


### Future features
- Social authentication (Google, GitHub) planned as a future enhancement using django-allauth's built-in social providers




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