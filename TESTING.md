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
| MT7 | Submit signup form with mismatched passwords | Form rejected, error shown | Password fields cleared, no error message in Edge | Failed | | 
| MT8 | Submit signup form with mismatched passwords | Form rejected, error shown | Password fields cleared, no error message in Chrome | Failed | |
| MT9 | Submit signup form with all valid fields | Account created, redirected to homepage | Account created, redirected to homepage | Pass | |  
| MT10 | Submit signup form with invalid email format (notanemail) | Form rejected, error shown | Form rejected, user prompted to include "@" | Pass | |


### Known Bugs

| Bug | Status |
|-----|--------|
| Mismatched passwords clears form with no error message | Open |


