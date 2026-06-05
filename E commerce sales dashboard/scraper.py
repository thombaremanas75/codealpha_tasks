# Ecommerce Sales Dataset using Web Scraping
# 100 Rows Dataset
# Using Requests + BeautifulSoup + Pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

# Website URL
url = "https://webscraper.io/test-sites/e-commerce/static"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all products
products = soup.find_all("div", class_="thumbnail")

# States
states = [
    "Maharashtra",
    "Delhi",
    "Gujarat",
    "Rajasthan",
    "Madhya Pradesh",
    "Uttar Pradesh"
]

# Categories
categories = {
    "Electronics": ["Mobiles", "Laptops", "Headphones"],
    "Fashion": ["Shirts", "Shoes", "Watches"],
    "Furniture": ["Tables", "Chairs", "Sofas"],
    "Accessories": ["Bags", "Wallets", "Belts"],
    "Books": ["Story", "Education", "Comics"]
}

# Payment Methods
payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash on Delivery",
    "Net Banking"
]

# Months
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

# Customer Names
customer_names = [
    "Harivansh",
    "Madhav",
    "Madan Mohan",
    "Shiva",
    "Aman",
    "Priya",
    "Rahul",
    "Sneha",
    "Rohan",
    "Kiran"
]

# Empty List
data = []

# Generate 100 Rows
for i in range(100):

    # Select Product
    product = products[i % len(products)]

    # Product Name
    name = product.find("a", class_="title")
    product_name = name.text.strip()

    # Amount / Price
    price = product.find("h4", class_="price")
    amount = float(price.text.replace("$", ""))

    # Quantity
    quantity = random.randint(1, 5)

    # Profit Calculation (20%)
    profit = round((amount * quantity) * 0.20, 2)

    # Category & Sub-Category
    category = random.choice(list(categories.keys()))
    sub_category = random.choice(categories[category])

    # Create Row
    row = {
        "Customer_Name": random.choice(customer_names),
        "Product_Name": product_name,
        "Category": category,
        "Sub_Category": sub_category,
        "Amount": amount,
        "Quantity": quantity,
        "Profit": profit,
        "State": random.choice(states),
        "Payment_Method": random.choice(payment_methods),
        "Month": random.choice(months)
    }

    # Add Row
    data.append(row)

# Create DataFrame
df = pd.DataFrame(data)

# Save CSV File
df.to_csv("ecommerce_sales_dataset.csv", index=False)

# Print First 10 Rows
print(df.head(10))

print("\n100 Rows Ecommerce Sales Dataset Created Successfully!")
print("File Saved: ecommerce_sales_dataset.csv")
