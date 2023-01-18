import requests
import sys
import time

def yml_veriables(cid):
  Cid = cid
  params = {
    'google_click_id': Cid,
    'conversion_name': "QDROgenerated",
    'conversion_time': time.time(),
    'conversion_value': '50',
    'conversion_currency': 'USD',
    }
  response = requests.get('https://script.google.com/macros/s/AKfycbz4YKL3XeNCuQswv80VCuM-kLR-VDJuKP5Pj2psYBy97x09QG2pSG_SLA9Zmig-lcrH/exec',params=params,)
  if response.status_code != 200:
    sys.exit(response.text)
    info = response.json()
