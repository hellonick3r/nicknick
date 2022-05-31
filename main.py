from discord.ext import commands
import  discord


client = discord.Client()

@client.event
async def on_ready():
    print(f'Successfully logged in as {client.user}')

@client.event
async def on_message(message):
	if message.content == 'สวัสดีครับบอท':
		await message.channel.send('ควยไอ่สัส ' + message.author.name)
	elif message.content == 'spam':
			for i in range(0+1,10):
				await message.channel.send(f'spam test for {message.author.name} '+ str(i))


token = 'OTgwNjk4NTQ2Nzc0ODcyMDk0.Gf8Opt.uSyYW_kTMoa7ryhNehWGzj6F6WGAKCNwjLDRS0'
client.run(token)