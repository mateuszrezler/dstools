from keras.preprocessing.image import load_img
from numpy.random import randint
from urllib.request import urlretrieve


def load_random_images(amount=10, length=360, width=360):

    """Load random images from `https://picsum.photos/` website"""

    images = []

    for image in range(amount):
        image_nr = randint(1, 1084+1)
        url = f'https://i.picsum.photos/id/{image_nr}/{length}/{width}.jpg'
        urlretrieve(url, f'{image_nr}.jpg')
        images.append(load_img(f'{image_nr}.jpg'))

    return images

