import argparse
from PIL import Image
import board
import neopixel


# Parse those command line args
parser = argparse.ArgumentParser()
parser.add_argument('--pin', '-p' )
parser.add_argument('--length', '-l')
parser.add_argument('--image', '-i', )
args = parser.parse_args()

# Pull in the image once and read it into a list of RGB tuples
def process_image(image):
    strips = []
    with Image.open('images/attachment-1.jpeg').convert("RGB") as im:
        im_length = im.getbbox()[3]
        for i in range(im_length):
            pixels = []
            for i in range(60):
                pixels.append(im.getpixel((0,i)))
            strips.append(pixels)
    return strips

def write_strips(data):
    strip = neopixel.NeoPixel(board.args.pin, args.length)
    for i in range(data.length()):
        strip[0:0] = i
        strip.show()

if __name__ == '__main__':
    strips = process_image(args.image)
    write_strips(strips)
