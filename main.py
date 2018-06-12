import JSON

import requests

from const import URL

from keys import username,password


text = str(input('Enter text you want translated from English'))

model_id = str(input('Spanish, French, German'))

Spanish = en-es

French = en-fr

German = en-gr

payload = { 'text' : text 'model_id' : model_id }



def translate():

    response = requests.get(URL,auth=(username, password),params=payload)

    if response.ok:
        data = response.json()
    else:
        data = None
    return data
