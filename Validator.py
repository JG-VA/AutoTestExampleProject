

class CommonChecks:
    """Holds common methods that return True or False\n

       comparetext: Compares two things\n
       isinlist: Checks if text is among the text elements found by the driver\n
    """
    def comparetext(texttocheck, intendedtext):
        """Compares what is in argument1 with argument2 \n
\n
           Keyword arguments: \n
               texttocheck: item 1 of comparison \n
               intendedtext: item 2 of comparison \n
           This is made to work with asserts in the main. No type conversions or cleaning,\n
           So make sure you do that before using this. Especially with elements\n
        """
        truthval = (texttocheck == intendedtext)
        return truthval

    def isinlist(elements, text):
        """Check if text occurs among a series of elements on the page\n
           Keyword arguments:\n
               elements: a list of elements (found by the webdriver) on the page to check the text of\n
               text: Text you are looking for\n

               If the element has no text a placeholder will be added to the list\n
               Returns true if present, false if not\n


        """
        textlist = []
        for item in elements:
            try:
                textlist.append(item.text)
            except AttributeError:
                print("TK TEXT NOT PRESENT")
        print(textlist)
        if text in textlist:
            return True
        else:
            return False
