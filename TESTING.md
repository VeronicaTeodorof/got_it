## User Acceptance Tests (UAT)


### Authentication 


| Test | Expected | Actual |Local | Deployment |
|------|----------|-------|-------|------------|
| Visit /accounts/signup/ | Signup form loads | Signup form loads | Pass | |
| Visit /accounts/signin/ | Signin form loads | Signin form loads | Pass | |
| Submit signup form without email | Form not submitted, error shown | Form not submitted, prompts to fill out email field | Pass | |
| Submit signup form without username | Form not submitted, error shown | Form not submitted, prompts to fill out username field | Pass | |
| Submit signup form without password 1 | Form not submitted, error shown | Form not submitted, prompts to fill out password 1 field | Pass | |
| Submit signup form without password 2 | Form not sumbitted, error shown | Form not submitted, prompts to fill out password 2 field | Pass | |
| Submit signup form with mismatched passwords | Form rejected, error shown | Password fields cleared, no error message in Edge | Failed | | 
| Submit signup form with mismatched passwords | Form rejected, error shown | Password fields cleared, no error message in Chrome | Failed | |
| Submit signup form with all valid fields | Account created, redirected to homepage | Account created, redirected to homepage | Pass | |


### Known Bugs

| Bug | Status |
|-----|--------|
| Mismatched passwords clears form with no error message | Open |


