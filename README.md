# AppName

Application is a web application designed for users to visit and pin recipes that they like. It was inspired by Pinterest and is created to be used either as a dietary aide, a way of sharing recipes and a means of learning new recipes.

Unregistered users can view a call to action page that encourages them to sign up. Users can sign up for the site from the registration form. They can then subsequently log in using the login button in the navigation bar. 

Registered users can view the Home page, which is a grid of "meal cards". A meal card contains a title, brief dietary information and preparation time. The user can then pin the card to add it to their "My Meals", thus pinning it and letting them save it for later. A user can also unpin meals in the same manner by clicking on the meals that are pinned. The pin changes from an outline when unpinned to a solid background when pinned. The user can also click on the "info" button and see the information from the meal card expanded to display the meal's type, full dietary information and recipe. Registered users can click on "My Meals" to get a list of the meals they have pinned. This page also contains the "info button" functionality. 

Creation, Reviewing, Updating and Deleting Meals are controlled from the admin panel, restricting who can create, update and delete meals from the site. The admin user can get to the admin panel in the navigation bar as long as they are logged onto their administration account. Administrators can also pin and unpin meals like regular users. 


![MealPin](responsive link)

The live site can be found here: [Site](sitelink)

# Table of Contents
- [User Experience]
- [Features]
  - [Feature1]
  - [Feature2]
- [Design]
- [Technologies Used]
- [Testing]
- [Deployment]
- [Credits]

# User Experience

### User Stories

The user stories used as part of the planning for the website have been consolidated here.

- As a Site User I can view the home page so that I can see the site's goal and be encouraged to sign up
- As a Site User I can log in so that I can gain access to the site's features
- As a Site User I can register for an account so that I can log in to gain access to the site's features
- As a Site User I can Log Out so that I can let someone else log in on my computer, leave myself signed out on public spaces or change accounts
- As a site user I can ... so that ...
- As a site user I can ... so that ...
- As a site user I can ... so that ...
- As a site user I can ... so that ...
- As a Site Administrator I can view administrator features so that I can add, edit and remove meal cards to the site
- As a Site Administrator I can view the meal CRUD Forms so that I can add, edit and remove meals from the site
- As a Developer I can create a model for the Meal database so that it is available for administrators to add meals

# Features
## General
### Navigation Bar

<details>
<summary>Navbar</summary>

![Navbar]
</details>

The navigation bar is featured across all pages.

For unregistered or logged out users of the site, the navbar displays... On large screens, the links are visible on the right hand side of the navbar. The list collapses into a dropdown menu on smaller screens which can be toggled by clicking the bars icon.

For registered users of the site, the navbar displays... 

The navbar is...(sourced from Bootstrap)

On the left hand side of the screen, there is the logo which acts as a link to the index page. 

### Footer

<details>
<summary>Footer</summary>

![Footer]
</details>

The footer is featured across all pages.

The footer features...

### Index Page

<details>
<summary>Index Page Unregistered</summary>

![Index Page]
</details>

<details>
<summary>Index Page Logged In</summary>

![Index Page]
</details>

The index page has two states depending on the user.

For unregistered or logged out users, the index page displays...

For users who are registered and logged in, the index page displays...

The index page is responsive in that....

### Feature2

<details>
<summary>Feature2</summary>

![Feature2]
</details>

The Feature2 page is available for... registered/unregistered

The primary purpose of feature2 page...

Feature2 page is responsive in that...

### Feature3

<details>
<summary>Feature3</summary>

![Feature3]
</details>

The Feature3 page is available for... registered/unregistered

The primary purpose of Feature3 page...

Feature3 page is responsive in that...

## Accounts

### Registration Page

<details>
<summary>Registration Page</summary>

![Registration]
</details>

The registration page is accessible through a "Sign Up" link in the navbar or "Register" CTA button on the index page for users who are not logged in. The page features a simple form that requires the users "Email", "First Name", "Last Name", "Password" and "Confirm Password". 

If the user attempts to register while leaving any of the fields blank, they are prompted to fill in the missing field. If the user attempts to register with an email that is already registered, they are given a message that the email is already in use. If the user attempts to register without the passwords matching, they are given a message that the password fields don't match. 

