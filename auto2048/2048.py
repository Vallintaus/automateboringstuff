# Automated 2048 game on browser. for some reason it scrolls to the bottom of the page

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

webdriver_path = '/usr/bin/geckodriver'

driver = webdriver.Firefox()

driver.get('https://gabrielecirulli.github.io/2048/')

game = driver.find_element(By.TAG_NAME, "html")


time.sleep(3)
cookie_button = driver.find_element(By.ID, "ez-accept-all")
cookie_button.click()

time.sleep(3)

prevent_scroll_js = """
window.addEventListener('keydown', function(e) {
    if(["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"].indexOf(e.code) > -1) {
        e.preventDefault();
    }
}, false);
"""
driver.execute_script(prevent_scroll_js)

grid_click = driver.find_element(By.TAG_NAME, "body")
grid_click.click()

while True:
    grid_click.send_keys(Keys.UP)
    time.sleep(0.1)
    grid_click.send_keys(Keys.RIGHT)
    time.sleep(0.1)
    grid_click.send_keys(Keys.DOWN)
    time.sleep(0.1)
    grid_click.send_keys(Keys.LEFT)
    time.sleep(0.1)