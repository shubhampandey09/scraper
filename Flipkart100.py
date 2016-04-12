# importing Libraries
import requests
from bs4 import BeautifulSoup
import itertools
import csv


search_word = "mobile"
sorting_way = raw_input("Enter integer for sort method: 0. Popularity 1. Relevance 2. Price low to high"
                        "3. Price high to low 4. Recent")
sort_ways_list = ["popularity", "relevance", "price_asc", "price_desc", "recency_desc"]


def scraper(x, g):
    product_list = []
    product_link_list = []
    #g = 0
    fetch = requests.get(x)
    src = fetch.text
    obj = BeautifulSoup(src, "lxml")
    for e in obj.find_all("a", {'class': 'fk-display-block'} and {'data-tracking-id': 'prd_title'}, limit=20):
        product_name = unicode(e.string)
        product_link = "http://www.flipkart.com/" + unicode(e['href'])
        g += 1
        product_list.append('Product ' + str(g) + ' :' + product_name)
        product_link_list.append('Link ' + str(g) + ' :' + product_link)
    return product_list, product_link_list

url = [0, 1, 2, 3, 4]
page = 21

url[0] = "http://www.flipkart.com/{}/pr?p%5B%5D=sort%3D{}&\
sid=tyy%2C4io&filterNone=true&q={}".format(search_word, sort_ways_list[int(sorting_way)], search_word)


for i in range(1, 5, 1):
    url[i] = "http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?p%5B%5D=sort%3D{}&\
sid=tyy%2C4io&filterNone=true&start={}&\
q={}&ajax=true&_=1460481718759".format(sort_ways_list[int(sorting_way)], page, search_word)
    page += 20

p_list = [[], [], [], [], []]
p_l_list = [[], [], [], [], []]
m = 0
n = 0
for k in url:
    p_list[m], p_l_list[m] = scraper(k, n)
    m += 1
    n += 20

final = list(itertools.chain(*p_list))
print '\n'.join(final)


with open('Product_List_flipkart', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(final)
