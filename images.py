from keras.preprocessing.image import load_img
from numpy.random import randint
from urllib.error import HTTPError
from urllib.request import urlretrieve


def load_random_images(amount=10, length=360, width=360,
                       last_image_number=1084):
    """Load random images from `https://picsum.photos/` website"""
    images = []
    while len(images) < amount:
        image_number = randint(1, last_image_number+1)
        url = f'https://i.picsum.photos/id/{image_number}/{length}/{width}.jpg'
        try:
            urlretrieve(url, f'{image_number}.jpg')
            images.append(load_img(f'{image_number}.jpg'))
        except HTTPError:
            pass
    return images

