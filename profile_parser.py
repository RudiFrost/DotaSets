import requests
import json
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs4




# DRIVER = webdriver.Chrome('/home/sirius/DotaGit/DotaSkin/chromedriver')

def steam_parser(URL):
    profile_name = DRIVER.find_element('xpath', '//*[@id="responsive_page_template_content"]/div[1]/div[2]/div/div/div/div[1]/div[1]/span[1]')
    DRIVER.get(URL)
    
    games = DRIVER.find_element('xpath', '//*[@id="responsive_page_template_content"]/div[1]/div[3]/div/div[1]/div[2]/div[4]/div[1]/a/span[1]').click()
    check_dota = DRIVER.find_element('xpath', '//*[@id="game_570"]')
    print(profile_name)

# steam_parser('https://steamcommunity.com/id/vnJ64/')

def take_nickname(URL):
    nickname = ''
    avatar_link = ''
    array = []
    response = requests.get(URL)
    soup = bs4(response.text, 'html.parser')
    quotes = soup.find_all('div', 'profile_header_bg')

    for quote in quotes:
        nickname = quote.find('span', class_='actual_persona_name').text
        avatar_link = quote.find('div', class_='playerAvatarAutoSizeInner').img
        array.append(nickname)
        array.append(avatar_link)
    

    ava = str(array).split('/')
    finish_link = 'https://' + ava[2] + '/' + ava[3][:-1]
    array.pop(1)
    array.append(finish_link)

    return array



take_nickname('https://steamcommunity.com/id/vnJ64/')