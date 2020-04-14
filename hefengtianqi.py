'''
和风api爬取天气预报数据
目标：https://free-api.heweather.net/s6/weather/forecast?key=cc33b9a52d6e48de852477798980b76e&location=CN101090101
   得到中国城市的代码：https://a.hecdn.net/download/dev/china-city-list.csv
  目前先查20个城市第二天的天气
'''
import requests
#now
url1 = 'https://free-api.heweather.net/s6/weather/now?key=138f2d4c6e3c4f67a8a4293cf9f2d0bb&location=杭州'
strhtml1  = requests.get(url1)
dict1 = strhtml1.json()
#lifestyle
url2 = 'https://free-api.heweather.net/s6/weather/lifestyle?key=138f2d4c6e3c4f67a8a4293cf9f2d0bb&location=杭州'
strhtml2  = requests.get(url2)
dict2 = strhtml2.json()
#forecast
url3 = 'https://free-api.heweather.net/s6/weather/forecast?key=138f2d4c6e3c4f67a8a4293cf9f2d0bb&location=杭州'
strhtml3  = requests.get(url3)
dict3 = strhtml3.json()


#for item in dict["HeWeather6"][0]['daily_forecast'][1:2]:
weather = {
    '省份':dict1["HeWeather6"][0]['basic']['admin_area'],
    '城市名':dict1["HeWeather6"][0]['basic']['location'],
    '当地时间':dict1["HeWeather6"][0]['update']['loc'],
    '当前温度':dict1["HeWeather6"][0]['now']['fl'],
    '最高温度':dict3["HeWeather6"][0]['daily_forecast'][0]['tmp_max'],
    '最低温度':dict3["HeWeather6"][0]['daily_forecast'][0]['tmp_min'],
    '相对湿度':dict3["HeWeather6"][0]['daily_forecast'][0]['hum'],
    '风力':dict3["HeWeather6"][0]['daily_forecast'][0]['wind_sc'],
    '风向':dict3["HeWeather6"][0]['daily_forecast'][0]['wind_dir'],
    '天气状况描述':dict3["HeWeather6"][0]['daily_forecast'][0]['cond_txt_d'],
    '降水概率':dict3["HeWeather6"][0]['daily_forecast'][0]['pop'],
    '舒适度指数':dict2["HeWeather6"][0]['lifestyle'][0]['txt'],
    '穿衣指数':dict2["HeWeather6"][0]['lifestyle'][1]['txt'],
    '感冒指数':dict2["HeWeather6"][0]['lifestyle'][2]['txt'],
    '运动指数':dict2["HeWeather6"][0]['lifestyle'][3]['txt'],
    '旅游指数':dict2["HeWeather6"][0]['lifestyle'][4]['txt'],
    '紫外线指数':dict2["HeWeather6"][0]['lifestyle'][5]['txt'],
    '洗车指数':dict2["HeWeather6"][0]['lifestyle'][6]['txt'],
    '空气污染扩散条件指数':dict2["HeWeather6"][0]['lifestyle'][7]['txt']
   }
print(weather)

Voice = "早上好！您正位于"+weather['省份']+"省"+weather['城市名']+"市,本地时间"+weather['当地时间']+"。今日最低温度为"+weather['最低温度']+"度,"+"今日最高温度为"+weather['最高温度']+"度。"
Voice = Voice + "当前温度为"+weather['当前温度']+"度。"+"今日的湿度指数为"+weather['相对湿度']+",风力为"+ weather['风力']+"级,"+weather['风向']+"。"
Voice = Voice + "今日天气状况为"+weather['天气状况描述']+"天,降水概率为百分之"+weather['降水概率']
Voice = Voice + "。接下来会介绍今日的生活方案哦,今天" + weather['舒适度指数'] + "对于衣着,这边"+weather['穿衣指数'] + "关于运动"+weather['运动指数']
Voice = Voice +"关于旅游"+weather['旅游指数']+"关于紫外线,今日"+weather['紫外线指数']+"而今日空气情况为"+weather['空气污染扩散条件指数']+"最后，亲爱的主人，对于您的车子"+weather['洗车指数']
print(Voice)


from aip import AipSpeech
APP_ID = '19386031'#引号之间填写之前在ai平台上获得的参数
API_KEY = 'sRYyMzbW11KwZWSKhItCkqdI'#如上
SECRET_KEY = '3eaXBWFlaCy7K2KRehHXfzDPHarj0QvL'#如上

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
lan=Voice
result = client.synthesis(lan, 'zh', 1, { 'vol': 5,'per':4,'spd':5 })
'''
固定值zh。语言选择,目前只有中英文混合模式，填写固定值zh
客户端类型选择，web端填写固定值1
spd语速，取值0-15，默认为5中语速(选填)
pit音调，取值0-15，默认为5中语调（选填）
vol音量，取值0-15，默认为5中音量（选填）
per发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫>，默认为普通女声
'''
#识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('Translate.mp3', 'wb') as f:
        f.write(result)

