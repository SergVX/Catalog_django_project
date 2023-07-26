from django import template


register = template.Library()


@register.simple_tag
def upload_media(image):
    if image:
        return f'/media/{image}'

    return '/static/coming_soon.jpg'