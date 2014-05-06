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
def adform_product_page(context, product):
    # TODO: to be finished
    ADFORM_PM = getattr(settings, 'ADFORM_PM', '')
    ADFORM_ID = getattr(settings, 'ADFORM_ID', '')

    if product.is_variant:
        product_name = product.get_default_variant().get_name
        product_id = product.get_default_variant().sku.split(' ')[0]
    else:
        product_name = product.get_name
        product_id = product.sku.split(' ')[0]

    parent_name = product.get_category().name
    return {
            "product_name": product_name,
            "product_id": product_id,
            "parent_name": parent_name,
            "adform_pm": ADFORM_PM,
            "adform_id": ADFORM_ID,
           }

@register.inclusion_tag('adform_cart.html', takes_context=True)
def adform_cart(context, price, items):
    # TODO: to be finished
    ADFORM_PM = getattr(settings, 'ADFORM_PM', '')
    ADFORM_ID = getattr(settings, 'ADFORM_ID', '')

    sales = str(price).replace(',','.') 
    basketsize = 0
    products = []

    for cart_item in items:
        products.append({
            'productname': cart_item['product'].get_name().encode("utf-8"),
            'productid': cart_item['product'].sku.encode("utf-8"),
            'categoryname': cart_item['product'].get_category().name.encode("utf-8"),
            'productsales': cart_item['product_price_gross'],
            'productcount': cart_item['quantity'],
            'step': '2'
        })
        basketsize += cart_item['quantity']
    
    #toglo gli apici per passare al js un dizionario pulito
    #products = str(products).replace("'","")

    return {
            "sales": sales,
            "products": products,
            "basketsize": basketsize,
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
def adform_thankyou(context, order):
    # TODO: to be finished
    ADFORM_PM = getattr(settings, 'ADFORM_PM', '')
    ADFORM_ID = getattr(settings, 'ADFORM_ID', '')

    sales = str(order.price).replace(',','.')
    basketsize = 0
    items = order.items.values()
    order_id = order.number

    products = []
    for item in items:
        products.append({
            'productname': item['product_name'].encode("utf-8"),
            'productid': item['product_sku'].encode("utf-8"),
            'categoryname': '',
            'productsales': item['product_price_gross'],
            'productcount': item['product_amount'],
            'step': '3'
        })
        basketsize += item['product_amount']

    #toglo gli apici per passare al js un dizionario pulito
    #products = str(products).replace("'","")

    return {
            "order_id": order_id,
            "basketsize": basketsize,
            "products": products,
            "sales": sales,
            "adform_pm": ADFORM_PM,
            "adform_id": ADFORM_ID,
           }

