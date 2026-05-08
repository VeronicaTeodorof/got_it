# Field Specifications


## User


### User ID  

| Property | Value |
|---|---|
| Parent table | User |  
| Specification type | Unique |  
| Description | A unique integer that identifies a single user record within the database. It enables the app to keep track of all its users. |  
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0-9) |  
| Key type | Primary |  
| Uniqueness | Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits not allowed |

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


### Source ID  

| Property | Value |
|---|---|
| Parent table | Source |  
| Specification type | Unique |
| Description | A unique integer that identifies a single source record within the database. It enables the app and the user to keep track of all Sources. |  
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0-9) |  
| Key type | Primary |  
| Uniqueness | Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits not allowed |  


### User ID   

| Property | Value |
|---|---|
| Parent table | Source |  
| Specification type | Replica |  
| Source specification | User ID number from the User table |
| Shared by | User, Source, Source Type, Tag | 
| Description | A unique integer that identifies a single user record within the database. It enables the app to keep track of all its users. |  
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0-9) |  
| Key type | Foreign |  
| Key structure | Simple |
| Uniqueness | Non-Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits not allowed | 


### Source Type ID  

| Property | Value |
|---|---|
| Parent table | Source |
| Specification type | Replica |  
| Source specification | Source Type ID number from the Source Type table |  
| Shared by | Source Type, Source |
| Description | A unique integer that identifies a single source type record within the database. It enables the app to keep track of all its source types. |  
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0-9) |  
| Key type | Foreign |  
| Key structure | Simple |
| Uniqueness | Non-Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits allowed | 


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
| Length | None |
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
| Length | None |
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


### Source Type ID  

| Property | Value |
|---|---|
| Parent table | Source Type |  
| Specification type | Unique |
| Description | A unique integer that identifies a single source type record within the database. It enables the app to keep track of all Source Types. |  
| Data type | Numeric | 
| Length | 10 |  
| Character support | Numbers (0-9) |  
| Key type | Primary |  
| Uniqueness | Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits not allowed |   


### User ID   

| Property | Value |
|---|---|
| Parent table | Source Type |  
| Specification type | Replica |  
| Source specification | User ID number from the User table |
| Shared by | User, Source, Source Type, Tag | 
| Description | A unique integer that identifies a single user record within the database. It enables the app to keep track of all its users. |  
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0-9) |  
| Key type | Foreign |  
| Key structure | Simple |
| Uniqueness | Non-Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits not allowed | 

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
| Key type | Alternate |
| Uniqueness | Unique |
| Null support | No nulls |
| Values entered by | User |
| Required | Yes |
| Edit rule | Enter now, edits allowed |  
| Range of values | Any title up to 50 characters. |  

Note: Definitions for Source Type Creation Date and Source Type Last Modified date showed no real value for these fields and therefore they've been removed altogether.


## Unit


### Unit ID  

| Property | Value |
|---|---|
| Parent table | Unit |  
| Specification type | Unique |  
| Description | A unique integer that identifies a single unit record within the database. It enables the app and the user to keep track of all Units. |  
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0-9) |  
| Key type | Primary |  
| Uniqueness | Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits not allowed |

### Source ID

| Property | Value |
|---|---|
| Parent table | Unit |
| Specification type | Replica |
| Source specification | Source identification number from Source table |
| Shared by | Source, Unit |
| Description | A unique integer that identifies a single source record within the database. It enables the app to keep track of all sources. |
| Data type | Numeric |  
| Length | 10| 
| Character support | Numbers (0-9) |
| Key type | Foreign |
| Key structure | Simple |
| Uniqueness | Non-unique |
| Null support | No nulls |
| Values entered by | System |
| Required | Yes |  
| Range of values | Any positive integer |
| Edit rule | Enter now, edits not allowed |  


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
| Range of values | Any name up to 100 characters. |
| Edit rule | Enter now, edits allowed |  


Note: Definition for Unit Creation Date showed no real value for this field and therefore it has  been removed.


### Unit Last Modified Date

| Property | Value |
|---|---|
| Parent table | Unit |
| Specification type | Unique |
| Description | The year, month, day and time a specific unit record was last edited in the app. It allows the app and the user to sort units by most recent activity, making it easy to return to work in progress. |
| Data type | Date/Time |  
| Length | None |
| Decimal places | None |
| Key type | Non |
| Uniqueness | Non-unique |
| Null support | No nulls |
| Values entered by | System |
| Required | Yes |  
| Range of values | Any date/time not earlier than the unit creation date|
| Edit rule | Enter now, edits not allowed |


