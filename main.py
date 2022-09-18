import requests
import json
import os
import discord
import colorama

from colorama import Fore
from discord.ext import commands

os.system('title message logger')

channelid = input(f'{Fore.MAGENTA} > {Fore.RESET} Channel ID: ')

def retrieve_messages(channelid):
    token = input(f'{Fore.MAGENTA} > {Fore.RESET} Token: ')
    headers = {
        'authorization': (f'{token}')
    }

    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    jsonn = json.loads(r.text)
    
    for value in jsonn:
        print(f'{Fore.MAGENTA} > {Fore.RESET} Message: ', value['content'], '\n' f'     {Fore.MAGENTA} > {Fore.RESET} Timestamp: ', '-', value['timestamp'], '\n' f'     {Fore.MAGENTA} > {Fore.RESET} Channel ID: ', '-', value['channel_id'], '\n' f'     {Fore.MAGENTA} > {Fore.RESET} Message ID: ', '-', value['id'], '\n' f'     {Fore.MAGENTA} > {Fore.RESET} Author: ', '-', value['author']['username'], value['author']['discriminator'],'\n')
        with open('messages.txt', 'a', encoding="utf-8") as file:
            file.write(f'> Message: ' + value['content'] + '\n' + f'     > Timestamp: ' + value['timestamp'] + '\n' f'     > Channel ID: ' + value['channel_id'] + '\n' + f'     > Message ID: ' + value['id'] + '\n' +  f'     > Author: ' + value['author']['username'] + value['author']['discriminator'] + '\n')
    

retrieve_messages(channelid)
input(f'{Fore.MAGENTA} > {Fore.RESET} All messages succesfully logged.')
