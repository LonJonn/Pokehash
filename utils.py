import json
import os
import time

import chalk
import requests

config = json.load(open("data/config.json"))

url = f"https://discordapp.com/api/v6/channels/{config['channel_id']}/messages"

header = {
    "authorization": config["token"],
    "Content-Type": "application/json"
}


def send_message(message: str) -> requests.Response:
    """
    Sends a message to discord

    returns request data
    """
    return requests.post(url, data=json.dumps({"content": message}), headers=header)


def download_image(url: str, path: str, silent: bool = False) -> str:
    """
    Downloads an image from a url

    returns the file path
    """
    try:
        res = requests.get(url)
    except:
        print(chalk.Chalk("red")("Failed to download image.", bold=True))
        return

    if "image" not in res.headers.get("content-type"):
        print(chalk.Chalk("yellow")("URL is not an image. Skipping.", bold=True))
        return

    with open(path, "wb") as f:
        f.write(res.content)
        if not silent:
            print(chalk.Chalk("green")(
                "Image download finished: " + f.name, bold=True))

        f.close()

        return f.name


def load_pokedex() -> dict:
    """Converts data/pokedex.json to dictionary"""
    try:
        pokedex = json.load(open("data/pokedex.json"))
        print(chalk.Chalk("cyan")("Pokedex loaded.", bold=True))
        return pokedex
    except:
        print(chalk.Chalk("red")(
            "Failed to load pokedex. Maybe it doesn't exist?.", bold=True))


def update_pokedex(data: dict) -> None:
    """Saves to .json file"""
    with open("data/pokedex.json", "w") as f:
        json.dump(data, f)
        print(chalk.Chalk("cyan")("Pokedex updated.", bold=True))
        f.close()


if __name__ == "__main__":
    while True:
        send_message("yo gabba gabba hiteth on that DAbBa!!")
        time.sleep(0.85)
