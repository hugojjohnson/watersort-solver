import PIL
from PIL import Image
img = Image.open('detectLines.png')
pix = img.load()
# print(pix[0,0])


threshold = 10


# for y in range(img.size[1]):
#     for x in range(img.size[0]):
#         r, g, b = pix[x,y]
#         pix[x, y] = (0, 0, 0)
#         if r > 100:
#             if pix[x-threshold, y-threshold][0] < 100 and pix[x+threshold, y+threshold][0] > 100:
#                 pix[x, y] = (255, 0, 0)
#             # print("whoop")
#             # print(f"{r}, {g}, {b}")
#         # pix[x,y] = (r, g, b)


y = 0
while y < img.size[1]:
    x = 0
    while x < img.size[0]:
        r, g, b = pix[x,y]
        pix[x, y] = (0, 0, 0)
        if r > 10:
            if pix[x-threshold, y-threshold][0] < 100 and pix[x+threshold, y+threshold][0] > 100:
                pix[x, y] = (255, 0, 0)
                for i in range(1, 16):
                    for j in range(1, 16):
                        pix[x + i, y+j] = (0, 0, 0)
                x += 15
        x += 1
    y += 1


img.save('lineCoords.png')