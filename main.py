from selenium import webdriver
from time import sleep

#Class for your email address, for getting a like from your account
class you_tube: 
    def __init__(self, username, password):
        self.bot = webdriver.Chrome('driver/chromedriver.exe')
        self.username = username
        self.password = password

    def login(self):
        bot = self.bot
        print("\nStarting Login process!\n")
        bot.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
        bot.implicitly_wait(10)
        self.bot.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.bot.find_element_by_xpath('//input[@type="email"]').send_keys(self.username)
        self.bot.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.bot.find_element_by_xpath('//input[@type="password"]').send_keys(self.password)
        self.bot.find_element_by_xpath('//*[@id="passwordNext"]').click()
        print("\nLoggedin Successfully!\n")
        sleep(2)
        self.bot.get('')  #Paste Your Youtube Channel Link over here

#Loop will go till the time every video isn't liked. It would take some time.
    def start_liking(self):
        bot = self.bot
        scroll_pause = 2
        last_height = bot.execute_script("return document.documentElement.scrollHeight")
        while True:
            bot.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            sleep(scroll_pause)

            new_height = bot.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                print("\nScrolling Finished!\n")
                break
            last_height = new_height
            print("\nScrolling")

        all_vids = bot.find_elements_by_id('thumbnail')
        links = [elm.get_attribute('href') for elm in all_vids]
        links.pop()
        for i in range(len(links)):
            bot.get(links[i])

            like_btn = bot.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a')
            check_liked = bot.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]')
            # Check if its already liked
            if check_liked.get_attribute("class") == 'style-scope ytd-menu-renderer force-icon-button style-text':
                like_btn.click()
                print("Liked video! Long Live You!!!\n")
                sleep(0.5)
            elif check_liked.get_attribute("class") == 'style-scope ytd-menu-renderer force-icon-button style-default-active':
                print("Video already liked.\n")

print("Let's make it the most liked channel\n\n")
username = str(input("Enter your YouTube/Google Email ID: "))
password = str(input("Enter your password: "))
bot_army = you_tube(username,password)
bot_army.login()
bot_army.start_liking()
print("\n\nVolla Done!!!!!!\n\n\nPress any key to end")
input()