from django import template

register = template.Library()


@register.filter
def startswith(text, starts):
    """
    Returns True if text starts with 'starts'
    """
    if not text or not starts:
        return False
    return text.startswith(starts)
