# BuyIt - Platform

[![Build Status](https://travis-ci.org/gello94/buyit.svg?branch=master)](https://travis-ci.org/gello94/buyit)


Build for Code-Institute as Full Stack Milestone Project.

## UX

BuyIt-Platform is an e-commerce platform with full management of the commercial business online by the owner.

With BuyIt it is possible to:
- Sell Products
- Manage Orders
- Manage Earning
- Use Voucher code
- Manage Users

### Owner

The owner will have a full Dashboard with data analisys of the business rendered as charts.

There is no need to be expert in computer. BuyIt Platform is very easy to use and the only things the owner has to do are:
- Add a Product
- Add a Category
- Add a Voucher
- Edit/Delete elements

There is no need of an Hi Tech computer, BuyIt is a light, performant Platform, build for computer but full responsive.
This means that is is possible to have the full control of the Platform from a Mobile Phone or from a Tablet.

The dashboard was build as Mobile First and the charts are full responsive, giving a nice and quick view about the business wherever the owner is, the only needed thing is an internet connection.

### User

But BuyIt is build as well to facilitate the User Experience of Buying Online.
The Checkout System is done by a Quick and safe Payment System, managed with [Stripe](https://stripe.com/).

The user has a Personal Profile Page where to manage and filter the orders and check the progress of same.

Add an element is very easy and simple, the user can just add the quantity wanted of a product and click on the "add to chart" button and the product will be added to the chart.

The user can continue to shop or proceed to the checkout by checking the elements presents in the chart, where it is possible to modify the quantity or remove the product.

### Scope
The scope of this Project is to build an E-Commerce Platform to manage an internet business in an easy way having a full management of the business itself.

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

- [Desktop Devices](#)
- [Mobile Devices](#)

The final design has changed slightly from the starting idea, multiple changes were applied to the website following ideas and improvements and the features implemented while developing the Web App.

An example is the Homepage with full width and height Backgound Carousel that was build as for my starting idea and then I decided to change the size of the same to 75% of the height view to made it easier for the user to navigate in the page.

## Scenarios

##### 1. New customer:
As customer of an online shop I would like to find easy information about a product, easy access to the content of the shop and I would like to filter the products to don't look hours and hours trying to find what i'm searching for.

BuyIt help the customers, there is a friendly search form in the navigation bar and the user can divide the products for categories.

##### 2. Registered customer:
As a registered customer of an online shop I would like to have a view of my orders, check what is the status of the orders and have info about same. 
I would like as well to manage my details and info.

In BuyIt User Profile section there are displayed all the orders that the user has made with all the info about.

In is possible as well, by an extra navigation bar, to edi the User deatails and to change the password.

##### 3. Business Owner with no computer skills:
As a owner of a business I would like to have an online shop, but not having good computer skills will made difficult to understand and manage the business online without have someone that can manage it for me.

BuyIt is build as well for owner without computer skills, in fact is very easy to use and everythig can be managed by the Admin Dashbord, as already explained above.

##### 4. Business Owner that would like to keep trace of the business:
As a owner I would like to check what are the trends of my business.

With BuyIt this can't be easier. In the Admin Dashboard is present a nice and easy to understand chart system that analyze all the main and basic business field as earnings, orders, products and reviews.

The earning and orders Charts can be sets as Monthly View or Daily View, this one is set to show the last 30 days.

## Feature left to implement:
- Send email from email.html template on order received and on order status change

All images taken from https://pixabay.com/images/search/earphones/

Quantity snipper taken from https://bootsnipp.com/snippets/Max59

