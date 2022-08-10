#Bing Rewards Auto Search Bot By Jason Mei
#Version 4.0.0
#Changelogs: Condensed and cleaned up code, supports a list of accounts as an array[infinite] 
#Changelogs V3.0: Added dictionary text file, allows you to search with a txt file of words, optimized+faster, corrected search amounts(34pc/20mobile)
#Changelogs V4.0: Fixed bugs, added .env for easier acc added, and num searches, optimized to be faster, corrected search errors

#import 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
import time
import math
import datetime
from time import sleep
from dotenv import load_dotenv


#Fill in accounts in this array, format email:pass, Ex. accounts = "email:pass,email2:pass2,email3:pass3"
#account array
accounts = [""]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# load env var from .env
load_dotenv()
# Get settings from .env
numSearch = os.environ.get("NUMBER_OF_SEARCHES")
numSearch1 = os.environ.get("NUMBER_OF_MOBILE_SEARCHES")
delay = os.environ.get("TIME_BETWEEN_SEARCHES")
numSearch = int(numSearch)
numSearch1 = int(numSearch1)
delay = int(delay)

#Loop through all accounts doing edge and mobile searches
def mainLoop():
    #Print system messages; num of accounts and approximate time to do all searches
    numAccounts = len(accounts)
    print("BingAutoSearch V4.0.0 will automatically run both computer and mobile searches on", end=" ")
    print(numAccounts, end=" ")
    print("accounts!")
    #Loop through the array of accounts, splitting each string into an username and a password, then doing edge and mobile searches
    for x in accounts:
        import time
        #Grab username
        colonIndex = x.index(":")+1
        user = x[0:colonIndex-1]
        print("Username [" + user + "] has been obtained")
        #Grab password
        lastIndex = len(x)
        pw = x[colonIndex:lastIndex]
        print("Password [" + pw + "] has been obtained")
        #Edge Searches(34 searches total)
        #Opens Edge Driver 
        PATH = "C:/Users/Capta/Documents/edgedriver_win64/msedgedriver.exe"
        driver = webdriver.Edge(PATH)
        driver.implicitly_wait(3)
        driver.get("https://bing.com/")
        #Sign out of existing account
        def signOut():
            driver.implicitly_wait(1)
            time.sleep(3)
            signOut = driver.find_element(by=By.ID, value = "id_l")
            signOut.click()
            print("Signing out of account. . .")
            time.sleep(2)
            out = driver.find_element(by=By.ID, value = "b_idProviders")
            out.click()
            print("Account signed out of!")
        signOut()
        #sign into new account
        def sign():
            time.sleep(2)
            signIn = driver.find_element(by = By.ID, value = "id_s")
            signIn.click()
            time.sleep(2)
            cred = driver.find_element(by= By.ID, value = "i0116")
            #Enters username
            print("Entering username ["+ user + "]")
            cred.send_keys(user)
            cred.send_keys(Keys.RETURN)
            time.sleep(1)
            passTo = driver.find_element(by = By.ID, value = "i0118")
            #Enters password
            print("Entering password [" + pw + "]")
            print("Logging into account")
            passTo.send_keys(pw)
            passTo.send_keys(Keys.RETURN)
            time.sleep(1)
            #stay signed in, click no
            stay_signed_in =driver.find_element(by = By.ID, value = "idBtn_Back")
            stay_signed_in.click()
            print("Account [" + user + "] logged in successfully! Auto search initiated.")
        sign()
        #First test search
        time.sleep(delay)
        first = driver.find_element(by= By.ID, value = "sb_form_q")
        first.send_keys("test")
        first.send_keys(Keys.RETURN)
        time.sleep(delay)
        #Starts Edge Search Loop 
        def search():
            #Main search loop
            for x in range(1,numSearch):
                #Open txt file
                fo = open("words.txt", "r")
                words = fo.readlines()
                #retrieve random word
                numWords = len(words)
                randomVal = random.randint(1,numWords)
                #keyword 1 
                keyword1 = words[randomVal-1]
                #keyword 2
                keyword2 = 'define '
                #Create string to send       
                value =  keyword2 + keyword1
                #Clear search bar
                ping = driver.find_element(by=By.ID, value = "sb_form_q")
                ping.clear()
                #Send random keyword
                ping.send_keys(value)
                time.sleep(delay)
                #Print progress after each search
                print ("Doing ", end="" )
                print (x+1, end="")
                print(" search out of ", end="")
                print(numSearch)
                percentDone = x/numSearch*100
                print ("This is ", end="")
                print( percentDone, end="")
                print("% done.")
            print("Account [" + user + "] has completed PC searches. Please close the window or complete the daily taskes!")
        search()
        #close tab
        driver.close()
        #Mobile Searches
        #Opens Mobile Driver
        mobile_emulation = { "deviceName": "Nexus 5" }
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        PATH = "C:/Users/Capta/Documents/chromedriver_win32/chromedriver.exe"
        driver = webdriver.Chrome(executable_path = PATH, chrome_options = chrome_options)
        driver.implicitly_wait(2)
        driver.get("https://bing.com/")
        time.sleep(1)
        driver.refresh()
        #Sign into new account
        def sign():
            time.sleep(1)
            panel = driver.find_element(by = By.ID, value = "mHamburger")
            panel.click()
            signIn = driver.find_element(by = By.ID, value = "hb_s")   
            signIn.click()
            time.sleep(1)
            cred = driver.find_element(by=By.ID, value="i0116")
            #Enters username
            print("Entering username ["+ user + "]")
            cred.send_keys(user)
            cred.send_keys(Keys.RETURN)
            time.sleep(1)
            passTo = driver.find_element(by=By.ID, value = "i0118")
            #Enters password
            print("Entering password [" + pw + "]")
            print("Logging into account")
            passTo.send_keys(pw)
            passTo.send_keys(Keys.RETURN)
            time.sleep(1)
        sign()
        print("Account [" + user + "] logged in successfully! Auto search initiated.")
        #First test search
        time.sleep(1)
        first = driver.find_element(by=By.ID, value = "sb_form_q")
        first.send_keys("test")
        first.send_keys(Keys.RETURN)
        #Starts Mobile Search Loop
        def mobile():
            #Main search loop
            for x in range(1,numSearch1):
                #Open txt file
                fo = open("words.txt", "r")
                words = fo.readlines()
             #retrieve random word
                numWords = len(words)
                randomVal = random.randint(1,numWords)  
                #keyword 1 
                keyword1 = words[randomVal-1]
                #keyword 2
                keyword2 = 'define '
                #Create string to send       
                value =  keyword2 + keyword1
                #Clear search bar
                ping = driver.find_element(by=By.ID, value ="sb_form_q")
                ping.clear()
                #Send random keyword
                ping.send_keys(value)
                #add delay to prevent ban
                time.sleep(delay)
                #Print progress after each search
                print ("Doing ", end="" )
                print (x, end="")
                print(" search out of ", end="")
                print(numSearch1)
                percentDone = x/numSearch1*100
                print ("This is ", end="")
                print( percentDone, end="")
                print("% done.")
            print ("Account [" + user + "] has completed mobile searches]")
        mobile()
        #close when done
        driver.close()
#Activate main loop
mainLoop()
print("BingAutoSearch V 4.0.0 has successfully boosted points on all accounts!")
	
