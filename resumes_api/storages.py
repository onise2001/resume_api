from django.conf import settings
from whitenoise.storage import CompressedManifestStaticFilesStorage

class WhiteNoiseMediaStorage(CompressedManifestStaticFilesStorage):
    location = settings.MEDIA_ROOT
    base_url = settings.MEDIA_URL