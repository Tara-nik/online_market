 

## Distinctiveness and Complexity:

This market web application offers consumers an easy-to-use and practical platform for browsing, purchasing, and managing goods. Users may easily register, log in, and manage their accounts, ensuring a personalized experience, thanks to strong authentication measures. Users may quickly explore a wide selection of products, put items in their carts, choose preferred delivery windows, and have a clear picture of their orders and overall expenses thanks to the user-friendly design. By utilizing the Django admin interface, administrators can easily add new products to the site, keeping the store current and varied.

Across every device, our application offers an agile and responsive shopping experience. Users may browse comprehensive product information, move between pages with ease, and confidently make transactions. Because SQLite is integrated as the default database, effective data storage and retrieval are ensured, which improves the application's overall reliability and efficiency.

This web application is different because, while it is simple, it offers features for better and more efficient use. For instance, on this marketplace site, users can make purchases by adding credit and easily manage their credit balance. A distinguishing feature of this application is the ability to select different delivery times, which automatically adjusts the price. In this process, if a customer's purchase exceeds their available credit, they are redirected to the credit management page for further action.

All in all, this market web application provides an all-inclusive solution that makes shopping easier and product administration more effective for both administrators and users. All stakeholders may enjoy a hassle-free and joyful experience on this platform, which meets their needs whether consumers are looking for their favorite goods, handling their orders, or administrators are adding new products to the store.


## What is contained:

-   **User Authentication**
-   **Adding Credit** 
-   **Goods Management** 
-   **Delivery Time Selection** 
-   **Order Summary** 
-   **Order Checkout** 
-   **Admin Functionality** 

## Installation & how to run the application

-   pip install -r requirements.txt
-   python manage.py migrate
-   python manage.py runserver

## Usage

### Register/Login

-   **Register** 
-   **Login** 

### Browsing Goods

-   Once logged in, you can browse available goods by clicking on the "Make Your Order" link in the navigation bar. This will take you to a page displaying all the goods available for purchase.

### Adding Goods to Cart

-   To add goods to your cart, click on the goods' name or image to view details. From there, you'll have the option to add the goods to your cart by clicking the "Add to Cart" button.

### Choosing Delivery Time

-   After adding goods to your cart, you can proceed to choose a delivery time. Click on the "Your Order" link in the navigation bar to view your cart summary. From there, you can select a delivery time from the available options presented.

### Reviewing Order Details

-   On the order detail page, you'll see a summary of the goods you've selected, along with their prices and the chosen delivery time. You'll also see the total price of your order.

### Checkout and Placing Order

-   If everything looks good, proceed to checkout by clicking the "Checkout" button. This will prompt you to confirm your order and deduct the total price from your account's credit (if sufficient).
    
-   If you have enough credit to cover the total price, your order will be successfully placed, and you'll be redirected to the home page with a confirmation message.
    
-   If you don't have enough credit to cover the total price, you'll receive an error message indicating insufficient credit. You'll then be redirected to the "Add Credit" page to top up your account balance. After adding credit, you can proceed with the checkout process again.
    
### Admin Functionality

-   **Adding New Products:** Administrators have the ability to add new products to the product list. To do this, the administrator should log in to the Django admin interface.
    
    -   Navigate to the admin interface by appending "/admin" to the base URL of the application and logging in with admin credentials.
    -   the administrator can access the "Goods" section, where all existing products are listed.
    -   To add a new product, the administrator can click on the "Add" button and fill out the required fields, such as the name, image URL, and price of the product.
    -   the administrator can save the new product, making it available for users to browse and purchase on the market web application.

### Adding Credit

-   click on the "Add Credit" link in the navigation bar. Enter the amount you wish to add, and the credit will be added to your account balance.

### Logging Out

## Files
-   market is the app where all the required files are present
-   market/static contains all the CSS, JS of the project.
-   market/templates contains all the HTML files of the project.
-   market/models.py contains all the models.
-   market/views.py contains all the views.
-   market/urls.py contains all the URLS.

## Technologies Used

-   **Django** 
-   **HTML/CSS** 
-   **JavaScript** 
-   **Bootstrap** 
-   **SQLite** 

[Enter the link to watch the video](https://www.youtube.com/watch?v=i8ljqNvPe5g)
