import os
import io
from contextlib import redirect_stdout

with open("user.json") as file:
    userDetails = json.load(file)

TOKEN = userDetails["DISCORD_TOKEN"]
client = discord.Client()

prefix = '>>'

def isCommand(msg):
    if msg[0,2] == prefix and "import os" not in msg:
        return True
    return False

def formatCommand(str):
    newStr = newStr.replace(prefix, "")
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
    if isCommand(message.content):
        python = formatCommand(message.content)
        if evalOrExec(python) == 'exec':
            func_str = python
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                exec(func_str)

            out = stdout.getvalue()
            reply = out, out.strip() == '3'
        else:
            reply = eval(python)

        await message.channel.send(reply)


client.run(TOKEN)
