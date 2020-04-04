from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
	def __init__(self,gebruikersnaam,wachtwoord):
		self.gebruikersnaam = gebruikersnaam
		self.wachtwoord = wachtwoord
		self.bot = webdriver.Firefox(executable_path = 'D:/instagrambot/geckodriver.exe')	

	def login(self):
		bot = self.bot
		bot.get('https://www.instagram.com/accounts/login/?hl=nl')		
		time.sleep(3)
		gebruikersnaam = bot.find_element_by_name('username').send_keys(self.gebruikersnaam)
		wachtwoord = bot.find_element_by_name('password').send_keys(self.wachtwoord + Keys.RETURN)
 		time.sleep(3)

	def zoekHashtag(self,hashtag):
		bot = self.bot

		bot.get('https://www.instagram.com/explore/tags/' + hashtag)

	def likeFotos(self,hoeveel):
		bot = self.bot
		bot.find_element_by_class_name('v1Nh3').click()
		i = 1
		while i <= hoeveel:
			time.sleep(2)
			bot.find_element_by_class_name('fr66n').click()
			bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
			time.sleep(2)

			i += 1
	
		


insta = InstagramBot('GEBRUIKERSNAAM-HOLDER','WACHTWOORD-HOLDER')
insta.login()
insta.zoekHashtag('howest')
insta.likeFotos(5)
