import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Firefox(executable_path="geckodriver.exe")

driver.maximize_window()

#getting the website homepage
driver.get("https://www.skipthedishes.com/")

try:
    cookies = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/div[2]/div/div/div[3]/button[3]")
    cookies.click()
except:
    pass

#getting the address box element
address_box = driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div[2]/form/input")

#passing the address in address box - you can pass your address here
address_box.send_keys("17 Dunsmore Lane, Barrie, ON, Canada")

time.sleep(2)

#Sending Enter Key to enter the address
address_box.send_keys(Keys.ENTER)

time.sleep(2)

#clicking the search button below the address
search = driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div/div/div[2]/div[1]/div/div/div/div/div[4]/button")

search.click()
time.sleep(2)

''' The 4 lines of code below is to get to the end of page and load all the restaurants'''
htmlelement= driver.find_element(By.TAG_NAME,'html')
htmlelement.send_keys(Keys.END)
time.sleep(1)
htmlelement.send_keys(Keys.END)


time.sleep(20)

#finding all the hyperlinks and storing them in *links*
links = driver.find_elements(By.XPATH,"/html/body/div[2]/div/main/div/div/div/div/div/div/li/div/a")
print(links)
#getting href and storing it in a list variable *link_list*
link_list = [i.get_attribute("href") for i in links]
print(len(links))

#creating Pandas dataframe and storing all the hyperlinks
restaurant_data = pd.DataFrame(data=link_list,columns=["Address"])

#saving the dataframe as csv file that can later be used as reference for URL's of different restaurants
restaurant_data.to_csv("links-for-nearby-restaurants.csv",index=False)

#creating empty lists so that further data can be appended later to these empty lists

name_list = [] #this stores all the names of restaurants
address_list = [] #this stores all the addresses of restaurants
stars_list = [] #this stores the stars they got out of 10
del_charge_list = [] #this stores the delivery fees charged by restaurants
del_charge_desc_list = [] #this stores descriptioj of all the delivery charges
service_fees_list = [] #This stores service fees of restaurants
timing_list = [] #this stores the timings of restaurants

for index,url in enumerate(restaurant_data['Address']):
    print(index)

    driver.get(url) #going to each restatutants homepage to scrape their information
    time.sleep(4)

    #Getting name of the restaurant
    try:
        name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div/div/div/div[1]/div/div[2]/div/div/div/div[1]/h1")
        name = name_element.text
        name_list.append(name)
    except:
        driver.get(url + "%20")
        time.sleep(4)
        name_element = driver.find_element(By.XPATH,"/html/body/div[2]/div/main/div/div/div/div[1]/div/div[2]/div/div/div/div[1]/h1")
        name = name_element.text
        name_list.append(name)

    #Getting address of the restaurant
    address_element = driver.find_element(By.CSS_SELECTOR,"span.styles__DetailTextWrapper-sc-14uzcgo-1:nth-child(2) > p:nth-child(1)")
    address = address_element.text
    address_list.append(address)

    try:
        #Getting stars restaurant got out of 10
        stars_element = driver.find_element(By.CSS_SELECTOR,"p.MuiTypography-body1:nth-child(2)")
        stars = stars_element.text
        stars_list.append(stars)
    except:
        stars_list.append("NA")

    #Getting delivery charges of the restaurant
    del_charge_element = driver.find_element(By.CSS_SELECTOR,".styles__DeliveryFeeRowText-sc-14uzcgo-5 > span:nth-child(1)")
    del_charge = del_charge_element.text
    del_charge_list.append(del_charge)

    try:
        service_fees_apply = driver.find_element(By.CSS_SELECTOR,".styles__VariableServiceFeeButton-sc-14uzcgo-2")
        service_fees_apply.click()

        #Getting delivery charge description of the restaurant
        del_charge_desc_element = driver.find_element(By.CSS_SELECTOR,"p.MuiTypography-paragraph:nth-child(2)")
        del_charge_desc = del_charge_desc_element.text
        del_charge_desc_list.append(del_charge_desc)

        # Getting service fee of the restaurant
        service_fee_element = driver.find_element(By.CSS_SELECTOR,"p.MuiTypography-root:nth-child(4)")
        service_fees = service_fee_element.text
        service_fees_list.append(service_fees.split(". ")[0])

        timing_element = driver.find_element(By.CSS_SELECTOR, "p.MuiTypography-root:nth-child(6)")
        timing = timing_element.text
        timing_list.append(timing)

    except:
        service_fees_list.append("NA")

        more_info= driver.find_element(By.CSS_SELECTOR,".styles__StyledTooltip-sc-1etxvxm-17")
        more_info.click()

        del_charge_desc_element = driver.find_element(By.CSS_SELECTOR,"p.MuiTypography-paragraph:nth-child(2)")
        del_charge_desc = del_charge_desc_element.text
        del_charge_desc_list.append(del_charge_desc)

        timing_element = driver.find_element(By.CSS_SELECTOR,"p.MuiTypography-root:nth-child(4)")
        timing = timing_element.text
        timing_list.append(timing)


#setting column names for the dataframe
column_names = ["Name","Address","Stars (Out of 10)","Delivery Charges","Delivery Charges Description","Services Fee","Timing"]

scraped_data = pd.DataFrame(data=list(zip(name_list,address_list,stars_list,del_charge_list,del_charge_desc_list,service_fees_list,timing_list)),columns=column_names)
scraped_data.to_csv("Final_data.csv",index=False) #Finally saving the scraped data as csv file in excel


