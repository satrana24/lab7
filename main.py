import PIL
from PIL import Image, ImageFilter


def first():
    with Image.open('cat.jpg') as img:
        img.load()

    img.show()

    size = img.size
    format = img.format
    color = img.mode

    print(f'''Размер изображения: {size}
Формат изображения: {format}
Тип цветовой модели: {color}''')


def second():
    name = 'cat.jpg'
    with Image.open(name) as img:
        img.load()

    img.show()

    second_image = img.resize((img.width // 4, img.height // 4))
    second_image.save('cat1.jpg')
    second_image.show()

    second_image = img.rotate(180)
    second_image.save('cat2.jpg')
    second_image.show()

    second_image = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    second_image.save('cat3.jpg')
    second_image.show()


def third():
    names = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

    for name in names:
        with Image.open(name) as img:
            img.load()
            new_img = img.filter(ImageFilter.FIND_EDGES)
            new_img.show()
