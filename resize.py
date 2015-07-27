from PIL import Image

def resize_and_save(filename,size):
    im = Image.open(filename)
    new_im = im.resize(size)

    name_parts = filename.split(".")
    new_im.save(name_parts[0] + "_resized." + name_parts[1])

filename = raw_input("What file to change? ")
width = int(raw_input("What is new width? "))
height = int(raw_input("What is new height? "))


resize_and_save(filename,(width,height))
