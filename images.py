from keras.preprocessing.image import load_img
from matplotlib.pyplot import axis, figure, imshow, show, subplot
from numpy.random import randint
from urllib.error import HTTPError
from urllib.request import urlretrieve


def display_grid_of_images(list_of_images, columns=2, size=1):
    """Display PIL images as subplots in a grid of a given number of columns"""
    for index, image in enumerate(list_of_images):
        if index % columns == 0:
            figure(figsize=(6.4*size, 4.8*size))
        subplot(1, columns, index % columns+1)
        axis('off')
        imshow(image)
    show()


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