### Unit Type

| Property | Value |
|---|---|
| Parent table | Unit |
| Specification type | Unique |
| Description | Indicates whether a unit was created automatically by the system or by the user. It allows the app to identify and handle default units differently, for example by sorting "My Thoughts" first in the unit list. |
| Data type | Boolean |  
| Length | None |
| Decimal places | None |
| Key type | Non |
| Uniqueness | Non-Unique |
| Null support | No nulls |
| Values entered by | System |
| Required | Yes |  
| Range of values | Default, Custom |
| Edit rule | Enter now, edits not allowed |


## Tag 


### Tag ID  

| Property | Value |
|---|---|
| Parent table | Tag |  
| Specification type | Unique |  
| Description | A unique integer that identifies a single tag record within the database. It enables the app to keep track of all tags. |  
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0-9) |  
| Key type | Primary |  
| Key structure | Simple |
| Uniqueness | Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Range of values | Any positive integer |  
| Required | Yes |  
| Edit rule | Enter now, edits not allowed |  


### User ID   

| Property | Value |
|---|---|
| Parent table | Tag |  
| Specification type | Replica |  
| Source specification | User ID number from the User table |
| Shared by | User, Source, Source Type, Tag | 
| Description | A unique integer that identifies a single user record within the database. It enables the app to keep track of all its users. |  
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0-9) |  
| Key type | Foreign |  
| Key structure | Simple |
| Uniqueness | Non-Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits not allowed | 

### Tag Name

| Property | Value |
|---|---|
| Parent table | Tag |
| Specification type | Unique |
| Description | A user-defined word or short expression that labels a note to add meaning to it, enabling the student to group and retrieve related notes across all sources within the application. |
| Data type | Alphanumeric |
| Length | 50 |
| Decimal places | None |
| Character support | Letters (A–Z), Numbers (0–9), Keyboard ( . , / $ # % ) |
| Key type | Alternate |
| Key structure | Simple |
| Uniqueness | Unique |
| Null support | No nulls |
| Values entered by | User |
| Required | Yes |  
| Range of values | Any name up to 50 characters |
| Edit rule | Enter now, edits allowed |


## Note Tags

### Tag ID


| Property | Value |
|---|---|
| Parent table | Note Tags |
| Specification type | Replica |  
| Source specification | Tag identification number from the Tag table |
| Shared by | Tag, Note Tags |
| Description |  A unique integer that identifies a single tag record within the database. It enables the app to keep track of all tags. |
| Data type | Numeric |
| Length | 10 |
| Decimal places | None |
| Character support | Numbers (0–9) |
| Key type | Foreign |
| Key structure | Composite |
| Uniqueness | Non-Unique |
| Null support | No nulls |
| Values entered by | System |
| Required | Yes |  
| Range of values | Any positive integer |
| Edit rule | Enter now, edits not allowed |


### Note ID


| Property | Value |
|---|---|
| Parent table | Note Tags |
| Specification type | Replica |  
| Shared by | Note, Note Tags, Reference, Own-Words, Question | 
| Source specification | Note identification number from the Note table |
| Description |  A unique integer that identifies a single note record within the database. It enables the app to keep track of all notes. |
| Data type | Numeric |
| Length | 10 |
| Character support | Numbers (0–9) |
| Key type | Foreign |
| Key structure | Composite |
| Uniqueness | Non-Unique |
| Null support | No nulls |
| Values entered by | System |
| Required | Yes |  
| Range of values | Any positive integer |
| Edit rule | Enter now, edits not allowed |


## Note 


### Note ID  

| Property | Value |
|---|---|
| Parent table | Note |  
| Specification type | Unique |   
| Description |  A unique integer that identifies a single note record within the database. It enables the app and to keep track of all notes. |  
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0–9) |  
| Key type | Primary |  
| Uniqueness | Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits not allowed |


### Unit ID

| Property | Value |
|---|---|
| Parent table | Note |  
| Specification type | Replica |  
| Source specification | Unit identification number from Unit table | 
| Shared by | Unit, Note | 
| Description | A unique integer that identifies a single unit record within the database. It enables the app to keep track of all units. |
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0–9) |  
| Key type | Foreign |  
| Key structure | Simple |  
| Uniqueness | Non-unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits not allowed |


