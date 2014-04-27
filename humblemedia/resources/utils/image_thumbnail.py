import os

from django.conf import settings
from PIL import Image, ImageEnhance


def reduce_opacity(im, opacity):
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im


def watermark(im, mark, position, opacity=1):
    if opacity < 1:
        mark = reduce_opacity(mark, opacity)
    if im.mode != 'RGBA':
        im = im.convert('RGBA')

    layer = Image.new('RGBA', im.size, (0,0,0,0))
    if position == 'tile':
        for y in range(0, im.size[1], mark.size[1]):
            for x in range(0, im.size[0], mark.size[0]):
                layer.paste(mark, (x, y))

    return Image.composite(layer, im, layer)


def get_image_thumbnail(input_file, output_file, size):
    import ipdb; ipdb.set_trace()
    image = Image.open(input_file)
    image.thumbnail(size)
    mark = Image.open(os.path.join(settings.STATIC_ROOT, 'images/watermark.png'))
    image = watermark(image, mark, 'tile', 0.5)
    image.save(output_file, 'JPEG')

    return True
