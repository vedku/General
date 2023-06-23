from PIL import Image

with Image.open('filename.jpg') as img:
    for i in range(100):
        img.save('temp.jpg', 'JPEG', quality=1) #quality is on a scale from 1 (worst) to 95 (best)
        img = Image.open('temp.jpg')
    img.save('mould.jpg')
