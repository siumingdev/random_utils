import os
import sys
from enum import Enum
import random
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


class Difficulty(Enum):
  easy = "Easy"
  medium = "Medium"
  hard = "Hard"


def get_question_by(difficulty: Difficulty, login: str, password: str):
  driver = webdriver.Firefox()
  driver.implicitly_wait(10)

  driver.get(f"https://leetcode.com/problemset/all/?difficulty={difficulty.value}&status=Todo")

  elem = driver.find_element_by_link_text("Sign in")
  elem.click()

  elem = driver.find_element_by_xpath("//a[@data-icon='github-c']")
  elem.click()

  elem = driver.find_element_by_xpath("//input[@id='login_field']")
  elem.send_keys(login)

  elem = driver.find_element_by_xpath("//input[@id='password']")
  elem.send_keys(password)

  elem = driver.find_element_by_xpath("//input[@value='Sign in']")
  elem.click()

  elem = random.choice(driver.find_elements_by_class_name("reactable-page-button"))
  elem.click()

  elem = random.choice(driver.find_elements_by_xpath("//a[starts-with(@href, '/problems/')]"))
  elem.click()
  
  # driver.close()


if __name__ == "__main__":
  with open(get_script_path() + "/credientials.txt", "r") as f:
    login = f.readline()
    password = f.readline()

  get_question_by(Difficulty.easy, login, password)
