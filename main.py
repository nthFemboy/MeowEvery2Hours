from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random
import os

USERNAME = "USERNAME GOES HERE"
PASSWORD = "PASSWORD GOES HERE"

# Setup
os.system('cls' if os.name == 'nt' else 'clear')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)

try:
    # Open Twitter (X)
    driver.get('https://x.com/login')

    # Log in
    wait.until(EC.presence_of_element_located((By.NAME, "text"))).send_keys(USERNAME + Keys.ENTER)
    sleep(2)
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(PASSWORD + Keys.ENTER)

    # Wait for tweet box to load
    tweet_box = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div[role='textbox'][data-testid='tweetTextarea_0']"))
    )

    # Focus tweet box and generate meows
    tweet_box.click()
    meow_count = random.randint(1, 55)
    tweet = " ".join(["meow"] * meow_count)
    tweet_box.send_keys(tweet)
    sleep(2)  # Give the UI time to enable the button

    # Try broader selector for tweet buttons
    buttons = driver.find_elements(By.XPATH, "//*[contains(@data-testid, 'tweetButton')]")
    print("Found", len(buttons), "possible tweet buttons.")

    if buttons:
        buttons[0].click()
    else:
        print("❌ Couldn't find the tweet button.")
        driver.save_screenshot("no_tweet_button.png")

    # Find and click the Post button
    tweet_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@data-testid='tweetButtonInline']")
    ))
    tweet_button.click()

    sleep(4)  # Wait for the tweet to be posted

finally:
    driver.quit()
