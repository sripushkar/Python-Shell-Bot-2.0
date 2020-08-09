import os
import io
import json
import discord
import traceback
from contextlib import redirect_stdout
#from dotenv import load_dotenv

#load_dotenv()
#TOKEN = os.getenv('TOKEN')
TOKEN = os.environ.get('TOKEN', None)
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
    if "\"" in str or "'" in str or "=" in str:
        return 'exec'
    return 'eval'

@client.event
async def on_message(message):
    pref = '>>'
    if isCommand(message.content, pref):
        python = formatCommand(message.content, pref)
        if evalOrExec(python) == 'exec':
            try:
                func_str = python
                stdout = io.StringIO()
                with redirect_stdout(stdout):
                    exec(func_str)
                out = stdout.getvalue()
                reply = out, out.strip() == '3'
                reply = str(reply[0])

            except:
                trace = traceback.format_exc()
                print("EROORRREUOFGO", trace)
        else:
            reply = eval(python)

        await message.channel.send(reply)


client.run(TOKEN)
