import stripe
from docassemble.base.util import get_config

stripe.api_key = get_config('stripe tsecret key')

def retrieve_product_price():
    product = stripe.Price.retrieve("price_1MWBmvBOgpkiH8jqnVQx2KQH")
    return product.unit_amount / 100  