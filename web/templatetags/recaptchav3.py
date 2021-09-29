from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag("recaptcha/recaptchav3.html")
def recaptchav3_token(action=None):
    return {"recaptcha_site_key": settings.RECAPTCHA_SITE_KEY, "action": action}
