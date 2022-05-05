#!/usr/bin/env python3

#Script to bomb blooket with fake players
#Only works for 60 players as host must have blooket+ to have 1000
#Make sure to have google chrome installed as well as the chromewebdriver included with the install on github,
#or download it here..."https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/"

#Created by marsacom, https://github.com/marsacom/

#Import packages
import time
import webbrowser
import colorama
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

colorama.init(autoreset=True)

print("Blooket-Bomb v1.0")

#Set info we will need to run
url = "https://dashboard.blooket.com/play"
code = input("Input your game code:  ")
name = input("Enter which name you would like to use:  ")
namen = str(name)
ntab = 0
otab = 0
numofbots = 1
count = 1

#If you would like to use the headless version of google to do this and not have the GUI show
#up, you can uncomment the 3 lines below and then comment out the 'driver=webdriver.Chrome()'

#options = Options()
#options.headless = True
#driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()

#Generate new name each time
def generatename():
	global name, namen, numofbots, count
	count = count + 1
	namen = (name + str(count))
	numofbots = numofbots + 1
	print("Bot # " + str(x))


#Join game with game code and generated name
def join():
	global code, namen, driver, ntab, otab
	if numofbots == 1:
		print(f"{Fore.CYAN}One window opening...")
	elif numofbots >= 2:
		print(f"{Fore.CYAN}New window opening...")
		driver.execute_script("window.open()")
		driver.switch_to.window(driver.window_handles[ntab])
	print("Going to blooket")
	driver.get(url)
	wait = WebDriverWait(driver, 5)
	#Find and input game code
	ele = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "styles__idInput___1zWUq-camelCase")))
	codeBox = driver.find_element_by_class_name("styles__idInput___1zWUq-camelCase")
	codeBox.send_keys(code)
	searchButton = driver.find_element_by_class_name("styles__joinButton___xSaJN-camelCase")
	searchButton.click()
	#Find and input name
	generatename()
	ele = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "styles__nameInput___20VdG-camelCase")))
	nameBox = driver.find_element_by_class_name("styles__nameInput___20VdG-camelCase")
	nameBox.send_keys(namen)
	joinButton = driver.find_element_by_class_name("styles__joinButton___2upCU-camelCase")
	joinButton.click()
	#Check to see if login was successful
	try:
		successful = driver.find_element_by_class_name("styles__headerTextCenter___4SlNZ-camelCase")
		print('Bot has joined game!')
	except:
		print(f"{Fore.RED}{Style.BRIGHT}ERROR{Style.BRIGHT}Unable to join game...")
	ntab = ntab + 1


#Loop to join game 60 times to flood game with random players
for x in range(60):
	join()
