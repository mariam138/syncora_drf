# Testing Tables

All tables for testing can be found here in this file. Tables for both manual and automated tests can be found here.

## Manual Tests

Separate tables were created for each model and it's API endpoints. Tables were converted to markdown using [tabletomarkdown](tabletomarkdown.com).

### Profile API

| Tested Feature                        | Expected Outcome                                                                                                                                        | Pass/Fail | Notes                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Profile creation                      | When a new user registers, a profile is automatically created for them with a default profile picture                                                   | Pass      | When creating the superuser, I had written the wrong file path for the default image so my image wasn't correct, but an image was appearing in the admin panel. This was then fixed for future profiles.                                                                                                                                |
| View list of profiles                 | At the '/profiles/' URL, a list of profiles can be seen                                                                                                 | Pass      | This was tested before adjusting the serialiser to display more specific fields. This API endpoint is only for testing purposes to see that profiles are being made correctly, and will not be used for the front end. Passes as well after adding custom serialiser fields.                                                            |
| Retrieve profile by id                | When typing 'profiles/:id/ as the URL, retrieve one profile associated with that id                                                                     | Pass      |                                                                                                                                                                                                                                                                                                                                         |
| Edit profile picture on profile by id | If you are the owner of the profile, the profile picture can be changed. No options to update the profile should be available if user is not the owner. | Pass      |                                                                                                                                                                                                                                                                                                                                         |
| Delete profile by id                  | When owner of the profile, I am able to click 'delete' to delete my profile.                                                                            | Pass      |                                                                                                                                                                                                                                                                                                                                         |
| Edit name on profile by id            | If you are the owner of the profile, you are able to update your name.                                                                                  | Fail      | Due to using dot notation to access the first_name field of the User model, this required creating my own update() method for the serialiser. Due to the more complicated nature and time constraints, I decided to remove the ability to edit a name for this project. However this is a feature that can be brought in in the future. |
| Upload new profile picture            | If uploading an image larger than 2MB, a message appears telling the user it is too large and they must upload a smaller image.                         | Pass      |

### Task API

| Tested Feature                | Expected Outcome                                                                                                      | Pass/Fail | Notes                                                                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------- |
| View list of tasks            | At the /tasks endpoint, a list of tasks can be seen.                                                                  | Pass      |                                                                                                                                 |
| View owner's list of tasks    | When logged in, at the /tasks endpoint, a list of only the owner's tasks can be viewed/                               | Pass      |                                                                                                                                 |
| Create a new task             | When logged in, a new task is able to be created.                                                                     | Pass      |                                                                                                                                 |
| Edit, View, Delete task by id | If I am not the owner of the task, I am only able to view it and don't have the options to update or delete the task. | Pass      |                                                                                                                                 |
| Edit task by id               | If I am the owner of the task, I am able to update my task.                                                           | Pass      |                                                                                                                                 |
| View task by id               | I am able to view the task's detail by id, regardless of whether I am the owner or not                                | Pass      | This feature could be handy if a 'followers' model or similar is brought in to allow others to view the task a user has created |
| Delete task by id             | If I am the owner of the task, I am able to delete the task                                                           | Pass      |

### Event API

| Tested Feature              | Expected Outcome                                                                                           | Pass/Fail | Notes |
| --------------------------- | ---------------------------------------------------------------------------------------------------------- | --------- | ----- |
| View list of events         | At /events/ endpoint, a list of events can be seen                                                         | Pass      |       |
| View owner's list of events | When logged in, at the /events endpoint, a list of only the owner's events can be viewed                   | Pass      |       |
| Create a new event          | When logged in, a new event is able to be created. This should not be accessible to unauthenticated users. | Pass      |       |
| View event detail by id     | Any user can view an event detail by id.                                                                   | Pass      |       |
| Update event detail by id   | If the user is the owner, the event can be updated. If not the owner, this functionality is not available. | Pass      |       |
| Delete event detail by id   | If the user is the owner, the event can be deleted. If not the owner, this functionality is not available. | Pass      |

### Note API

