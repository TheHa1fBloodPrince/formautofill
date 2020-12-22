#Created by: TheHalfBloodPrince
from selenium import webdriver 
import pyautogui 
from datetime import datetime 
from threading import Timer  

print ('Executing Order 66...')

option = webdriver.ChromeOptions() 

browser = webdriver .Chrome('/usr/bin/chromedriver') 
browser.get ("Insert form link") 

#Function that makes script run at the right time - example, this is set to run tommorow @8:55 am
x=datetime.today()
y=x.replace(day=x.day+1, hour=8, minute=55, second=0, microsecond=0) 
delta_t=y-x

secs=delta_t.seconds+1

def auto_sign_in(): 
    #import datetime again so it fills out the correct day in the form and not the day the scirpt was run, see last question
    from datetime import datetime
    current_time = datetime.now() 
     
    #This section is if you need to sign in to your organizations emaill account to get access like I do, so you may be able to comment this whole section out... 
    #school email sign in
    pyautogui.write('email address') 
    pyautogui.press('enter', interval=4.00) 

    #login 
    pyautogui.press('tab', interval=0.25) 
    pyautogui.write('username') 

    pyautogui.press('tab', interval=0.25) 
    pyautogui.write('password') 

    pyautogui.press('tab', interval=0.25) 
    pyautogui.press('enter', interval=4.00) 

    #confirm this account belongs to you: 
    pyautogui.press('tab', interval=0.25) 
    pyautogui.press('enter', interval=4.00) 


    #Questions 

    #full name? 
    pyautogui.press('tab', interval=0.25) 
    pyautogui.press('tab', interval=0.25) 
    pyautogui.write('name', interval=0.25) 

    #Are you here? (Radio button) 
    pyautogui.press('tab', interval=0.25) 
    pyautogui.press('space', interval=0.25) 

    #you understand the work? (Radio button) 
    pyautogui.press('tab', interval=0.25) 
    pyautogui.press('space', interval=0.25) 

    #input date
    #DD
    pyautogui.press('tab', interval=0.25) 
    pyautogui.write(current_time.strftime('%d')) 
    #MM 
    pyautogui.write(current_time.strftime('%m')) 
    #yyyy
    pyautogui.write(current_time.strftime('20%y')) 

    #submit 
    pyautogui.press('tab') 
    pyautogui.press('enter') 

t = Timer(secs, auto_sign_in) 
t.start() 

print ('Finished')


