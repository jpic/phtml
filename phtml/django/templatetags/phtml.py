from django.utils.safestring import mark_safe
from django.template import Library

register = Library()


@register.filter
def render_form(form, request=None):
    return mark_safe(form._phtml.jinja.clone(form=form, request=request))
