import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import re

# Customer Names
customer_names = [
    "Aarav", "Vivaan", "Aditya", "Siddhi",
    "Anaya", "Priya", "Rahul", "Sneha",
    "Rohan", "Neha"
]

# States
states = [
    "Maharashtra",
    "Delhi",
    "Karnataka",
    "Gujarat",
    "Tamil Nadu",
    "Rajasthan",
    "Punjab",
    "Kerala"
]

# Payment Methods
payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash on Delivery",
    "Net Banking"
]

# Categories
categories = [
    "Books",
    "Electronics",
    "Fashion",
    "Home",
    "Beauty"
]

# Empty list
all_products = []

# Scrape only 5 pages
# Each page has around 20 products
# Total ≈ 100 rows

for page in range(1, 6):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all(
        "article",
        class_="product_pod"
    )

    for product in products:

        # Product Name
        product_name = product.h3.a["title"]

        # Price
        price_text = product.find(
            "p",
            class_="price_color"
        ).text

        # Clean Price
        price = float(
            re.sub(r"[^\d.]", "", price_text)
        )

        # Rating
        rating = product.p["class"][1]

        # Random Discount
        discount = random.randint(5, 50)

        # Random Reviews
        reviews = random.randint(20, 500)

        # Profit
        profit = round(
            price * random.uniform(0.10, 0.35),
            2
        )

        # Random Fields
        customer = random.choice(customer_names)

        state = random.choice(states)

        payment = random.choice(payment_methods)

        category = random.choice(categories)

        # Store Data
        all_products.append({
            "Customer Name": customer,
            "Product Name": product_name,
            "Category": category,
            "Price": price,
            "Discount (%)": discount,
            "Rating": rating,
            "Reviews": reviews,
            "Payment Method": payment,
            "Profit": profit,
            "State": state
        })

# Create DataFrame
df = pd.DataFrame(all_products)

# Keep only first 100 rows
df = df.head(100)

# Save CSV
df.to_csv(
    "ecommerce_dataset_100_rows.csv",
    index=False
)

# Save Excel
df.to_excel(
    "ecommerce_dataset_100_rows.xlsx",
    index=False
)

# Print Dataset
print(df)

print("\n100 Rows Dataset Created Successfully!")
