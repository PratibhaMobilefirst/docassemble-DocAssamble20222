global_var = False
def check_coupon(coupon_code):
  global global_var
  if coupon_code == "Free100":
    global_var = True
    return global_var
  else:
    global_var = False
    return global_var
def get_coupon_response():
  return global_var