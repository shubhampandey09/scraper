# importing Libraries
import requests
from bs4 import BeautifulSoup


# asking input for sorting way
sorting_way = raw_input("Enter integer for sort method: 0. Popularity 1. Relevance 2. Price low to high"
                        "3. Price high to low 4. Recent")
sort_ways_list = ["popularity", "relevance", "price_asc", "price_desc", "recency_desc"]

# inserting search word and sorting way in the url
url = "http://www.flipkart.com/{}/pr?\
p%5B%5D=sort%3D{}&sid=tyy%2C4io&filterNone=true&q=mobile".format("mobile", sort_ways_list[int(sorting_way)])

# getting response from the server and getting the html part using beautiful soup
fetch = requests.get(url)
src = fetch.text
obj = BeautifulSoup(src, "lxml")

# In case want to print the html code
"""print obj.prettify()"""

g = 0

product_list = []
product_link_list = []

# Getting product title and its link , into lists and printing them
for e in obj.findAll("a", {'class': 'fk-display-block'} and {'data-tracking-id': 'prd_title'}, limit=100):
    product_name = unicode(e.string)
    product_link = "http://www.flipkart.com/" + unicode(e['href'])
    product_list.append(product_name)
    product_link_list.append(product_link)
    g += 1
    print 'Product ' + str(g) + ' :' + product_name + '\n'
    print 'Link ' + str(g) + ' :' + product_link + '\n'

