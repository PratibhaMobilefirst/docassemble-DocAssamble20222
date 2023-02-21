import requests
import sys
import time
import datetime
import stripe
from docassemble.base.util import get_config

stripe.api_key = get_config('stripe tsecret key')

def retrieve_product_price():
    product = stripe.Price.retrieve("price_1MWBmvBOgpkiH8jqnVQx2KQH")
    return product.unit_amount / 100 

def yml_veriables(cid):				
  Cid = cid
  if Cid.startswith( 'gclid' ) or Cid.startswith( 'graid' ) or Cid.startswith( 'wbraid' ):
    params = {
      'Google Click ID': ''.join(filter(lambda i: i.isdigit(), Cid)),
      'Conversion Name': "QDROgenerated",
      'Conversion Time': datetime.datetime.now() ,
      'Conversion Value': retrieve_product_price(),
      'Conversion Currency': 'USD',
      }
    response = requests.get('https://script.google.com/macros/s/AKfycbz4YKL3XeNCuQswv80VCuM-kLR-VDJuKP5Pj2psYBy97x09QG2pSG_SLA9Zmig-lcrH/exec?gid=0',params=params,)
    if response.status_code != 200:
      sys.exit(response.text)
      info = response.json()
    else:
      return ''

  elif Cid.startswith( 'msckld' ):						
    params = {
      'Microsoft Click ID': ''.join(filter(lambda i: i.isdigit(), Cid)),
      'Conversion Name': "QDROgenerated",
      'Conversion Time': datetime.datetime.now() ,
      'Adjustment Value': retrieve_product_price(),
      'Adjustment Currency': 'USD',
      'Adjustment Type': '',
      'Adjustment Time': datetime.datetime.now() ,
      }
    response = requests.get('https://script.google.com/macros/s/AKfycbzSkMLhY4XxoWlLGBa2cFiJFAsihpuQy5jzqaGq5wnwwLeZUIwG7Xi3hXvuky2y_uvuqg/exec?gid=0',params=params,)
    if response.status_code != 200:
      sys.exit(response.text)
      info = response.json()
    else:
      return ''
      
  elif len(Cid) > 0:
    params = {
      'Others Click ID': ''.join(filter(lambda i: i.isdigit(), Cid)),
      'Conversion Name': "QDROgenerated",
      'Conversion Time': datetime.datetime.now() ,
      'Adjustment Value': retrieve_product_price(),
      'Adjustment Currency': 'USD',
      'Adjustment Type': '',
      'Adjustment Time': datetime.datetime.now() ,
      }
    response = requests.get('https://script.google.com/macros/s/AKfycby63B0W7W4MtlJqxia3HHctt4uDgdsgAaA4tGpbQVBqmFXCubOUAF1h9fOPyoefT77rSw/exec?gid=0',params=params,)
    if response.status_code != 200:
      sys.exit(response.text)
      info = response.json()
    else:
      return ''