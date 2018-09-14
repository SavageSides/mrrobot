import discord
from discord.ext import commands
import time
import asyncio
import random


client = commands.Bot(command_prefix='>')
client.remove_command('help')

@client.event
async def on_ready():
    print('I am ready:')
    await client.change_presence(game=discord.Game(name=f"over {len(set(client.get_all_members()))} users - >help"))

@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None, *, reason=None):
    author = ctx.message.author
    if ctx.message.author.server_permissions.kick_members:
        if user is None:
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the user you want me to kick!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Kick - Information')
            embed.add_field(name='Reason:', value='{0}'.format(reason), inline=True)
            embed.add_field(name='Author:', value='``{}``'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.send_message(user, embed=embed)
            await client.kick(user)
            #Sends the user a message when he is kicked!
            embed = discord.Embed(color=0x36393E)
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Kick - Information')
            embed.add_field(name='Reason:', value='**{0}**'.format(reason), inline=True)
            embed.add_field(name='Author:', value='**{}**'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Kick Members``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def ban(ctx, user: discord.Member = None, *, reason=None):
    author = ctx.message.author
    if ctx.message.author.server_permissions.ban_members:
        if user is None:
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the user you want me to ban!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Ban - Information')
            embed.add_field(name='Reason:', value='{0}'.format(reason), inline=True)
            embed.add_field(name='Author:', value='``{}``'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.send_message(user, embed=embed)
            await client.ban(user)
            #Sends the user a message when he is kicked!
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Ban - Information')
            embed.add_field(name='Reason:', value='**{0}**'.format(reason), inline=True)
            embed.add_field(name='Author:', value='**{}**'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.say(embed=embed)

    else:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Ban Members``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def mute(ctx, user: discord.Member = None, *, reason=None):
    author = ctx.message.author
    server = ctx.message.server
    if ctx.message.author.server_permissions.mute_members:
        MutedRole = discord.utils.get(ctx.message.server.roles, name='Muted')
        if user is None:
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the user you want me to mute!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            await client.add_roles(user, MutedRole)
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Mute - Information')
            embed.add_field(name='Server:', value='**{}**'.format(server.name), inline=False)
            embed.add_field(name='Reason:', value='{0}'.format(reason), inline=True)
            embed.add_field(name='Author:', value='``{}``'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.send_message(user, embed=embed)
            #Sends the user a message when he is kicked!
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Mute - Information')
            embed.add_field(name='Server:', value='**{}**'.format(server.name), inline=False)
            embed.add_field(name='Reason:', value='**{0}**'.format(reason), inline=True)
            embed.add_field(name='Author:', value='**{}**'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Mute Members``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def unmute(ctx, user: discord.Member = None):
    author = ctx.message.author
    server = ctx.message.server
    if ctx.message.author.server_permissions.mute_members:
        MutedRole = discord.utils.get(ctx.message.server.roles, name='Muted')
        if user is None:
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the user you want me to unmute!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            await client.remove_roles(user, MutedRole)
            embed = discord.Embed(color=0x36393E)
            embed.add_field(name='Unmute - Information', value='You have been unmuted!', inline=False)
            embed.add_field(name='Server:', value='**{}**'.format(server.name), inline=False)
            embed.add_field(name='Author:', value='``{}``'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.send_message(user, embed=embed)
            #Sends the user a message when he is kicked!
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Unmute - Information')
            embed.add_field(name='Server:', value='**{}**'.format(server.name), inline=False)
            embed.add_field(name='Author:', value='**{}**'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Mute Members``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def nick(ctx, member:discord.User=None, *, newnick=None):
    author = ctx.message.author
    if ctx.message.author.server_permissions.manage_nicknames:
        if member is None:
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the user you want me to change the nickname of!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            await client.change_nickname(member, newnick)
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='{} Nickname has been changed.'.format(member.name))
            embed.add_field(name='Changed:', value='You have changed the nickname to: **{}**'.format(newnick), inline=True)
            await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Manage Nicknames``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def clear(ctx, amount=None):
    if ctx.message.author.server_permissions.manage_messages:
        if amount is None:
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the amount of messages you want me to delete!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            channel = ctx.message.channel
            author = ctx.message.author
            messages = []
            async for message in client.logs_from(channel, limit=int(amount)):
                messages.append(message)
            await client.delete_messages(messages)
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Clear - Information')
            embed.add_field(name='Amount:', value='**I have deleted {} messages**'.format(amount), inline=False)
            embed.add_field(name='Author:', value='**{}**'.format(author.name), inline=False)
            msg = await client.say(embed=embed)
            await asyncio.sleep(5)
            await client.delete_message(msg)
    else:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Manage Messages``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)


@client.command(pass_context=True)
async def timer(ctx, time=None):
    if time is None:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the seconds you want me to set for you!', inline=False)
        embed.set_footer(text='Please set a timer >timer <amount>')
        await client.say(embed=embed)
    channel = ctx.message.channel
    author = ctx.message.author
    message = []
    embed = discord.Embed(color=0x36393E)
    embed.add_field(name=':stopwatch: Robot Timer!:', value='Timer set for **{}** seconds'.format(int(time), inline=True))
    embed.set_footer(text='I love you.')
    await client.say(embed=embed)
    await asyncio.sleep(int(time))
    msg=await client.say('{}'.format(author.mention))
    await client.delete_message(msg)
    embed = discord.Embed(color=0x36393E)
    embed.add_field(name=':stopwatch: Timer Up:', value='Timer is up **{}**'.format(author.name), inline=True)
    embed.set_footer(text='I love you.')
    await client.say(embed=embed)

@client.command()
async def invite():
    embed = discord.Embed(color=0x0cf0f0)
    embed.title = '__Mr. Robotist Link__'
    embed.url = 'https://discordapp.com/api/oauth2/authorize?client_id=488831342243741746&permissions=8&scope=bot'
    embed.set_footer(text='More commands coming!')
    await client.say(embed=embed)

@client.command()
async def add(left : int, right : int):
    embed = discord.Embed(color=0x0cf0f0)
    embed.add_field(name='Math Equations!', value='**{} + {} = {}**'.format(left, right, left + right), inline=True)
    await client.say(embed=embed)

@client.command()
async def sub(left : int, right : int):
    embed = discord.Embed(color=0x0cf0f0)
    embed.add_field(name='Math Equations!', value='**{} - {} = {}**'.format(left, right, left - right), inline=True)
    await client.say(embed=embed)

@client.command()
async def mul(left : int, right : int):
    embed = discord.Embed(color=0x0cf0f0)
    embed.add_field(name='Math Equations!', value='**{} x {} = {}**'.format(left, right, left * right), inline=True)
    await client.say(embed=embed)

@client.command()
async def div(left : int, right : int):
    embed = discord.Embed(color=0x0cf0f0)
    embed.add_field(name='Math Equations!', value='**{} / {} = {}**'.format(left, right, left / right), inline=True)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def ping(ctx):
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        embed=discord.Embed(title=":hourglass_flowing_sand:  Ping has been summoned:", description='**Latency: {}ms**'.format(round((t2-t1)*1000)), color=0x36393E)
        await client.say(embed=embed)

@client.event
async def on_member_join(member: discord.Member):
    await client.change_presence(game=discord.Game(name=f"over {len(set(client.get_all_members()))} users - >help"))
    server = member.server
    channel = discord.utils.get(server.channels, name='welcome')  
    embed = discord.Embed(color=0x36393E)
    embed.add_field(name='Welcome **{}** , welcome to **{}** :envelope_with_arrow:'.format(member.name, server.name), value='Please read the rules of this server and follow corretly. Also type ?help for more commands of this bot!', inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    await client.send_message(channel, embed=embed)


@client.command()
async def botinfo():
    embed = discord.Embed(color=0x36393E)
    embed.title = '**__aQuiVeR YouTube Channel__**'
    embed.add_field(name='Author - Creator', value='**SaVaGe;_;#5185 **', inline=False)
    embed.add_field(name='Creation - Time', value='**9/9/2018**', inline=True)
    embed.add_field(name='Editor - Profile', value='**aQuiVeR#5076** He is also a youtuber his link is here!', inline=False)
    embed.url = 'https://www.youtube.com/aquiveraq'
    await client.say(embed=embed)

@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x36393E)
    embed.set_author(name="Server info")
    embed.add_field(name="**Name**", value=ctx.message.server.name, inline=True)
    embed.add_field(name="**ID**", value=ctx.message.server.id, inline=True)
    embed.add_field(name="**Roles**", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="**Members**", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def info(ctx, user: discord.Member = None):
    if user is None:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! Please specify a user for me to give info about!', inline=False)
        await client.say(embed=embed)
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x36393E)
    embed=discord.Embed(color=0x36393E)
    embed.add_field(name="**Users Name Is:**", value="{}".format(user.name), inline=False)
    embed.add_field(name="**Highest Role Is:**", value="{}".format(user.top_role), inline=False)
    embed.add_field(name="**Users ID Is:**", value="{}".format(user.id), inline=False)
    embed.add_field(name="**Users Nickname Is:**", value="{}".format(user.nick), inline=False)
    embed.add_field(name="**Users Status Is:**", value="{}".format(user.status), inline=False)
    embed.add_field(name="**Users Game Is:**", value="{}".format(user.game), inline=False)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def avatar(ctx, user: discord.Member = None):
    if user is None:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! Please specify a user you want me to avatar!', inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name='Robo!', value='**{}s** avatar'.format(user.name), inline=True)
        embed.set_image(url=user.avatar_url)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(color=0xff0179)
    embed.set_author(name='Mr. Robot Help!')
    embed.add_field(name=':lock_with_ink_pen: | Moderation :', value='``Kick``,``Ban``,``Clear``,``Mute``,``Unmute``,``Nick``', inline=True)
    embed.add_field(name=':tada: | Utility & Fun :', value='``Roast``,``Gay``,``Avatar``,``Roast``,``Invite``,``Info``,``Botinfo``,``Serverinfo``,``Die``,``Remind``', inline=False)
    embed.add_field(name=':timer: | Time & Pinging :', value='``Ping``,``Timer``', inline=True)
    embed.add_field(name=':thinking: | Math & Calculations :', value='``Add``,``Sub``,``Mul``,``Div``', inline=False)
    embed.add_field(name=':warning: | Administration :', value='``Welcome Message``,``Remindsetup``', inline=True)
    embed.add_field(name=':open_mouth: | Help Server :', value='**__https://discord.gg/Y5FkGb__**', inline=False)
    embed.add_field(name=':interrobang: | Upcoming Projects :', value='``Gooder Bot``,``Intersteller Bot``', inline=True)
    embed.add_field(name=':bust_in_silhouette: | Upcoming Description :', value='**Intersteller** Bot will be a galaxy bot! With Moderation and more! **Gooder** Bot will be a moderation bot you can invite!', inline=False)
    embed.set_footer(text='Reminder: All commands need to be lower case!')
    await client.send_message(author, embed=embed)
    embed = discord.Embed(color=0x36393E)
    embed.add_field(name='We have sent you a message!', value='You have got mail!', inline=False)
    await client.say(embed=embed)

@client.command()
async def web():
    embed = discord.Embed(color)
    embed.add_field(name='Veiw My bots website now!', value='There is a desription and everything!'. inline=False)
    embed.title = '**__Robot Website!__**'
    embed.url = 'https://gsavage664.wixsite.com/robot'
    await client.say(embed=embed)
    
    

@client.command(pass_context=True)
async def gay(ctx, user: discord.Member = None):
    if user is None:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the user you want me to rate them 1 - 100 of gayness!', inline=False)
        embed.set_footer(text='You are gay af!')
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x36393E)
        responses = [
            '{} Is 1% Gay  '.format(user.name),
            '{} Is 2% Gay  '.format(user.name),
            '{} Is 3% Gay  '.format(user.name),
            '{} Is 4% Gay  '.format(user.name),
            '{} Is 5% Gay  '.format(user.name),
            '{} Is 6% Gay  '.format(user.name),
            '{} Is 7% Gay  '.format(user.name),
            '{} Is 8% Gay '.format(user.name),
            '{} Is 9% Gay  '.format(user.name),
            '{} Is 10% Gay  '.format(user.name),
            '{} Is 11% Gay '.format(user.name),
            '{} Is 12% Gay  '.format(user.name),
            '{} Is 13% Gay  '.format(user.name),
            '{} Is 14% Gay  '.format(user.name),
            '{} Is 15% Gay  '.format(user.name),
            '{} Is 16% Gay '.format(user.name),
            '{} Is 17% Gay  '.format(user.name),
            '{} Is 18% Gay  '.format(user.name),
            '{} Is 19% Gay '.format(user.name),
            '{} Is 20% Gay '.format(user.name),
            '{} Is 21% Gay  '.format(user.name),
            '{} Is 22% Gay  '.format(user.name),
            '{} Is 23% Gay  '.format(user.name),
            '{} Is 24% Gay '.format(user.name),
            '{} Is 25% Gay  '.format(user.name),
            '{} Is 26% Gay  '.format(user.name),
            '{} Is 27% Gay  '.format(user.name),
            '{} Is 28% Gay '.format(user.name),
            '{} Is 29% Gay  '.format(user.name),
            '{} Is 30% Gay  '.format(user.name),
            '{} Is 31% Gay  '.format(user.name),
            '{} Is 32% Gay  '.format(user.name),
            '{} Is 33% Gay  '.format(user.name),
            '{} Is 34% Gay  '.format(user.name),
            '{} Is 35% Gay '.format(user.name),
            '{} Is 36% Gay  '.format(user.name),
            '{} Is 37% Gay  '.format(user.name),
            '{} Is 38% Gay '.format(user.name),
            '{} Is 39% Gay  '.format(user.name),
            '{} Is 40% Gay  '.format(user.name),
            '{} Is 41% Gay  '.format(user.name),
            '{} Is 42% Gay  '.format(user.name),
            '{} Is 43% Gay '.format(user.name),
            '{} Is 44% Gay  '.format(user.name),
            '{} Is 45% Gay  '.format(user.name),
            '{} Is 46% Gay  '.format(user.name),
            '{} Is 47% Gay '.format(user.name),
            '{} Is 48% Gay '.format(user.name),
            '{} Is 49% Gay '.format(user.name),
            '{} Is 50% Gay  '.format(user.name),
            '{} Is 51% Gay  '.format(user.name),
            '{} Is 52% Gay  '.format(user.name),
            '{} Is 53% Gay  '.format(user.name),
            '{} Is 54% Gay  '.format(user.name),
            '{} Is 55% Gay  '.format(user.name),
            '{} Is 56% Gay  '.format(user.name),
            '{} Is 57% Gay '.format(user.name),
            '{} Is 58% Gay '.format(user.name),
            '{} Is 59% Gay '.format(user.name),
            '{} Is 60% Gay '.format(user.name),
            '{} Is 61% Gay '.format(user.name),
            '{} Is 62% Gay '.format(user.name),
            '{} Is 63% Gay '.format(user.name),
            '{} Is 64% Gay '.format(user.name),
            '{} Is 65% Gay '.format(user.name),
            '{} Is 66% Gay '.format(user.name),
            '{} Is 67% Gay '.format(user.name),
            '{} Is 68% Gay '.format(user.name),
            '{} Is 69% Gay '.format(user.name),
            '{} Is 70% Gay '.format(user.name),
            '{} Is 71% Gay '.format(user.name),
            '{} Is 72% Gay '.format(user.name),
            '{} Is 73% Gay '.format(user.name),
            '{} Is 74% Gay '.format(user.name),
            '{} Is 75% Gay '.format(user.name),
            '{} Is 76% Gay '.format(user.name),
            '{} Is 77% Gay '.format(user.name),
            '{} Is 78% Gay '.format(user.name),
            '{} Is 79% Gay '.format(user.name),
            '{} Is 80% Gay '.format(user.name),
            '{} Is 81% Gay '.format(user.name),
            '{} Is 82% Gay '.format(user.name),
            '{} Is 83% Gay '.format(user.name),
            '{} Is 84% Gay '.format(user.name),
            '{} Is 85% Gay '.format(user.name),
            '{} Is 86% Gay '.format(user.name),
            '{} Is 87% Gay '.format(user.name),
            '{} Is 88% Gay '.format(user.name),
            '{} Is 89% Gay '.format(user.name),
            '{} Is 90% Gay '.format(user.name),
            '{} Is 91% Gay '.format(user.name),
            '{} Is 92% Gay '.format(user.name),
            '{} Is 93% Gay '.format(user.name),
            '{} Is 94% Gay '.format(user.name),
            '{} Is 95% Gay '.format(user.name),
            '{} Is 96% Gay '.format(user.name),
            '{} Is 97% Gay '.format(user.name),
            '{} Is 98% Gay '.format(user.name),
            '{} Is 99% Gay '.format(user.name),
            '{} Is 100% Gay '.format(user.name),
        
        
            ]
        embed.set_author(name=(random.choice(responses)))
        embed.set_image(url=user.avatar_url)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def die(ctx, *,reason=None):
    author = ctx.message.author
    if reason is None:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the reason you want to die!', inline=False)
        embed.set_footer(text='You are dead!')
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name='**{}** has died :sob:'.format(author.name), value='The reason was because: {}'.format(reason), inline=False)
        embed.set_thumbnail(url=author.avatar_url)
        await client.say(embed=embed)
    
@client.command(pass_context=True)
async def remind(ctx, *, remind):
    if remind is None:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the remind you want me to set!', inline=False)
        embed.set_footer(text='You are dead!')
        await client.say(embed=embed)
    else:
        server = ctx.message.server
        channel = discord.utils.get(server.channels, name='reminders') 
        author = ctx.message.author
        embed = discord.Embed(color=0x36393E)
        embed.set_author(name='Reminder')
        embed.add_field(name='By:', value="{0}".format(author.mention), inline=False)
        embed.add_field(name="Reminder: ", value="{0}".format(remind), inline=False)
        await client.send_message(channel, embed=embed)
        #Space Lol
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name='**{}** Reminer:'.format(author.name), value='Go to the channel that you have sent the reminder to!', inline=False)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def remindsetup(ctx):
    if ctx.message.author.server_permissions.manage_channels:
        server = ctx.message.server
        await client.create_channel(server=server, name="Reminders")
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name='Remind setup', value='I have setup a remind channel. ``Please fix the permission for the channel.``', inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Manage Channels``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def coinflip(ctx):
    author = ctx.message.author
    embed = discord.Embed(color=0x36393E)
    choices = [
        '{} You have lost because you picked **Heads**'.format(author.name),
        '{} You won because you picked **Tails**'.format(author.name),
        '{} You have lost because you picked **Tails**'.format(author.name),
        '{} You have won because you picked **Heads**'.format(author.name),
    ]
    embed.add_field(name='Coin-Flip - Command', value=(random.choice(choices)), inline=False)
    await client.say(embed=embed)
    
@client.command(pass_context=True)
async def roast(ctx, user: discord.Member = None):
    embed = discord.Embed(color=0x36393E)
    roast = [
        'Is your ass jealous of the amount of shit that just came out of your mouth?',
        'YO MAMAS so FAT When She asked for a water bed they put a blanket over the ocean!',
        'Were u born on a highway? Cause thats where most accidents happen',
        'If u Ran like your mouth u will be in good shape',
    ]
    embed.add_field(name='Roasted!', value=(random.choice(roast)), inline=False)
    await client.say(embed=embed)
    
 
client.run('NDg4ODMxMzQyMjQzNzQxNzQ2.Dnh7Qw.4HYkq3P_lQTQqLTIriCkxhQWb2s')

