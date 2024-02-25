# KitRate
Kit Rate is a website for activity enthusiasts who want to research kit (products) before they buy. This site is building a community of active product testers who can provide the viewer an insight into a product with reviews and ratings which can help inform a buying decision. The initial release of this site is focused around Mountain Biking kit but it has been designed to be scalable to other sports and activities in the future. 

# Development Planes
In order to develop this site in a guided and efficient manner, the five development planes have been considered. These are focused on design lead thinking and allow the critical elements of the site to be developed before committing to code. 

# Strategy
## Agile management:
To break the project down into manageable pieces, an Agile management approach has been taken which allows each user story to be addressed with defined tasks and acceptance criteria. 
The following user stories have been added into GitHub projects with the project board being used to manage the tasks in defined, manageable iterations. 

<a href="https://github.com/users/TR94/projects/4" target="_blank">Link to the GitHub project</a>

## User Experience
### Target audience:
This site is designed to be a central hub of product information for mountain bike enthusiasts. Users will be able to add products to the site and invite other users to leave their reviews. The target audience will be interested in researching a particular product before they buy to see how other people have rated it.

### Initiative: 
Create a space where users can review products independently providing real-life feedback to inform other people’s buying decisions. Initially the space will be focused on mountain biking but can be expanded in future. 

### User personas: [check if these are needed in the criteria]

### User Groups: 
For this website there are two different user groups:
“Admin” - has the ability to edit and delete content that is deemed unsuitable
“Users” - people who want to view product reviews and/or leave their own reviews

### Epic 1: 
See frontend documentation for epic 1.

### Epic 2: 
The website needs a database to hold the information required to make if functional. Based on Epic 1, this will include database tables for:
* Profiles
* Products
* Categories
* Reviews
* Favourites
* Subscriptions
* Notifications

### User stories related to the API:

#### User Authentication
Sign Up: As a user I want to be able to create a new account so that I can interact with the website.
	Acceptance
1. A link for the user to follow to sign up
2. A page where to user can enter the required details to create an account
3. Confirm the account details are sent to the back end API and the Profile is created

Sign-In: As a user I want to be able to sign in to the app so that I can gain full access to all the features on the site.
	Acceptance
A link for the user to follow to sign in
A page where the user can enter their sign-in details 
Confirm the request is sent to the back end API and authentication is successful
Full access to all the site’s features becomes available after signing in 


#### Navigation

Routing: As a user I want to be able to navigate through pages in a seamless fashion so that I can continue to view content without waiting for pages to load. 
	Acceptance
Pages will be created using React framework where components will refresh without the page reloading 
Whilst waiting for backend API responses, some kind of loading indication must be used

#### Adding & Saving Products
Create a product review: As a logged in user I want to be able to create a new product so that I can share my review of the product and invite others to share their experiences. 
	Acceptance
A link to a product creation page must be easily visible
The production creation page must have:
Image upload
Product title
Product description 
First review 
Star rating (out of 5)
Confirm data has been received by the backend API
Confirm data has been displayed on the site

View a product review: As a user I want to be able to view the details of a single product review so that I can learn more about it.
	Acceptance
Page must display the details of the product 
Page must display the reviews with their individual ratings 
An overall rating should be displayed next to the product averaging out the individual reviews 

Save a product review: As a logged in user I want to be able to save a product review so that I can easily find it again in my own favourites collection.
	Acceptance
Functionality to save an individual post by clicking a button on it
A dedicated page of products that have been saved by the user for their interest
The link to this collection should be in the navigation bar


#### The Products Page
View most recent products: As a user I want to be able to view all the most recent products, ordered by most recently reviewed first so that I am up to date with the newest content.
	Acceptance
Products displayed on the page in the most recent order

View favourited products: As a logged in user I want to be able to view the products I’ve favourited so that I can find the reviews I’ve found useful. 
	Acceptance
1.   A dedicated page of products that have been favourited by the user for their interest
The link to this collection should be in the navigation bar

