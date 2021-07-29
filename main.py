# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details.

import discord

client = discord.Client()

@client.event
async def on_message(ctx):
    if ctx.channel.id == INSERT_INPUT_CHANNEL_HERE:
        output_channel = client.get_channel(INSERT_OUTPUT_CHANNEL_HERE)
        await output_channel.send(ctx.content)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run('INSERT_TOKEN_HERE')
