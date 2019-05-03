import discord
import pokehash


client = discord.Client()


@client.event
async def on_ready():
    print("Gonna catch 'em all!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == 365975655608745985:
        if message.embeds:
            embed = message.embeds[0]
            if embed.description.startswith("Guess"):
                pokehash.catch(embed.image.url)
                # await message.channel.send("It's a " + found[:3] + "...!")

if __name__ == "__main__":
    client.run("NTcxOTgyMjIwMTY0ODU3ODU2.XMVqSg._6yO9G6PNdRoCqnNVDDQOnvzKMU")
