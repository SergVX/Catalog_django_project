from django import template


register = template.Library()


@register.simple_tag
def mediapath_tag(image):
    if image:
        return f'/media/{image}'

    return '/static/coming_soon.jpg'