When the user registers, they are logged in and redirected to the index page where they are informed their account is awaiting approval.

### Login Page

<details>
<summary>Login Page</summary>

![Login]
</details>

The login page is accessible through a "Sign In" link in the navbar. The page features a simple form that requires the user's "Email" and "Password". If the user attempts to submit an empty field, they are prompted to fill in the required field. If the user's credentials are invalid, they are given a message that their login is invalid.

When the user logs in, they are redirected to...

![Logout]
</details>

The logout option is accessible through a "Logout" link in the navbar. When the user logs out, they are redirected to...


## Admin Panel

### Admin Panel

<details>
<summary>Admin Panel</summary>

![Admin Panel]
</details>

From the admin panel, the admin user is able to create, update and delete...This is done through...


## Future Features
1. __Stretch One__. This is a description of a stretch goal that provides a new feature
2. __Stretch Two__. This is a description of a stretch goal that provides a new feature
3. __Stretch Three__. This is a description of a stretch goal that provides a new feature


# Design

The concept for ApplicationName was a site for... As such, the aim of the design ...


## CRUD Functionality

This describes CRUD functionality for all users that have it.


## Colour
![Colour Palette]

Clarity, Accessibility, Aesthetic


## Typography

Font Choices detailed here and why


## Wireframes

Wireframes were created in Balsamiq. They were used for initial planning of template layouts.

<details>
<summary>Index Wireframe</summary>

![Index Wireframe]()
</details>

<details>
<summary>Feature1 Wireframe</summary>

![Feature1 Wireframe]()
</details>

<details>
<summary>Feature2 Wireframe</summary>

![Feature2 Wireframe]()
</details>

<details>
<summary>Register Wireframe</summary>

![Register Wireframe]()
</details>

<details>
<summary>Login Wireframe</summary>

![Login Wireframe]()
</details>

<details>
<summary>Admin Panel Wireframe</summary>

![Admin Panel Wireframe]()
</details>


## Agile Methodology

[GitHub Projects Page]()

GitHub Projects was used in part for the planning of this website to create and track User Stories as they were implemented and fulfilled. This section documents sprints and implementation of the plan


## Entity Relationship Diagram

