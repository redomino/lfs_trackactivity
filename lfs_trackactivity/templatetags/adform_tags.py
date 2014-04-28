from django.template import Library
from lfs.page.models import Page
from django.conf import settings

register = Library()

@register.inclusion_tag('adform_master.html', takes_context=True)
def adform_master(context):
    # TODO: to be finished
    ADFORM_PM = getattr(settings, 'ADFORM_PM', '')
    ADFORM_ID = getattr(settings, 'ADFORM_ID', '')
    return {
            "adform_pm": ADFORM_PM,
            "adform_id": ADFORM_ID,
           }

@register.inclusion_tag('adform_product_page.html', takes_context=True)
def adform_product_page(context):
    # TODO: to be finished
    ADFORM_PM = getattr(settings, 'ADFORM_PM', '')
    ADFORM_ID = getattr(settings, 'ADFORM_ID', '')
    return {
            "adform_pm": ADFORM_PM,
            "adform_id": ADFORM_ID,
           }

@register.inclusion_tag('adform_cart.html', takes_context=True)
def adform_cart(context):
    # TODO: to be finished
    ADFORM_PM = getattr(settings, 'ADFORM_PM', '')
    ADFORM_ID = getattr(settings, 'ADFORM_ID', '')
    return {
            "adform_pm": ADFORM_PM,
            "adform_id": ADFORM_ID,
           }

@register.inclusion_tag('adform_checkout.html', takes_context=True)
def adform_checkout(context):
    # TODO: to be finished
    ADFORM_PM = getattr(settings, 'ADFORM_PM', '')
    ADFORM_ID = getattr(settings, 'ADFORM_ID', '')
    return {
            "adform_pm": ADFORM_PM,
            "adform_id": ADFORM_ID,
           }

@register.inclusion_tag('adform_thankyou.html', takes_context=True)
def adform_thankyou(context):
    # TODO: to be finished
    ADFORM_PM = getattr(settings, 'ADFORM_PM', '')
    ADFORM_ID = getattr(settings, 'ADFORM_ID', '')
    return {
            "adform_pm": ADFORM_PM,
            "adform_id": ADFORM_ID,
           }

