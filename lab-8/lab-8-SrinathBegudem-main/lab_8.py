# Lab 8
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement


# ----------------- Question 1 -----------------
import requests
import string

import requests
import string

def count_unique_words(url):
    response = requests.get(url)
    if response.status_code == 200:
        text = response.text
        words = ''.join(c if c not in string.punctuation else ' ' for c in text).lower().split()
        unique_words = set(words)
        unique_count = len(unique_words)
        return unique_count
    else:
        return -1

# invoke the function with relevant args of your choice

url = "https://data.pr4e.org/romeo-full.txt"
unique_count = count_unique_words(url)



# ----------------- Question 2 -----------------


import requests
from bs4 import BeautifulSoup

def get_books_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        books = []
        for book in soup.find_all('article', class_='product_pod'):
            title = book.h3.a['title']
            price_text = book.find('p', class_='price_color').text.strip()[1:]
            price = float(price_text)
            books.append({'title': title, 'price': price})
        return books
    else:
        print("Failed to fetch webpage")
        return []


# invoke the function with relevant args of your choice

url = "http://books.toscrape.com"
book_data = get_books_data(url)

