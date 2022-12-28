import json
import time

import requests
import telebot
from telebot import types

from parser import get_match

with open('token.txt') as fbt:
    TOKEN = fbt.readline().strip()

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer1 = types.KeyboardButton('Main information about hero')
    answer2 = types.KeyboardButton('Information about matches')
    markup.add(answer1, answer2)
    bot.send_message(message.chat.id, 'What do you want /start', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Main information about hero')
def bot_message(message):
    if message.chat.type == 'private':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        bot.send_message(message.chat.id, 'Enter hero name', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Information about matches')
def bot_message(message):
    if message.chat.type == 'private':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        bot.send_message(message.chat.id, 'Enter All Pick match id', reply_markup=markup)


@bot.message_handler(commands=['random'])
def bot_message(message):
    if not message.text.isdigit():
        with open('data/heroes_name.json') as f:
            templates = json.load(f)
        try:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            r = requests.get('http://127.0.0.1:5000/api/heroes/0')
            r = r.text.split('"')[-2]
            print(r)
            photo = open('../static/avatars/' + r + '_ava.png', 'rb')
            r = r.split("_")
            for i in range(len(r)):
                r[i] = r[i][0].upper() + r[i][1:]
            r = " ".join(r)
            if r == "Templar":
                r = "Templar Assassin"
            if r == "Legion":
                r = "Legion Commander"
            answer1 = types.KeyboardButton('Main information about hero')
            answer2 = types.KeyboardButton('Information about matches')
            markup.add(answer1, answer2)
            bot.send_photo(message.chat.id, photo, caption="Id: " + str(templates[r]["id"]) + "\n" +
                                                           "Hero command name: `" + templates[r][
                                                               "name"] + "`\n" +
                                                           "Main attribute: " + templates[r][
                                                               "primary_attr"] + "\n" +
                                                           "Attack type: " + templates[r][
                                                               "attack_type"] + "\n" +
                                                           "Role: " + (str(
                str(templates[r]["roles"]).split(",")[0]))[2:-1] + "\n",
                           parse_mode='MarkdownV2', reply_markup=markup
                           )
        except:
            bot.send_message(message.chat.id, "Hero doesn't exist", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    message.text = message.text.title()
    if not message.text.isdigit():
        with open('data/heroes_name.json') as f:
            templates = json.load(f)
        try:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            photo = open('../static/avatars/' + message.text + '_ava.png', 'rb')
            answer1 = types.KeyboardButton('Main information about hero')
            answer2 = types.KeyboardButton('Information about matches')
            markup.add(answer1, answer2)
            bot.send_photo(message.chat.id, photo, caption="Id: " + str(templates[message.text]["id"]) + "\n" +
                                                           "Hero command name: `" + templates[message.text][
                                                               "name"] + "`\n" +
                                                           "Main attribute: " + templates[message.text][
                                                               "primary_attr"] + "\n" +
                                                           "Attack type: " + templates[message.text][
                                                               "attack_type"] + "\n" +
                                                           "Role: " + (str(
                str(templates[message.text]["roles"]).split(",")[0]))[2:-1] + "\n",
                           parse_mode='MarkdownV2', reply_markup=markup
                           )
        except:
            bot.send_message(message.chat.id, "Hero doesn't exist", reply_markup=markup)

    elif message.text.isdigit():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        answer1 = types.KeyboardButton('Main information about hero')
        answer2 = types.KeyboardButton('Information about matches')
        markup.add(answer1, answer2)
        try:
            get_match(message.text)

            with open('data/match.json') as f1:
                templates = json.load(f1)
            match_duration = time.gmtime(templates["duration"])
            first_blood = time.gmtime(templates["first_blood_time"])
            final_message = "Match id: " + message.text + "\n\n" + \
                            str(templates['radiant_win']) + " victory" + "\n\n" + \
                            "Radiant total kills: " + str(templates['radiant_score']) + "\n" + \
                            "Dire total kills: " + str(templates['dire_score']) + "\n\n" + \
                            "Match duration: " + time.strftime("%H:%M:%S", match_duration) + "\n\n" + \
                            "Heroes pick and order: \n" + \
                            templates["picks_bans"][0]["team"] + " - " + templates["picks_bans"][0]["hero_id"] + "\n" + \
                            templates["picks_bans"][1]["team"] + " - " + templates["picks_bans"][1]["hero_id"] + "\n" + \
                            templates["picks_bans"][2]["team"] + " - " + templates["picks_bans"][2]["hero_id"] + "\n" + \
                            templates["picks_bans"][3]["team"] + " - " + templates["picks_bans"][3]["hero_id"] + "\n" + \
                            templates["picks_bans"][4]["team"] + " - " + templates["picks_bans"][4]["hero_id"] + "\n" + \
                            templates["picks_bans"][5]["team"] + " - " + templates["picks_bans"][5]["hero_id"] + "\n" + \
                            templates["picks_bans"][6]["team"] + " - " + templates["picks_bans"][6]["hero_id"] + "\n" + \
                            templates["picks_bans"][7]["team"] + " - " + templates["picks_bans"][7]["hero_id"] + "\n" + \
                            templates["picks_bans"][8]["team"] + " - " + templates["picks_bans"][8]["hero_id"] + "\n" + \
                            templates["picks_bans"][9]["team"] + " - " + templates["picks_bans"][9][
                                "hero_id"] + "\n\n" + \
                            "First blood on " + time.strftime("%M:%S", first_blood)
            bot.send_message(message.chat.id, final_message, reply_markup=markup)
        except:
            bot.send_message(message.chat.id, "Not valid id", reply_markup=markup)


bot.polling(none_stop=True)
