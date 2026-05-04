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


## Source

### Source Name

| Property | Value |
|---|---|
| Parent table | Source |
| Specification type | Unique |
| Description | The title of the body of material being studied. Serves as the primary identifier for a Source record and allows the user to group, filter, and navigate all notes associated with that material. |
| Data type | Alphanumeric |
| Length | 255 |
| Decimal places | None |
| Character support | Letters (A–Z), Numbers (0–9), Keyboard ( . , / $ # % ), Special ( © ® ™ ) |
| Key type | Non |
| Uniqueness | Non-unique |
| Null support | No nulls |
| Values entered by | User |
| Required | Yes |
| Range of values | Any title up to 255 characters |
| Edit rule | Enter now, edits allowed |


### Source Creation Date

| Property | Value |
|---|---|
| Parent table | Source |
| Specification type | Unique |
| Description | The year, month, day and time a specific source record was created in the app. It allows the app and the user to sort sources in chronological or reverse chronological order. |
| Data type | Date/Time |
| Decimal places | None |
| Key type | Non |
| Uniqueness | Non-unique |
| Null support | No nulls |
| Values entered by | System |
| Required | Yes |
| Range of values | Any date/time not earlier than the app launch date |
| Edit rule | Enter now, edits not allowed |


### Source Last Modified Date

| Property | Value |
|---|---|
| Parent table | Source |
| Specification type | Unique |
| Description | The year, month, day and time a specific source record was last edited in the app. It allows the app and the user to sort sources by most recent activity, making it easy to return to work in progress. |
| Data type | Date/Time |
| Decimal places | None |
| Key type | Non |
| Uniqueness | Non-unique |
| Null support | No nulls |
| Values entered by | System |
| Required | Yes |
| Range of values | Any date/time not earlier than source creation date |
| Edit rule | Enter now, edits allowed |


### Source Author

| Property | Value |
|---|---|
| Parent table | Source |
| Specification type | Unique |
| Description | The people or institutions who created the material being studied. It allows the user to keep an accurate record of the origin of their study materials. |
| Data type | Alphanumeric |
| Length | 100 |
| Decimal places | None |
| Character support | Letters (A–Z), Keyboard ( . , / $ # % ) |
| Key type | Non |
| Uniqueness | Non-unique |
| Null support | Nulls allowed |
| Values entered by | User |
| Required | No |
| Range of values | Any name up to 100 characters |
| Edit rule | Enter now, edits allowed |


## Source Type

### Source Type Name

| Property | Value |
|---|---|
| Parent table | Source Type |
| Specification type | Unique |
| Description | A label that describes the kind of material being studied. It allows the app and the user to organize and retrieve material by this label. |
| Data type | Alphanumeric |
| Length | 50 |
| Decimal places | None |
| Character support | Letters (A–Z), Keyboard ( . , / $ # % ) |
| Key type | Non |
| Uniqueness | Unique |
| Null support | No nulls |
| Values entered by | User |
| Required | Yes |
| Edit rule | Enter now, edits allowed |

Note: Definitions for Source Type Creation Date and Source Type Last Modified date showed no real value for these fields and therefore they've been removed altogether.


## Unit

### Parent Source

| Property | Value |
|---|---|
| Parent table | Unit |
| Specification type | Replica |
| Shared by | Source, Unit |
| Description | The name of the source a unit belongs to. It allows the app and the user to group and retrieve all units associated with a specific source. |
| Data type | Other |
| Decimal places | None |
| Key type | Foreign |
| Key structure | Simple |
| Uniqueness | Non-unique |
| Null support | No nulls |
| Values entered by | User |
| Required | Yes |
| Edit rule | Enter now, edits allowed |


### Unit Name

| Property | Value |
|---|---|
| Parent table | Unit |
| Specification type | Unique |
| Description | The title of a subtheme within a source. It allows the app and the user to identify and navigate to a specific unit within their study material. |
| Data type | Alphanumeric |
| Length | 100 |
| Decimal places | None |
| Character support | Letters (A–Z), Numbers (0–9), Keyboard ( . , / $ # % ) |
| Key type | Non |
| Uniqueness | Non-unique |
| Null support | No nulls |
| Values entered by | User |
| Required | Yes |
| Edit rule | Enter now, edits allowed |


Note: Definition for Unit Creation Date showed no real value for this field and therefore it has  been removed.


### Unit Last Modified Date

| Property | Value |
|---|---|
| Parent table | Unit |
| Specification type | Unique |
| Description | The year, month, day and time a specific unit record was last edited in the app. It allows the app and the user to sort units by most recent activity, making it easy to return to work in progress. |
| Data type | Date/Time |
| Decimal places | None |
| Key type | Non |
| Uniqueness | Non-unique |
| Null support | No nulls |
| Values entered by | System |
| Required | Yes |
| Edit rule | Enter now, edits not allowed |


### Unit Type

| Property | Value |
|---|---|
| Parent table | Unit |
| Specification type | Unique |
| Description | Indicates whether a unit was created automatically by the system or by the user. It allows the app to identify and handle default units differently, for example by sorting "My Thoughts" first in the unit list. |
| Data type | Boolean |
| Decimal places | None |
| Key type | Non |
| Uniqueness | Unique |
| Null support | No nulls |
| Values entered by | System |
| Required | Yes |
| Edit rule | Enter now, edits not allowed |