# Python-Shell-Bot 2.0
### A Discord bot which brings a Python Shell into your Discord server.

Python Shell Bot is a bot built with Python that brings adds a Python Shell into a server. This is mostly for fun, and does not support input(yet).

This is based off of my first version of the bot, built using node.js, which can be found <a href = https://github.com/sripushkar/Python-Shell-Bot>here</a>

### Add the bot:
You can add the bot with this link: https://discord.com/api/oauth2/authorize?client_id=741814683346141204&permissions=10240&scope=bot
### To build manually 
You will need the following installed:
* Python 3
* pip

Download this repo, and create a .env file. Then create a discord bot account, and add the bot token in the .env file like this: 

`TOKEN = [your token here]`

Then to install the dependencies, do 

`pip install discord.py`

`pip install python-dotenv`

To run the bot, use 

`python bot.py`

### To use the bot:
Start off with >>, then your python command. For example: >>print("hello") will make the bot send 'hello' in the server. To use multiple lines, you can either enter using a new line in the message, or seperate your statements with a semicolon. For example: >>print("Hello"); print("World")

