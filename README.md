# Skip-the-Dishes Scraper

This repository contains a web scraping project designed to extract restaurant information from the Skip-the-Dishes website. The project uses Selenium for automating the data extraction process and outputs the information into Excel files.

## Installation

To run this project, you'll need to install the necessary dependencies. Use the following command to install the required libraries:

```bash
pip install -r requirements.txt
```

Ensure you have Python and pip installed on your system.

## How to Use

1. **Retrieve the GitHub Repository:**
   - Clone this repository to your local machine.

2. **Execute the `main.py` Script:**
   - Open the `main.py` script in a code editor.
   - On line 27, you'll find an option to input your address. Replace the default address with your desired address.
     ```python
     address_box.send_keys("23 bothwell crescent")
     ```
   - After making the necessary adjustments, save the file and run the script. This will start the automation process, extracting data from the Skip-the-Dishes website.

3. **Results:**
   - Once the scraping process completes, you will find two Excel files generated in the directory:
     1. **`links-for-nearby-restaurants.csv`**: Contains a list of URLs for the nearby restaurants.
     2. **`Final_data.csv`**: Contains detailed information about each restaurant, such as names, addresses, and other relevant details.
   - These files will provide you with a comprehensive overview of the restaurants around the specified address.

## Pre-existing Data

In the repository, you'll notice two Excel files already containing essential data. These files focus on restaurants located near the address:

- **23 Bothwell Crescent, Barrie**

Feel free to modify the address in the `main.py` script according to your needs. After doing so and running the script, you'll obtain specific information for the new location.

