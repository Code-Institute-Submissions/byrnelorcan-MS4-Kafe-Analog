# **MS4 - Kafe Analog**

## **[View the Live Website Here!](https://kafe-analog.herokuapp.com/)** ##

![Image](media/mockup.png)

## **Code Institute Milestone 4 Project - Full Stack Frameworks Django**
The project has been undertaken to build an efficient, simple and accessible online retail website. The site will enable users to purchase products, register as a user and access user only content. The site will also be fully functioning with payment application stripe.





# Table of Contents:
- [**UX**](#--ux--)
  * [User Stories](#user-stories)
  * [Strategy](#strategy)
  * [Scope](#scope)
  * [Structure](#structure)
  * [Skeleton](#skeleton)
    + [**Wireframes**](#--wireframes--)
    + [**Changes to initial wireframes**](#--changes-to-initial-wireframes--)
  * [Surface](#surface)
- [**Features**](#--features--)
  * [1. Landing Page](#1-landing-page)
  * [2. Profile Page](#2-profile-page)
  * [3. Login and Book Features](#3-login-and-book-features)
- [**Technologies**](#--technologies--)
  * [Languages](#languages)
  * [Libraries, Frameworks and Technologies](#libraries--frameworks-and-technologies)
  * [Workspace and Version Control](#workspace-and-version-control)
- [**Testing**](#--testing--)
  * [Code Validators](#code-validators)
  * [Javascript](#javascript)
  * [Python](#python)
  * [Responsive Elements](#responsive-elements)
  * [Search Accuracy and Functionality](#search-accuracy-and-functionality)
  * [UX User Story Test](#ux-user-story-test)
- [Deployment](#deployment)
  * [Github Pages Deployment:](#github-pages-deployment-)
  * [Forking The Repository:](#forking-the-repository-)
  * [Creating a local clone:](#creating-a-local-clone-)
  * [Heroku Deployment](#heroku-deployment)
- [**Credits**](#--credits--)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)


# **UX**
## User Stories
----------------
In this project there are three groups of target users. They include general users, the admin and site owner and club members. The user stories for each group are defined below.

__Applicable to all users__
- As a user, I want to be able to quickly understand the purpose of the site
- As a user, I need to be able to navigate around the page in a standard format
- As a user, I would like to see products that I can purchase without signing up to become a member of the page
- As a user, I would like to know where the company is based and the team behind it.
- As a user, I require the ability to see my cart, how much the total about is and what products have been added.
- As a user, I would like the ability to register for more interesting topics.
- As a user, the ability to purchase my products safely is a necessity. 
- As a user, I require the need to be able to use the site on mobile, tablet and desktop.

__General user__
- As a general user, I require to be able to view and use elements of the site without logging in.
- As a general user, I would like to still have the option to follow the link to buy without registering an account.

__Club member__
- As a club member, I would like access to content that a user who is not a member cannot access, for example a blog or playlists etc. 
- As a club member, I require access to a profile where I can see my order history.
- As a club member, I need a seamless ability to sign in and log out.

__Admin Users__
- As a Super-user, I require the ability to edit, add and delete products for sale and listings.
- As a Super-user, I need to add to the club blog post section. 


## Strategy
----------------
__Project goals__

The aim of this project is present the company products in a simple and clear but professional way. It was important to create a user-friendly and approachable site with a modern design and feel. The products have to be presented in a clear and familar way. This makes the site more accessible to users who are new to the site and need to find information quickly.

The features and content of the site therefore had to include;
- Product Titles, Descriptions and Prices.
- Familar genres and types.
- An approachable user interface and registration/login functionality.


__User goals__ 

The user goals will be met by enabling the user get access to the products, purchasing and blogs in a clear and concise format. The users require the ability to quickly search for their topic and filter out the irrelevant information. The users goals will be achieved through a landing page featuring nav links, a search element and registration/login option. There will also be links to the club section which is for registered users only.



## Scope 
----------------

The site will be built for purpose and the content should be accesible and user friendly. The scope therefore includes:
- A landing page featuring nav links and topics clearly displayed.
- The ability to learn about the company and what products available.
- An ability to search from the landing page, access a user profile and login/register.
- A log in function where the user inputs username and password.
- A register function, the user will input relevant details and create a profile.
- A profile page, displaying the order history of the user and the previous saved shipping detail.
- An ability to add products to cart and checkout safely and securley.
- An registered-access only element that displays blogs and news etc.



## Structure
----------------

The structure of the site is built around the main landing page where the user can navigate and search through the page.


1. **Landing Page**
- Simple landing page, with carosuel showing links and relevant images.
- A navbar that directs users to product pages, blogs and profiles.
- Nav elements will also have a modal search and active cart element.
- The footer of the page will diplay some info about the company and further nav elements to social media etc.
2. **Log In/Register Page**
- This page enables the user to input a username and password.
- The page will link to a register page where the user can register details.
3. **Profile Page**
- This page displays the user profile with their order history and shipping details.
4. **Products Page**
- This page displays filtered products and enables the user to click to find out more information.
- The product cards will show images and names, genres and pricing.
5. **Products Detail**
- The detail page will display product descriptions and pricing.
- This page will enable the user to add the product to their cart.
- The detail will also display if the product is in stock or not.
6. **Checkout Page**
- The checkout enables the user to pay for their items and add shipping details relevant to their order.
- This will be a safe secure checkout using stripe.
7. **Blog Page**
- The blog/ club will display only to users who are registered.
- The content will be relevant to the company goals and areas of interest.



## Skeleton 
----------------
### **Wireframes** ###

The Skeleton of the project design was built utilising [Figma](https://www.figma.com/). 

The overall basic design breakpoints can be seen below:

![Wireframes]()


### **Changes to initial wireframes** ###
A number of design edits were made throughout the project with the purpose of increased userability and clarity. These include:
- The navbar will be consistent throughout the pages.
- The landing page will feature an image carosuel that has relevant product links.
 

## Surface 
----------------
The site aimed to be dark with bright elements. The colour choice was to be dark so that nothing distracts from the key data and information. The light will be contrasted with bright yellow nav elements, white footer elements and a white background product page.

**Colour Theme**

![Image](static/images/colours.png)

**Typography**

- The font used for both body and headings is [Montserrat](https://fonts.google.com/specimen/Montserrat). This font was chosen for its professionalism and clarity.
I wanted to bring a modern design feel to the site and utilising a font that is widely used was effective.
The site also has 'Sans Serif' as an alternative font.
- The main logo or title is [Comfortaa](https://fonts.google.com/specimen/Comfortaa)

# **Features**
----------------
## 1. Landing Page
-----------------
- The landing page features a carosuel view with three slides displaying relevant background photos and links. The page features a modal search bar to enable users to search through the site. The nav displays a user profile icon that links to log in and registration. When logged in that will change to profile and log out etc. The user will also see their cart with the total amount.


----------------------
## 2. Profile Page
----------------------
- The profile page features the users order history and shipping details that are previously used. There are options for the user to edit their details and save for future use.

---------------------
## 3. Login and Register Features
---------------------
- The login page is simple and displays prompts for the user to input their username/email and password. The site also features a link to register if the user has not yet done so. The registration page is simple and prompts username and emails, as well as passwords.
---------------------
## 4. Products, Detail and Bag Page
---------------------
**Products**
- The products page features cards that display the products information and pricing. The site is fully responsive and also features a filter element so that users can filter from most expensive or A-Z etc.
- Each product links to their product detail page.

**Product Detail**
- The product detail page features an accordion displaying a product description and then a breakdown of products details.
- This page enables the user to add a product to their cart and navigate to continue shopping.

**Bag**
- The bag page displays the items the user has placed in their bag.
- There is the ability to add more quantity to the products if the user requires to do so.
- The total cost is displayed, along with shipping costs and indivdual costs.
- The page links to a secure checkout.

---------------------
## 5. Checkout Page
---------------------
- The checkout is a secure page with a payment form and a stripe function.
- The card input element will display red if there is a card error or green if the card is accepted.
- The user can also go back and adjust their bag if need be.

# **Technologies**
## Database
---------------
Two relational databases were used to create this site - during production SQLite was used and then Postgres was used for the deployed Heroku version. The data is broken down into:
- Products:
  - Categorys	
  - Conditions
  - Genres
  - Products

The data for users, orders and blogs is also stored.

The content is broken down in clear descriptions with text inputs from the forms. The images are uploaded directly. The naming convention was kept concise and relevant to the site.

## Languages
---------------
For this project two languages were used:
- [HTML](https://www.w3schools.com/html/#:~:text=HTML%20is%20the%20standard%20markup,learn%20%2D%20You%20will%20enjoy%20it!)
- [CSS](https://www.w3schools.com/css/)
- [Javascript](https://www.javascript.com/)
- [Python](https://www.python.org/)

## Libraries, Frameworks and Technologies
---------------

- [Bootstrap](https://bootstrap.com/) - Bootstrap was used to for its easy to use grid and repsonsive layout. Elelments of the navbar, cards and forms were taken from the site.

- [Coolors](https://coolors.co) - Used to create colour palette and test colour themes.

- [Google Fonts](https://fonts.google.com/) - Google font 'Lato' was included in the project.

- [Font Awesome](https://fontawesome.com/) - All icons used throughout the project come from fontawesome.

- [JQuery](https://jquery.com/) - Used for aspects of userability.

- [Django](https://www.djangoproject.com/) - The main build of the site is around Django.

- [Mock-Up Generator](https://techsini.com/multi-mockup/index.php) - Used for title photo.

- [Heroku](https://id.heroku.com/login) - Used for site deployment.

- [AWS](https://aws.amazon.com/) - Used for file storage.

## Workspace and Version Control
--------------------
- [Github](https://github.com/) - The project is hosted on Github and the live website is worked through Github pages.

- [Gitpod](https://www.gitpod.io/) - The project used Gitpod IDE for build and development. 

# **Testing**
## Code Validators 
---------------
A number of code validation techniques were utilised to ensure proper testing of site. 
For HTML and CSS, I used the [W3C Markup Validator](https://validator.w3.org) and [W3C CSS Validation Services](https://jigsaw.w3.org/css-validator/). 
See below for results.

- HTML: Warnings related to user-id fields and javascript type label. No fix required
- CSS: No errors. 


## Javascript
--------------
A combination of [JSHint](https://jshint.com/) and manual testing was completed on the javascript to ensure adequate quality. 
- No errors found in manual test. Basic javascript from Code Institute Project Ado project.

## Python
--------------
Python was manually tested and functioned well. Some indentation issues and line length issues arose and are unable to fix.

## Responsive Elements 
--------------

The responsivity of the page was tested primarily using [Google Chrome Dev Tools]() and manual resizing of windows. The test provided positive results for each 
device option. The responsive breakpoints and resizing worked throughout the site. The site was shared with colleagues and friends and tested 
on their devices. The site worked well on all devices tested and there was no problem with browser compatibility found during these tests.

  
## Search Accuracy and Functionality
--------------
Manual testing was completed and the following results were found:

- The search function worked well.
- The add, edit and delete functions completed their required tasks and were easy to use.
- The login and register functions were tested and performed well.

## UX User Story Test
--------------
The user stories previously laid out in the UX Design section are tested, to ensure that project achieves the user goals.

__Applicable to all users__
- As a user, I want to be able to quickly understand the purpose of the site
  - The user lands on an informative site.
- As a user, I need to be able to navigate around the page in a standard format
  - The nav bar is clear and structured in a familar format.
- As a user, I would like to see products that I can purchase without signing up to become a member of the page
  - I can view all products without registering an account. 
- As a user, I would like to know where the company is based and the team behind it.
   - A brief introduction to the team is clear in the footer.
- As a user, I require the ability to see my cart, how much the total about is and what products have been added.
  - I can see my cart and the total amount
- As a user, I would like the ability to register for more interesting topics.
  - I can register and view blogsposts.
- As a user, the ability to purchase my products safely is a necessity. 
  - The secure checkout functions properly.
- As a user, I require the need to be able to use the site on mobile, tablet and desktop.
  - The site a has good responsive elements.

__General user__
- As a general user, I require to be able to view and use elements of the site without logging in.
  - I can view all core elements of the site without the need to log in.
- As a general user, I would like to still have the option to follow the link to buy without registering an account.
  - I can purchase products without being a member of the site. 

__Club member__
- As a club member, I would like access to content that a user who is not a member cannot access, for example a blog or playlists etc. 
  - As a club member I get access to the blog.
- As a club member, I require access to a profile where I can see my order history.
  - I can see order history and shipping details.
- As a club member, I need a seamless ability to sign in and log out.
  - I can log out and log in similar to standard practice.

__Admin Users__
- As a Super-user, I require the ability to edit, add and delete products for sale and listings.
  - Admin has full CRUD functionality.
- As a Super-user, I need to add to the club blog post section. 
  - Admin can add blogpost.





# Deployment 

## Github Pages Deployment:
The project is deployed to GitHub Pages. To deploy the site follow the instruction below.
1. In GitHub navigate to the []().
2. Locate '_Settings_', navigate to '_Source_' and select _Master Branch_ from the dropdown and click _Save_.
3. The site will be published and confirmation shown on the page.

## Forking The Repository:
To create a fork of the Repository simply:
1. Navigate to the []().
2. Select '_Fork_' on the right hand corner of the page.

## Creating a local clone:
1. In GitHub navigate to the []().
2. Above the file list select '_Code_' with the download icon. 
3. To clone select the copy icon at the far right side of URL.
4. Open your terminal in respective IDE, and edit working directory to the desired location.
5. Type `git clone` and paste copied URL.
6. Select Enter and local clone will be created. 

For more specific information relating to the clone follow this [link](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

## Heroku Deployment:
This project is deployed using Heroku.

1. ### Requirements and Procfile
- In the GitPod terminal, type pip3 freeze --local > requirements.txt to create your requirements file.
- Create your Procfile and insert the following code: web: gunicorn kafe-analog.wsgi:application

2. ### Creating Heroku App
- Log into Heroku
- Select 'Create New App' from your dashboard
- Choose an app name
- Select the appropriate region based on your location
- Click 'Create App'

3. ### Connecting to GitHub
- From the dashboard, click the 'Deploy'
- Go to 'Deployment Method' and choose 'GitHub'
- Locate your repository by name , click 'Connect'
 
4. ### Environment Variables
- Click the 'Settings' tab towards the top of the page
- Go to 'Reveal Config Vars':
  - Input your relevant variable names.

5. ### Deployment
- 'Manual Deploy' choose the master branch and click 'Deploy Branch'.
- Click 'Open App' from the top of the page.

# **Credits**
## Content
--------------
 - The project backend structure came from the Code Institute Boutique Ado Project.
 - The structure of the site from Bootstrap.
 - All images for products come from google search of high quality images.
 - Unsplash was used for free high quality images.

## Media 
--------------
- All icons were sourced from [font awesome](https://fontawesome.com/)

## Acknowledgements
-------------- 
Thanks to the [Code Institute](https://codeinstitute.net) for the tutorials and resources. 