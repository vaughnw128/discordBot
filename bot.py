# Work with Python 3.6
import discord

TOKEN = 'NTcxMTEzMTExMTMwNDcyNDQ4.XMYvKQ.ctbsjlaPAP8jmovfJIUcJBqK2c0'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself

    if message.author == client.user:
        return

    if message.content.startswith('c!status'):
        msg = 'Cringedar: Active'.format(message)
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)