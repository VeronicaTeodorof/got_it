## Manual Testing (MT)


### Authentication 


| Test ID | Test | Expected | Actual |Local | Deployment |
|---------|------|----------|-------|-------|------------|
| MT1 | Visit /accounts/signup/ | Signup form loads | Signup form loads | Pass | |
| MT2 | Visit /accounts/signin/ | Signin form loads | Signin form loads | Pass | |
| MT3 | Submit signup form without email | Form not submitted, error shown | Form not submitted, prompts to fill out email field | Pass | |
| MT4 | Submit signup form without username | Form not submitted, error shown | Form not submitted, prompts to fill out username field | Pass | |
| MT5 |Submit signup form without password 1 | Form not submitted, error shown | Form not submitted, prompts to fill out password 1 field | Pass | |
| MT6 | Submit signup form without password 2 | Form not sumbitted, error shown | Form not submitted, prompts to fill out password 2 field | Pass | |
| MT7 | Submit signup form with mismatched passwords | Form rejected, error shown | Form rejected, prompts to fill out the same password | Pass | | 
| MT8 | Submit signup form with all valid fields | Account created, redirected to homepage | Account created, redirected to homepage | Pass | |  
| MT9 | Submit signup form with invalid email format (notanemail) | Form rejected, error shown | Form rejected, user prompted to include "@" | Pass | |  
| MT10 | Submit signup form with password similar to other personal information | Form rejected, error shown | Form rejected, "Password too similar to username" shown | Pass | |
| MT11 | Submit signup form with password too short | Form rejected, error shown | Form rejected, "This password is too short. It must contain at least 8 characters." shown | Pass | |
| MT12 | Submit signup form with password too common | Form rejected, error shown | Form rejected, "This password is too common." shown | Pass | |
| MT13 | Submit signup form with password entirely numeric | Form rejected, error shown | Form rejected, "This password is entirely numeric." shown. | Pass | |
| MT14 | Submit signup form with already registered email address | Form rejected, feedback message shown | Form rejected, "A user with that email already exists" shown | Pass | |
| MT15 | Submit signup form with already registered username | Form rejected, feedback message shown | Form rejected, "A user with that username already exists" shown | Pass | |
| MT16 | Submit signin form with valid credentials | Signed in, redirect to homepage | Signed in, redirect to homepage | Pass | |
| MT17 | Submit signin form with incorrect password | Form rejected, error shown | Form rejected, "The username and/or password you specified are not correct." shown | Pass | |
| MT18 | Submit signin form with unregistered email | Form rejected, error shown | Form rejected, "The username and/or password you specified are not correct." shown | Pass | |
| MT19 | Submit signin form without email | Form rejected, error shown | Form refected, user prompted to fill out email field | Pass | |
| MT19 | Submit signin form without password | Form rejected, error shown | Form refected, user prompted to fill out password field | Pass | |


