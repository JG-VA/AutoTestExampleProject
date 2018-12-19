from selenium.webdriver.common.action_chains import ActionChains


class Sequences:
    """Superclass to create a chain of actions for the driver"""
    def __init__(self, driver):
        self.actions = ActionChains(driver)


class MenuText(Sequences):
    """Function for sending text to an element and click\n


    Keyword arguments:
        textfield: element to send the text too\n
        button: element to click after entering text\n
        inputtext: text to be sent to textfield\n

    Initially made for the search bar, could be used for other sequences\n
    """
    def searchfor(self, textfield, button, inputtext):
        self.actions.send_keys_to_element(textfield, inputtext)
        self.actions.click(button)
        self.actions.perform()


def find(driver, element):
    """Function for finding an element, usually linked to Pages\n

    Keyword arguments:\n
        driver: pass the webdriver in so it can use it\n
        element: A tuple, the part contains the location method (eg By.ID), second contains\n
        what to be used with it (eg "product-name")\n

        The element portion was designed to work with the format of the attributes\n
        found in the Pages.py project file\n

        This should handle both single and lists of elements being found\n
        Expect either to come out when writing tests\n
        """
    element = driver.find_elements(element[0], element[1])
    if len(element) == 1:
        return element[0]
    else:
        return element
