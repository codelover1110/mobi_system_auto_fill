from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta
import json
import time

browser = webdriver.Firefox()
browser.get('https://app.ace.aaa.com/b2b/home/mortgagee-request/requesttype')
browser.set_window_size(1366,1000)

data = None

def page_1(data):
    # Select Type of request
    select = browser.find_elements(By.TAG_NAME, "input")
    for one in data["select"]:
        select[one-1].click()

    # pause for 2 seconds
    time.sleep(2)

    # next!
    select = browser.find_element(By.CLASS_NAME, "buttonText")
    select.click()
    
def page_2(data):

    # select policyNumber and set value
    select = browser.find_element(By.ID, "policyNumber")
    select.send_keys(data["policyNumber"])

    # select firstNameFirstInsured and set value
    select = browser.find_element(By.ID, "firstNameFirstInsured")
    select.send_keys(data["firstNameFirstInsured"])

    # select lastNameFirstInsured and set value
    select = browser.find_element(By.ID, "lastNameFirstInsured")
    select.send_keys(data["lastNameFirstInsured"])

    # select firstNameSecondInsured and set value
    select = browser.find_element(By.ID, "firstNameSecondInsured")
    select.send_keys(data["firstNameSecondInsured"])

    # select lastNameSecondInsured and set value
    select = browser.find_element(By.ID, "lastNameSecondInsured")
    select.send_keys(data["lastNameSecondInsured"])

    # select street and set value
    select = browser.find_element(By.ID, "street")
    select.send_keys(data["street"])

    # select unitNumber
    select = browser.find_element(By.ID, "unitNumber")
    
    # remove space, _, - note: Only English letters and numbers can be entered.
    tmp = data["unitNumber"]
    str = tmp.replace(" ", "")
    str = str.replace("-", "")
    str = str.replace("_", "")
    select.send_keys(str)

    # select city and set value
    select = browser.find_element(By.ID, "city")
    select.send_keys(data["city"])
    
    # select state
    actions = ActionChains(browser)
    element = browser.find_element(By.ID, "MUISelect-state")
    # Scroll down the page
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Move the mouse to the element at the specified position (x, y)
    actions.move_to_element_with_offset(element, 10, 10)
    # Perform the click action
    actions.click()
    # Perform the actions
    actions.perform()

    try:
        # Select the desired item from list elements
        element = browser.find_elements(By.TAG_NAME, "li")
        for one in element:
            browser.execute_script("arguments[0].scrollIntoView();", one)
            if one.text == data["state"]:
                one.click()
    except Exception as e:
        print(e)
        pass
    
    # Select zip number and set vaule
    select = browser.find_element(By.ID, "zip")
    select.send_keys(data["zip"])

    # pause for 2 seconds
    time.sleep(2)
    # next!
    select = browser.find_element(By.TAG_NAME, "form")
    select.submit()


