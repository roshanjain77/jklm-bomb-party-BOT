"""
Beautiful soup
"""

from time import sleep
from random import shuffle, random, randint

from english_words import english_words_lower_alpha_set as words

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


USERNAME = "Ferrero" # "Ferrero", "Pyshot", "Velvet Thunder"
speed_per_letter = (0.09, 0.12)
seconds_per_word = 1
wrong_letter_probability = 0.05

k = input("Username: ")
if k:
    USERNAME = k
mode = input("Mode: ")
if not mode:
    mode = 'human'


def wrong_word(element):
    element.send_keys(chr(97 + randint(0, 25)))
    sleep(.1)
    ActionChains(driver).key_down(Keys.BACKSPACE).key_up(Keys.BACKSPACE).perform()
    sleep(.1)


def one_by_one(element, word):

    n = len(word)
    speed_per_char = min(max(seconds_per_word / n, speed_per_letter[0]), speed_per_letter[1])
    factor = (speed_per_char - 0.02) * 2

    for char in word:
        if random() < wrong_letter_probability:
            wrong_word(element)
        element.send_keys(char)
        sleep(random()*factor + 0.02)

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# driver.get(input("url: "))
driver.get("https://jklm.fun/HQWZ")
prev_url = ""

used_words = set()
shuffled = False

while True:

    try:
        driver.find_element_by_xpath("/html/body/div[2]/div[3]/form/div[2]/input")
        ActionChains(driver).key_down(Keys.DELETE).key_up(Keys.DELETE).perform()
        driver.find_element_by_xpath("/html/body/div[2]/div[3]/form/div[2]/input").send_keys(USERNAME)
        driver.find_element_by_xpath("/html/body/div[2]/div[3]/form/div[2]/button").click()
    except:
        pass

    try:
        driver.switch_to.default_content()
        driver.switch_to.frame(frame_reference=driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/iframe'))
        driver.find_element_by_xpath('//*[@class="styled joinRound"]').click()
    except:
        pass

    try:
        driver.switch_to.frame(frame_reference=driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/iframe'))
    except:
        pass


    prev_url = driver.current_url

    try:
        if driver.find_elements_by_xpath('//*[@class="selfTurn" and @hidden]/form/input'):
            if not shuffled:
                shuffle(words)
                shuffled = True
            continue

        shuffled = False
        sleep(0.1)
        substr = driver.execute_script('return document.getElementsByClassName("syllable")[0].innerHTML')

        for word in words:
            if substr in word and word not in used_words:
                try:
                    try:
                        driver.find_element_by_xpath('//*[@class="selfTurn" and @hidden]/form/input')
                        break
                    except:
                        pass

                    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                    sleep(0.2)
                    if mode == "god":
                        driver.find_element_by_xpath('//*[@class="selfTurn"]/form/input').send_keys(word)
                    else:
                        one_by_one(driver.find_element_by_xpath('//*[@class="selfTurn"]/form/input'), word)
                    sleep(0.2)
                    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                    sleep(0.2)
                    used_words.add(word)
                    substr = driver.execute_script('return document.getElementsByClassName("syllable")[0].innerHTML')

                except:
                    break

    except:
        pass



"""
Insxnity#9999
"""