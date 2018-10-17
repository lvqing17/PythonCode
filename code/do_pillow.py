from PIL import Image, ImageDraw, ImageColor, ImageFilter
from PIL import ImageFont
import random

#im = Image.open('./tutu/妈妈.jpeg')

#w, h = im.size
#print('Original image size: %sx%s' % (w, h))

#im.thumbnail((w//2, h//2))
#print('Resize image to: %sx%s' % (w//2, h//2))

#im.save('./tutu/thumbnail.jpg', 'jpeg')

#im2 = im.filter(ImageFilter.BLUR)
#im2.save('./tutu/blur.jpg','jpeg')

#def rndChar():
#    return chr(random.randint(65, 90))

def rndColor(): 
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

#width = 60 * 4
#height = 60
#image = Image.new('RGB', (width, height), (255, 255, 255))

im = Image.open('./tutu/妈妈.jpeg')

font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 36)

draw = ImageDraw.Draw(im)

# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
texts = "王wangjiacun"
for t in range(len(texts)):
    draw.text((10,60 * t + 10),texts[t], font=font, fill=rndColor2())

# image = im.filter(ImageFilter.BLUR)
im.save('./tutu/code.jpg', 'jpeg')