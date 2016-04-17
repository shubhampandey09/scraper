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
    fetch = requests.get(x)
    src = fetch.text
    obj = BeautifulSoup(src, "lxml")
    for e in obj.find_all("a", {'class': 'fk-display-block'} and {'data-tracking-id': 'prd_title'}, limit=20):
        product_name = unicode(e.string)
        product_link = "http://www.flipkart.com" + unicode(e['href'])
        g += 1
        product_list.append('Product ' + str(g) + ' :' + product_name)
        product_link_list.append(product_link)
    return product_list, product_link_list


def get_reviews(y, p, r):
    review_list = []
    fetch1 = requests.get(y)
    src1 = fetch1.text
    obj1 = BeautifulSoup(src1, "lxml")
    for e in obj1.find_all("p", {'class': 'review-title'}):
        r += 1
        review = unicode(e.string)
        review_list.append('Product ' + str(p) + 'review' + str(r) + ' :' + review)
    return review_list

url = [0, 1, 2, 3, 4]
page = 21
p_list = [[], [], [], [], []]
p_l_list = [[], [], [], [], []]
r_list = []
m = 0
n = 0
pn = 1
temp_list = []

url[0] = "http://www.flipkart.com/{}/pr?p%5B%5D=sort%3D{}&\
sid=tyy%2C4io&filterNone=true&q={}".format(search_word, sort_ways_list[int(sorting_way)], search_word)


for i in range(1, 5, 1):
    url[i] = "http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?p%5B%5D=sort%3D{}&\
sid=tyy%2C4io&filterNone=true&start={}&\
q={}&ajax=true&_=1460481718759".format(sort_ways_list[int(sorting_way)], page, search_word)
    page += 20

for k in url:
    p_list[m], p_l_list[m] = scraper(k, n)
    m += 1
    n += 20

for lin in p_l_list:
    for link in lin:
        rn = 0
        temp_list = get_reviews(link, pn, rn)
        r_list.append(temp_list)
        pn += 1

final_p_l = list(itertools.chain(*p_list))
final_r_l = list(itertools.chain(*r_list))

print '\n'.join(final_r_l)
"""
with open('Product_List_flipkart', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(final_r_l)
"""
