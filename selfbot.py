import sys, os
import random, asyncio
from datetime import datetime, timedelta

import discord
from discord.ext import commands



__name__ = "Pineapple Cookie"
__version__ = "1.1.373"

# Selfbot's DISCORD TOKEN
SELFBOT_TOKEN = ""
# Guild ID where selfbot works
GUILD_ID = 549251000167301120
# Channel ID in the Guild where selfbot works
CHANNEL_ID = 788999750758039552

random.seed()

client = commands.Bot(cache_auth=False,command_prefix="...",help_command=None=)

BUY_CD = 4*60*60

contents = [
	"->loot",
	"->chop",
	"->mine",
	"->fish",
	"->equip comet axe",
	"->equip star axe",
	"->equip axe",
	"->equip comet pick",
	"->equip star pick",
	"->equip pick",
	"->equip comet rod",
	"->equip star rod",
	"->equip rod",

	# Optional for pet using
	# "->pet feed \"Steak\" full",
	# "->pet hydrate full",
	# "->pet clean",
	# "->pet pet"
]

crates = [
	"->opencrate Fish Treasure",
	"->opencrate Chop",
	"->opencrate Gem Crate",
	"->opencrate",
]

sell_list = [
	"->sell allof wood",
	"->sell allof apple",
	"->sell allof pear",
	"->sell allof crab",
	"->sell allof squid",
	"->sell allof fish",
	"->sell allof 📺",
	"->sell allof pizza",
	"->sell allof 📰",
	"->sell allof 👕",
	"->sell allof blowfish",
	"->sell allof 🐠",
	"->sell allof leaves",
	"->sell allof shrimp",
	"->sell allof 🌸",
	"->sell allof 🥛",
	"->sell allof 👗",
	"->sell allof 🌙",
	"->sell allof 💫",
]

mantaro_items_list = [
	"->buy 5 rod",
	"->buy 5 pickaxe",
	"->buy 5 axe",
	"->buy mop",
	"->daily",
	"->useitem mop"
]



@client.event
async def on_command_error(ctx, error):
	pass



async def buying():
	await client.wait_until_ready()

	t_now = datetime.utcnow()
	t_delay = BUY_CD - ((int(t_now.timestamp())) % BUY_CD)
	await asyncio.sleep(t_delay)

	while True:
		try:
			guild = client.get_guild(GUILD_ID)
			channel = guild.get_channel(CHANNEL_ID)
			random.shuffle(mantaro_items_list)
			for content in mantaro_items_list:
				await channel.send(content=content)
				await asyncio.sleep(random.uniform(1, 3))

			random.shuffle(sell_list)
			for content in sell_list:
				await channel.send(content=content)
				await asyncio.sleep(random.uniform(3, 5))


			await asyncio.sleep(BUY_CD)
		except Exception as e:
			print(e)
			await asyncio.sleep(60)

async def mantaro_farming():
	await client.wait_until_ready()

	while True:
		try:
			guild = client.get_guild(GUILD_ID)

			channel = guild.get_channel(CHANNEL_ID)

			random.shuffle(contents)

			for content in contents:
				await channel.send(content=content)
				await asyncio.sleep(random.uniform(1, 3))

			# Crates opening (Optional)
			await channel.send(content=random.choice(crates))

			await asyncio.sleep(5 * 60 + random.uniform(1, 60))
		except Exception as e:
			print(e)
			await asyncio.sleep(60)


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

	client.loop.create_task(buying())
	client.loop.create_task(mantaro_farming())



client.run(SELFBOT_TOKEN, bot=False)
