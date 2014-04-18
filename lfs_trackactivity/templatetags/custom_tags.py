from django.template import Library
from lfs.page.models import Page

register = Library()

@register.inclusion_tag('adform.html', takes_context=True)
def adform(context):
    # TODO: to be finished
    from lfs.caching.utils import lfs_get_object_or_404
    page = lfs_get_object_or_404(Page)
    if page and page.active:
    return {
            "page": page,
           }

