import PIL
from PIL import Image
img = Image.open('modified_lines.jpg')
pix = img.load()
# print(pix[0,0])


for y in range(img.size[1]):
    for x in range(img.size[0]):
        # r, g, b = pix[x,y]
        # # pix[x, y] = (0, 0, 0)
        # if r > 250:
        #     pix[x, y] = (0, 255, 0)
        #     print(r)
        if x%2 == 0 and y%2 == 0:
            pix[x, y] = (255, 0, 255)
        elif x%2 == 0:
            pix[x, y] = (0, 255, 0)
        elif y%2 == 0:
            pix[x, y] = (255, 0, 0)
        else: 
            pix[x, y] = (0, 0, 0)
        # pix[x, y] = (255, 0, 255)

img.save('modified_lines2.png')