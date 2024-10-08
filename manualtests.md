# Manual Testing Tables

All tables for manual testing are found in this file. Separate tables were created for each model and it's API endpoints. Tables were converted to markdown using [tabletomarkdown](tabletomarkdown.com).

## Profile API

| Tested Feature                        | Expected Outcome                                                                                                                                        | Pass/Fail | Notes                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Profile creation                      | When a new user registers, a profile is automatically created for them with a default profile picture                                                   | Pass      | When creating the superuser, I had written the wrong file path for the default image so my image wasn't correct, but an image was appearing in the admin panel. This was then fixed for future profiles.                                                                                                                                |
| View list of profiles                 | At the '/profiles/' URL, a list of profiles can be seen                                                                                                 | Pass      | This was tested before adjusting the serialiser to display more specific fields. This API endpoint is only for testing purposes to see that profiles are being made correctly, and will not be used for the front end. Passes as well after adding custom serialiser fields.                                                            |
| Retrieve profile by id                | When typing 'profiles/:id/ as the URL, retrieve one profile associated with that id                                                                     | Pass      |                                                                                                                                                                                                                                                                                                                                         |
| Edit profile picture on profile by id | If you are the owner of the profile, the profile picture can be changed. No options to update the profile should be available if user is not the owner. | Pass      |                                                                                                                                                                                                                                                                                                                                         |
| Delete profile by id                  | When owner of the profile, I am able to click 'delete' to delete my profile.                                                                            | Pass      |                                                                                                                                                                                                                                                                                                                                         |
| Edit name on profile by id            | If you are the owner of the profile, you are able to update your name.                                                                                  | Fail      | Due to using dot notation to access the first_name field of the User model, this required creating my own update() method for the serialiser. Due to the more complicated nature and time constraints, I decided to remove the ability to edit a name for this project. However this is a feature that can be brought in in the future. |
| Upload new profile picture            | If uploading an image larger than 2MB, a message appears telling the user it is too large and they must upload a smaller image.                         | Pass      |

## Task API

| Tested Feature                | Expected Outcome                                                                                                      | Pass/Fail | Notes                                                                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------- |
| View list of tasks            | At the /tasks endpoint, a list of tasks can be seen.                                                                  | Pass      |                                                                                                                                 |
| Create a new task             | When logged in, a new task is able to be created.                                                                     | Pass      |                                                                                                                                 |
| Edit, View, Delete task by id | If I am not the owner of the task, I am only able to view it and don't have the options to update or delete the task. | Pass      |                                                                                                                                 |
| Edit task by id               | If I am the owner of the task, I am able to update my task.                                                           | Pass      |                                                                                                                                 |
| View task by id               | I am able to view the task's detail by id, regardless of whether I am the owner or not                                | Pass      | This feature could be handy if a 'followers' model or similar is brought in to allow others to view the task a user has created |
| Delete task by id             | If I am the owner of the task, I am able to delete the task                                                           | Pass      |

## Event API

| Tested Feature            | Expected Outcome                                                                                           | Pass/Fail | Notes |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- | --------- | ----- |
| View list of events       | At /events/ endpoint, a list of events can be seen                                                         | Pass      |       |
| Create a new event        | When logged in, a new event is able to be created. This should not be accessible to unauthenticated users. | Pass      |       |
| View event detail by id   | Any user can view an event detail by id.                                                                   | Pass      |       |
| Update event detail by id | If the user is the owner, the event can be updated. If not the owner, this functionality is not available. | Pass      |       |
| Delete event detail by id | If the user is the owner, the event can be deleted. If not the owner, this functionality is not available. | Pass      |

## Note API

| Tested Feature           | Expected Outcome                                                                       | Pass/Fail | Notes |
| ------------------------ | -------------------------------------------------------------------------------------- | --------- | ----- |
| View list of notes       | At the notes/ endpoint, a list of notes can be seen                                    | Pass      |       |
| Create a new note        | At notes/new/, the user is able to create a note if authenticated.                     | Pass      |       |
| Create a new note        | If unauthorised, the option to create a note is not available.                         | Pass      |       |
| View note detail by id   | Authroised and unauthorised users are able to view a note's detail by id               | Pass      |       |
| Update note by id        | If the owner of the note, the note can then be updated                                 | Pass      |       |
| Delete note by id        | If owner of the note, then the note can be deleted                                     | Pass      |       |
| Update/delete note by id | If not the owner or an unauthorised user, then these functionalities are not available | Pass      |