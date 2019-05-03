import os
import requests
import json
import time

config = json.load(open("data/config.json", "r"))

url = f"https://discordapp.com/api/v6/channels/{config['channel_id']}/messages"

header = {
    "authorization": config["token"],
    "Content-Type": "application/json"
}


def send_message(message):
    """
    Sends a message to discord

    returns request data
    """
    return requests.post(url, data=json.dumps({"content": message}), headers=header)


def download_image(url, path):
    """
    Downloads an image from a url

    returns the path
    """
    img = requests.get(url)

    with open(path, "wb") as f:
        f.write(img.content)
        f.close()

        return f.name


def load_pokedex():
    """Converts .json file to dictionary"""
    return json.load(open("data/pokedex.json", "r"))


def update_pokedex(data):
    """Saves to .json file"""
    with open("data/pokedex.json", "w") as f:
        json.dump(data, f)
        f.close()

if __name__ == "__main__":
    while True:
        send_message("yo gabba gabba hiteth on that DAbBa!!")
        time.sleep(0.85)
