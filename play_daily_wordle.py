import wordle_solver as ws
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


if __name__ == "__main__":
    # Using Chrome to access web
    driver = webdriver.Chrome()
    # Open the website
    driver.get('https://www.nytimes.com/games/wordle/index.html')
    exitButton = driver.find_element(By.CLASS_NAME, "Modal-module_closeIcon__TcEKb")
    exitButton.click()
    board = driver.find_element(By.XPATH, "/html/body")
    board.screenshot("a.png")
    driver.close()