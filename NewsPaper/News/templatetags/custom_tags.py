from django import template


register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['requsts'].Get.copy()
    for k, v in kwargs.items():
        d[k] = v
        return d.urlencode()