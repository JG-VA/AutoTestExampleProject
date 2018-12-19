**Intro:**

This Python framework is designed to automate the testing of the example website. It uses Selenium for automating actions inside the browser, and Pytest for organizing the tests. You will need Chromedriver installed and your PATH variable set to run the tests. Several tests are included, along with supporting modules. The tests themselves are held in the Main file, and are run with Pytest. The test fixtures are also in this file. To allow for flexibility, other areas have been separated into their own files. TestData is for loading and processing the test data, Pages holds references and methods related to specific parts of the website, CommonFunctions holds functions that may be used repeatedly by tests, and Validator holds functions for checking correctness to evaluate test results.

**Getting Started:**

Let’s look at an example test:

``` 
def test_iteminfo(wdriver, id, namevalue): 
_"""Check name is associated with correct ID in URL for each item"""_ 
wdriver.get("http://automationpractice.com/index.php?id_product="
+ id + "&controller=product")  
  nametocheck = find(wdriver, ItemPage.productnames).text assert CommonChecks.comparetext(nametocheck, namevalue) is True
```
Our tests are held in functions, designated with the word test_ in front of the name. This works with Pytest’s discovery feature. We pass in three arguments: the selenium WebDriver used to perform actions is first, the item’s id is the second, and the item’s name is the third. To check that the name is correct, the WebDriver navigates to a url based on the id with the first line of code. Then it calls the function to look for the name on the page second line with the second. Finally, it passes both the intended name given at the start of the function and the name it found on the page into a function to check if they are the same. Pytest will record if it passed or failed and collect the results along with other tests.

**Running a test**

run_test.py will invoke Pytest to run the tests found in Main. If you would like to only run a few tests or invoke other options, Pytest’s built in functions are useful, the full documentation can be found here: https://docs.pytest.org/en/latest/contents.html . Pytest also accepts Fixtures, which are set up actions performed before tests to ensure conditions are right, or run after tests to clean up loose ends. Here’s an example fixture:

``` @pytest.fixture(scope="session") def wdriver(): _"""Fixture to start driver and have available for all tests"""_ return WebDriver.Chrome()``` 

**Creating a test**

Before creating a test, it is beneficial to think about what the test needs to accomplish. There are many ways of thinking about testing, a simple three step process is provided below:

**1.** Figure out what you want to check, and any necessary preconditions

**2.** Determine the actions you will need to perform from starting your test until you are ready to confirm

**3.** Decide how you will confirm that the system behaved as expected

Once you know these three pieces of information, you should be ready to write your test. This framework has been made with the intention to follow logically from this three step model. 


Test data which is supplied before the test is executed should be loaded with a function in the TestData module; currently it supports CSV files that are transformed into Python Dictionaries for use in testing. Reading from an external file increases flexibility. Either way, if you need pre-existing data, it must be loaded beforehand and be available for use with your test function.

Executing actions will be the bulk of most test functions. To allow for code reuse, CommonFunctions holds functions that are useful in test cases, and it should be extended where possible. In web testing, most cases will involve interacting with the page. Selenium provides many actions for its WebDriver, a full list can be found [https://selenium-python.readthedocs.io/](https://selenium-python.readthedocs.io/) , but most actions will need to be performed on a specific element on a page. The Pages module contains classes which relate to pages on the website, the classes themselves have ways to find inividual elements on the pages and functions that are specific to the page.

Websites change often, so it is important to confirm the locators inside Pages are kept up to date. When used together, the functions in CommonFunctions, the elements and functions inside Pages, and the built-in functions of the Selenium WebDriver can be used to do nearly anything a human can do. It can be challenging to figure out at first. A good tip when writing tests is to use a debugger and try entering your commands inside the console, seeing for yourself what happens at each step before you finalize writing your test.

Tests should have a definitive ending, they either pass or fail. An assert statement provides this boolean choice to us, and every test in this framework should use them to determine their ultimate status. CommonChecks inside Validator holds functions that return True or False, which pair well with asserts. Send your arguments to a function in CommonChecks and assert that it will return your desired outcome; that will serve as the conclusion of a test.

**Modules:**

**Pages**

Each webpage of the site used in testing has its own class, containing attributes and functions. Page attributes are tuples, containing a selection method and a selector. When one of these is sent to the WebDriver’s find_elements function, it tells the driver both what method to use to find the object on the page and what values to use inside the method. Please keep this format for adding additional attributes. Pages also have functions. In general, please place a function here if it should only be used with this class of page, if it is generally applicable to many types of pages it is better suited for the common functions module.

BasicPage is a parent class of other pages; it contains things that should be attached to all pages on the site, such as the search bar or the footer.

MainPage is the front page of the site, it has item listings along with shortcuts to other parts of the site.

SearchPage is the search results page, exact contents will vary based on what was searched for.

ItemPage is the page for details about a particular item, including how to add it to the cart. Be aware that this page has pop-up dialogs, if you need to interact with them your test will need to know if a pop-up is displayed at a given time.

CartPage is the page for the user’s shopping cart. The state of it can vary greatly depending on what is in it, think about how many items may or may not be present when the test is run.

Locating the correct element is one of the greatest challenges of automated web testing. Websites are subject to constant change, and it is common for formerly reliable locators to fail. There are a few guidelines that can help. IDs are generally the most stable, but it is quite common for many elements to lack unique IDs. Without IDs, CSS Selectors are generally preferred, and the inspector in most browsers can help you find them. Beware of overly long CSS selectors, shorter ones that also work are generally more robust to small changes. Using class along with a basic CSS Selector can be very powerful and surprisingly resilient.

**CommonChecks**

These functions are used to check asserts inside tests. All of these functions should return Boolean values.

isinlist checks the text of a series of elements to see if a particular string is among them

comparetext will check if two items are the same

**TestData**

This prepares the data for test runs, along with some basic cleaning and error checking. At the moment it relies on reading the data from a csv file. Other methods for loading test data should be placed here.

For now, the CSV files are formatted like this:

Product Name: Name of item as it appears on website

Price: Price of item on website

Image Path: Unused for now

ID: ID of product in URLs on website

If the file is set up incorrectly, it will print a message instead of loading

The field names must be on the first line of the file

pricechecker will clean up prices into floating points

**CommonFunctions**

This holds functions that are not true/false checks that are frequently used in testing.

Sequences is a parent class for working with WebDriver sequences, which hold several WebDriver actions together so they can be executed in sequence. It is used for MenuText.searchfor, which sends text to one element, then clicks a second element. find will be extremely common; it’s a basic function for using the WebDriver to find an element. It takes in the driver and tuples, in the same format provided in Pages. Here’s an example: find(wdriver, ItemPage.productnames)

**Further Documentation is available in _build/singlehtml/index.html**