View products of followed categories: As a logged in user I want to be able to view content filtered by a specific category so that I can keep up to date with new products of interest.
	Acceptance
A category filter is present on the main page 
Filter only displays products related to a single category 

#### Feed page
Page of content based on the categories followed by the user 
Most followed categories: As a user I want to be able to see a list of the most followed categories so that I can see which categories are popular.
	Acceptance
List of most popular categories displayed on the page 

Follow/Unfollow a category: As a logged in user I want to be able to follow and unfollow product categories so that I can see and remove products in my posts feed.
	Acceptance
Functionality to follow / unfollow categories 
Confirm that following a category populates the feed page with products related to that category 
Confirm unfollowing a category removes the products from the feed page 

Create a review: As a logged in user I want to be able to add reviews to a product so that I can share my thoughts about the product.
	Acceptance
Space on the Product page to leave a free text review 
Review should have an option to rate the product out of 5 stars

View reviews: As a user I want to be able to read reviews on products so that I can understand what other users think about the product.
	Acceptance
Product page has facility to view reviews associated to that product 
Reviews are in date created order - newest first

Delete a review: As an owner of a review I want to be able to delete my review so that I can control my contributions to the site.
	Acceptance
If the user logged in owns the review, they’ll have the option to delete the review
Delete function has a warning and confirmation before caring out the action
Confirm upon submitting the new information, the backend API updates
Confirm the new information is displayed on the site

Edit a review: As an owner of a review I want to be able to edit my review so that I can fix or update my existing content.
	Acceptance
If the user logged in owns the review, they’ll have the option to edit the content
Editing function automatically fills in the current information
Confirm upon submitting the new information, the backend API updates
Confirm the new information is displayed on the site


#### The Profile Page
User profile - user stats: As a user I want to be able to view statistics about a specific user: bio, number of products owned, number of reviews made and their rating trends (count of 5 star, 4 star, etc ratings) so that I can make a judgement of how valid their content is.
	Acceptance
Profile page must contain the following information related to the specific profile:
Number of reviews made 
Number of products owned 
Rating trends
Feed of products they own

Edit profile: As a logged in user I want to be able to edit my profile so that I can change my profile picture and bio
	Acceptance
If the user logged in owns the profile, they’ll have the option to edit the content
Editing function automatically fills in the current information
Confirm upon submitting the new information, the backend API updates
Confirm the new information is displayed on the site

# Scope
Defining the scope at this stage allows the project to be clear on what the deliverables are before the detailed design start. 
Based on the strategy above and the agile management approach, the content requirements along with the acceptance criteria and tasks will be centred around the User Stories.
 
# Structure
For the backend database, a diagram helps to depict the data fields, their groupings (tables) and the relationships between them all. This diagram becomes a key reference whilst building the models and therefore agreement at this stage is key to a smooth development process. 

![KitRate Database Diagram](/static/readme_files/.png)


# Features
## Admin
## Categories
## Favourites
## Notifications
## Products
## Reviews
## Subscriptions

# Security
Security is taken care of using an env.py file which is included in the gitignore file to ensure it is never committed publicly. Three key pieces of secret information are included in the env.py file:
Cloudinary URL connection
Django secret key 
postgreSQL database URL
This information has been created as variables in the settings.py file and references the env.py. 


## Features to add in the future
The Notifications functionality has been created in the backend but hasn’t been tested in the front end as its part of the future work to be completed. As the notification functionality is developed in the front end there may be changes required to the back-end to achieve the desired behaviour.

# Code standards and Practices


# Technologies Used
Coding languages used:
-   HTML5
CSS3
Python3
JavaScript including ES6

Libraries used:
A variety of libraries have been used to enable functionality:
oauth: handles user validation with login, logout and register functions
Django REST framework: python based framework for database interaction
cloudinary storage: third party cloud based storage with unique URLs for persistent storage
django-filter: adds filters to the database for queries 
gunicorn: web server application 
pillow: handles image processing 
psycopypg2: handles postgreSQL interactions 
whitenoise: used to handle static files in deployment such as CSS files

