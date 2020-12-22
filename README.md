Google Form Auto Complete 
This is for filling out google forms that need to be completed at a certain time each day, I created it to complete an attendance form every morning for online school. So this is built for filling out the same form every day or every few days at a certain time so you don't need to do it manually. I used this on Linux Ubuntu 20.04 LTS, but it should work in any debian based Linux os, It has not been tested in windows, but all the tools this script requires to run will work on windows. The code was made to be easily customizable for different google forms and different types of questions. Often when linking the html code from the form it will not allow the script to interact with the elements. I worked around this by useing keyboard presses instead, to move from question to question the script presses the 'tab' button, the 'space' button will bubble in/select the current radio button for filling out multiple choice questions, it has the option for inputing text for long and short answer questions etc. So as long as you know the questions on the form, you will be able to navigate and answer any questions with this code. I found the best way to figure out what key presses to do is to fill out the form manually with only keyboard presses and record what buttons you need to press to answer each question and then simply record it and put them into the script. I have included a screenshot of the google form my script was meant to fill out to help you figure out what key presses do what. There is also a part of the script that signs into an email account, becuase if this is for work or school you may be required to sign into the gmail account from your organization before you can gain access. Much of this code will need to be changed for you, but I have tried to make it as easy as possible to customize. 
Also note that this script will not work if the comuter locks, so if you are running this script from terminal the computer must be kept on and unlocked or the script will not execute, this can be fixed by changing your power settings. You can turn the monitor off to save power, so I recommend using this on a desktop computer instead of a laptop if possible. 	


Getting Started 
This script requires a few tools to run properly, the tools you need to download are: 

1. Google Chrome (other browsers will work, but Chrome works best, note to linux users, set up for chromium will also require a different driver, so I recommend only using Chrome) 
install: visit chromes official website and download the most recent version: https://www.google.com/intl/en_ca/chrome/ 

2. Chrome webdriver 
install: check your chrome version by clicking the 3 dots at the top right of the screen, from the drop down navigate to help then to about google chrome
Download the matching chrome driver from here: https://chromedriver.storage.googleapis.com/index.html 
for linux users, once the zip file has been downloaded run these commands for install: 

unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver

wget https://selenium-release.storage.googleapis.com/3.13/selenium-server-standalone-3.13.0.jar 

to test chrome driver run command:
chromedriver --url-base=/wd/hub
if the output is: 'Chromedriver was started successfully.' It is working and you can close that terminal now.

3. Selenium 
install: run command: 
pip3 install selenium 
if the command is not found install it by running command: 
sudo apt install python3-pip 
then run command "pip3 install selenium" again 

4. pyautogui 
install: run command: 
pip3 install pyautogui 


Customization 
This script uses keypresses to naviagte the page here are some of the keypresses and what they do to help you customize this script for your needs. 
to press any button write command: 
'tab' button will allow you to jump from question to question
'space' will fill bubble in the selected radio button 
'enter' will select submit button 
pyautogui.write('text') will allow you to input text in long or short answer questions 
for a full list of commands and how to use the keypress software visit: https://pyautogui.readthedocs.io/en/latest/keyboard.html 

Setting time: 
pretty straight forward, just note that inputting '0' in day slot will make it fill out the form the day the script is being run and inputting '1' will fill out the form the next day 


Deployment: 
To Run Script use command: 
python3 formAutoFill.py 
OR if you changed the file name run command: python3 *Title*.py 
*note you may need to install python3, if so run command: 
sudo apt install python3 


Author: 
TheHalfBloodPrince 
