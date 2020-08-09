import os

TOKEN = os.environ['TOKEN']
prefix = '>>'

@client.event
async def on_message(message):
    pass
    #await message.channel.send("Sorry, please try again by starting a new game.")

client.run(TOKEN)
