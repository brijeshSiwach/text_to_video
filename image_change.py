import numpy as np
from PIL import Image

f = open("text.txt", "r")

imageList = []
seq = []
for char in f.read():
    if len(seq) == 256*256:
        imageList.append(seq)
        seq = []
    seq.append(int(ord(char)))

if len(seq) > 0:
    while len(seq) != 258*258:
        seq.append(1)
    imageList.append(seq)


# taking half of the width:
frames = []
for frame in imageList:
    input_image = Image.open("256_256.jpg")
    
    pixel_map = input_image.load()
    width, height = input_image.size
    print(width, height)
    row, col = 0, 0
    for i in range(len(frame)):
        pixel_map[row, col] = (frame[i])
        # print(row, col, pixel_map[row, col], end = " ")
        # print(frame[i], end = "\n")
        col += 1
        if col == 258:
            row += 1
            col = 0     
    # print("\n")
    input_image.save("./images/grayscale.png", format="png")
    frames.append(np.asarray(input_image)) 
    
print(frames[0])
# print(frames[0][256][253])

def image_to_text(image_array):
    width, height = len(image_array), len(image_array[0])
    text = ""
    for i in range(width):
        for j in range(height):
            val = image_array[j][i]
            if val == 1:
                break
            
            text += chr(val)
    print(text)

image_to_text(frames[0])
