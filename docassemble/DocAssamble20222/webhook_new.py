import requests
import sys
import time

def yml_veriables(cid):				
  Cid = cid
  if Cid.startswith( 'gclid' ) or Cid.startswith( 'graid' ) or Cid.startswith( 'wbraid' ):
    params = {
      'Google Click ID': Cid,
      'Conversion Name': "QDROgenerated",
      'Conversion Time': time.time(),
      'Conversion Value': '50',
      'Conversion Currency': 'USD',
      }
    response = requests.get('https://script.google.com/macros/s/AKfycbz4YKL3XeNCuQswv80VCuM-kLR-VDJuKP5Pj2psYBy97x09QG2pSG_SLA9Zmig-lcrH/exec?gid=0',params=params,)
    if response.status_code != 200:
      sys.exit(response.text)
      info = response.json()

  elif Cid.startswith( 'msckld' ):						
    params = {
      'Microsoft Click ID': Cid,
      'Conversion Name': "QDROgenerated",
      'Conversion Time': time.time(),
      'Adjustment Value': '50',
      'Adjustment Currency': 'USD',
      'Adjustment Type': '',
      'Adjustment Time': time.time(),
      }
    response = requests.get('https://script.google.com/macros/s/AKfycbzSkMLhY4XxoWlLGBa2cFiJFAsihpuQy5jzqaGq5wnwwLeZUIwG7Xi3hXvuky2y_uvuqg/exec?gid=0',params=params,)
    if response.status_code != 200:
      sys.exit(response.text)
      info = response.json()
      
  elif len(Cid) > 0:
    params = {
      'Others Click ID': Cid,
      'Conversion Name': "QDROgenerated",
      'Conversion Time': time.time(),
      'Adjustment Value': '50',
      'Adjustment Currency': 'USD',
      'Adjustment Type': '',
      'Adjustment Time': time.time(),
      }
    response = requests.get('https://script.google.com/macros/s/AKfycby63B0W7W4MtlJqxia3HHctt4uDgdsgAaA4tGpbQVBqmFXCubOUAF1h9fOPyoefT77rSw/exec?gid=0',params=params,)
    if response.status_code != 200:
      sys.exit(response.text)
      info = response.json()
  else:
    return ''