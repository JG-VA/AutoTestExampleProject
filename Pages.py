from selenium.webdriver.common.by import By
import time


class PageBasic(object):
    """Parent class with objects on all pages of website\n
    Kewword Arguments:\n
    driver: this one holds the driver for things that need it\n
    searchbar: Searchbar on page, found by looking for a class with CSS\n
    searchbutton: Search button, looks for button inside a specific class\n
    infoitems: Items at the bottom of the page, found with ID\n
    cartbutton: Button for going to car, uses CSS to look under a div with a specific ID\n
    All attributes are tuples, containing the locator strategy and the string for driver\n

    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.timeout = 30

    searchbar = (By.CSS_SELECTOR, '#search_query_top')
    searchbutton = (By.CSS_SELECTOR, "#searchbox > button")
    infoitems = (By.CSS_SELECTOR, "#block_various_links_footer")
    cartbutton = (By.CSS_SELECTOR, "div.shopping_cart > a")


class MainPage(PageBasic):
    """Class for the homepage\n
\n
    Kewword Arguments:\n
    productnames: all of the prodcut names displayed on the page\n
    productprice: all of the product prices displayed on the page\n
    topmenuID: A menu at the top\n
    bestsellers: Products in the best seller area"""
    productnames = (By.CSS_SELECTOR, "a.product-name")
    productprice = (By.CSS_SELECTOR, "span.price.product-price")
    topmenuID = (By.ID, "block_top_menu")
    bestsellers = (By.ID, "blockbestsellers")


class SearchPage(PageBasic):
    """Class for search results. searchnames is list of product names retrieved"""
    searchnames = (By.CSS_SELECTOR, "div.right-block > h5 > a.product-name")


class ItemPage(PageBasic):
    """Class for the detail page of an item\n

    Kewword Arguments:\n
    productnames: Name of product\n
    productprice: price of product\n
    productdescription: body text describing product\n
    productimage: image of product\n
    addtocart: button for adding to cart\n
    xclose: x button to close window that appears after adding to cart\n

    Note that the selectors used here are different from other places where\n
    products appear, that is needed"""
    productnames = (By.CSS_SELECTOR, ".pb-center-column > h1:nth-child(1)")
    productprice = (By.ID, "our_price_display")
    productdescription = (By.ID, "short_description_content")
    productimage = (By.ID, "bigpic")
    addtocart = (By.CSS_SELECTOR, "#add_to_cart > button")
    xclose = (By.CSS_SELECTOR, ".cross")

    def add_to_cart(driver):
        """Add item to cart. Needed own function to close pop-up afterwards"""
        driver.find_element(ItemPage.addtocart[0], ItemPage.addtocart[1]).click()
        time.sleep(1)
        driver.find_element(ItemPage.xclose[0], ItemPage.xclose[1]).click()


class CartPage(PageBasic):
    """Page for the user's current shopping cart\n

    Keyword arguments:\n
        productnames: Name of product\n
        productprice: price of product\n
        trashbutton: Buttons to remove items from cart\n
        notaxtotal: Total without taxes, useful for checking that addition is correct\n
    """
    productnames = (By.CLASS_NAME, 'product-name')
    productprice = (By.CLASS_NAME, 'cart_unit')
    trashbutton = (By.CLASS_NAME, 'icon-trash')
    notaxtotal = (By.ID, 'total_product')
