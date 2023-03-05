import discord
import asyncio

intents = discord.Intents.default()
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!delete'):
        if not message.author.guild_permissions.manage_messages:
            await send_discord('You do not have permission to delete messages.')
            return
        limit = int(message.content.split(' ')[1]) if len(message.content.split(' ')) > 1 else 1
        total = 0
        async for msg in message.channel.history(limit=limit+1):
            await message.channel.purge(limit=1)
            await asyncio.sleep(1)
            total += 1
        await send_discord('Deleted {} messages from {}'.format(total -1 , message.channel.mention))
        
def send_discord(message):
    channel = client.get_channel(12345) #Log channel ID
    return channel.send(message)

client.run('*******')