## External resources used:
### Git-Hub / Git-Pod:

### Heroku 

### Cloudinary
Cloud based storage for images and static files which remains stable to ensure links stay open indefinitely. 

# Testing
## Manual Testing
### Functionality testing:
Thorough manual testing has been carried out to test the functionality of the site and ensure it is operating as expected. 

<a href=“…” target="_blank">Link to testing document</a>

### Validator Testing 

### Functionality testing:

Validation testing using W3C Mark-Up Validation Service: HTML for each page:
—-

CI Pep8 Python linter:

Categories
* models.py: no errors
* serialisers.py: no errors
* urls.py: no errors
* views.py: no errors

Favourites
* models.py: no errors
* serialisers.py: no errors
* urls.py: no errors
* views.py: no errors

Notifications
* models.py: no errors
* serialisers.py: no errors
* urls.py: no errors
* views.py: no errors

Products
* models.py: no errors
* serialisers.py: no errors
* urls.py: no errors
* views.py: no errors

Profiles
* models.py: no errors
* serialisers.py: no errors
* urls.py: no errors
* views.py: no errors

Reviews
* models.py: no errors
* serialisers.py: no errors
* urls.py: no errors
* views.py: no errors

Subscriptions
* models.py: no errors
* serialisers.py: no errors
* urls.py: no errors
* views.py: no errors# Bugs

## Solved bugs:

Unfixed Bugs
Issues still remaining in the GitHub project:

# Deployment 
The project was developed using GitPod and all changes were pushed to GitHub to keep a version history and store the code. The website is deployed using Heroku which provides a link to the website once it has been published. 

It is recommended to deploy the barebones of the project onto Heroku as soon as possible to ensure the connections have been made before the development begins.

### Local deployment is fro the Github repository using the following steps:
1. Clone the repository from Github using the “Code” button (or if you have an extension to GitPod, click this)
2. Open your IDE and link the Github repository to import the files
3. Install the requirements for the site using `pip install -r requirements.txt`
4. The application is built around environment variables which keep access keys secret for security purposes. This file will need to be created each time a local deployment is required because this file is not stored in the repository for security reasons. See Environment Variables for steps on how to do this. 
5. With a database connected, make and run the migrations using `python3 manage.py makemigrations` and `python3 manage.py migrate`.
6. The application requires a super user in order to access the admin area - this is created using the command `python3 manage.py createsuperuser`
7. Products can be created within the admin panel using the “Products” section.
8. Run the app using the `python3 manage.py runserver` command. Note, the local host address will need to be added to the “ALLOWED HOSTS” section within the settings.py file.

### Heroku deployment for public use:
1. Login to your Heroku account and create a new app from the dashboard 
2. Connect the GitHub repository to the Heroku app 
3. Within the settings tab, set-up the environment variables in the Config Vars section.
4. In the deploy tab, you can enable automatic deployments linked to the GitHub repository 
5. Deploy the files using “Deploy branch” from main branch
6. Once the app has finished building, click “View” to open the app. 

### Environment variables:
For Heroku deployment the variables are stored in the Config Vars settings within the app.
For local deployment, an env.py file is required to control the variables. 

To create the env.py the following variables are needed:
* URL to database 
* URL to cloudinary storage 
* Django secret key

# Credits 
Code:
* W3Schools and Stack Overflow helped with various coding challenges 
* Code Institute for walk-through projects and associated code that this site is based on. 

Acknowledgements:
* Thank you to my mentor, Richard Wells, for his time, patience and guidance on the development of this website. 
* Thanks also are given to the Code Institute Slack Community who are always on hand to help at a moments notice.
* Thanks to the Code Institute tutor support who have been very persistent in helping with coding challenges throughout the project.
