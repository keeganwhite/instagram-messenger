from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
from dotenv import load_dotenv
import os


def main():
    print("Running main...")
    print("Starting chrome...")
    global chrome
    # starts a new chrome session
    chrome = webdriver.Chrome("./chromedriver")
    print("Running main...")
    login()
    message = load_text()
    send_message(message)
    chrome.close()


def login():
    # Read in Login Credentials
    load_dotenv()
    username = os.getenv('USER_NAME')
    password = os.getenv('PASSWORD')
    url = os.getenv('USER_URL')
    chrome.get(url)
    time.sleep(2)
    log_but = chrome.find_element_by_class_name("L3NKy")
    time.sleep(2)
    log_but.click()
    time.sleep(2)
    # finds the username box
    usernameBox = chrome.find_element_by_name("username")
    # sends the entered username
    usernameBox.send_keys(username)
    # finds the password box
    time.sleep(2)
    passwordBox = chrome.find_element_by_name("password")
    # sends the entered password
    time.sleep(2)
    passwordBox.send_keys(password)
    time.sleep(2)
    # press enter after sending password
    passwordBox.send_keys(Keys.RETURN)
    time.sleep(5.5)
    # Finding Not Now button
    notk = chrome.find_element_by_class_name("yWX7d")
    notk.click()
    time.sleep(3)


def load_text():
    file = open("day_number.txt", "r")
    day_number_read = file.read()
    day_number_write = int(day_number_read)
    day_number_write = day_number_write + 1
    file.close()

    file = open("day_number.txt", "w")
    file.write(str(day_number_write))
    file = open("message.txt", "r")
    message = file.read() + " " + day_number_read
    file.close()
    return message


def send_message(message):
    # Find message button
    message_button = chrome.find_element_by_class_name('_862NM ')
    message_button.click()
    time.sleep(2)
    chrome.find_element_by_class_name('HoLwm ').click()
    time.sleep(1)
    text_area = chrome.find_element_by_tag_name('textarea')
    text_area.send_keys(message)
    text_area.send_keys(Keys.RETURN)
    time.sleep(1.2)


if __name__ == '__main__':
    main()
