# Field Specifications


## User

### First Name

| Property | Value |
|---|---|
| Parent table | User |
| Specification type | Unique |
| Description | The first part of a user's full name. It exists to personalise the user's experience within the application. |
| Data type | Alphanumeric |
| Length | 50 |
| Decimal places | None |
| Character support | Letters (A–Z) |
| Key type | Non |
| Uniqueness | Non-unique |
| Null support | No nulls |
| Values entered by | User |
| Required | Yes |
| Range of values | Any string of characters up to 50 |
| Edit rule | Enter now, edits allowed |


### Last Name

| Property | Value |
|---|---|
| Parent table | User |
| Specification type | Unique |
| Description | Last part of a user's full name. Together with the first name, it forms the user's complete name for personalisation purposes. |
| Data type | Alphanumeric |
| Length | 50 |
| Decimal places | None |
| Character support | Letters (A–Z) |
| Key type | Non |
| Uniqueness | Non-unique |
| Null support | No nulls |
| Values entered by | User |
| Required | Yes |
| Range of values | Any string of characters up to 50 |
| Edit rule | Enter now, edits allowed |


### Email Address

| Property | Value |
|---|---|
| Parent table | User |
| Specification type | Unique |
| Description | An expression following the pattern choice@service.something utilized by the user for electronic correspondence. It allows the app to authenticate and communicate with the user |
| Data type | Alphanumeric |
| Length | 254 |
| Decimal places | None |
| Character support | Letters (A–Z), Numbers (0–9), Keyboard ( . , / $ # % ) |
| Key type | Alternate |
| Key structure | Simple |
| Uniqueness | Unique |
| Null support | No nulls |
| Values entered by | User |
| Required | Yes |
| Range of values | Any valid email address format |
| Edit rule | Enter now, edits not allowed |


### Password

| Property | Value |
|---|---|
| Parent table | User |
| Specification type | Unique |
| Description | A set of characters kept secret by the user and utilized in authentication. |
| Data type | Alphanumeric |
| Length | 255 |
| Decimal places | None |
| Character support | Letters (A–Z), Numbers (0–9), Keyboard ( . , / $ # % ), Special ( © ® ™ ) |
| Key type | Non |
| Uniqueness | Non-unique |
| Null support | No nulls |
| Values entered by | User |
| Required | Yes |
| Range of values | Any valid hash string |
| Edit rule | Enter now, edits allowed |


### Email Verification Status

| Property | Value |
|---|---|
| Parent table | User |
| Specification type | Unique |
| Description | A binary yes or no status indicating whether the user has confirmed ownership of the address they provided. It tells the app whether the user is permitted to access their account. |
| Data type | Boolean |
| Length | None |
| Decimal places | None |
| Key type | Non |
| Uniqueness | Non-unique |
| Null support | No nulls |
| Values entered by | System |
| Required | Yes |
| Range of values | True or False |
| Edit rule | Enter now, edits not allowed |


### Username

| Property | Value |
|---|---|
| Parent table | User |
| Specification type | Unique |
| Description | A set of characters chosen by the user to be displayed on their account. It is used by the app to differentiate between its users, along with First and Last Name fields and may also be used for authentication. |
| Data type | Alphanumeric |
| Length | 20 |
| Decimal places | None |
| Character support | Letters (A–Z), Numbers (0–9), Keyboard ( . , / $ # % ) |
| Key type | Alternate |
| Key structure | Simple |
| Uniqueness | Unique |
| Null support | No nulls |
| Values entered by | User |
| Required | Yes |
| Range of values | Any string of characters up to 20 |
| Edit rule | Enter now, edits allowed |