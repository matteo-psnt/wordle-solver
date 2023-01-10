import wordle_solver as ws
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Using Chrome to access web
driver = webdriver.Chrome()
# Open the website
driver.get('https://www.nytimes.com/games/wordle/index.html')

driver.close()

if __name__ == "__main__":
    wordle = ws.wordle_solver()
    print('update')
    wordle.in_word_add('')
    wordle.out_word_add('')
    wordle.word = [None, None, None, None, None]
    print('psbl_word')
    wordle.psbl_word()