### Note Title  

| Property | Value |
|---|---|
| Parent table | Note |  
| Specification type | Unique |  
| Description | A short heading that summarises the main idea of a note. It allows the student to identify and distinguish it from other notes at a glance. |  
| Data type | Alphanumeric |  
| Length | 100 |  
| Character support | Letters (A–Z), Numbers (0–9), Keyboard ( . , / $ # % ), Special ( © ® ™ ) |  
| Key type | Non |  
| Uniqueness | Non-unique |  
| Null support | Nulls-Allowed |  
| Values entered by | User |  
| Required | No |  
| Range of values | Any title up to 100 characters |  
| Edit rule | Enter now, edits allowed |


### Note Content  

| Property | Value |
|---|---|
| Parent table | Note |  
| Specification type | Unique |  
| Description | The body of a note, containing the student's written record of the material being studied. It is the primary substance of the note. |  
| Data type | Alphanumeric |  
| Length | 10000 |  
| Character support | Letters (A–Z), Numbers (0–9), Keyboard ( . , / $ # % ), Special ( © ® ™ ) |  
| Key type | Non |  
| Uniqueness | Non-unique |  
| Null support | No nulls | 
| Values entered by | User |  
| Required | Yes |  
| Range of values | Any non-empty string of characters up to 10,000 characters, excluding strings composed entirely of whitespace |  
| Edit rule | Enter now, edits allowed |



### Note Creation Date  

| Property | Value |
|---|---|
| Parent table | Note |  
| Specification type | Unique |
| Description | The year, month, day and time a specific note record was created in the app. It allows the app and the user to sort notes in chronological or reverse chronological order. |  
| Data type | Date/time |  
| Length | None |  
| Key type | Non |  
| Uniqueness | Non-Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any date/time not earlier than the app launch date. |  
| Edit rule | Enter now, edits not allowed |



### Note Last Modified Date  

| Property | Value |
|---|---|
| Parent table | Note |  
| Specification type | Unique |  
| Description | The year, month, day and time a specific note record was last edited in the app. It allows the app and the user to sort notes by most recent activity, making it easy to return to work in progress. |  
| Data type | Date/time |  
| Length | None |  
| Key type | Non |  
| Uniqueness | Non-Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any date/time not earlier than the note creation date. |  
| Edit rule | Enter now, edits not allowed |


## Reference


### Ref ID  

| Property | Value |
|---|---|
| Parent table | Reference |  
| Specification type | Unique |  
| Description | A unique integer that identifies a single reference record within the database. It enables the app to keep track of all Reference notes. |  
| Data type | Numeric |  
| Length | 10 |
| Character support | Numbers (0-9) |  
| Key type | Primary |  
| Uniqueness | Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits not allowed |  


### Note ID  

| Property | Value |
|---|---|
| Parent table | Reference |  
| Specification type | Replica |  
| Shared by | Note, Note Tags, Reference, Own-Words, Question |  
| Source specification | Note identification number from Note table |  
| Description |  A unique integer that identifies a single note record within the database. It enables the app to keep track of all notes. |  
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0–9) |  
| Key type | Foreign |  
| Key structure | Simple | 
| Uniqueness | Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits not allowed |


### Ref Active Status  

| Property | Value |
|---|---|
| Parent table | Reference |  
| Specification type | Unique |  
| Description | A binary yes or no status indicating whether the student has made a decision regarding the comprehension of a reference note. It allows the user to distinguish between notes that have been acted on and those that have been deferred. |  
| Data type | Boolean |  
| Length | None |  
| Key type | Non |  
| Uniqueness | Non-Unique |  
| Null support | No nulls |  
| Values entered by | User |  
| Required | Yes |  
| Range of values | Yes, No |  
| Edit rule | Enter now, edits allowed |


## Own-Words 


### Own-Words ID  

| Property | Value |
|---|---|
| Parent table | Own-Words |  
| Specification type | Unique |  
| Description | A unique integer that identifies a single user own-words note within the database. It enables the app to keep track of all the Own-Words Notes. |  
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0-9) |  
| Key type | Primary |  
| Key structure | Simple |  
| Uniqueness | Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits not allowed |  


### Note ID  

