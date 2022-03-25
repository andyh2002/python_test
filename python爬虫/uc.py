import requests

url = 'http://swgj.bil.anhuitelecom.com:25102/ah_bss'
res = requests.get(url=url)

print(res)
print(res.content)
print(res.content.decode('utf-8'))
print(res.text)
print(res.headers)
print(res.status_code)
print(res.url)

