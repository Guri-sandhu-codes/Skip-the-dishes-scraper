# Skip-the-dishes-scraper

**Install necessary libraries**:
- pip3 install -U selenium
- pip3 install pandas
_____________

**Process to run the program**

Retrieve the GitHub repository, and execute the `main.py` script. 

Within the `main.py` script, you have the option to input your address on line 26. Once you've made this adjustment, run the script. This will initiate the automation process, allowing you to extract data from the website.

I have used `geckodriver.exe` which is saved in the same folder and the path is passed in `driver = webdriver.Firefox(executable_path="geckodriver.exe")`
_____________________
What is `geckodriver.exe`?

`geckodriver.exe` is a component of the Mozilla Gecko rendering engine, primarily used for automating web browser actions. It is commonly associated with the Firefox web browser and facilitates interactions between your code (written in a programming language like Python, Java, etc.) and the browser.

When you're using tools like Selenium for web automation, you often need a WebDriver specific to the browser you're automating. `geckodriver` serves as the WebDriver for Firefox. It enables your code to open a Firefox browser window, manipulate web pages, and perform actions such as clicking buttons, filling out forms, and scraping data from websites.

If you're running automation scripts that involve Firefox browser actions, you typically need to download the appropriate version of `geckodriver.exe` compatible with your system and your version of the Firefox browser. This executable acts as a bridge between your automation code and the browser itself, allowing you to control and interact with the browser programmatically.

____________________________
Once the scraping procedure wraps up, you'll end up with two Excel files as outcomes. 

The initial one, named `links-for-nearby-restaurants.csv` will encompass a collection of URLs pointing to various restaurants. 

The second file, labeled `Final_data.csv` will contain comprehensive details about individual restaurants, including their names, addresses, and other pertinent information.

To put it simply, after the scraping is done, you'll get one Excel file containing restaurant web links and another Excel file with comprehensive restaurant information like names and addresses.
__________________________
In this repository, you'll notice two pre-existing Excel files that already hold the essential data. 

This data is specifically centered around restaurants located in proximity to the address `17 Dunsmore Lane, Barrie`.

As we previously talked about, you have the flexibility to modify this address according to your needs. Once you make this adjustment and execute the script, you'll obtain the specific information you're seeking.




