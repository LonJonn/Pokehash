import sys

import discord
import chalk

import pokehash
import utils

client = discord.Client()

if "-h" in sys.argv:
    helper_mode = True
    print(chalk.Chalk("cyan")("Running in helper mode.", bold=True))


@client.event
async def on_ready():
    print("Gonna catch 'em all!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == 365975655608745985 and message.embeds:
        embed = message.embeds[0]
        if embed.description.startswith("Guess"):
            found = pokehash.find_pokemon(embed.image.url, is_url=True)
            if helper_mode:
                await message.channel.send("It's a " + found[:3] + "...!")
            else:
                utils.send_message("p!catch " + found)
                utils.send_message("p!info latest")

if __name__ == "__main__":
    client.run("NTcxOTgyMjIwMTY0ODU3ODU2.XMVqSg._6yO9G6PNdRoCqnNVDDQOnvzKMU")
