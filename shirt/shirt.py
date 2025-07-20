from sys import argv
from sys import exit
import os
from PIL import Image, ImageOps

def main():
    try:


        dude_perfect = Image.open(argv[1]).convert("RGB")

        overlay = Image.open('shirt.png').convert("RGBA")


        size = overlay.size

        dude_perfect = ImageOps.fit(dude_perfect, size)
        dude_perfect.paste(overlay, overlay)

        dude_perfect.save(f"/workspaces/194432821/Problem_sets/shirt/{argv[2]}")
    except FileNotFoundError:
        exit("Input does not exist")



def check_extension():
    thing, exten = argv[1].split(".")
    name2, type2 = argv[2].split(".")
    possible = ["jpg","jpeg","png"]
    if exten and type2 not in ["jpg","jpeg","png"]:
        exit("Invalid output")

    if exten != type2:
        exit("Input and output have different extensions")




if len(argv) > 3:
    exit("Too many command-line arguments")
elif len(argv) < 3:
    exit("Too few command-line arguments")
check_extension()

main()
