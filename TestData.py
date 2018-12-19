import csv
import re


class LoadCSV:
    """Methods for loading test data from a CSV\n

       pricechecker:Converts prices in data to floating point\n
       loadfile: Loads CSV of test data into a dictionary that it returns\n
    """

    def pricechecker(inputprice):
        """Attempts to convert price to floating point\n

        Keyword arguments:\n
            inputprice:The price to convert to float\n
            This will try to remove whitespace with regex and remove dollar signs\n
            This was made in case of sloppy test data\n
            It will return a string if it can't get a float\n
        """

        cleanedprice = re.sub(r'\s', '', str(inputprice))  # Regex to remove whitespace
        cleanedprice = cleanedprice.replace('$', '')
        try:
            float(cleanedprice)
            return cleanedprice
        except ValueError:
            return "N/A"

    def loadfile(file):
        """This loads a CSV file of test data, and returns it as a dictionary\n
        Keyword arguments:\n
            file: address of CSV file to load\n
            
            The CSV file is read as a dictionary by the dictionary reader\n
            It looks for four columns, as follows:\n
            Product Name: Name of item as it appears on website\n
            Price; Price of item on website\n
            Image Path; Unused for now\n
            ID; ID of product in URLs on website\n
            If the file is set up incorrectly, it will print a message instead\n
            """
        with open(file, newline='') as csvfile:
            products = {}
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    print(row['Product Name'],
                          row['Price'],
                          row['Image Path'],
                          row['ID'])
                except KeyError:
                    print("Error, file not formatted correctly")
                products[row['ID']] = {"Image": row['Image Path'],
                                       "Name": row['Product Name'],
                                       "Price": LoadCSV.pricechecker(row['Price'])}
            return products
