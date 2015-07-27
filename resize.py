from PIL import Image

def resize_and_save(filename,size):
    im = Image.open(filename)
    new_im = im.resize(size)

    name_parts = filename.split(".")
    new_im.save(name_parts[0] + "_resized." + name_parts[1])

filename = raw_input("What file to change? ")
print "How would you like to resize?"
print "1) Fixed size"
print "2) Change to a %"
print "3) your text here"
choice = raw_input("")
if (choice == "1"):
    width = int(raw_input("What is new width? "))
    height = int(raw_input("What is new height? "))
    resize_and_save(filename,(width,height))
elif (choice == "2"):
    im = Image.open(filename)
    old_size = im.size
    percent = raw_input("What % to scale to? ")
    if (percent[-1] == "%"):
        percent = percent[0:-1]
    scale = int(percent)/100.0
    new_width = int(old_size[0] * scale)
    new_height = int(old_size[1] * scale)
    new_size = (new_width,new_height)
    # calculate the new size
    resize_and_save(filename, new_size)
elif (choice == "3"):
    # get old size
    # get longer edge
    # calculate scale = target/original
    # calculate new size
    # call resize and save
