import sys
import os
from PIL import Image

try:
    location = sys.argv[1]
    destination = sys.argv[2]

    print(location)
    print(destination)

    if not os.path.isdir(location): 
        print('location does not exist')

    os.makedirs(destination, exist_ok=True)

    images = os.listdir(location)
    for img in images:
        image = Image.open(os.path.join(location,img))
        print(image)
        image.save(os.path.join(destination, f'{os.path.splitext(img)[0]}.png'), 'png')
except IndexError:
    print("incomplete args")
