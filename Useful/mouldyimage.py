from PIL import Image
import numpy as np
import cv2

img = Image.open('filename.jpg') #add ur own filename

if img.mode != 'RGB':
    img = img.convert('RGB')

for i in range(100):
    img.save('temp.jpg', 'JPEG', quality=10) #quality is on a scale from 1 (worst) to 95 (best)
    img = Image.open('temp.jpg')
    smaller = img.resize((int(img.width / 2), int(img.height / 2)), Image.BICUBIC)
    img = smaller.resize(img.size, Image.BICUBIC)
    img_array = np.array(img)
    yuv = cv2.cvtColor(img_array, cv2.COLOR_RGB2YUV)
    img_array = cv2.cvtColor(yuv, cv2.COLOR_YUV2RGB)
    img = Image.fromarray(img_array)

img.save('blud.jpg')
