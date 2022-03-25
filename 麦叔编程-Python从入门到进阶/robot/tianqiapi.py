import requests
import json

# # 天气预报免费实时天气API接口1
# url = "https://tianqiapi.com/api"
# # 接口调用参数
# d = {"appid": "56446388", "appsecret": "YVH4UmE2", "version": "v6", "city": "合肥"}
# rep = requests.get(url, d)
# print(rep.json())
# # print(rep.text)


# # 天气预报免费实时天气API接口2,不需要注册APPID
url = "http://wthrcdn.etouch.cn/weather_mini"
d = {"city": "合肥"}

rep = requests.get(url, d)
print(type(rep))    # <class 'requests.models.Response'> Response对象
print(rep.json())
print(rep.json()['data']['forecast'][0]['date']+"的最高温度是:"+rep.json()['data']['forecast'][0]['high'])
print(rep.json()['data']['forecast'][1]['date']+"的最高温度是:"+rep.json()['data']['forecast'][0]['high'])
print(rep.json()['data']['forecast'][2]['date']+"的最高温度是:"+rep.json()['data']['forecast'][0]['high'])
# print(type(rep.json()['data']['forecast']))   # 列表
for i in rep.json()['data']['forecast']:
    # print(type(i)) # 字典
    print(i)
print(type(rep.json()))
