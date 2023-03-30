import numpy as np
from PIL import Image

class txt_to_video:
    def __init__(self, path_to_image):
        self.imageList = []
        self.frames = []
        self.path_to_image = path_to_image
        self.input_image = Image.open(path_to_image)
        self.width, self.height = self.input_image.size
        
    def read(self, path_to_txt):
        txt = open(path_to_txt, "r")
        seq = []
        for char in txt.read():
            if len(seq) == self.width * self.height:
                self.imageList.append(ord(char))
                seq = []
            seq.append(ord(char))
            
            
        if len(seq) > 0:
            while len(seq) != self.width * self.height:
                seq.append(1)
            
            self.imageList.append(seq)  
    
    def create_frames(self):
        cnt = 0
        for frame in self.imageList:
            input_image = Image.open(self.path_to_image)
            pixel_map = input_image.load()
            
            row, col = 0, 0
            for i in range(len(frame)):
                pixel_map[row, col] = (frame[i])
                col += 1
                if col == self.width :
                    row += 1
                    col = 0
                    
            path = "./images/frame" + str(cnt) + ".png"
            input_image.save(path, format="png")
            self.frames.append(np.asarray(input_image))
            cnt += 1
            
    def print_frames(self):
        print(self.frames[0])
        
    def image_to_text(self, frame):
        width, height = len(frame), len(frame[0])
        text = ""
        for i in range(width):
            for j in range(height):
                val = frame[j][i]
                if val == 1:
                    break
                text += chr(val)
                
        return text
    
    def call(self):
        print(self.image_to_text(self.frames[0]))
        
if  __name__ == "__main__":
    obj = txt_to_video("256_256.jpg")
    obj.read("text.txt")
    obj.create_frames()
    obj.print_frames()
    print(obj.call())
    