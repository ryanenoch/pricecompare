# pricecompare
This is a Python Dash web app that can show the latest prices for each product. Makes use of DuckDB SQL database management system to query prices from CSV data
<img width="1059" alt="Screen Shot 2023-02-28 at 12 20 41 AM" src="https://user-images.githubusercontent.com/105472843/221761276-ab87eeff-7b9b-40e2-bd13-9c8a0b2de973.png">
**Note:** The above screenshot is taken on a Macbook using Brave Browser. The web app may look differently depending on the device and the web browser used

### How does it work?
On initial setup, the CSV price data is copied to a table in the SQL database. Then the SQL queries are executed on the table to show the latest price changes and product availability. The results are obtained as a dataframe and displayed to the user using a Dash datatable on the web app

### How to Use:
It's simple. Just type part of the name of the product and you will get the list of products matching your input and their prices. Now you can compare prices and potentially save money on groceries
