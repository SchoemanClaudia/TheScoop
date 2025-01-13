# The Scoop

xxxxx

Live Link: https://the-scoop-670ac5b1567b.herokuapp.com/

![Screen Mock-up](assets/images/responsive-mockup.webp)

## Contents
- [Overview](#overview)
- [Features](#features)
- [User Stories](#user-stories)
- [Agile](#agile)
- [Solution Model](#solution-model)
- [UX/UI Wireframing](#ux-ui-wireframing)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## Overview

- xxxxx

## Features

__Existing features:__
- 

  ![Home screen](static/images/home.webp)

- 
  - 

  ![Review cards](static/images/review-cards.webp)

- 
  - 
    - 

  ![Post detail page](static/images/post-detail.webp)

- 
  - 
  - 

  ![Login](static/images/login.webp)  ![Register](static/images/register.webp)

- 
  - 
  
  ![Comment](statics/images/comment.webp)  ![Edit](static/images/edit.webp) | ![Delete](static/images/delete.webp)

- 
  - 
    - 

  ![Contact form](static/images/contact-form.webp)

- 
  - 

  ![Admin page](static/images/admin-page.webp) ![Admin panel](static/images/admin-panel.webp)

__Future Features__
- 
  - 
    - 

## User Stories

User stories were used to keep track of the MOSCOW framework and project MVP as working through the project. 

![User stories](static/images/user-stories.webp)

| USER STORY | DETAILS | ACCEPTANCE CRITERIA |
|:---:|:---:|:---:|

## Agile

For the Agile process I utilised the Github project board and user stories. Detailing the production process and highlighting issues when they arose. 

### Project Issues

![Agile](static/images/agile.webp)

New user stories have been added as the project progressed and based on user feedback during the final testing phase. 

A MOSCOW framework has been utilised. 

Mo: Full review details, CRUD functionality.(Leave reviews, edit reviews, delete reviews) \
S: Ratings that are shown on all pages and averaged.  \
C: Code and style revisement. Future features such as Carousel view, ratings convered to star ratings. \
oW: Ability to add own reviews as a user. 

## Solution Model

### Flowchart

![Flowchart](static/images/flowchart.webp)

## UX/UI Wireframing



### Wireframe

### Accessibility

### ERD Design

### Database Model


## Technologies Used

### Languages

- HTML5
- CSS3
- JavaScript
- Python
- Django
- Boostrap

### Other Sites

- 

- 

- Flowchart diagram created using Miro app:
  - Miro: https://miro.com/
    
- Image assets reduced with online platforms:
  - TinyPNG: https://tinypng.com/
  - XConvert: https://www.xconvert.com/

- Assisted problem solving sites:
  - 

## Testing 

- I have manually tested by checking the following:

| TEST INPUT | CORRECT OUTCOME | MEET REQUIREMENTS |
|:---:|:---:|:---:|
| xxx | PASS |
| 

### Validator Testing 

- 

  ![Errors encountered](static/images/errors.webp)

- 

![No errors](static/images/clear.webp)

### Bugs Encountered

- 
  - 

![bug](assets/images/bug.webp)

- 

![Initial deployment](assets/images/first-deploy.webp)

### Unfixed Bugs

- No unfixed bugs, app running with no errors.

![Final Result Success](assets/images/heroku-app.webp)

## Deployment

### Cloning of the Repository Code locally
- The terminal function and template for the deployable application was provided by Code Institute
  - Go to the Github repository that you want to clone
  - Click on the Code button located above all the project files
  - Click on HTTPS and copy the repository link
  - Open the IDE of your choice and paste the copied git url into the IDE terminal
  - The project is now created as a local clone

| **Step** | **Code** | 
|---|---|
| **In Github** |
| Create a new Github Repo | Github > new Repository |
| Open Repo | If your Github is utlising the plugin click 'Open' to launch your preferred IDE |
| **In IDE**|
| Install Django: | pip3 install Django~=4.2.1 |
| Create requirements file | pip3 --local > requirements.txt |
| Create Project (proj_name)| Django-admin startproject proj_name . |
| Run Server | python3 manage.py runserver |
| Add Servers to ALLOWED_HOSTS in settings.py | ALLOWED_HOSTS = ALLOWED_HOSTS = ['.codeinstitute-ide.net', '.herokuapp.com'] |
| Create App (app_name) | python3 manage.py startapp app_name |
| Add to INSTALL_APPS in settings.py | INSTALLED_APPS = [… 'app_name',] |
| **Set Up Heroku** |
| Heroku Dashboard | https://www.heroku.com/ |
| Create new Heroku App | Choose unique name / select close region |
| Add Config Vars | Config Vars > Reveal Config Vars > Add New Key > DISABLE_COLLECTSTATIC value 1 |
| **In IDE** |
| Install web server Gunicorn and freeze | pip3 install gunicorn~=20.1 \ pip3 freeze --local>requirements.txt |
| Create Procfile | create Procfile in root directory |
| Declare Procfile | Add web : gunicorn proj_name.wsgi in Procfile |
| **In Heroku** |
| Connect Repository | Navigate to Deploy tab > connect to Github Repo |
| Check Add ons & Dynos | Inside app resources make sure to use Eco Dynos. Delete PostGres DB Add-ons |
| **Database** |
| Create Postgres Database | CI Database Creator - https://dbs.ci-dbs.net/ |
| **In IDE** |
| Install Database Packages | pip3 install dj-database-url~=0.5 psycopg / then pip3 freeze --local > requirements.txt |
| Create env.py file | Root directoy add env.py and add to .gitignore |
| **In env.py** |
| import OS | Top line 'import os' |
| set enviroment variables | os.environ["DATABASE_URL"] = "Paste in PostgreSQL database URL" |
| Secret Key | os.environ["SECRET_KEY"] = "Make up your own randomSecretKey" |
| **In Heroku** | 
| Add Secret Ket to config Vars |  SECRET_KEY, “randomSecretKey” |
| Add a Config Var called DATABASE_URL | DATABASE_URL, “yourDBUrlgoeshere” |
| **In settings.py** |
| Link to env.py | from pathlib import Path, import os, import dj_database_url, if os.path.isfile("env.py"): import env |
| Remove secret key | SECRET_KEY = os.environ.get('SECRET_KEY') |
| Comment out old Database section | # DATABASES = { } ( # on each line ) |
| Add new Databases section | DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} |
| **Migrate Database** |
| Save all files and Migrate | python3 manage.py migrate |
| **Create Super User** |
| Create Super User | python3 manage.py createsuperuser |
| **In settings.py** |
| Set DEBUG to false | DEBUG = False |
|**Redeploy** |
| Push all Git changes and commits | Redeploy to Heroku |

### Version Control
- The Scoop was created using Gitpod editor and pushed to Github to the remote repository 'TheScoop'
- Git commands were used throughout the development to push the code to the remote repository
- The following git commands were used:
  - git add .  to add the files to the staging area before being committed
  - git commit -m "commit message", to commit changes to the local repository queue that are ready for the final step
  - git push, to push all committed code to the remote repository on Github
  - pip3 install imports, for python library loads
  - add loaded packages to requirements.txt file for Heroku:
    - run, pip3 freeze > requirements.txt, to terminal

## Credits 

- Slack channel peers for their feedback and support
- My mentor for the support and knowledge shared, helping to keep this prototype simple and clean
- Tutor Assist for the support