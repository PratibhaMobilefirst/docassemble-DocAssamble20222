import stripe
from docassemble.base.util import get_config

def check_coupon(coupon_code):
  stripe.api_key = get_config('stripe tsecret key')
  coupon = stripe.Coupon.retrieve(coupon_code)
  if coupon:
    return True
  else:
    return False