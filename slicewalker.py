import argparse
from PIL import Image
import board
import neopixel
from time import sleep

# Parse those command line args
parser = argparse.ArgumentParser()
parser.add_argument('--pin', '-p' )
parser.add_argument('--length', '-l')
parser.add_argument('--image', '-i', )
args = parser.parse_args()

# Pull in the image once and read it into a list of RGB tuples
def process_image(image):
    strips = []
    with Image.open('images/attachment-3.jpeg').convert("RGB") as im:
        im_length = im.getbbox()[2]
        for i in range(im_length):
            pixels = []
            for j in range(60):
                pixels.append(im.getpixel((i,j)))
            strips.append(pixels)
    return strips

def write_strips(data):
    strip = neopixel.NeoPixel(board.D18, 60)
    strip = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            strip[j] = data[i][j]
        # print(strip)
        strip.show()
        # pass
        sleep(2)

if __name__ == '__main__':
    strips = process_image(args.image)
    # print(strips)
    print(len(strips))
    write_strips(strips)
