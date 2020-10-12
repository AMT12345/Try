# Before you Begin (https://selenium-python.readthedocs.io/installation.html)
# 1) pip install selenium, pip install PyAutoGUI
# 2) go to https://sites.google.com/a/chromium.org/chromedriver/downloads to get driver(rememer location fro driver)

# First Collect All our Libraries
#------------------------------------------------------------------------------------------------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities # Change load method
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
from PIL import Image
from threading import Thread

def Function_UploadOBJ(String1,String2,String3, String4, String5, String6 ):
    # Connect the LabVIEW and Python Variables
    #------------------------------------------------------------------------------------------------------
    OBJ1Location = String1 #'C:/Users/rieml/Desktop/Past GitHub/Case 1/Heart.obj'
    OBJ2Location = String2 #'C:/Users/rieml/Desktop/Past GitHub/Case 1/Veins.obj'

    GitHubUserName = String3 #'AMT12345'
    GitHubPassword = String4 #'Amt55155515'
    GitHubProjectName = String5 #'Try'
    DriverPath = String6
    # Preset Python Vairables
    #------------------------------------------------------------------------------------------------------
    NameofOBJ1 = 'Heart.obj'
    NameofOBJ2 = 'Veins.obj'

    # Define The Main URLs
    #------------------------------------------------------------------------------------------------------
    GitHubLoginURL = 'https://github.com/session'
    GitHubProjectURL = 'https://github.com/' + GitHubUserName + '/' + GitHubProjectName #'https://github.com/AMT12345/Try'
    GitHubUploadURL = 'https://github.com/' + GitHubUserName + '/' + GitHubProjectName + '/upload/master' #'https://github.com/AMT12345/Try/upload/master'

    # Change Chrome Settings
    caps = DesiredCapabilities().CHROME
    #caps["pageLoadStrategy"] = "normal"  #  complete
    caps["pageLoadStrategy"] = "eager"  #  interactive

    # Open The Account and login
    driver = webdriver.Chrome(desired_capabilities=caps,executable_path=DriverPath) #'C:/Users/rieml/Downloads/\chromedriver_win32/chromedriver.exe')
    driver.get(GitHubLoginURL)
    time.sleep(1)
    seq_query_field = driver.find_element_by_name("login")
    seq_query_field.send_keys(GitHubUserName)
    seq_query_field = driver.find_element_by_name("password")
    seq_query_field.send_keys(GitHubPassword)
    driver.find_element_by_name('commit').click()
    time.sleep(1)

    # Open to Main Project File
    driver.get(GitHubProjectURL)
    time.sleep(1)
    # Delete old Files if they are there and return
    # OBJ File 1
    try:
        input = '//*[@title="' + NameofOBJ1 + '"]'
        driver.find_element_by_xpath(input).click()
        time.sleep(1)
        input = '//*[@aria-label="Delete this file"]'
        driver.find_element_by_xpath(input).click()
        time.sleep(1)
        input = '//*[@id="submit-file"]'
        driver.find_element_by_xpath(input).click()
        time.sleep(1)
        driver.get(GitHubProjectURL)
        time.sleep(1)
    except:
        print("Didn't Delete File 1")
        driver.get(GitHubProjectURL)
        time.sleep(1)
    # OBJ File 2
    try:
        input = '//*[@title="' + NameofOBJ2 + '"]'
        driver.find_element_by_xpath(input).click()
        time.sleep(1)
        input = '//*[@aria-label="Delete this file"]'
        driver.find_element_by_xpath(input).click()
        time.sleep(1)
        input = '//*[@id="submit-file"]'
        driver.find_element_by_xpath(input).click()
        time.sleep(1)
        driver.get(GitHubProjectURL)
        time.sleep(1)
    except:
        print("Didn't Delete File 2")
        driver.get(GitHubProjectURL)
        time.sleep(1)

    # Upload New Files
    # Get File 1
    driver.get(GitHubUploadURL)
    time.sleep(1)
    field = driver.find_element_by_id("upload-manifest-files-input")
    driver.execute_script("arguments[0].style.display = 'block';", field)
    field = driver.find_element_by_id("upload-manifest-files-input")
    field.send_keys(OBJ1Location)
    time.sleep(1)
    # Make sure its finished uploading
    element = driver.find_element_by_xpath('//*[@class="bg-green js-upload-meter"]')
    while (element.get_attribute("style") != 'width: 100%;'):
        Style = element.get_attribute("style")
    # Get File 2
    time.sleep(1)
    field = driver.find_element_by_id("upload-manifest-files-input")
    driver.execute_script("arguments[0].style.display = 'block';", field)
    field = driver.find_element_by_id("upload-manifest-files-input")
    field.send_keys(OBJ2Location)
    time.sleep(1)
    # Make sure its finished uploading
    element = driver.find_element_by_xpath('//*[@class="bg-green js-upload-meter"]')
    while (element.get_attribute("style") != 'width: 100%;'):
        Style = element.get_attribute("style")
    # Upload changes
    time.sleep(1)
    input = '//*[@data-edit-text="Commit changes"]'
    driver.find_element_by_xpath(input).click()
    #Wait for it to Finish Upload
    while (driver.current_url != GitHubProjectURL):
        CurrentURL = driver.current_url
    time.sleep(1)

    # Check the Raw Data of the New Files
    # Change Chrome Settings
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"  
    driver = webdriver.Chrome(desired_capabilities=caps,executable_path=DriverPath)
    # Open File 1 for 3 seconds
    driver.get(GitHubProjectURL)
    time.sleep(1)
    driver.get('https://github.com/' + GitHubUserName + '/' + GitHubProjectName + '/blob/master/' + NameofOBJ1 + '?raw=true')
    time.sleep(3)
    # Open File 2 for 3 seconds
    driver.get(GitHubProjectURL)
    time.sleep(1)
    driver.get('https://github.com/' + GitHubUserName + '/' + GitHubProjectName + '/blob/master/' + NameofOBJ2 + '?raw=true')
    time.sleep(3)
    
    return ("Done")

