from PIL import Image
import imagehash

import sys
import os

import utils

pokedex = utils.load_pokedex()


def download_pokedex_images():
    """Downloads all pokemon images from assets.pokemon.com"""
    for pokemon in pokedex:
        utils.download_image(
            f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{pokemon['id']}.png",
            f"data/images/{pokemon['id']}.png")


def calculate_hashes():
    """calculates the dhashes for each pokemon image and stores them in pokedex.json"""
    for pokemon in pokedex:
        hash = imagehash.dhash(
            Image.open(f"data/images/{pokemon['id']}.png"))
        pokemon["hash"] = str(hash)

    utils.update_pokedex(pokedex)


def find_pokemon(img):
    """Returns the name of the pokemon from the local image"""
    search_hash = str(imagehash.dhash(Image.open(img)))
    os.remove(img)
    for pokemon in pokedex:
        if search_hash == pokemon["hash"]:
            return pokemon["name"]


def find_pokemon_remote(link):
    """Returns the name of the pokemon from the remote image"""
    img = utils.download_image(link, "data/temp.png")
    return find_pokemon(img)


def catch(img):
    """Catches a Pokemon"""
    if "https" in img:
        found = find_pokemon_remote(img)
    else:
        found = find_pokemon(img)

    print("Catching: " + found)
    utils.send_message("p!catch " + found)
    utils.send_message("p!info latest")


if __name__ == "__main__":
    catch(sys.argv[1])
