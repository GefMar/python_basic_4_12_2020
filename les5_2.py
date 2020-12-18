import requests

url = "https://geekbrains.ru/posts/avtomatizaciya-testirovaniya-na-python-novyj-kurs"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15'
}

response = requests.get(url, headers=headers)
print(1)
file = open('post.html', 'w', encoding='UTF-8')
try:
    file.write(response.text)
except IOError:
    pass
finally:
    file.close()
