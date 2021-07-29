# Fake Cleverbot

A stupid little Discord bot I made so you can prank your friends

---
Here's how it works:
Basically, we have a bot user which whoever you're pranking will think is actually speaking for itself. However, instead we are going to be feeding the bot messages to send. :-)

## Setup

0. Get admin on the server you're pranking them on
1. Create a new application on the Discord developer portal
2. Create a new bot and name it whatever you want
3. Copy the token from the application into the program where it says 'INSERT_TOKEN_HERE'
4. Create a new private channel in the server you're using to prank your friends so only admins can see it (and your friends can't)
5. Copy the second number in the link of the private channel (Example: https[]()://discord.com/channels/870173255057698867/***870173255057698870***) and put it in the program where it says 'INSERT_INPUT_CHANNEL_HERE'
6. Copy the second number in the link of the channel you'll be sending the prank messages in (Example: https[]()://discord.com/channels/870173255057698867/***870173255057698870***) and put it in the program where it says 'INSERT_OUTPUT_CHANNEL_HERE'
7. have fun 🤡

## Running the Bot

0. Install python 3.5 or higher (https://python.org/download)
1. Install the discord.py API wrapper for python using the command 'py -m pip install discord' on windows or 'python3 -m pip install discord' on macos and linux
2. Then type 'py main.py' on windows or 'python3 main.py' on macos and linux

## Using the Bot

0. Make sure you've completed setup and started the bot up by running it
1. Go to the private channel that you have created and start typing messages
2. The messages you typed in the private channel should appear in the channel you have designated as the output channel
3. There is no step 3, have fun :-)
