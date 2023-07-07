import wordle_solver as ws
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def hints_incomplete(clues):
    try:
        if len(clues) != 5:
            return True
        for clue in clues:
            if len(clue) != 2:
                return True
    except TypeError:
        return True
    except IndexError:
        return True
    return False


if __name__ == "__main__":
    # Using Chrome to access web
    driver = webdriver.Chrome()

    # Open the website
    driver.get('https://www.nytimes.com/games/wordle/index.html')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Click the "Play" button
    try:
        playButton = driver.find_element(By.CLASS_NAME, "Welcome-module_button__ZG0Zh")
        playButton.click()
    except Exception as ex:
        print(ex)


    # Close the rules popup
    try:
        exitButton = driver.find_element(By.CLASS_NAME, "Modal-module_closeIcon__TcEKb")
        exitButton.click()
    except Exception as ex:
        print(ex)


    # Enter the word "crane"
    time.sleep(2)
    board = driver.find_element(By.XPATH, "/html/body")
    board.send_keys("crane")
    board.send_keys(Keys.RETURN)
    time.sleep(4)

    wordle = ws.wordle_solver()
    rows = driver.find_elements(By.CLASS_NAME, "Row-module_row__pwpBq")
    for row in rows:
        letters = ['empty'] * 5
        hints = [None] * 5
        while hints_incomplete(hints):
            time.sleep(1)
            letters = row.find_elements(By.CLASS_NAME, "Tile-module_tile__UWEHN")
            hints = []
            for letter in letters:
                hints.append(letter.get_attribute("aria-label").split(' '))

        print("\nword hint:")
        for item in hints:
            print("letter {} is {}".format(item[0].capitalize(), item[1]), end="\t\t")

        for i, letter in enumerate(hints):
            if letter[1] == 'absent':
                wordle.out_word_add(letter[0])
            if letter[1] == 'present':
                wordle.out_of_order_letter_add(letter[0], i)
            if letter[1] == 'correct':
                wordle.letter_add(letter[0], i)

        if wordle.complete():
            print("\n\nWord: ", *[letter.capitalize() for letter in wordle.word], sep='')
            time.sleep(5)
            break

        time.sleep(2)
        board.send_keys(wordle.psbl_word())
        board.send_keys(Keys.RETURN)
        time.sleep(3)

