# 3rd party packages
from easy_thumbnails.files import get_thumbnailer


image_types = [
    'jpg', 'jpeg',
    'png', 'JPG'
]


def thumbnail_files(image, width: int=None, height: int=None) -> str:
    img_type = image.name.split('.')[-1]
    if img_type not in image_types:
        return image.url
    if not width and not height:
        return image.url
    options = {'size': (width, height), 'crop': True}
    return get_thumbnailer(image).get_thumbnail(options).url