| Tested Feature             | Expected Outcome                                                                       | Pass/Fail | Notes |
| -------------------------- | -------------------------------------------------------------------------------------- | --------- | ----- |
| View list of notes         | At the notes/ endpoint, a list of notes can be seen                                    | Pass      |       |
| View owner's list of notes | When logged in, at the /notes endpoint, a list of only the owner's notes can be viewed | Pass      |       |
| Create a new note          | At notes/new/, the user is able to create a note if authenticated.                     | Pass      |       |
| Create a new note          | If unauthorised, the option to create a note is not available.                         | Pass      |       |
| View note detail by id     | Authroised and unauthorised users are able to view a note's detail by id               | Pass      |       |
| Update note by id          | If the owner of the note, the note can then be updated                                 | Pass      |       |
| Delete note by id          | If owner of the note, then the note can be deleted                                     | Pass      |       |
| Update/delete note by id   | If not the owner or an unauthorised user, then these functionalities are not available | Pass      |

## Automated Tests

Separate tables were again made for each API end point. Automated tests were split into their classes and their tests. The result of each individual test is recorded in these tables.

## Profile API Tests

| Test Class             | Test Name                                      | Expected outcome                  | Pass/Fail |
| ---------------------- | ---------------------------------------------- | --------------------------------- | --------- |
| ProfileDetailViewTests | test_retrieve_profile_by_id                    | Get 200 OK response code          | Pass      |
|                        | test_cannot_retrieve_profile_that_doesnt_exist | Do not get 200 OK response code   | Pass      |
|                        |                                                | Get a 404 not found response code | Pass      |

### Events API Tests

| Test Class           | Test Name                                      | Expected outcome                               | Pass/Fail                                                | Notes                                                                                                                                                                                                                                                      |
| -------------------- | ---------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EventListViewTests   | test_view_list_of_events                       | Get a 200 response code                        | Pass                                                     |                                                                                                                                                                                                                                                            |
|                      |                                                | True if the event title is in response.content | Pass                                                     |                                                                                                                                                                                                                                                            |
| CreateEventViewTests | test_authenticated_user_can_create_new_event   | Get 201 created response code                  | Pass                                                     |                                                                                                                                                                                                                                                            |
|                      | test_unauthorised_user_cannot_create_new_event | Get 403 forbidden response code                | Pass                                                     |                                                                                                                                                                                                                                                            |
| EventDetailViewTests | test_user_can_retreieve_event_detail           | Get 200 OK response code                       | Pass                                                     |                                                                                                                                                                                                                                                            |
|                      | test_event_owner_can_update_event              | Get 200 OK response code                       | Fail - with self.client.put, Pass with self.client.patch | As I was using self.client.put, I was getting an assertion error 400 != 200. I learnt that this is because put means replacing all fields of a model, whereas a patch request only updates one field. This test then passed when set to self.client.patch. |
|                      | test_user_cannot_update_another_users_event    | Get 403 forbidden response code                | Pass                                                     |                                                                                                                                                                                                                                                            |
|                      | test_owner_can_delete_event                    | Get 204 no content response code               | Pass                                                     |                                                                                                                                                                                                                                                            |
|                      | test_user_cannot_delete_another_users_event    | Get 403 forbidden response code                | Pass                                                     |

### Notes API Tests

| Test Class          | Test Name                                    | Expected outcome                                 | Pass/Fail |
| ------------------- | -------------------------------------------- | ------------------------------------------------ | --------- |
| NoteListViewTests   | test_view_list_of_notes                      | Get a 200 response status                        | Pass      |
|                     |                                              | True if test note title is in response.content   | Pass      |
|                     |                                              | True if test note content is in response.content | Pass      |
| CreateNoteViewTests | test_authenticated_user_can_create_note      | Get a 201 created response                       | Pass      |
|                     | test_unauthenticated_user_cannot_create_note | Get a 403 forbidden response                     | Pass      |
| NoteDetailViewTests | test_user_can_retreive_note_detail           | Get a 200 response status                        | Pass      |
|                     | test_owner_can_update_own_note               | Get a 200 response status                        | Pass      |
|                     | test_user_cannot_update_another_users_note   | Ensure 200 response status is not received       | Pass      |
|                     |                                              | Get a 403 forbidden response                     | Pass      |
|                     | test_user_can_delete_own_note                | Get a 204 no content response                    | Pass      |
|                     | test_user_cannot_delete_another_users_note   | Get a 403 forbidden response                     | Pass      |
