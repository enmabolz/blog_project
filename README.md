## Title:
Blog Project

## Description:
This is the code of a blog project built with Django. This was built in order to put into practice some of my skills in Django. It has features like user authentication, user registration, post creation and post comment creation.

## Table of Contents:
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Some Technical Details](#sometechnicaldetails)

## Features:
- User authentication (registration, login, logout)
- User permission managment
- Posts creation, edition, removal and update 
- comment creation on posts
- User profiles

## Installation:

1. **Clone the repository:**
   Use these command to do it:   
   - git clone https://github.com/yourusername/django-blog.git
   - cd blog_project

2. Create a virtual enviroment and activate it:  
   a. Be sure that you have python installed and accesible from command prompt or terminal.  
   b. Use this command to create the virtual enviroment: **python -m venv <name_of_virtual_enviroment>**  
   c. Activate the virtual enviroment with this command:  
     - On Windows: **<name_of_virtual_enviroment>\Scripts\activate**  
     - On Linux: **source <name_of_virtual_enviroment>/bin/activate**
  
3. Install the dependecies. You can use this command: **pip install -r requirements.txt**  
4. Run the **python manage.py migrate** command to create the database file (using SLQLite).  
5. Create a superuser (user with administration rights).
   To do so, you will need to run **python manage.py createsuperuser** command and follow the instructions. Do not forget the credentials of this user.     
5. Run the development server: **python manage.py runserver**
6. Access to the application: Open your browser and go to 127.0.0.1

## Usage:
After accesing to the main page, you will have all the available posts listed and a navbar at the top of the webpage. The navbar have links to Login and Register.

This is how it looks like:
![alt text](image.png)
If there is any post, you have the possibility to read it entirely. To leave a comment, you need to register. 


### User managment, permission and creation

#### User permissions
Users can be created with one of the following type of permissions: Subscriber, Author and Admin.
   - Subscriber user: it has the right to comment posts.
   - Author user: it has all the rights of a Subscriber user and also it can create posts.   
   - Admin user: It has all the rights of an Author user, it can visualize, edit all users, create them and edit all posts.

All the users has the right of delete a post that was created by itself. Only admin users can delete posts that was not created by them. 

#### Registering
To comment posts, you need to register. To do so, you only need to click on the Register link and fill out the fields that appear. After registering, you will automatically logged and redirect to the main page. By default, users are created with Subscriber permissions. Only admin users, can create users with Author or Admin permission.

If you have followed the steps in the Installation part, you will have by default an admin user (superuser). If an Author or Admin users are needed to be created, you need to be logged as admin first. This was made in this way in order to give all the control on who can publish posts to the admin user/s. No everyone can do it.  

#### Login and Logout
If you want to login with an existing user, you need to click to the login link at the right of the navbar and then put your credentials.

#### User Profile and Options
After being logged to the system, there will be some actions that you can perform. Those options vary on the permission that the logged user has but even that, all the users has the option to view their user profile, change some user fields or logout.    

Additionally to that:
   - Subscriber users have the option of comment.
   - Author users have the option of comment posts, create posts and edit or delete posts that they created.
   - Admin users have the option of comment posts, create posts, edit/delete any posts, create/edit or delete users.


# Technologies:
Technologies used to build this blog:
- Django Framework
- Python Programming Language
- HTML, CSS, Django template language (For the frontend part)
- Bootstrap (CSS Framework for the frontend part)

# Some technical details (for those who has some knowledge of Django):
To build this project, I created two apps (users and posts) and used a CBV (class based view) approach. 

I created two apps with the purpose of divide the logic of users and posts. Since comments are tightly coupled with posts and there is no a projection of expanding it in the future, I decide to write the functionality of both in just one app. In a real-world scenario with projection of expansion, it would be a better practice to separate comment and post functionality in two apps.

I am using class based views in order to speed up my skills using them and they can be very usefull when you would like to save time doing lots of implementations of code and have it cleaner but depending on the case, it is not always convinient to use them. For more details about it, check this article: https://forum.djangoproject.com/t/using-class-based-or-function-based-views/2598.   