| Property | Value |
|---|---|
| Parent table | Own-Words |  
| Specification type | Replica |  
| Shared by | Note, Note Tags, Reference, Own-Words, Question |  
| Source specification | Note identification number from Note table |  
| Description |  A unique integer that identifies a single note record within the database. It enables the app to keep track of all notes. |  
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0–9) |  
| Key type | Foreign |  
| Key structure | Simple | 
| Uniqueness | Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits not allowed |


### Ref ID

| Property | Value |
|---|---|
| Parent table | Own-Words |  
| Specification type | Replica |  
| Source specification | Reference identification number from Reference table |   
| Shared by | Reference, Own-Words, Question |  
| Description | A unique integer that identifies a single reference record within the database. It enables the app to keep track of all Reference notes. |  
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0-9) |  
| Key type | Foreign |  
| Key structure | Simple |  
| Uniqueness | Non-Unique |  
| Null support | Nulls Allowed | 
| Values entered by | System |  
| Required | No |
| Range of values | Any positive integer | 
| Edit rule | Enter now, edits not allowed |


## Question 


### Question ID  

| Property | Value |
|---|---|
| Parent table | Question |  
| Specification type | Unique |
| Description | A unique integer that identifies a single question record within the database. It enables the app to keep track of all Questions. |  
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0-9) |  
| Key type | Primary |  
| Uniqueness | Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits not allowed |  


### Note ID  

| Property | Value |
|---|---|
| Parent table | Question |  
| Specification type | Replica |  
| Shared by | Note, Note Tags, Reference, Own-Words, Question |  
| Source specification | Note identification number from Note table |  
| Description |  A unique integer that identifies a single note record within the database. It enables the app to keep track of all notes. |  
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0–9) |  
| Key type | Foreign |  
| Key structure | Simple | 
| Uniqueness | Unique |  
| Null support | No nulls |  
| Values entered by | System |  
| Required | Yes |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits not allowed |


### Ref ID 

| Property | Value |
|---|---|
| Parent table | Question |  
| Specification type | Replica |  
| Source specification | Reference identification number from Reference table |  
| Shared by | Reference, Question, Own-Words |  
| Description | A unique integer that identifies a single reference record within the database. It enables the app and the user to keep track of all Reference notes.|  
| Data type | Numeric | 
| Length | 10 |  
| Character support | Numbers (0-9) |  
| Key type | Foreign |  
| Uniqueness | Non-Unique |  
| Null support | Nulls-Allowed |  
| Values entered by | User |  
| Required | No |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits allowed |  


### Own-Words ID  

| Property | Value |
|---|---|
| Parent table | Own-Words |  
| Specification type | Replica |  
| Shared by | Own-Words, Question |  
| Source specification | Own-Words identification number from Own-words table |
| Description | A unique integer that identifies a single Own-Words record within the database. It allows the app and the user to keep track of all Own-Words notes. |  
| Data type | Numeric |  
| Length | 10 |  
| Character support | Numbers (0-9) |  
| Key type | Foreign |  
| Key structure | Simple |  
| Uniqueness | Non-Unique |  
| Null support | Nulls allowed |  
| Values entered by | User |  
| Required | No |  
| Range of values | Any positive integer |  
| Edit rule | Enter now, edits not allowed |  


### Answered Status  

| Property | Value |
|---|---|
| Parent table | Question |  
| Specification type | Unique |  
| Description | A binary yes or no status indicating whether a question note has been answered. It allows the user to distinguish between resolved and unresolved questions. |  
| Data type | Boolean |  
| Length | None |  
| Key type | Non |  
| Uniqueness | Non-Unique |  
| Null support | No nulls |  
| Values entered by | User |  
| Required | Yes |  
| Range of values | Yes, No |  
| Edit rule | Enter now, edits allowed |


### Marked Status  

| Property | Value |
|---|---|
| Parent table | Question |  
| Specification type | Unique |
| Description | A binary yes or no status indicating whether the user is satisfied with their own-words answer and has consciously resolved the question. It allows the user to distinguish between questions they consider fully understood and those they still have doubts about. |  
| Data type | Boolean |  
| Length | None |  
| Key type | Non |  
| Uniqueness | Non-Unique |  
| Null support | No nulls |  
| Values entered by | User |  
| Required | Yes |  
| Range of values | Yes, No |  
| Edit rule | Enter now, edits allowed |




