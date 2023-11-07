import re
from rest_framework.serializers import ValidationError


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        youtube_url_pattern = r'https://www.youtube.com'
        tmp_val = dict(value).get(self.field)
        if not tmp_val.startswith(youtube_url_pattern):
            raise ValidationError(f'{tmp_val} is not youtube url')
