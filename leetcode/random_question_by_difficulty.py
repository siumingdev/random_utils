from enum import Enum
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Difficulty(Enum):
  easy = "Easy"
  medium = "Medium"
  hard = "Hard"


def get_question_by(difficulty: Difficulty=Difficulty.easy):
  driver = webdriver.Firefox()
  driver.implicitly_wait(10)

  driver.get(f"https://leetcode.com/problemset/all/?difficulty={difficulty.value}")

  elem = random.choice(driver.find_elements_by_class_name("reactable-page-button"))
  print(elem)
  elem.click()

  elem = random.choice(driver.find_elements_by_xpath("//a[starts-with(@href, '/problems/')]"))
  print(elem)
  elem.click()

  print(driver.current_url)
  
  # driver.close()


if __name__ == "__main__":
  get_question_by(difficulty=Difficulty.easy)
