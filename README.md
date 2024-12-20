# Syncora

## Introduction

Syncora is a web application designed to help improve your productivity and organisation in day to day life. It allows you to view all your events, tasks and any notes you write down all in one place, making everything easier to find. Why not sign up today and start being the organised person you've always wanted to be?

This repository is for the back-end of the application made using the Django REST framework. The front-end of this project utitilises the React framework. The repository for the front end can be found [here](https://github.com/mariam138/syncora_react).

## Project Goals

Syncora is a web application that is the virtual version of a personal planner or diary. The primary goals of the app are:

1. Help users to stay organised by writing down tasks which need completing and any upcoming events. All of this information can then be found in one place in a much more condensed version compared to a paper diary.

2. Provide a place to write down any notes quickly and easily, compared to having to search around for a pen and paper to jot something down.

3. Provide a simple and easy to use interface, making it intuitive for anyone over the age of 13 to use.

4. Offer minimal but impactful features in an achievable development time, with the ability to further improve the app with more useful features in the future.

## Planning

Firstly, user stories were created for the frontend in order to map out which features were to be included in the project. These user stories were created based around the project goals outlined above. User stories were recorded using Github's issues and project features - the **Syncora** project board can be found [here](https://github.com/users/mariam138/projects/7).

### Data Models

Data models for the app were created using an entity relationship diagram. This diagram was created on [lucidchart](lucid.app/lucidchart).

![ERD Diagram for Syncora models](static/syncora-erd-diagram.jpeg)

##### Profile

This model represents the user profile, to be created upon a user registering for the site. The Profile model has a one-to-one relationship with Django's User model. From registration, the **username**, **name** and **email** fields will be used in the Profile model. A default profile image will also be used, which can then later be edited by the user. 

##### Task

The Task model has a many-to-one relationship with the *Profile* model, allowing a user to create several tasks. This many-to-one relationship is formed by the `owner` field. A `title` field is provided to quickly name the task, and a `due_date` field also. Then the user can choose a `priority` for their task, choosing from: *low*, *medium* and *high*. A `category` can also be chosen for the task for further organisation. An optional `description` field is provided to allow the user to add any extra notes if desired. Finally, a `completed` field is provided. This is a **BooleanField** which will render as a checkbox, initially set to **False** indicating that the task is not completed.

##### Event

Like the *Task* model, the **Event** model also has a many-to-one relationship with the *User* model. This allows a user to create several events on the app. This relationship is provided by the `owner` field. A `name` is required for each event, followed by a `date`, a `start_time` and `end_time`. Events can also be categorised, providing a list of choices for the `category` field. A `location` can also be added for events. Although initially _django-location-field_ was included in the database scheme, due to time constraints with including an interactive map on the front end to work with the back end, this was replaced with a character field instead. Finally, a separate `notes` field is provided which is optional, allowing the user to choose whether to provide extra notes or not.

##### Note

The final custom model for the app is the **Note** model. Same as the *Task* and *Event* models, the **Note** model has a many-to-one relationship with the *Profile* model. A `title` field is provided but this field is optional, which allows a user to save time when writing a note as a title may not always be necessary. `date_created` and `date_updated` fields are part of the model. These fields aren't editable by the user, but will help in organising and filtering notes. Each time a note is updated, it will then appear at the top of the notes list unless the user chooses a different filter. Finally, the **Note** model contains a `content` field where the main body of the note will be written.

## API Endpoints

Once the user stories were created, they were then mapped out to different API endpoints and their url's. This was to help with planning which HTTP methods and views would be needed. Below is a table of all the API endpoints and which user stories they relate to. Each api endpoint also has the needed permissions which was used during creation of each endpoint.

### Profile API Endpoints

| HTTP   | URL           | CRUD Operation | CRUD Description          | View Name | User Story    | Permissions      | Notes                                                                                                                                                                        |
| ------ | ------------- | -------------- | ------------------------- | --------- | ------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GET    | /profiles     | read           | retrieve list of profiles | LIST      | \-            | Read only        | For testing purposes only                                                                                                                                                    |
| GET    | /profiles/:id | read           | retrieve profile by id    | DETAIL    | #36           | Read only        | Although initially I wanted to make these visible only to the owner, this will be handy for future features that allow users to follow others or invite them to events, etc. |
| PUT    | /profiles/:id | update         | edit profile by id        | DETAIL    | #35, #37      | IsUserOrReadOnly |                                                                                                                                                                              |
| DELETE | /profiles/:id | delete         | delete profile by id      | DETAIL    | #19, #20, #21 | IsUserOrReadOnly |

### Task API Endpoints

| HTTP   | URL        | CRUD Operation | CRUD Description                 | View Name | User Story         | Permissions       | Notes                                                 |
| ------ | ---------- | -------------- | -------------------------------- | --------- | ------------------ | ----------------- | ----------------------------------------------------- |
| GET    | /tasks     | read           | view list of tasks on tasks page | LIST      | #30, #40, #23      | ReadOnly          | This API endpoint will also be used for the dashboard |
| GET    | /tasks/:id | read           | view task detail by id           | DETAIL    | #39                | ReadOnly          |                                                       |
| POST   | /tasks/new | create         | create a new task                | LIST      | #38, #44, #46, #27 | IsOwnerOrReadOnly |                                                       |
| PUT    | /tasks/:id | update         | edit or update a task by id      | DETAIL    | #41, #43           | IsOwnerOrReadOnly |                                                       |
| DELETE | /tasks/:id | delete         | delete a task by id              | DETAIL    | #42                | IsOwnerOrReadOnly |

### Event API Endpoints

| HTTP   | URL          | CRUD Operation | CRUD Description                   | View Name | User Story         | Permissions               | Notes                                    |
| ------ | ------------ | -------------- | ---------------------------------- | --------- | ------------------ | ------------------------- | ---------------------------------------- |
| GET    | /events      | read           | view list of events on events page | LIST      | #29, #52, #22      | ReadOnly                  | endpoint will also be used for dashboard |
| GET    | /events/:id  | read           | view event detail by id            | DETAIL    | #51                | ReadOnly                  |                                          |
| POST   | /events/new/ | create         | create a new event                 | LIST      | #50, #26, #55, #57 | IsAuthenticatedOrReadOnly |                                          |
| PUT    | /events/:id  | update         | update an event by id              | DETAIL    | #53                | IsOwnerOrReadOnly         |                                          |
| DELETE | /events/:id  | delete         | delete a task by id                | DETAIL    | #54                | IsOwnerOrReadOnly         |

### Note API Endpoints

| HTTP   | URL         | CRUD Operation | CRUD Description                 | View Name | User Story    | Permissions               | Notes                                    |
| ------ | ----------- | -------------- | -------------------------------- | --------- | ------------- | ------------------------- | ---------------------------------------- |
| GET    | /notes      | read           | view list of notes on notes page | LIST      | #31, #66, #24 | ReadOnly                  | endpoint will also be used for dashboard |
| GET    | /notes/:id  | read           | view note detail by id           | DETAIL    | #65           | AllowAll                  |                                          |
| POST   | /notes/new/ | create         | create a new note                | LIST      | #28, #64      | IsAuthenticatedOrReadOnly |                                          |
| PUT    | /notes/:id  | update         | edit a note by id                | DETAIL    | #67, #71      | IsOwnerOrReadOnly         |                                          |
| DELETE | /notes/:id  | delete         | delete a note by id              | DETAIL    | #68           | IsOwnerOrReadOnly         |


Tables were converted to markdown syntax using [tabletomarkdown](https://tabletomarkdown.com/). The tables can also be viewed [here](https://docs.google.com/spreadsheets/d/1CRyoUpEjVBolPIXQgQctQdQ-qx7E5KorJemjMhpCZus/edit?usp=sharing) on Google Sheets.

## Frameworks, libraries and dependencies

The **Syncora** API is created with Python using Django 4.2 and the Django REST Framework 3.14.0. The following additional dependencies were also used in creating the API:

- **Cloudinary 1.41.0** - To allow storage of profile pictures when users upload a new one
- **django-cloudinary-storage 0.3.0** - To allow integration of storage with the Django framework
- **Pillow 10.4** - For use with Django's ImageField, as recommended by the django-cloudinary-storage docs
- **dj-database-url 2.2.0** - To connect to my extgernal postgreSQL database using a URL
- **psycopg2 2.9.9** - Used as a PostgreSQL database adapter when connecting to the external database
- **dj-rest-auth 5.1.0** - For use in providing REST API endpoints for user registration and authentication
- **django-allauth 0.61.1** - Although not explicitly used in this API, it is used in conjunction with *dj-rest-auth* to include registration functionality, as suggested by the documentation.
- **djangorestframework-simplejwt 5.3.1** - To allow use of JSON web tokens in the production version of the API
- **django-cors-headers 4.3.1** - To add Cross-Origin Resource Sharing (CORS) headers to responses, allowing in-browser requests from other origins
- **gunicorn 23.0.0** - For use with serving the API on a web framework
- **django-filter 23.5** - Used to allow more advanced filtering options within list views for the API, such as filtering by a category.
- **python3-openid 3.2.0** - This is a prerequisite library used in conjuction with _dj-rest-auth_
- **pytz 2024.2** - This is a library installed by Django 4.2 as a dependency, although not explicity used within the app

## Testing

### Manual Testing

Manual testing took place throughout development of the app, for both front-end and back-end. This section will focus on testing for the back-end API.

Testing tables were created using **Google Sheets**. Each row containted the feature being tested, the expected outcome, whether the test passed or failed and an extra notes column for further explanation. The tables have been converted to markdown format and can be found [here](https://github.com/mariam138/syncora_drf/blob/main/testing.md).

### Automated Testing

Some automated testing was also completed for the API. Full automated testing was done for the Notes and Events API endpoints. The Profile API was partly tested with automation. All tables have been converted to markdown format and can be found in the [testing.md](https://github.com/mariam138/syncora_drf/blob/main/testing.md) file.

### Python Validation

Each file was validated using the **Code Institute** [python linter](https://pep8ci.herokuapp.com). Below is a table with any comments about validation. The table was created in Google Sheets and converted to markdown format using [tabletomarkdown](tabletomarkdown.com).

| App         | File           | Notes                                                                                                                                                                         |
| ----------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| syncora_api | settings.py    | 4 errors appeared for lines being too long at lines: 151, 154, 157 and 160. These were due to django's password validators. As these cannot be changed, they were left as is. |
|             | permissions.py | Shortened comment on line 1. Passes with no validation errors.                                                                                                                |
|             | serializers.py | No validation errors                                                                                                                                                          |
|             | urls.py        | Shortened lines 29 and 31. Passes with no validation errors.                                                                                                                  |
|             | views.py       | Passes with no validation errors.                                                                                                                                             |
| events      | admin.py       | Added new line at end of file. Passes with no validation errors.                                                                                                              |
|             | models.py      | Passes with no validation errors.                                                                                                                                             |
|             | serializers.py | Passes with no validation errors.                                                                                                                                             |
|             | tests.py       | Passes with no validation errors.                                                                                                                                             |
|             | urls.py        | Passes with no validation errors.                                                                                                                                             |
|             | views.py       | Passes with no validation errors.                                                                                                                                             |
| notes       | admin.py       | Passes with no validation errors.                                                                                                                                             |
|             | models.py      | Passes with no validation errors.                                                                                                                                             |
|             | serializers.py | Passes with no validation errors.                                                                                                                                             |
|             | tests.py       | Passes with no validation errors.                                                                                                                                             |
|             | urls.py        | Passes with no validation errors.                                                                                                                                             |
|             | views.py       | Passes with no validation errors.                                                                                                                                             |
| profiles    | admin.py       | Passes with no validation errors.                                                                                                                                             |
|             | models.py      | Shortened line 16. Passed with no validation errors.                                                                                                                          |
|             | serializers.py | Shortened lines 23, 25 and 36. Passes with no validation errors.                                                                                                              |
|             | signals.py     | Passes with no validation errors.                                                                                                                                             |
|             | tests.py       | Passes with no validation errors.                                                                                                                                             |
|             | urls.py        | Passes with no validation errors.                                                                                                                                             |
|             | views.py       | Passes with no validation errors.                                                                                                                                             |
| tasks       | admin.py       | Added new line at end of file. Passes with no validation errors.                                                                                                              |
|             | models.py      | Passes with no validation errors.                                                                                                                                             |
|             | serializers.py | Passes with no validation errors.                                                                                                                                             |
|             | urls.py        | Passes with no validation errors.                                                                                                                                             |
|             | views.py       | Passes with no validation errors.                                                                                                                                             |

## Bugs

1. The first bug I came across was during the creation of my Task serialisers. I wanted to implement an `is_overdue` serialiser method field. I hoped to do this by comparing the current datetime to the due date set in the task. The first error I came across was this type error:

    > TypeError: can't compare offset-naive and offset-aware datetimes

    After searching around, I was able to fix this error. However, then I was struggling to compare the current datetime and the duedate. The due date would be saved in my current time zone, but using print statements to debug, the current datetime was only printing in UTC. I tried several solutions, including creating a custom Mixin and implementing it into the serialiser and the view, but unfortunately this did not work. In the end I decided to remove this feature from the backend and will implement it in the frontend, using the timezone of the user's browser for comparison. Another solution would be to add a **timezone** field to the **Profile** model, then localising the current datetime to this timezone. Whether this would conflict with Django's timezone settings is unclear however.

2. In relation to the front-end of this project, I came across a bug where my front-end application was unable to make requests to the API, leading to errors being displayed in the console. More information can be found in the Syncora React [README](https://github.com/mariam138/syncora_react#bugs). After conversing with tutor support, this bug was able to be fixed by checking the compatibility of the installed dependencies, using the terminal command `pip install -r requirements.txt`. This showed that there was compatibility issues between the dependencies and the version of Django that I was using. Initially, I was using Django 5.0, but downgrading to 4.2 helped to solve the error. This has been updated in this README as well. 

3. Another bug which appeared during creation of the front-end was the registration of a new user. When a new user was registered, the expected behaviour was not occurring but instead a 500 console error was being displayed. More information can be found in the front-end [README](ttps://github.com/mariam138/syncora_react#bugs). This issue turned out to be related to the e-mail configuration of the back-end. An issue under the **dj-rest-auth** repository which had a similar issue linked me to [this](https://github.com/MuhammadAnas47/django-rest-auth/blob/master/demo/demo/settings.py) demo template with some added e-mail configurations in `settings.py`. Implementing these settings into my workspace solved this issue, leading to the expected behaviour on the front-end.

    **a.** The same console issue occurred after including the first_name field in the custom register serialiser. After some debugging, this appeared to be because of using email to sign up with again. Potentially there was conflict with the new custom registration serialiser and the already established serialiser provided by *dj-rest-auth*. After coming across an [issue](https://github.com/Tivix/django-rest-auth/issues/534) on GitHub with the same problem, this was solved by including the *allauth* urls, as dj-rest-auth relies on *allauth* for authentication. This solved the 500 console error.

   **b.** A further issue occurred again with registration without using an e-mail. A 500 error console again was displayed if a user tried to sign up without an e-mail address. Opening up the development server and trying to register on the back-end manually led to the following error: 

    > IntegrityError at /dj-rest-auth/registration/ null value in column "email" of relation "auth_user" violates not-null constraint

    Although I had set required to false in the register serialiser, it was being assigned null which was not allowed. Adding `allow_blank = True` to the email serialiser field solved this problem, allowing users to sign up successfully without using an email.

4. When creating the functionality on the front-end to allow a user to change their profile picture and testing it, the default picture was being removed but the new picture was not being set. Instead, with debugging statements, the profile picture was set to `null`. Although initially there were no issues uploading images from the back-end when testing the API, checking again after encountering this error on the front end lead to the same result. It appeared that the custom validator I had created in the profile serialiser was causing no images to be uploaded at all, from both the front and back end. I temporarily commented it out on the back end and added some validation on the front end. I then uncommented the custom validator in the profile serialiser, making sure to add `return value` at the end of the method after using print statements to check that images were being recognised when uploaded. This fixed the upload error on both the front and back ends of the app.

## Deployment

The following steps were followed in order to deploy the API onto Heroku:

1. From the Heroku dashboard, click **'New*'* and then select *'Create new app'*
2. Enter an app name (In this case, *syncora-api*) and choose a region. For this app, *Europe* was chosen as the region.
3. Click the **Create app** button at the bottom of the page
4. On the app, access the **Deploy** tab. Choose **GitHub** as the deployment method to connect to your GitHub account.
5. Connect to the repository to connect the app through GitHub.
6. Access the **Settings** tab. Click **Reveal Config Vars** to create your own environment variables.
7. Set up variables for your *Cloudinary* API, your database and your secret key. 
8. Create a **DISABLE_COLLECTSTATIC** key and set the value to **1**.
9. Ensure all code is pushed to GitHub before deployment.
10. Going back to the **Deploy** tab, scroll to the bottom to the *'Deploy a GitHub branch* setting.
11. Click **Deploy Branch** ensuring the branch is set to *main*.

### Fork repository

To work on this repository independently without affecting the original source code, the repo can be forked.

1. Open the repository to view its details.
2. Click the arrow on the **Fork** button to show a dropdown menu.
3. From the dropdown menu, click **Create a new fork**
4. Rename the repository if you wish to do so.
5. Ensure that the checkbox is ticked to copy the main branch only.
6. Click **Create fork**.

### Clone repository

This repository can be cloned onto your own machine locally which will be synced with the repository on GitHub. This can be done to contribute directly.

1. Open the repository to view its details.
2. Click the green **<> Code** button to reveal a dropdown menu.
3. A **Clone** tab will appear, giving three options to clone the repository:
    a. Clone via **HTTPS** using the web URL
    b. Clone via an **SSH** using the provided URL
    c. Clone using the **GitHub CLI** with the provided command.

## Credits

### Media

- Default avatar icon is by [Dixit Lakhani_02](https://www.freepik.com/icon/user_8407889#fromView=search&page=1&position=29&uuid=d6bcc367-7dd9-404e-b466-6f8daca02ae7) on freepik.com

### Code

Initial set up of dependencies, libraries and frameworks were done following the documentation. Creation of serialisers in the Django REST Framework for example was done following their documentation. Below are code adaptations for more specific bits of code in the API.

- Code for signals to create a Profile instance whenever a user registers is adapted from [this post](https://dev.to/earthcomfy/django-user-profile-3hik) by Hana Belay on **dev.to**
- Code to create the **`IsOwnerOrReadOnly`** custom permission class is adapted from the Django REST framework documentation [here](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#object-level-permissions)
- Code to check if the currently logged in user is the owner of the profile is adapted from **Code Institute**'s 'Authentication, authorization and serializer method fields' video in the Django REST Framework module
- Code to create a custom register serializer, used with django-rest-auth, to make sure a first name is mandatory is adapted from [this](https://stackoverflow.com/questions/36910373/django-rest-auth-allauth-registration-with-email-first-and-last-name-and-witho) and related comments on *stackoverflow*
- Code to add a custom validator for uploading a new profile image is adapted from **Code Institute's** 'Django REST Framework' [walkthrough](https://github.com/Code-Institute-Solutions/drf-api/blob/d3c9498d97a590fa04c78142b41eb78a621d2abe/posts/serializers.py)
- Code for using the annotate method to get a count of a profile's events, notes and tasks is adapted from **Code Institute**'s 'Django REST Framework' walkthrough project, with the source code found [here](https://github.com/Code-Institute-Solutions/drf-api/blob/a7033eacc714c79df49679fbebd455e300e09d95/posts/views.py)
- The updated e-mail configuration settings are adapted from [this](https://github.com/MuhammadAnas47/django-rest-auth/blob/master/demo/demo/settings.py) demo template from the **dj-rest-auth** GitHub repository
- Addition of **allauth**'s urls to prevent another 500 console error when a user signs up with email is adapted from [this](https://github.com/Tivix/django-rest-auth/issues/534#issuecomment-491849803) solution on GitHub
- Code to display the human readable display from the choices list in both the Task and Event serialisers is adapted from [this](https://github.com/encode/django-rest-framework/issues/1755#issuecomment-945167944) and [this](https://github.com/encode/django-rest-framework/issues/1755#issuecomment-962522139) comment from GitHub's DRF Issues