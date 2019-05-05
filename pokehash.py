import os
import sys

import chalk
import imagehash
from PIL import Image

import utils

pokedex = utils.load_pokedex()


def download_pokedex_images() -> None:
    """Downloads all pokemon images from assets.pokemon.com"""
    for pokemon in pokedex:
        utils.download_image(
            f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{pokemon['id']}.png",
            f"data/images/{pokemon['id']}.png")


def calculate_hashes() -> None:
    """calculates the dhashes for each pokemon image and stores them in pokedex.json"""
    for pokemon in pokedex:
        hash = imagehash.phash(
            Image.open(f"data/images/{pokemon['id']}.png"))
        pokemon["hash"] = str(hash)
        print(chalk.Chalk("green")(
            pokemon["name"] + "\t=> " + pokemon["hash"]))

    utils.update_pokedex(pokedex)


def find_pokemon(img: str, is_url: bool = False) -> str:
    """Returns the name of the pokemon from an image"""
    if is_url:
        img = utils.download_image(img, "data/temp.png", silent=True)

    search_hash = str(imagehash.phash(Image.open(img)))
    os.remove(img)

    for pokemon in pokedex:
        if search_hash == pokemon["hash"]:
            return pokemon["name"]


if __name__ == "__main__":
    found = find_pokemon(sys.argv[1])
    if found:
        utils.send_message("p!catch " + found)
        utils.send_message("p!info latest")
    else:
        print(chalk.Chalk("red")("Unable to find pokemon."))
