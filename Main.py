"""All tests go in here. Also includes data loading and test fixtures

Current tests:
test_iteminfo: Checks that names of items and IDs are paired correctly
test_searchitems: Checks that search retrieves items
test_mainlinks: Checks that links on mainpage work
test_carttotal: Checks that cart can add items and calculate total
test_cartempty: Checks that cart can be emptied
"""
import time

import pytest
from selenium import webdriver

from CommonFunctions import *
from Pages import *
from TestData import LoadCSV
from Validator import CommonChecks

#Below we load our data and set up our URLs
Products = LoadCSV.loadfile('ProductData.csv')
urlstem = "http://automationpractice.com/index.php?id_product="
urlend = "&controller=product"
mainurl = "http://automationpractice.com/index.php"



#This fixture works with pytest to set up one browser session for all tests
@pytest.fixture(scope="session")
def wdriver():
    """Fixture to start driver and have available for all tests"""
    return webdriver.Chrome()

# This parameter goes to iteminfo, getting the name and value from the Products
# and pass them as arugments as it runs the test for each of them
@pytest.mark.parametrize("id,namevalue", [
    (k, v["Name"]) for (k, v) in Products.items()]
                         )
def test_iteminfo(wdriver, id, namevalue):
    """Check name is associated with correct ID in URL for each item"""
    wdriver.get(urlstem + id + urlend)
    nametocheck = find(wdriver, ItemPage.productnames).text
    assert CommonChecks.comparetext(nametocheck, namevalue) is True

# This parameter goes to iteminfo, getting the name Products
# and passes it as an arugment as it runs the test for each name
@pytest.mark.parametrize("namevalue", [Products[v]["Name"] for v in Products])
def test_searchitems(wdriver, namevalue):
    """Search for the first 3 letters of each name and confirm priduct appears in results"""
    wdriver.get(mainurl)  # clear text by loading page fresh
    searchbar = find(wdriver, PageBasic.searchbar)
    searchbutton = find(wdriver, PageBasic.searchbutton)

    # It will search for the item using the first three letters of it's name
    MenuText(wdriver).searchfor(searchbar, searchbutton, namevalue[:3])
    nametocheck = find(wdriver, SearchPage.searchnames)
    if isinstance(nametocheck, list) is True:  # check if list
        assert CommonChecks.isinlist(nametocheck, namevalue) is True
    else:
        nametocheck = nametocheck.text
        assert CommonChecks.comparetext(nametocheck, namevalue) is True


def test_mainlinks(wdriver):
    """Test first 5 links on homepage"""
    wdriver.get(mainurl)
    for i in range(0, 4):
        namesonpage = find(wdriver, MainPage.productnames)

        linkname = namesonpage[i].text
        time.sleep(1) #Sleep to give page time to load
        namesonpage[i].click()
        pagename = find(wdriver, ItemPage.productnames)
        if isinstance(pagename, list) is True:
            pagename = pagename[0].text
        else:
            pagename = pagename.text
        CommonChecks.comparetext(linkname, pagename)
        wdriver.back()
        time.sleep(.5)


def test_carttotal(wdriver):
    """Test to add all Products to cart and check total adds correctly"""
    cartotal = 0
    for item in Products:
        wdriver.get(urlstem + item + urlend)
        ItemPage.add_to_cart(wdriver)
        if Products[item]["Price"] is not "N/A": #Load CSV places N/A in price on error
            cartotal += float(Products[item]["Price"])
            print(cartotal)
    find(wdriver, PageBasic.cartbutton).click()
    totalcheck = find(wdriver, CartPage.notaxtotal).text #Gets total that excludes tax
    totalcheck = totalcheck.replace("$", "")
    assert CommonChecks.comparetext(cartotal, float(totalcheck)) is True
    itemincart = find(wdriver, CartPage.productnames)


    #Also checks that item names in cart are correct
    for item in Products:
        assert CommonChecks.isinlist(itemincart, Products[item]["Name"]) is True


def test_cartempty(wdriver):
    """Paired with prior test to check that cart is emptied successfully"""
    for item in Products:
        wdriver.get(urlstem + item + urlend)
        ItemPage.add_to_cart(wdriver)
    wdriver.get('http://automationpractice.com/index.php?controller=order')

    for item in Products:

        trash = find(wdriver, CartPage.trashbutton)
        removeditem = find(wdriver, CartPage.productnames)
        if isinstance(trash, list) is True: #To handle lists and single items
            removeditem = removeditem[0].text
            print(removeditem)
            trash[0].click()
            time.sleep(1)
            itemincart = find(wdriver, CartPage.productnames)
            CommonChecks.isinlist(itemincart, removeditem)
        else:
            trash.click()
            time.sleep(1)
            assert find(wdriver, CartPage.productnames).text == ""
