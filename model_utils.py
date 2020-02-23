#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from models import Shelf, Book

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
