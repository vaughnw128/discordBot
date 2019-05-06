# Work with Python 3.6
import discord

#TODO: allow for spaces in the terms, respond to cringe, display a PMed cringe list, voice chat features

client = discord.Client()

#list of terms
terms = []

def updateTerms(terms):
    with open("terms.txt", "r") as file:    
        terms = []
        # rawTerms = file.readlines()
        # terms = [x.strip() for x in rawTerms]
        for line in file:
            terms.append(line)
 
def addTerm(term):
    terms.append(term)
    with open("terms.txt", "a") as file:
        if len(terms) > 0:
            index = len(terms)-1
        else:
            index = 0
        file.write(terms[index] + '\n')
    updateTerms(terms)

def delTerm(term):
    terms.remove(term)
    with open("terms.txt", "r") as file:
        lines = file.readlines()
    with open("terms.txt", "w") as file:
        for line in lines:
            if line.strip("\n") != term:
                file.write(line)
    updateTerms(terms)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('c!status'):
        msg = 'Cringedar: Active'.format(message)
        await message.channel.send(msg)

    #Adding a term
    if message.author.id == 173232081575346178:
        if message.content.startswith('c!addterm'):
            term = (message.content.split())
            
            if len(term) < 2:
                msg = 'Please include a term.'
            else:
                tempTerm = ""
                for x in range(1, len(term)):
                    tempTerm += term[x]
                    if(x != len(term)-1):
                        tempTerm += ' '
                term = tempTerm
                if term in terms:
                    msg = 'Term already exists.'
                else:
                    addTerm(term)
                    msg = 'Added ' + term + ' to cringe list.'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('c!delterm'):
            term = (message.content.split())
            if len(term) < 2:
                msg = 'Please include a term.'
            else:
                term = term[1]
                delTerm(term)
                msg = 'Removed ' + term + ' from the cringe list.'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('c!cringelist'):
            updateTerms(terms)
            
            #msg = '```'
            #for x in terms:
            #    msg += ' ' + str(terms.index(x)) + '. ' + x + '\n'
            #msg += '```'
            #msg.format(message)
            await message.channel.send(msg)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#Starts bot
tfile = open("token", "r")
TOKEN = tfile.read()
client.run(TOKEN)
