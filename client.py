import requests
flask_url = "http://127.0.0.1:5000/ads"
create_ad = [
    {"header":"Сделаю ремонт", 
     "discript": "Быстро и качественно",
     "date": "10 декабря 2024", 
     "name": "Боря"},
{"header":"Пропала собака", 
     "discript": "Черная немецкая овчарка",
     "date": "11 декабря 2024", 
     "name": "Алена"}     

]
for i in create_ad:
    response_post = requests.post(flask_url, json = i)
    print("status_code POST", response_post.status_code)
    print(response_post.json())
response_post = requests.get(flask_url)
id_ad = 1
response_del = requests.delete(f'{flask_url}/{id_ad}')