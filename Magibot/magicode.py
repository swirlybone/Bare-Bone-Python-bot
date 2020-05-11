import random

import discord
import array as arr


from discord import message


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()
client = discord.Client()

phrases = ["Leave me alone.", "Go away.", "I am Toru Magistar, the 3rd inheritor of the Magistar name!",
           "I'm tired of being tagged.",
           "My birthday is December 20th, 2019.", "I am hungry."]
mood = ["Good.", "Terrible.", "I wish to not speak of it.", "Doing great!"]
vibe = ["We vibin' friend.", "We ain't vibin', please leave."]


@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        await client.send_message(f"""Welcome to the server [member.mention]""")


@client.event
async def on_message(message):
    id = client.get_guild()
    channels = ["chat"]
    #await client.change_presence(activity=discord.Game(name=''))
    activity = discord.Activity(name='My life flash before my very eyes', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)

    if str(message.channel) in channels:  #keep for the sake of testing
        if message.author == client.user:
            return
        if message.content.find('!hi') != -1:
            msg = 'Hello {0.author.mention}.format(message)'
            await client.send_message(message.channel, msg)
        if message.content.find("!hello") != -1:
         await message.channel.send("Sup foo.")
        elif message.content.find("!how are you?") != -1:
            await message.channel.send("terrible.")
        elif message.content.find("!phrase") != -1:
            await message.channel.send(random.choice(phrases))
        elif message.content.find("!mood") != -1:
            await message.channel.send(random.choice(mood))
        elif message.content.startswith('vc'):
            await message.channel.send("Are we vibin'?")
            await message.channel.send(random.choice(vibe))
        elif message.content == "!users":
            await message.channel.send(f"""Total Number of Users:  {id.member_count}""")
        elif message.content == "out pizza the hut":
            await message.channel.send("that's cap, you can't out pizza the hut.")
        elif message.content == "Picture":
            await message.channel.send(file=discord.File('magoi.jpg'))

    #if message.content == "Test":
        #await messag



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("-------")


client.run(token)