def page_3(data):
    # finds all the input elements on the web page and clicks on the element specified by the data['select'] value.
    select = browser.find_elements(By.TAG_NAME, "input")
    select[data['select']-1].click()
    
    # finds the element with the ID "clauseName" and inputs the value of data["clauseName"] into the element.
    select = browser.find_element(By.ID, "clauseName")
    select.send_keys(data["clauseName"])

    # This code snippet finds the element with the ID "successorLanguage" and inputs the value of data["successorLanguage"] into the element.
    select = browser.find_element(By.ID, "successorLanguage")
    select.send_keys(data["successorLanguage"])
    
    # This code snippet finds the element with the ID "mortgageeMailingAddress" and inputs the value of data["mortgageeMailingAddress"] into the element.
    select = browser.find_element(By.ID, "mortgageeMailingAddress")
    select.send_keys(data["mortgageeMailingAddress"])

    # This code snippet finds the element with the ID "mortgageeUnitNumber" and inputs the value of data["mortgageeUnitNumber"] into the element.
    select = browser.find_element(By.ID, "mortgageeUnitNumber")
    select.send_keys(data["mortgageeUnitNumber"])

    # This code snippet finds the element with the ID "mortgageeCity" and inputs the value of data["mortgageeCity"] into the element.
    select = browser.find_element(By.ID, "mortgageeCity")
    select.send_keys(data["mortgageeCity"])
    

    # same 2 page
    actions = ActionChains(browser)
    element = browser.find_element(By.ID, "MUISelect-mortgageeState")
    # Scroll down the page
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Move the mouse to the element at the specified position (x, y)
    actions.move_to_element_with_offset(element, 10, 10)
    # Perform the click action
    actions.click()
    # Perform the actions
    actions.perform()

    try:
        element = browser.find_elements(By.TAG_NAME, "li")
        for one in element:
            # print (one.text)
            if one.text == data["mortgageeState"]:
                print (one.text)
                browser.execute_script("arguments[0].scrollIntoView();", one)
                one.click()
    except Exception as e:
        pass

    # Select mortgageeZipCode element and set value
    select = browser.find_element(By.ID, "mortgageeZipCode")
    select.send_keys(data["mortgageeZipCode"])

    # Select mortgageeLoanNumber element and set value
    select = browser.find_element(By.ID, "mortgageeLoanNumber")
    select.send_keys(data["mortgageeLoanNumber"])

    # Select Escrowed element and Insert the next day of the week
    select = browser.find_elements(By.TAG_NAME, "input")
    if data["Escrowed"] == "yes" or data["Escrowed"] == "Yes":
        select[11].click()
    else:
        select[12].click()

    current_date = datetime.now()
    one_week_later = current_date + timedelta(weeks=1)
    formatted_date = one_week_later.strftime("%m/%d/%Y")

    select = browser.find_element(By.ID, "effectiveDate-maskedInput")
    select.clear()
    select.send_keys(formatted_date)

    # pause for 2 seconds and next
    time.sleep(10)
    select = browser.find_element(By.TAG_NAME, "form")
    select.submit()

def page_4(data):
    # finds all the input elements on the web page and clicks on the element specified by the data['select'] value.
    select = browser.find_elements(By.TAG_NAME, "input")
    select[data['select']-1].click()
    
    # Select requesterFullName element and set value
    select = browser.find_element(By.ID, "requesterFullName")
    select.send_keys(data["requesterFullName"])

    # Select companyName element and set value
    select = browser.find_element(By.ID, "companyName")
    str = data["companyName"].replace(" ", "")
    select.send_keys(str)

    # Select requesterEmail element and set value
    select = browser.find_element(By.ID, "requesterEmail")
    select.send_keys(data["requesterEmail"])

    # Select requesterPhoneNumber element and set value
    select = browser.find_element(By.ID, "requesterPhoneNumber")
    select.send_keys(data["requesterPhoneNumber"])
    
    # Select option element and select for preferred
    select = browser.find_elements(By.TAG_NAME, "input")
    if data["preferred"] == "Email" or data["preferred"] == "email":
        select[6].click()
    else:
        select[7].click()
    
    # Select option element and select for upload
    select = browser.find_elements(By.TAG_NAME, "input")
    if data["upload"] == "yes" or data["upload"] == "Yes":
        select[8].click()
    else:
        select[9].click()

    # pause for 2 seconds and next
    time.sleep(2)
    select = browser.find_element(By.TAG_NAME, "form")
    select.submit()

def input_data():
    global data
    # Open the JSON file
    with open('test.json') as f:
        # Load the JSON data
        data = json.load(f)


if __name__ == '__main__':
    # Input Json file
    input_data()

    # First page automation
    page_1(data["page1"])

    # Second page automatiion
    page_2(data["page2"])

    # third page automation
    page_3(data["page3"])

    # four page automation
    page_4(data["page4"])
    time.sleep(2)

    browser.quit()