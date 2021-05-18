import discord
import os
import requests
import json
from match_bot import match_bot

with open("responses.json") as f:
    responses = json.loads(f.read())

with open("auth.json") as f:
    auth = json.loads(f.read())

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  bot_says = match_bot(responses,message.content, get_quote)
  if bot_says:
    await message.channel.send(bot_says)

client.run(auth["discord_key"])
  