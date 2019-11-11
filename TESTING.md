# BuyIt - Platform -- Testing

Build for Code-Institute as Full Stack Milestone Project.

## Django Test Suite

I used the Django Test Suite to test all my apps and used Coverage to generate a report in which scored 97% with 123 tests. 

A full screen of all the testing percentage can be found [here](https://github.com/gello94/buyit/blob/master/final_coverage.png) as separate file.

All tests can be viewed within each app folder.

Testing for Django Rest Framewrok API not executed because of limited experience with testing and timing problems, I will go deeper in testing after the end of the course, understanding the importance of a clear and performant testing.

## Travis CI

I used Travis CI as continuous integration service testing the project on every deployment on github.

## Manual Testing 

### Users & Authentications - Accounts App

#### Register a new user testing form errors
- Click the register link on the navigation bar
- Try to create a test account with not matching password and check error status
- Try to miss values in field to see error fields
- Register a new testing user with a valid email
- Redirected now on personal page
- Check that 'Profile' and 'Logout' voices appear on navigation bar
- Check personal email to check the registration welcoming email with welcome voucher code


#### Register a customer who is already logged in
- Log in
- Enter register link
- Check that the user is correctly redirected to the personal page


#### Login a registered user testing form errors 
- Click on Login in the navigation bar
- Enter incorrect details and check error messages
- Enter correct details
- User now redirected to Personal page
- Check that 'Profile' and 'Logout' voices appear on navigation bar

#### Try to login in already logged
- Log in
- Enter login link
- Check that the user is correctly redirected to the personal page


#### Logout a user
- Login
- Click on Logout in navigation bar
- User redirected in homepage and check logged out message


#### Reset password
- Go to Login page (if already logged it logout first)
- Click on 'Forgot my password'
- Add your email address
- Check your email provider
- Click on the link provided
- Follow the instruction and add a new password
- Click on the Login link and login

#### Edit user details
- Login
- Go to the personal page
- Click on "Edit Personal Info"
- Try to change the email using an existing email, for example use 'user1@testing.com'
- Try to change the username using an existing username, for example use 'user1'
- Try to add unique username/email
- Check success change name alert


#### Edit password
- Login
- Go to the personal page
- Click on "Edit Password"
- Insert old password
- Insert new valid password
- Check success change name alert

### Dashboard App

#### Enter Dashboard
- Login as superuser with following user details:
``` 
Username: admin
Password: admin
```
N.B.: This user will be deleted after the project assessment by CodeInstitute assessors.
- Check the new voice on the navbar 'Dashboard'
- Click on the Dashoard link
- Navigate in the Dashboard

#### Test Data Visualization Views
- Enter in the Dashboard Homepage
- Click on "Daily" in the earnings or in the orders chart view
- Move the pointer in any of the chart areas to find more details about

#### Test Stock Percentage and Percentage Bar
- Enter in the Dashboard Homepage
- Go to Products
- Click on the side narrow
- Click on "Stock Status"
- Select Not in Stock/In stock (products are in stock by default)
- Click the Submit button
- Go to the Dashboard Homepage
- Check The changes in the percentage and on the progress bar

#### Test Order Filtering
- Enter in the Dashboard Homepage
- Go to Orders
- Click on Filter Button
- Enter a filter (example enter Order Status: Delivered)
- Click on Filter Button
- Check the filtered orders

#### Test Change Order Status
- Enter in the Dashboard Homepage
- Go to Orders
- Click on the order id
- Select as order status 'Delivered'
- Click on 'Change Status' button
- Check the order status change and the icon change

#### Test Add A Product
- Enter in the Dashboard Homepage
- Go to Add a Product
- Fill the form
- Click on 'Save' button
- Check the product added in the products list

#### Test Edit A Product
- Enter in the Dashboard Homepage
- Go to Products
- Click on the side narrow
- Click on 'Edit'
- Edit a voice of the form
- Click on 'Save' button
- Check the changes in the product details view

#### Test Delete A Product
- Enter in the Dashboard Homepage
- Go to Products
- Click on the side narrow
- Click on "Delete Product"
- Click on "Yes, Delete" to delete product

#### Test Add a Category
- Enter in the Dashboard Homepage
- Go to Add a Category
- Click on "Save"
- Go to Products
- Click on 'Edit'
- Check the new category voice between the categories


#### Test Edit / Delete Voucher
- Enter in the Dashboard Homepage
- Go to Voucher
- Click on "Edit" to edit the voucher
- Click on 'Save' to apply changes
- Check the new changes
- Click on "Delete" to delete VOucher
- Check the voucher is not anymore on the list


#### Test Add a Voucher
- Enter in the Dashboard Homepage
- Go to Voucher
- Click on "Add a Voucher"
- Fill the form
- Click on 'Save' to apply changes
- Go on Voucher to check the added voucher


### Add to Cart - Cart App

#### Test Add a Product to the Cart and Cart View
- Go to All Products page
- Select a product quantity
- Click on the "Add to Cart" icon
- Check the quantity of products in the cart icon in the navigation bar
- Click on the cart icon in the navication bar
- Check you products in the cart

#### Test Modify Quantity of Products
- Go to All Products page
- Select a product quantity
- Click on the "Add to Cart" icon
- Check the quantity of products in the cart icon in the navigation bar
- Click on the cart icon in the navication bar
- Check you products in the cart
- Change Quantity number in the product details
- Click on Amend
- Check the updated quantity

#### Test Renove Product from Cart
- Go to All Products page
- Select a product quantity
- Click on the "Add to Cart" icon
- Check the quantity of products in the cart icon in the navigation bar
- Click on the cart icon in the navication bar
- Check you products in the cart
- Click on "Remove"
- Check that the product in not anymore in the cart


#### Test Shipping Costs
- Go to All Products page
- Select a product with price less than 49.99€
- Click on the "Add to Cart" icon
- Check the quantity of products in the cart icon in the navigation bar
- Click on the cart icon in the navication bar
- Check you products in the cart
- Check the Shipping costs are 10.00€
- Amend quantity of product to reach the cost > 49.99€
- Check the Shipping Costs are 0.00€


### Add a Voucher Code in Cart - Voucher App

#### Test add a voucher if user not logged
- If logged in Logout
- Go to All Products page
- Select a product
- Click on the "Add to Cart" icon
=- Click on the cart icon in the navication bar
- Check you products in the cart
- Add voucher code 'new'
- Click on 'Redeem'
- Check warning alert message


#### Test add a voucher if user logged in
- If logged in Logout
- Go to All Products page
- Select a product
- Click on the "Add to Cart" icon
- Click on the cart icon in the navication bar
- Check you products in the cart
- Add voucher code 'new'
- Click on 'Redeem'
- Check new total and success alert message


### Checkout and Payment - Order App

#### Test order a product
- If logged in Logout
- Go to All Products page
- Select a product
- Click on the "Add to Cart" icon
- Check the quantity of products in the cart icon in the navigation bar
- Click on the cart icon in the navication bar
- Check you products in the cart
- Click on 'Checkout'
- Check your order summary
- Fill the personal info form
- Use the number card '4242424242424242'
- Use '123' as cvv
- Use a future date
- Check alert message in your personal page after the redirect
- Check the order details in your personal page


#### Test order a product with invalid card
- If logged in Logout
- Go to All Products page
- Select a product
- Click on the "Add to Cart" icon
- Check the quantity of products in the cart icon in the navigation bar
- Click on the cart icon in the navication bar
- Check you products in the cart
- Click on 'Checkout'
- Check your order summary
- Fill the personal info form
- Fill the card details form with invalid input eg. card number or invalid date
- Check warning alert


### Products App

#### Filter by category
- Go to All Products page
- Click on 'Filter By Categories'
- Check the product in that category

### Review App

#### Add a review if logged
- Login
- Click on one product to acceed to the Product Detail page
- Click on "Add a Review"
- Fill the review form
- Check the new review on the product details page

#### Add a review if logged but already reviewed a product
- Login
- Click on the product you have already reviewed
- Click on "Add a Review"
- Check the warning alert message

#### Add a review if not logged in
- Login
- Click on the product you have already reviewed
- Click on "Add a Review"
- Check that the redirected page is the login page


### Cross Web Testing

#### Mobile Browsers
* Chrome
* Safari
* Internet Samsung 

#### Desktop Browsers
* Chrome
* Firefox
* Edge

#### Devices
* Hp Laptop
* Acer Laptop
* Samsung S8
* iPhone X
* Vernee Thor
* 42" Screen Desktop PC

During the testing I used Chrome Developer tools to test the responsive design on different size and the features of the page on different width.

Chrome Developer tools was used during the developing process to test HTML, CSS, JavaScript and jQuery.

Javascript and jQuery testing was done by using the ```console.log('function called')``` code in the function i wanted to check or by using the DOM.




















