import discord
import os
import requests

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!random'):
      if len(message.content) == 7:
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1&swear=0")
        res = response.text
        list = res.strip('][').replace('"','').split(',')
        msg = ""
        for i in list:
          msg += i+"\n"
        await message.channel.send(msg)
      if len(message.content) == 9 and message.content[-1] != "0" and message.content[-1].isnumeric() and message.content[-2:-1] == " ":
        url = "https://random-word-api.herokuapp.com/word?number="+message.content[-1]+"&swear=0"
        response = requests.get(url)
        res = response.text
        list = res.strip('][').replace('"','').split(',')
        msg = ""
        for i in list:
          msg += i+"\n"
        await message.channel.send(msg)
      if len(message.content) > 9:
        await message.channel.send("Please use the command in proper form:\n!random [*A Number from 1-9*]")
#https://random-word-api.herokuapp.com/word?number=10&swear=0

    

client.run(os.getenv('TOKEN'))
