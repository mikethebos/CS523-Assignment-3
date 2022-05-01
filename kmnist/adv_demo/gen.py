import os
from PIL import Image
import random

random.seed()

imgs = []
path_dirs = []
for i in range(10):
    path_dirs.append(["fashion-mnist_png/data/train/" + str(i) + "/", "fashion-mnist_png/data/test/" + str(i) + "/"])

for num in path_dirs:
    l = []
    for p in num:
        for p2 in os.listdir(p):
            if p2.endswith(".png"):
                l.append(os.path.join(p, p2))
    random.shuffle(l)
    l = l[:20]
    l = [Image.open(x) for x in l]
    imgs.append(l)

new_img = Image.new('RGB', (560,280))

x = 0
y = 0
for num in imgs:
    for i in num:
        new_img.paste(i, (x, y))
        x += 28
    x = 0
    y += 28

new_img.save("composite.png")
