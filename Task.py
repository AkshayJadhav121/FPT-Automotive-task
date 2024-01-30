from selenium import webdriver
from selenium.webdriver.common.by import By


# Below function is for Skip Advertiesment
def adv(xpath, browser):
    try:
        ele = browser.find_element(By.XPATH, value=xpath)
    except:
        print("Could not find element {}".format(xpath))
        exit()
    ele.click()

# Below function is for Skip Advertiesment and send login details
def sendtext(xpath, browser, cred):
    try:
        ele = browser.find_element(By.XPATH, value=xpath)
    except:
        print("Could not find element {}".format(xpath))
        exit()
    ele.send_keys(cred)

browser = webdriver.Chrome()
url = "http://practice.automationtesting.in/"
browser.get(url) #1. Open the browser 2. Enter the URL http://practice.automationtesting.in/

adv(r'//*[@id="menu-item-50"]/a', browser) #3. Click on My Account Menu
sendtext('//*[@id="username"]', browser, "1test@test.com") #4. Enter registered username in username textbox
sendtext('//*[@id="password"]', browser, "1test@test.com") #5. Enter password in password textbox

adv('//*[@id="customer_login"]/div[1]/form/p[3]/input[3]', browser) #6. Click on login button

browser.find_element(by=By.LINK_TEXT,value="Sign out")#7. User must successfully login to the web page

adv(r'//*[@id="menu-item-50"]/a', browser) #8. Click on Myaccount link
adv(r'//*[@id="page-36"]/div/div[1]/nav/ul/li[2]/a', browser) #9. Click on Orders link

browser.find_element(by=By.XPATH,value=r'//*[@id="page-36"]/div/div[1]/div/div/a') #10. User must view their orders on clicking orders link
browser.quit()
