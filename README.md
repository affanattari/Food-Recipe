# Food-Recipe
Food Recipe app using Django
> Features
1. User Authentication & Authorization

Login and Logout: Secure login and logout functionality to manage user sessions.

User Registration: Allows new users to sign up with validation to prevent duplicate usernames. Displays an error message if the username already exists.

2. Recipe Management

Create Recipes: Users can add new recipes with all relevant details.

Update Recipes: Edit existing recipes to keep them up to date.

Delete Recipes: Delete specific recipes from the database.

3. Search Functionality
   
Search Recipes: Users can search for recipes by keywords or names, making it easier to find desired content.

# Login Page
![Login Page](https://github.com/user-attachments/assets/b330822b-7a52-4c20-8527-b7d90a1a74bb)
# Registration page
![Registration Page (2)](https://github.com/user-attachments/assets/29199c13-926c-4438-b24d-6e5770b157c2)
# Main Page
here you can add recipe name, description and image 
![Registration Page](https://github.com/user-attachments/assets/7aa0ee8a-ec50-4ab9-845c-8b066b51d0d2)
# Main Page
Tables
![main page](https://github.com/user-attachments/assets/39005a06-9697-4a4e-ad71-635e55dbc757)
# Update Page
![Update Page](https://github.com/user-attachments/assets/11edf1e8-4ce9-445d-92ef-23f894845258)

# Project Setup
1. Create a virtual environment for the project so it's packages are separated from others on your computer. In your terminal type:
Windows:
> python -m venv env
> .\env\scripts\activate
2. Next we need to install Django, in your terminal type:
> pip install django==3.2.*
3. Create a Django project. Each Django project may consist of 1 or more apps, in your terminal type (the '.' creates in current dir):
> django-admin startproject config .
4. Run the server and view localhost:8000. In your terminal type (type ctr+c to stop the server):
> python manage.py runserver

# NOTE:- on the localhost:8000/ (you will get error) so to go to login page use
> localhost:8000/login/
