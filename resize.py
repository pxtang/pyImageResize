from PIL import Image
import glob, os

def safe_open(filename):
    try:
        im = Image.open(filename)
        return im
    except IOError:
        print "File not found: %s" % filename
        return False

def resize_and_save(filename,size):
    im = safe_open(filename)
    if (im == False):
        return 0
    new_im = im.resize(size)

    name_parts = filename.split(".")
    new_im.save(name_parts[0] + "_resized." + name_parts[1])

def resize_scale(filename, scale):
    im = safe_open(filename)
    if (im == False):
        return 0
    old_size = im.size
    new_width = int(old_size[0] * scale)
    new_height = int(old_size[1] * scale)
    new_size = (new_width,new_height)

    # calculate the new size
    resize_and_save(filename, new_size)

def task_done(filename):
    print "%s was resized" % (filename)

def main():
    filename = raw_input("What file to change? ")
    batch = False
    if (filename[0] == "*"):
        batch = True
    print "How would you like to resize?"
    print "1) Fixed size\n2) Change to a %\n3) your text here"
    choice = raw_input("")
    if (choice == "1"):
        while(True):
            width = int(raw_input("What is new width? "))
            if (width > 0):
                break # continue to rest of code
            print "You gave me an invalid number"
        height = int(raw_input("What is new height? "))
        if (batch):
            for infile in glob.glob(filename):
                resize_and_save(infile,(width,height))
                task_done(infile)
        else:
            resize_and_save(filename,(width,height))
    elif (choice == "2"):
        percent = raw_input("What % to scale to? ")
        if (percent[-1] == "%"):
            percent = percent[0:-1]
        scale = int(percent)/100.0

        if (batch):
            for infile in glob.glob(filename):
                resize_scale(infile, scale)
                task_done(infile)
        else:
            resize_scale(filename, scale)
    elif (choice == "3"):
        long_edge = float(raw_input("What is longest edge? "))
        if (batch):
            for infile in glob.glob(filename):
                im = safe_open(infile)
                if (im == False):
                    continue
                old_size = im.size
                original = max(old_size[0],old_size[1])
                scale = long_edge/original
                resize_scale(infile, scale)
        else:
            im = safe_open(filename)
            if (im == False):
                return 0
            old_size = im.size
            original = max(old_size[0],old_size[1])
            scale = long_edge/original
            resize_scale(filename, scale)

if __name__ == '__main__':
    main()
