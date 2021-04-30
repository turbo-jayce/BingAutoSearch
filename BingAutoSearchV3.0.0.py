#Bing Rewards Auto Search Bot By Jason Mei
#Version 3.0.0
#Changelogs: Condensed and cleaned up code, supports a list of accounts as an array[infinite] 
#Changelogs V3.0: Added dictionary text file, allows you to search with a txt file of words, optimized+faster, corrected search amounts(34pc/20mobile)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#import 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
import time
import math



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Loop through all accounts doing edge and mobile searches
def mainLoop():
    #V A R I A B L E S  Y O U  N E E D  T O C H A N G E ~~~~~~~~~~~~~~~~! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !


    
    #I N S T R U C T I O N S = = = = = = = = = = Enter in all accounts in the following format, user:pass, into the 'accounts' string array!!!!= = = = = = = = = = = = = = = = = = = = = 
    accounts = ["username:password","example:example","email:pass"]

    #numSearch is number of PC searches
    numSearch = 34

    #numSearch1 is number of mobile searches
    numSearch1 = 20
    
    
    

    

    #DO NOT CHANGE ANYTHING BELOW THIS LINE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    delay = int(input("How many seconds do you want to add as delay between searches?(Recommended amount is 5-10 seconds, but I use 3): "))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #Print system messages; num of accounts and approximate time to do all searches
    numAccounts = len(accounts)
    print("BingAutoSearch V2.0.0 will automatically run both computer and mobile searches on", end=" ")
    print(numAccounts, end=" ")
    print("accounts!")
    print("This process will take approimately", end=" ")
    time = (numAccounts*((numSearch+numSearch1*delay))+ 46)/60
    print(time,end=" ")
    print("minutes!")



    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~          
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
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #Edge Searches(34 searches total)



        #Opens Edge Driver 
        PATH = "C:/Users/Capta/Documents/edgedriver_win64/msedgedriver.exe"
        driver = webdriver.Edge(PATH)
        driver.implicitly_wait(3)
        driver.get("https://bing.com/")



        #Sign out of existing account
        def signOut():
            time.sleep(5)
            signOut = driver.find_element_by_id("id_l")
            signOut.click()
            print("Signing out of account. . .")
            time.sleep(3)
            out = driver.find_element_by_id("b_idProviders")
            out.click()
            print("Account signed out of!")
       # signOut()



        #sign into new account
        def sign():
            time.sleep(4)
            signIn = driver.find_element_by_id("id_s")
            signIn.click()
            time.sleep(3)
            cred = driver.find_element_by_id("i0116")
            #Enters username
            print("Entering username ["+ user + "]")
            cred.send_keys(user)
            cred.send_keys(Keys.RETURN)
            time.sleep(3)
            passTo = driver.find_element_by_id("i0118")
            #Enters password
            print("Entering password [" + pw + "]")
            print("Logging into account")
            passTo.send_keys(pw)
            passTo.send_keys(Keys.RETURN)
            time.sleep(3)
       # sign()
        print("Account [" + user + "] logged in successfully! Auto search initiated.")


        
        #First test search
        time.sleep(3)
        first = driver.find_element_by_id("sb_form_q")
        first.send_keys("test")
        first.send_keys(Keys.RETURN)



        #Starts Edge Search Loop 
        def search():
            #I N P U T = = = = = N E E D E D = = = = =  =Input number of searches wanted in 'numSearch' or uncomment #numSearch to input while the code is running
            #numSearch = int(input("Please enter number of searches: "))
            numSearch = 34


       

            #Main search loop
            for x in range(1,numSearch+1):
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
                ping = driver.find_element_by_id("sb_form_q")
                ping.clear()

                #Send random keyword
                ping.send_keys(value)

                #add delay to prevent ban
                time.sleep(1)
                go = driver.find_element_by_id("sb_form_go")
                go.click()

                #add delay to prevent ban
                time.sleep(delay)

                #Print progress after each search
                print ("Doing ", end="" )
                print (x, end="")
                print(" search out of ", end="")
                print(numSearch)
                percentDone = x/numSearch*100
                print ("This is ", end="")
                print( percentDone, end="")
                print("% done.")
            print("Account [" + user + "] has completed PC searches. Please close the window or complete the daily taskes!")
        search()
        #Mobile Searches (20 searches total)

        #Opens Mobile Driver
        mobile_emulation = { "deviceName": "Nexus 5" }
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        PATH = "C:/Users/Capta/Documents/chromedriver_win32/chromedriver.exe"
        driver = webdriver.Chrome(executable_path = PATH, chrome_options = chrome_options)
        driver.implicitly_wait(3)
        driver.get("https://bing.com")




        #Sign into new account
        def sign():
            time.sleep(4)
            panel = driver.find_element_by_id("mHamburger")
            panel.click()
            signIn = driver.find_element_by_id("hb_s")   
            signIn.click()
            time.sleep(3)
            cred = driver.find_element_by_id("i0116")
            #Enters username
            print("Entering username ["+ user + "]")
            cred.send_keys(user)
            cred.send_keys(Keys.RETURN)
            time.sleep(3)
            passTo = driver.find_element_by_id("i0118")
            #Enters password
            print("Entering password [" + pw + "]")
            print("Logging into account")
            passTo.send_keys(pw)
            passTo.send_keys(Keys.RETURN)
            time.sleep(3)
        sign()
        print("Account [" + user + "] logged in successfully! Auto search initiated.")



        #First test search
        time.sleep(3)
        first = driver.find_element_by_id("sb_form_q")
        first.send_keys("test")
        first.send_keys(Keys.RETURN)



        #Starts Mobile Search Loop
        def mobile():
            #I N P U T = = = = = N E E D E D = = = = = = =Input number of searches wanted in 'numSearch' or uncomment #numSearch to input while the code is running
            #numSearch = int(input("Please enter number of searches: "))
            


            #Main search loop
            for x in range(1,numSearch1+ 1):
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
                ping = driver.find_element_by_id("sb_form_q")
                ping.clear()

                #Send random keyword
                ping.send_keys(value)

                #add delay to prevent ban
                time.sleep(1)
                go = driver.find_element_by_id("sb_form_go")
                go.click()

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
      

    
#Activate main loop
mainLoop()
print("BingAutoSearch V 3.0.0 has successfully boosted points on all accounts!")
	
