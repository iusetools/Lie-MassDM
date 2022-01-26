import discord
import os
import colorama
from colorama import Fore, Style
import requests
import time
from colorama import Fore



def Cls():
    os.system('cls')
Cls()
b = Style.BRIGHT
message = input("WHAT U WANN SAY? ")
Cls() 


token = input("PASTE TOKEN: ")

Cls()

b = Style.BRIGHT
print(f"""
{b+Fore.GREEN}


██      ██ ███████     ███    ███  █████  ███████ ███████ ██████  ███    ███ 
██      ██ ██          ████  ████ ██   ██ ██      ██      ██   ██ ████  ████ 
██      ██ █████       ██ ████ ██ ███████ ███████ ███████ ██   ██ ██ ████ ██ 
██      ██ ██          ██  ██  ██ ██   ██      ██      ██ ██   ██ ██  ██  ██ 
███████ ██ ███████     ██      ██ ██   ██ ███████ ███████ ██████  ██      ██
               

                                                    
                                                             
{b+Fore.BLUE} > {Fore.RESET}MASS DM
{b+Fore.BLUE} > {Fore.RESET}Creator: isaiah#6969
""")

iah = discord.Client()


@iah.event
async def on_connect():
  for user in iah.user.friends:
    try:
      isaiah = discord.Embed(color= discord.Color(0x9400D3))
      isaiah.set_author(name="https://discord.gg/A2UVmknk")
      isaiah.add_field(name="DISCORD.GG/LAIR",value=message)
      isaiah.set_image(url="https://cdn.discordapp.com/attachments/812926762806673441/813177367962189844/GIF-210221_172132.gif")
      time.sleep(.1)
      await user.send(embed=isaiah)
      time.sleep(.1)
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")
       print(f"Directed messaged all users friends")


iah.run(token, bot=False)