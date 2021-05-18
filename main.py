import discord
import os
import requests
import json

greetings = ['hello', 'hi', "greetings"]
inspire_command = 'inspire'
midterm_command = 'midterm'
final_command ='final'
midterm_time = "now"
midterm_content = "everything"
final_time = "now"
final_content = "now"
final_dict = {"when" : "now", "what" : "everything"}
midterm_dict = {"when" : "now", "what" : "everything"}

bot_says = " "

midterm_default_line = "The midterm is on " + midterm_time + " and " + midterm_content + " is on it." 

client = discord.Client()

def get_quote():
  global bot_says
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  bot_says = quote

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  global bot_says, greetings, inspire_command, final_command
  if message.author == client.user:
    return
  
  data = str(message.content)
  data = data.lower() 
  if inspire_command in data:
    get_quote()
  elif midterm_command in data:
    midterm_returns(data)
  elif final_command in data:
    finals_returns(data)
  for greeting in greetings:
    if greeting in data:
      greeting_return()

  await message.channel.send(bot_says)
  data = ""
  
def greeting_return():
  global bot_says
  bot_says = "Hi!"

def midterm_returns(data):
  global bot_says, midterm_dict, midterm_default_line
  data = string_processing(data)
  bot_says = midterm_dict.get(data, midterm_default_line)

def finals_returns(data):
  global bot_says, final_dict
  data = string_processing(data)
  bot_says = final_dict.get(data, "oops")

def string_processing(data):
  if ('when' in data) and ('what' in data):
   data = 'x'
  elif 'when' in data:
   data = "when"
  elif "what" in data:
   data = "what"
  else:
   data = 'x'
  return data

  


client.run(insert token here)
