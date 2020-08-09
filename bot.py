import os
import io
import json
import discord
from contextlib import redirect_stdout

with open("user.json") as file:
    userDetails = json.load(file)

TOKEN = userDetails["TOKEN"]
client = discord.Client()

def isCommand(msg, prefix):
    if msg[0:2] == prefix and "import os" not in msg:
        return True
    return False

def formatCommand(str, prefix):
    newStr = str.replace(prefix, "")
    newStr = newStr.replace("’", "'")
    newStr = newStr.replace("“", "\"")
    newStr = newStr.replace("”", "\"")
    return newStr

def evalOrExec(str):
    if "\"" in str or "'" in str:
        return 'exec'
    return 'eval'

@client.event
async def on_message(message):
    pref = '>>'
    if isCommand(message.content, pref):
        python = formatCommand(message.content, pref)
        if evalOrExec(python) == 'exec':
            func_str = python
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                exec(func_str)

            out = stdout.getvalue()
            reply = out, out.strip() == '3'
            reply = reply[0]
        else:
            reply = eval(python)

        await message.channel.send(reply)


client.run(TOKEN)
