# BuyIt - Platform

[![Build Status](https://travis-ci.org/gello94/buyit.svg?branch=master)](https://travis-ci.org/gello94/buyit)


Build for Code-Institute as Full Stack Milestone Project.

## UX

BuyIt-Platform is an e-commerce platform with full management of the commercial business online by the owner.

With BuyIt it is possible to:
- Sell Products
- Manage Orders
- Manage Earnings
- Manage Users

### Owner

The owner will have a full Dashboard with data analysis of the business rendered as charts.

There is no need to be an expert on computers. BuyIt Platform is very easy to use and the only things the owner has to do are:
- Add a Product
- Add a Category
- Add a Voucher
- Edit/Delete elements

There is no need of a Hi-Tech computer, BuyIt is a light, performant Platform, fully responsive.
This means that it is possible to have the full control of the Platform from a Mobile Phone or from a Tablet.

The dashboard was built as Mobile First and the charts are fully responsive, giving a nice and quick view about the business wherever the owner is, the only needed thing is an internet connection.

### User

But BuyIt is built as well to facilitate the User Experience of Buying Online.
The Checkout System is done by a Quick and safe Payment System, managed with [Stripe](https://stripe.com/).

The user has a Personal Profile Page where to manage and filter the orders and check the progress of the same.

Add an element is very easy and simple, the user can just add the quantity wanted of a product and click on the "add to chart" button and the product will be added to the chart.

The user can continue to shop or proceed to the checkout by checking the elements presents in the chart, where it is possible to modify the quantity or remove the product.

### Scope
The scope of this Project is to build an E-Commerce Platform to manage an internet business in an easy way having full management of the business itself.

As Example of Business I decided to use a shop of headphones/earphones, but the choice of the product category used is only as example of how this Platform works.

This is a responsive Web App with collection of data and demonstration of the use of the method **CRUD**:

```
C = Create 
R = Read 
U = Update 
D = Delete
```

### Moq Ups
The starting design drafts were done with the use of the free tool [Pencil Project](https://pencil.evolus.vn/).

The wireframe of the starting idea can be found divided for desktop and mobile devices at the following link:

- [Desktop Devices](https://github.com/gello94/buyit/tree/master/moqups/desktop)
- [Mobile Devices](https://github.com/gello94/buyit/tree/master/moqups/mobile-view)

The final design has changed slightly from the starting idea, multiple changes were applied to the website following ideas and improvements and the features implemented while developing the Web App.

An example is the Homepage with full width and height Background Carousel that was built as for my starting idea and then I decided to change the size of the same to 75% of the height view to made it easier for the user to navigate in the page.

## Scenarios

##### 1. New customer:
As a customer of an online shop I would like to find easy information about a product, easy access to the content of the shop and I would like to filter the products to don't look hours and hours trying to find what I'm searching for.

BuyIt helps the customers, there is a friendly search form in the navigation bar and the user can divide the products for categories.

##### 2. Registered customer:
As a registered customer of an online shop I would like to have a view of my orders, check what is the status of the orders and have info about the same. 
I would like as well to manage my details and info.

In BuyIt User Profile section there are displayed all the orders that the user has made with all the info about.

It is possible as well, by an extra navigation bar, to edit the User details and to change the password.

##### 3. Business Owner with no computer skills:
As an owner of a business I would like to have an online shop, but not having good computer skills will made difficult to understand and manage the business online without having someone that can manage it for me.

BuyIt is built as well for owner without computer skills, in fact, is very easy to use and everything can be managed by the Admin Dashboard, as already explained above.

##### 4. Business Owner that would like to keep track of the business:
As an owner I would like to check what are the trends of my business.

With BuyIt this can't be easier. In the Admin Dashboard is present a nice and easy to understand chart system that analyzes all the main and basic business field as earnings, orders, products and reviews.

The earning and orders Charts can be sets as Monthly View or Daily View, this one is set to show the last 30 days.

## Feature left to implement/ Planned future feature:
- Send email when an order status is updated
- Add quantity stock in product model
- Modify max-quantity add to cart pending on quantity stock 
- Render rating as star system (for same [django-likert-field](https://pypi.org/project/django-likert-field/) library will be used)
- Add delete account option
- Edit UI for confirm delete product button

## Technologies Used

For this project I used:

- [Visual Studio Code](https://code.visualstudio.com/)
- Used as Ide to develop the code.

- [Python](https://www.python.org)
- The project use **Python** as developing language to build BuyIt Platform and as a server side/back-end language.

- [Django](https://www.djangoproject.com/)
- The project use **Django** as Python Web Framework.

- [Django Rest Framework](https://www.django-rest-framework.org/)
- The project use **Django Rest Framework** to create the Dashboard Api and render the charts data.

- [Heroku Postgres](https://www.heroku.com/postgres)
- The project use **Heroku Postgres Free Service** as SQL Database Service.

- [HTML5]( https://en.wikipedia.org/wiki/HTML5)
- The project use **HTML5** to structure the content in line with modern semantic HTML5.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets#CSS_3)
- The project use **CSS3** to style the html content.

- [SCSS/SASS](https://sass-lang.com)
- The project use **SCSS**.

- [JavaScript](https://it.wikipedia.org/wiki/JavaScript)
- The project use **JavaScript** to manipulate the frontend.

- [JQuery](https://jquery.com)
- The project use **JQuery** to control toggle features.

- [Chart.js](https://www.chartjs.org/)
- The project use **Chart.js** to visualize the data.

- [Bootstrap](https://getbootstrap.com/)
- The project use **Materialize 0.100.2** to Layout the html content.

- [FontAwesome](https://fontawesome.com/)
- The project use **FontAwesome** to add icons for social media and contact forms.

- [Stripe](https://stripe.com/)
- The project use **Stripe** to manage epayments online.

- [Travis CI](https://travis-ci.org/)
- **Travis CI** was used as a continuous testing development tool.


#### Python Libraries Used

The following Python Libraries are installed and used in this project:
- *django bootstrap forms* used for styling of forms
- *pillow* needed for using images
- *dj database url* to allow connection to database url
- *psycopg2* to allow connection to postgress database
- *django storages* and *botoS3* used to link media and static files on *AWS S3*
- *gunicorn* to connect to heroku
- *pycodestyle* to check the style of the python code is correct and show any styling errors
- *coverage* to measure the code coverage in testing
- *django widget tweaks* to be able to personalize rendered forms
- *django filter* to add filtering

The full list of libraries used is present in requirements.txt file.


## Testing
Because of the size of the testing section all the testing information are present in a separate file.

[See Testing File](https://github.com/gello94/buyit/blob/master/TESTING.md)

## Deployment
The web site has been deployed on Heroku for hosting and on GitHub to share the full development code.

### Heroku
This page has been deployed to ["Heroku"](https://buyit-platform.herokuapp.com/).

- Created requirements.txt file with the code ```$ python freeze --local > requirements.txt```
- Created the Procfile with the code ```$ echo web: gunicorn buyit.wsgi:application>Procfile```
- Created a new Heroku App - unique name and EU Server
- Added the Heroku Postgress Database as resource
- Installed the package dj-database-url to allow connection to a database url
- Installed the package psycopg2 for connecting to postgress databases
- Installed the package gunicorn to connect the project to Heroku.
- Setup the default database in settings.py to the postgres database
- Migrated the project in order to use the new postgres datatbase
- Created a superuser
- Set up a AWS S3 bucket to serve the website
- Installed django-storages and botoS3 in order to use django with AWS S3
- Setup Django to connect with AWS
- Setup config variables in Heroku
- Disabled collectstatic in Heroku sto prevent uploading static files
- Connected Github repository to Heroku App through 'Deployment Method' in Heroku - App Dashboard
- Deploy Branch through Manual Deploy' in Heroku App Dashboard
- Added the heroku address to valid hosts in settings.py


### GitHub
The code has been deployed to ["Github"](https://github.com/gello94/buyit).

GitHub is used to host the code and publish the pages.

A new repository was created in GitHub called: buyit.

The repository has been pushed following these commands

```
>$git remote add origin https://github.com/gello94/buyit
>$ git push -u origin master
```

After a final Git Add and Git commit

```
>$git add .
>$git commit -m "final commit"
```

The pages were pushed to the GitHub repository

```
>$ git push -u origin master
>$Username
>$Password
```


### During development & Bugs

During the development I had an insidious problem having the following error code:

```
django.core.exceptions.ValidationError: [“'_auth_user_id' value must be an integer.”]
```

This problem was appearing at the logout and at the start I tried modifying my voucher system management and trying to understand better the Django session management. 

I asked for help to the StackOverflow community, my question can be found at the following link - https://stackoverflow.com/questions/58330033/django-core-exceptions-validationerror-auth-user-id-value-must-be-an-integ

After few days of researches and reading on the [Official Django Session Documentation](https://docs.djangoproject.com/en/2.2/topics/http/sessions/) and several changes to the voucher views code the problem seemed to be solved.

After few weeks I started having the same problem again and modify the voucher or deleting the session by python shell was not solving the problem this time. 

Then I decided to contact the tutoring support of Code Institute for more technical support, and thanks to Samantha Dartnall, tutor at Code Institute, I was redirected to build a personal context processor as possible solution to manage the voucher and store it as for the cart management.

After few hours of testing finally the solution of building a contexts.py in the Voucher app demonstrated successful and solved the problem.


### Media

- All images taken from https://pixabay.com/images/search/earphones/ with free licence to reuse.


## Extra Sources

More info were taken from the following documentation files and Communities:

- [Django - Documentation](https://docs.djangoproject.com/en/2.2/)
- [Stackoverflow](https://stackoverflow.com/) - widely used during this project to find errors similar to mine
- [PyPI](https://pypi.org/)
- [Stripe - Documentation](https://stripe.com/docs)
- [Bootsnipp - Quantity Spinner Snippet](https://bootsnipp.com/snippets/Max59)


## Credits

Thanks to CodeInstitute Slack Community helping me to find extra material to study to improve my knowledges to develop this web app. 

A big Thanks to all the students, always positive and very motivational during this year, always ready to help me were a problem was encountered and for all the advices given.

Thanks to the tutor Ali Ashik that has been always available to help me to understand and clarify areas of this project that were difficult to me.