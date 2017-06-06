import vkapi
import os
import importlib
from command_system import command_list

def load_modules():
   files = os.listdir("commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])

def get_answer(text):
    message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
    attachment = ''
    body = text.split()[0]
    for c in command_list:
        if body in c.keys:
            message, attachment = c.process(text)
    return message, attachment

def create_answer(data, token):
    load_modules()
    user_id = data['user_id']
    message, attachment = get_answer(data['body'].lower())
    vkapi.send_message(user_id = user_id,token = token, message = message, attachment = attachment)
