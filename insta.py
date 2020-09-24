from user import username, password, listname, useracc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
from random import randint

class insta:
    def __init__(self, username, password, listname, useracc):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages' :'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password
        self.listname = listname
        self.useracc = useracc
        

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        time.sleep(1)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollowers(self):
        time.sleep(2)
        self.browser.get(f"https://www.instagram.com/{self.useracc}")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"first count: {followerCount}")

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followerCount != newCount:
                followerCount = newCount
                print(f"first count: {followerCount}")
                print(f"second count: {newCount}")
                time.sleep(1)
            else:
                break

        
        followers = dialog.find_elements_by_css_selector("li")
        fList = []

        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            result = re.search('https://www.instagram.com/(.*)/', link)
            fList.append(result.group(1))

        with open(self.listname, "w", encoding="UTF-8")  as file:
            file.write("\n".join(fList))

    def followUser(self, listname):
        testsite_array = []
        with open(listname) as my_file:
            for line in my_file:
                testsite_array.append(line)

        while True:
            for x in range(len(testsite_array)): 
                if x < len(testsite_array):
                    self.browser.get("http://www.instagram.com/" + testsite_array[x])
                    time.sleep(randint(1,4))

                    followButton = self.browser.find_element_by_xpath("/html/body/div[@id='react-root']/section/main/div/header/section/div[1]/div[1]/span/span[1]/button")

                    print(followButton.text)
                    if followButton.text != "Message":
                        followButton.click()
                        time.sleep(randint(1,4))
                    else:
                        print("You are following this account")
                    time.sleep(randint(2,10))
                else:
                    break
                


    def unFollowUser(self, uusername):
        self.browser.get("http://www.instagram.com/" + uusername)
        time.sleep(2)

        followButton1 = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/button")
        followButton = self.browser.find_element_by_tag_name("button")
        print(followButton.text)
        print(followButton1.text)
        if followButton.text == "Message":
            followButton1.click()
            time.sleep(2)
            self.browser.find_element_by_xpath('//button[text()="Unfollow"]').click()
        else:
            print("You aren't following this account")

#instag = insta(username, password)
#instag.signIn()
#instag.getFollowers()
#instag.followUser("finic_nl")
#instag.unFollowUser("finic_nl")

"""
list = ["finic_nl", ""]

for user in list:
    instag.followUser(user)
    time.sleep(3)
"""
