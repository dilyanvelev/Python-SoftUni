from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Ensure this value contains only letters.')


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError('Max file size is 5.00 MB')
# def validate_image_size(max_size_mb):
#
#
#     def validate(image):
#         if image.size > max_size_bytes:
#             raise ValidationError('Max file size is 5.00 MB')
#
#     return validate
