# Week 1.3, Session 2: Sales Data Statistics
#Date,Product,Sales_Amount,Units_Sold,Region
#2024-01-01,Widget A,5000,50,North
# We want to analyse a set of sales data in sales.csv

with open("sales.csv", "r") as infile:
    header = infile.readline()        

    top_sale = 0
    top_date = ""
    top_product = ""

    total_sales = 0
    count_rows = 0

    units_per_widget = {}            

    for line in infile:
        date, product, sales, units, region = line.strip().split(",")
        sales = int(sales)              
        units = int(units)

        if sales > top_sale:
            top_sale = sales
            top_date = date
            top_product = product

        total_sales += sales
        count_rows += 1

        units_per_widget[product] = units_per_widget.get(product, 0) + units

    average_sale = total_sales / count_rows

    best_widget = max(units_per_widget, key=units_per_widget.get)
    best_widget_units = units_per_widget[best_widget]

    print(f"Largest sale day:  {top_date} ({top_product}, ${top_sale:,})")
    print(f"Average sale:      ${average_sale:,.2f}")
    print(f"Most sold widget:  {best_widget} ({best_widget_units} units)")
# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format


# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows