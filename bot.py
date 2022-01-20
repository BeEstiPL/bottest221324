import discord
from discord.ext import commands

token = "OTMzNzU1NDIzNzk2ODg3NTgz.YemJgQ.3sx6OM_Ow75b-klI4U05efVySc8"
client = commands.Bot(command_prefix="$", case_insensitive=True)

@client.event
async def on_ready():
          print('We have logged in as {0.user}'.format(client))


@client.command()
async def move(ctx,member: discord.Member=None, VoiceChannel=None):
          try:
                    channel = discord.utils.get(ctx.guild.channels, id=int(VoiceChannel))
                    if member == None:
                              await ctx.message.author.move_to(channel)
                    else:
                              await member.move_to(channel)
          except Exception as e:
                    embed = discord.Embed(
                              title = '**ERROR**',
                              description = e,
                              color = discord.Color.red()
                    )
                    await ctx.send(embed=embed)

@client.event
async def on_message(mesage):
    ctx = await client.get_context(mesage)
    if ctx.valid:
        await client.invoke(ctx)

client.run(token)