#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from models import Shelf, Book
import sqlite3

def construct_shelves(url):
    driver = webdriver.Firefox()
    driver.get(url)
    shelfContainer = driver.find_elements_by_class_name("userShowPageShelfListItem")
    shelves = [grab_shelf(ii) for ii in shelfContainer]
    driver.close()
    return shelves

def grab_shelf(shelf):
    name = re.split(r'\([0-9]+\)',shelf.text)[0].replace("(","").replace(")","").strip()
    num_books = int(re.findall(r'\([0-9]+\)',shelf.text)[0].replace("(","").replace(")",""))
    link = shelf.get_attribute("href")
    return Shelf(name,num_books,link)


def add_shelf_to_db(url):
    driver = webdriver.Firefox()
    driver.get(c[0].link)
    cookies = unpickle_thing("cookies")
    for ii in cookies:
        driver.add_cookie(ii)
    driver.get(c[0].link)
    driver.find_elements_by_id("shelfSettingsLink")[0].click()
    driver.find_elements_by_name("shelf[display_fields][isbn13]")[0].click()
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        # Calculate new scroll height and compare with last scroll height
        dd =driver.find_elements_by_id("infiniteStatus")

        frac,total = [int(jj) for jj in dd[0].text.replace(" loaded","").split(" of ")]
        if frac == total:
            break

    titles = driver.find_elements_by_class_name("field.title")
    author = driver.find_elements_by_class_name("author")
    isbn13 = driver.find_elements_by_class_name("isbn13")

    conn = sqlite3.connect('books.db')
    curs = conn.cursor()

    if len(titles) == len(author) == len(isbn13):
        for i in range(1,len(titles)):
            bb = Book(
                titles[i].text,
                author[i].text,
                titles[i].find_elements_by_class_name("value")[0].find_element_by_tag_name("a").get_attribute("href"),
                isbn13[i].text,
                shelf_url = url)
            curs.execute(f"INSERT into books values {astuple(bb)}")
    conn.commit()
    curs.close()

    driver.close()      

def sqlite_helper(query_str,db_name):
    conn = sqlite3.connect(db_name)
    curs = conn.cursor()
    curs.execute(query_str)
    output =  curs.fetchall()
    conn.commit()
    conn.close()
    return output