The below Entity Relationship Diagram was created on [diagrams.net](https://www.diagrams.net/). It illustrates the relationships between the models present in the project: 

<details>
<summary>ERD</summary>

![ERD]()
</details>


# Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5): mark-up language.
- [CSS3](https://en.wikipedia.org/wiki/CSS): styling.
- [JavaScript](https://www.javascript.com/): programming language.
- [Python 3](https://www.python.org/): programming language.
- [Django 3.2](https://www.djangoproject.com/)
  - [Django Crispy Forms](https://pypi.org/project/django-crispy-forms/): for forms.
  - [Crispy Bootstrap5](https://pypi.org/project/crispy-bootstrap5/): bootstrap5 template pack for crispy forms.
- [Bootstrap](https://getbootstrap.com/): styling.
- [Cloudinary](https://cloudinary.com/): store static and media files.
- [GIT](https://git-scm.com/): for version control.
- [GitHub](https://github.com/): for host repository.
- [Gitpod](https://www.gitpod.io/): online IDE.
- [Heroku](https://)
- [Google Fonts](https://fonts.google.com/): to import fonts.
- [Font Awesome](https://fontawesome.com/): to import icons.
- [Balsamiq](https://balsamiq.com/): to create wireframes.
- [Diagrams.net](https://www.diagrams.net/): for Entity Relationship Diagram.

# Testing

Testing for the site can be found at the below link:

[Link to TESTING.md](TESTING.md)


# Deployment
## Steps to deploy site using Heroku:
- Assuming gunicorn, dj_database_url, psycopg2 and dj3-cloudinary-storage have been installed
- On the Heroku dashboard, select "New" and click "Create new app"
  - Create a unique app name - this will be added to allowed hosts in the project settings
  - Select your region
  - Click "Create app"
- Go to the Resources tab:
  - Search for "postgres" in the add-ons search bar and select "Heroku Postgres"
  - Click "Submit Order Form"
- Go to the settings tab:
  - Scroll down to the config vars section and select "Reveal Config Vars"
  - DATABASE_URL will be set after adding Heroku Postgres - this will be copied to the project
  - Add a new config var for SECRET_KEY - create your own or use a django secret key generator
  - Add a new config var for CLOUDINARY_URL - copy the "API Environment variable" from your cloudinary dashboard, remove "CLOUDINARY_URL="
  - Add a new config var for DISABLE_COLLECTSTATIC, with the value 1 - this will be removed before deployment
- In your project, for your environment variables:
  - Create a new env.py file in the top level directory
  - In env.py:
    - Import os
    - Add 'os.environ["DATABASE_URL"] = "Paste the DATABASE_URL from the Heroku app here"'
    - Add 'os.environ["SECRET_KEY"] = "Paste your new secret key here"'
    - Add 'os.environ["CLOUDINARY_URL"] = "Paste your CLOUDINARY_URL as in the Heroku app here"'
  ```
  import os

  os.environ['DATABASE_URL'] = 'postgres://exampledatabaseurl'
  os.environ['SECRET_KEY'] = 'examplesecretkey'
  os.environ['CLOUDINARY_URL'] = 'cloudinary://examplecloudinaryurl'
  ```
  - If not already present, create a .gitignore file and add env.py to it

- In your project, in settings.py:
  - Import os
  - Import dj_database_url
  - if os.path.isfile('env.py'):
	import env
  ```
  import os
  import dj_database_url
  if os.path.isfile('env.py'):
      import env
  ```
  - Replace the insecure secret key with "SECRET_KEY = os.environ.get('SECRET_KEY')"
  ```
  SECRET_KEY = os.environ.get('SECRET_KEY')
  ```
  - Link new database by commenting out old DATABASES section and adding:
	DATABASES = {
			'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
			}
  ```
  DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
  ```
  - Add Heroku to the allowed hosts: "ALLOWED_HOSTS = ['the_app_name_from_heroku.herokuapp.com']
  ```
  ALLOWED_HOSTS = ['example-heroku-app-name.herokuapp.com', 'localhost']
  ```
  - Add 'cloudinary_storage' (above 'django.contrib.staticfiles') and 'cloudinary' (below) to INSTALLED_APPS
  ```
  ...
  'cloudinary_storage',
  'django.contrib.staticfiles',
  'cloudinary',
  ...
  ```
  - Setup Cloudinary to store static and media files
  ```
    STATIC_URL = '/static/'
	STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
	STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
	STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

	MEDIA_URL = '/media/'
	DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
  ```
  - Run 'python3 manage.py collectstatic' to collect static files
- In your project:
  - Create a Procfile in the top level directory and add 'web: gunicorn project_name.wsgi' to tell 
  ```
  web: gunicorn project_name.wsgi
  ```
  - Create a requirements file with 'pip3 freeze --local > requirements.txt' for Heroku to install required packages
  ```
  pip3 freeze --local > requirements.txt
  ```
  - Make migrations with 'python3 manage.py migrate'
  ```
  python3 manage.py migrate
  ```
  - Commit and push to GitHub
- Prior to final deployment:
  - Set DEBUG = False in project settings.py
  - Remove DISABLE_COLLECTSTATIC config var from Heroku
- Go to the Deploy tab:
  - Select GitHub and confirm connection to GitHub account
  - Search for the repository and click "Connect"
  - Scroll down to the deploy options
  - Select automatic deploys if you would like automatic deployment with each new push to the GitHub repository
  - In manual deploy, select which branch to deploy and click "Deploy Branch"
  - Heroku will start building the app
- The link to the app can be found at the top of the page by clicking "Open app"

The live site can be found here: [Application]()


## Steps to clone site:
- In the GitHub repository, click the "Code" button.
- Select "HTTPS" and copy the URL.
- Open Git Bash and navigate to the repository where you would like to locate the cloned repository.
- Type "git clone" followed by the copied URL.
- Press enter to create the clone.
- Install required packages with the command "pip3 install -r requirements.txt"

# Credits
## Code
- 

## Media
- Icons are from [Font Awesome](https://fontawesome.com)
- The  fonts are imported from [Google Fonts](https://fonts.google.com)

- Images from 
  - 
  - 

## Acknowledgement
I'd like to thank my mentor...