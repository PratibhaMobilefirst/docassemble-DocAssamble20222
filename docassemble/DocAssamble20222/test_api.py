import requests
def signUp():
  headers = {'X-API-Key': 'BAFOoOjnlUAVoidn8tb3NSjbvHmpQJfA'}
  myobj = {'username': 'test_user@gmail.com','password': 'abc@123', 'first_name': 'firstname', 'last_name': 'lastname'}

  user = requests.post('https://mobilefirst.lemmalegal.com/api/user/new', headers=headers, data=myobj)
  if user.status_code != 200:
    log(user.text)
    validation_error(user.text)
  info = user.json()
  log(info)

  user_id = info.get('user_id')
  log(user_id)