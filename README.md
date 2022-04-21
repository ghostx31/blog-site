# blog-site
Readme file for blog-site:

IMPORTANT!!
To source local files, use `{% static '/path/to/file/' %}` in the html pages. 
At top of every html file, add `{% load static %}`
While naming any file, do not use space.

In settings.py, all the app names are self-explanatory.
```
''' STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
''' 
```
This part tells django where to get and store user related images. 

```
''' SITE_ID = 1
####################################
    ##  CKEDITOR CONFIGURATION ##
####################################

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}

###################################
'''
```
This contains the script to user CKEDITOR which is a WSIWYG editor used in the `create_new page` to write blogs which will be discussed further. 

This README file will be updated on every update and new additions will be marked with * in front of them. 

Apps:
1. accounts: Contains all the data from login, register and logout.
    views.py: 
        register() - Takes the username, fname, lname, and takes two passwords to confirm them and then saves the data to the database and then redirects the user back to the login page.
        login_view() - Checks the username and password entered and checks the database to confirm if user exists and password if correct and then logins the user to the homepage or create blog page.
        logout_view() - Logs the user out if they click the logout button.  
    urls.py:
        urls.py has three urls, register, logout and login. The names are self explanatory.
    models.py:
         Contains the model for user registration. The last field login_count is deprecated and is no longer used. It is substituted by a better condition which has been used in login_view.

2. blog: Blog is the main app which contains the main urls.py and settings.py

3. Data: Data is now deprecated and will be removed in further updates. 

4. homepage: Contains all the views for the main homepage, about, contact and other views are described as follows:
    views.py:
        home() - Contains the link to the hone page.
        aboutus() - Links to the aboutus page.
        contact() - Links to the contactus page and also contains the fields for the feedback form on the contactus page. The feedback form also performs the email validation and asks the user for a valid email if '@' is absent in the entered email field.
        create() - Contains fields for the submission of the blog and saves the blog into the database and is only done if the method of request is POST, meaning when the user presses the submit button to submit the blog. 
        If the method of request is GET, then it renders out the create_new page which contains the necessary tools to write and save a blog.
        login() - Is deprecated and will be removed in further updates.
        search() - Links to the page shown with search results.
        *likeField() - Adds a like to the post currently being read by the user. Is incomplete. Will be completed soon. 
    urls.py: 
        urls.py has the main links for the main pages:
        '' - links to the main homepage.
        about, contact, create, profile and search are self-explanatory.
    
    models.py:  Contains the model for the feedback form in contactus page.
    Contains class feedbackModel(). It has the following fields:
    opt is the dictionary when user selects an option from the drop down menu. 
    FeedbackType accepts this dictionary as an argument. 
    firstname, lastname, email and subject are self-explanatory.

    Another class used is BlogPost() which contains the fields for the create_new blog post page.

    The class Uploads has been deprecated and will be removed.

5. posts: Contains the views for user data and post related functionality. 
    views.py:
        userBlogs() - Links to all the blogs posted by the user. Is not functional yet. 
        userFav() - Links to the page showing all the blogs liked by the user. Not functional yet.
        UserFirst() - Contains the fields for accepting user data from profile page shown to the first time users. Once the data is saved, it redirects the user back to the homepage. This redirection functionality will be changed in the future updates.
        UserNormal() - Links to the user's profile when the user is not logging in for the first time. The linked page will be changed further on when provided by the frontend team.
    models.py: Contains all the fields for accepting the data from user to build a profile. The names are self-explanatory.
    urls.py - Contains links to all the user related links. blogs, favourites and profile are self-explanatory. first/ is used when a user logs in for the first tine and has to build a profie.

6. Search() - Will be used to provide for the search bar functionality. Has not been completed yet and will be completed in further updates. 


Folders:
1. Static: Contains all the plugins, images, styling and js scripts.
2. Assets: Is the folder which is generated by django engine to save the static filea and render them out wherever needed. 
3. Templates: Contains all the *.html pages which are renedered out by the django engine.
4. UserPics: Contains the images uploaded by the user when building a profile.

