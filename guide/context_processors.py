from django.conf import settings  # import the settings file


def image_url(request):
    # Allow access to the image_url setting.
    return {'IMAGE_URL': settings.IMAGE_URL}
