import os
import requests
import datetime
import re

os.mkdir('aomen')

#获取当天日期
day = str(datetime.datetime.now().day)
#获取配置文件
time = requests.get("https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/time.txt").text

times = time.split("|")

xg = times[2]
if times[1] == day:
    qishu = str(times[0])
else:
    qishu = str(int(times[0])+1)



#获取澳门挂牌玄机 https://49152c.com
pic01 = requests.get(f"https://tk2.sycccf.com:4949/col/{qishu}/n1.jpg")
if pic01.headers['Content-Type'] == 'image/jpeg':
    print ('图下01')    
    with open('aomen/pic01.jpg', 'wb') as f:
        f.write(pic01.content)
    files = {'files': open('aomen/pic01.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url01 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic01.jpg'
    else:
        url01 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url01)
else:
    print ('error')
    url01 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic01.jpg'

#获取香港挂牌玄机 https://49152c.com
pic02 = requests.get(f"https://tk.sycccf.com:4949/col/{xg}/n1.jpg")
if pic02.headers['Content-Type'] == 'image/jpeg':
    xg = str(int(xg)+1)
    print ('图下02')   
    with open('aomen/pic02.jpg', 'wb') as f:
        f.write(pic02.content)
    files = {'files': open('aomen/pic02.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url02 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic02.jpg'
    else:
        url02 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url02)
else:
    print ('error')
    url02 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic02.jpg'

#获取东成西就 https://49152c.com
pic03 = requests.get(f"https://tk2.sycccf.com:4949/col/{qishu}/dcxj.jpg")
if pic03.headers['Content-Type'] == 'image/jpeg':
    print ('图下03')    
    with open('aomen/pic03.jpg', 'wb') as f:
        f.write(pic03.content)
    files = {'files': open('aomen/pic03.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url03 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic03.jpg'
    else:
        url03 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url03)
else:
    print ('error')
    url03 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic03.jpg'

#获取石狮镇码 https://49152c.com
pic04 = requests.get(f"https://tk2.sycccf.com:4949/col/{qishu}/sszm.jpg")
if pic04.headers['Content-Type'] == 'image/jpeg':
    print ('图下04')    
    with open('aomen/pic04.jpg', 'wb') as f:
        f.write(pic04.content)
    files = {'files': open('aomen/pic04.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url04 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic04.jpg'
    else:
        url04 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url04)
else:
    print ('error')
    url04 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic04.jpg'

#获取绝杀五肖霸王杀五肖 https://www.353583.com/
pic05 = requests.get(f"https://www.353583.com/tutu/faf{qishu}.jpg")
if pic05.headers['Content-Type'] == 'image/jpeg':
    print ('图下05')    
    with open('aomen/pic05.jpg', 'wb') as f:
        f.write(pic05.content)
    files = {'files': open('aomen/pic05.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url05 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic05.jpg'
    else:    
        url05 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url05)
else:
    print ('error')
    url05 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic05.jpg'

#获取二肖二码 https://www.353583.com/
pic06 = requests.get(f"https://www.353583.com/tutu/fgmc{qishu}.jpg")
if pic06.headers['Content-Type'] == 'image/jpeg':
    print ('图下06')    
    with open('aomen/pic06.jpg', 'wb') as f:
        f.write(pic06.content)
    files = {'files': open('aomen/pic06.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url06 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic06.jpg'
    else:
        url06 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url06)
else:
    print ('error')
    url06 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic06.jpg'

#获取六肖12码 https://www.353583.com/
pic07 = requests.get(f"https://www.353583.com/tutu/6i12m{qishu}.jpg")
if pic07.headers['Content-Type'] == 'image/jpeg':
    print ('图下07')    
    with open('aomen/pic07.jpg', 'wb') as f:
        f.write(pic07.content)
    files = {'files': open('aomen/pic07.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url07 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic07.jpg'
    else:
        url07 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url07)
else:
    print ('error')
    url07 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic07.jpg'

#获取天书三肖 https://www.353583.com/
pic08 = requests.get(f"https://www.353583.com/tutu/gd{qishu}.jpg")
if pic08.headers['Content-Type'] == 'image/jpeg':
    print ('图下08')    
    with open('aomen/pic08.jpg', 'wb') as f:
        f.write(pic08.content)
    files = {'files': open('aomen/pic08.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url08 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic08.jpg'
    else:
        url08 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url08)
else:
    print ('error')
    url08 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic08.jpg' 

#获取四肖八码 https://www.353583.com/
pic09 = requests.get(f"https://www.353583.com/tutu/lhwt{qishu}.jpg")
if pic09.headers['Content-Type'] == 'image/jpeg':
    print ('图下09')    
    with open('aomen/pic09.jpg', 'wb') as f:
        f.write(pic09.content)
    files = {'files': open('aomen/pic09.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url09 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic09.jpg' 
    else:
        url09 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url09)
else:
    print ('error')
    url09 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic09.jpg' 

#获取四肖四码 https://www.353583.com/
pic10 = requests.get(f"https://www.353583.com/tutu/ugyf{qishu}.jpg")
if pic10.headers['Content-Type'] == 'image/jpeg':
    print ('图下10')    
    with open('aomen/pic10.jpg', 'wb') as f:
        f.write(pic10.content)
    files = {'files': open('aomen/pic10.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url10 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic10.jpg'
    else:
        url10 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url10)
else:
    print ('error')
    url10 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic10.jpg'

#获取看图找生肖 https://49629a.com/ 49图库 https://49629a.com/img/ktzsx{qishu}.jpg
pic11 = requests.get(f"https://tk2.sycccf.com:4949/col/{qishu}/ktzsx.jpg")
if pic11.headers['Content-Type'] == 'image/jpeg':
    print ('图下11')    
    with open('aomen/pic11.jpg', 'wb') as f:
        f.write(pic11.content)
    files = {'files': open('aomen/pic11.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url11 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic11.jpg'
    else:
        url11 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url11)
else:
    print ('error')
    url11 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic11.jpg'

#获取澳门精准四肖12码 https://49629a.com/
pic12 = requests.get(f"https://49629a.com/img/amhg{qishu}.jpg")
if pic12.headers['Content-Type'] == 'image/jpeg':
    print ('图下12')    
    with open('aomen/pic12.jpg', 'wb') as f:
        f.write(pic12.content)
    files = {'files': open('aomen/pic12.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url12 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic12.jpg'
    else:
        url12 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url12)
else:
    print ('error')
    url12 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic12.jpg'

#获取西游家野 三肖中特 https://49629a.com/
pic13 = requests.get(f"https://49629a.com/img/zbxyb{qishu}.jpg")
if pic13.headers['Content-Type'] == 'image/jpeg':
    print ('图下13')    
    with open('aomen/pic13.jpg', 'wb') as f:
        f.write(pic13.content)
    files = {'files': open('aomen/pic13.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url13 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic13.jpg'
    else:
        url13 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url13)
else:
    print ('error')
    url13 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic13.jpg'

#获取澳门内幕 四肖四码 https://49629a.com/
pic14 = requests.get(f"https://49629a.com/img/nm4x8m{qishu}.jpg")
if pic14.headers['Content-Type'] == 'image/jpeg':  
    print ('图下14')  
    with open('aomen/pic14.jpg', 'wb') as f:
        f.write(pic14.content)
    files = {'files': open('aomen/pic14.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url14 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic14.jpg'
    else:
        url14 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url14)
else:
    print ('error')
    url14 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic14.jpg'

#获取三肖六码 https://123186.com
pic15 = requests.get(f"https://123186a.com/gsbtu/baoma{qishu}.jpg")
if pic15.headers['Content-Type'] == 'image/jpeg':
    print ('图下15')    
    with open('aomen/pic15.jpg', 'wb') as f:
        f.write(pic15.content)
    files = {'files': open('aomen/pic15.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url15 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic15.jpg'
    else:
        url15 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url15)
else:
    print ('error')
    url15 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic15.jpg'

#获取皇道吉日 https://123186.com
pic16 = requests.get(f"https://123186a.com/gsbtu/hdjr{qishu}.jpg")
if pic16.headers['Content-Type'] == 'image/jpeg':
    print ('图下16')    
    with open('aomen/pic16.jpg', 'wb') as f:
        f.write(pic16.content)
    files = {'files': open('aomen/pic16.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url16 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic16.jpg'
    else:
        url16 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url16)
else:
    print ('error')
    url16 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic16.jpg'


#获取马经 https://666.003123.me/js8/tu/ktzsx.png
page = requests.get("https://amtutu.003123.club/yjjy/index.php?c=5").text
pattern = re.compile('Title: <a href="(.*?)">No Title')
m =  re.findall(pattern, page)
page2 = requests.get(m[0]).text

pattern2 = re.compile('InterPhoto.image.php(.*?)"')
m2 =  re.findall(pattern2, page2)
headers = {
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
    'Referer': m[0],
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

pic17 = requests.get("https://amtutu.003123.club/yjjy/InterPhoto.image.php"+m2[0],headers=headers)
if pic17.headers['Content-Type'] == 'image/jpeg':
    print ('图下17')    
    with open('aomen/pic17.jpg', 'wb') as f:
        f.write(pic17.content)
    files = {'files': open('aomen/pic17.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url17 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic17.jpg'
    else:
        url17 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url17)
else:
    print ('error')
    url17 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic17.jpg'

#获取守护幸福 https://777.003123.me/index.php?c=2
page = requests.get("https://amtutu.003123.club/yjjy/index.php?c=2").text
pattern = re.compile('Title: <a href="(.*?)">No Title')
m =  re.findall(pattern, page)
page2 = requests.get(m[0]).text

pattern2 = re.compile('InterPhoto.image.php(.*?)"')
m2 =  re.findall(pattern2, page2)


headers = {
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
    'Referer': m[0],
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

pic18 = requests.get("https://amtutu.003123.club/yjjy/InterPhoto.image.php"+m2[0],headers=headers)

if pic18.headers['Content-Type'] == 'image/jpeg':
    print ('图下18')
    with open('aomen/pic18.jpg', 'wb') as f:
        f.write(pic18.content)
    files = {'files': open('aomen/pic18.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url18 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic18.jpg'
    else:
        url18 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url18)
else:
    print ('error')
    url18 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic18.jpg'



#获取招财猫四肖八码 https://49152c.com
pic19 = requests.get(f"https://tk2.sycccf.com:4949/col/{qishu}/rv.jpg")
if pic19.headers['Content-Type'] == 'image/jpeg':
    print ('图下19')    
    with open('aomen/pic19.jpg', 'wb') as f:
        f.write(pic19.content)
    files = {'files': open('aomen/pic19.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url19 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic19.jpg'
    else:
        url19 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url19)
else:
    print ('error')
    url19 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic19.jpg'
    
#获取香港马经
page = requests.get("https://xgtutu.003123.club/yjjy/index.php?c=16")
page.encoding = "utf-8"

pattern = re.compile('Title: <a href="(.*?)">马经')
m =  re.findall(pattern, page.text)

page2 = requests.get(m[0]).text

pattern2 = re.compile('InterPhoto.image.php(.*?)"')
m2 =  re.findall(pattern2, page2)
headers = {
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
    'Referer': m[0],
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

pic20 = requests.get("https://xgtutu.003123.club/yjjy/InterPhoto.image.php"+m2[0],headers=headers)
if pic20.headers['Content-Type'] == 'image/jpeg':
    print ('图下20')    
    with open('aomen/pic20.jpg', 'wb') as f:
        f.write(pic20.content)
    files = {'files': open('aomen/pic20.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url20 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic20.jpg'
    else:
        url20 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url20)
      
else:
    print ('error')
    url20 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic20.jpg'
    
#获取香港守护幸福
page = requests.get("https://xgtutu.003123.club/yjjy/index.php?c=17")
page.encoding = "utf-8"

pattern = re.compile('Title: <a href="(.*?)">守护幸福')
m =  re.findall(pattern, page.text)

page2 = requests.get(m[0]).text

pattern2 = re.compile('InterPhoto.image.php(.*?)"')
m2 =  re.findall(pattern2, page2)
headers = {
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
    'Referer': m[0],
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

pic21 = requests.get("https://xgtutu.003123.club/yjjy/InterPhoto.image.php"+m2[0],headers=headers)
if pic21.headers['Content-Type'] == 'image/jpeg':
    print ('图下21')    
    with open('aomen/pic21.jpg', 'wb') as f:
        f.write(pic21.content)
    files = {'files': open('aomen/pic21.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url21 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic20.jpg'
    else:
        url21 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url21)
      
else:
    print ('error')
    url21 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic20.jpg'
    
#获取黄大仙发财符 https://49152c.com/#/picture/28247
pic22 = requests.get(f"https://tk2.sycccf.com:4949/col/{qishu}/tt38.jpg")
if pic22.headers['Content-Type'] == 'image/jpeg':
    print ('图下22')    
    with open('aomen/pic22.jpg', 'wb') as f:
        f.write(pic22.content)
    files = {'files': open('aomen/pic22.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url22 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic22.jpg'
    else:
        url22 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url22)
else:
    print ('error')
    url22 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic22.jpg'
    
#获取澳门火凤凰 https://49152c.com/#/picture/209347
pic23 = requests.get(f"https://tk2.sycccf.com:4949/col/{qishu}/amffh.jpg")
if pic23.headers['Content-Type'] == 'image/jpeg':
    print ('图下23')    
    with open('aomen/pic23.jpg', 'wb') as f:
        f.write(pic23.content)
    files = {'files': open('aomen/pic23.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url23 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic23.jpg'
    else:
        url23 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url23)
else:
    print ('error')
    url23 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic23.jpg'
    
#获取澳门火凤凰 https://49152c.com/#/picture/209351
pic24 = requests.get(f"https://tk2.sycccf.com:4949/col/{qishu}/amfql.jpg")
if pic24.headers['Content-Type'] == 'image/jpeg':
    print ('图下24')    
    with open('aomen/pic24.jpg', 'wb') as f:
        f.write(pic24.content)
    files = {'files': open('aomen/pic24.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url24 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic24.jpg'
    else:
        url24 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url24)
else:
    print ('error')
    url24 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic24.jpg'
    
#获取澳门签牌 https://49152c.com/#/picture/28096
pic25 = requests.get(f"https://tk2.sycccf.com:4949/col/{qishu}/twqp.jpg")
if pic25.headers['Content-Type'] == 'image/jpeg':
    print ('图下25')    
    with open('aomen/pic25.jpg', 'wb') as f:
        f.write(pic25.content)
    files = {'files': open('aomen/pic25.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url25 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic25.jpg'
    else:
        url25= "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url25)
else:
    print ('error')
    url25 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic25.jpg'
    
#获取金龙三肖 https://49629a.com/img/jl3x273.jpg
pic26 = requests.get(f"49629a.com/img/jl3x{qishu}.jpg")
if pic26.headers['Content-Type'] == 'image/jpeg':
    print ('图下26')    
    with open('aomen/pic26.jpg', 'wb') as f:
        f.write(pic26.content)
    files = {'files': open('aomen/pic26.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url26 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic26.jpg'
    else:
        url26= "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url26)
else:
    print ('error')
    url26 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic26.jpg'
    
#获取发财单双 https://www.353583.com/
pic27 = requests.get(f"https://www.353583.com/tutu/ujcc{qishu}.jpg")
if pic27.headers['Content-Type'] == 'image/jpeg':
    print ('图下27')    
    with open('aomen/pic27.jpg', 'wb') as f:
        f.write(pic27.content)
    files = {'files': open('aomen/pic27.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url27 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic27.jpg'
    else:    
        url27 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url27)
else:
    print ('error')
    url27 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic27.jpg'
    
#获取独家平特 https://www.29761a.com/img/djpt273.jpg
pic28 = requests.get(f"https://www.29761a.com/img/djpt{qishu}.jpg")
if pic28.headers['Content-Type'] == 'image/jpeg':
    print ('图下28')    
    with open('aomen/pic28.jpg', 'wb') as f:
        f.write(pic28.content)
    files = {'files': open('aomen/pic28.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url28 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic28.jpg'
    else:    
        url28 = "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url28)
else:
    print ('error')
    url28 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic28.jpg'
    
#获取单双主三肖 https://49629a.com/img/1xzt273.jpg
pic29 = requests.get(f"49629a.com/img/1xzt{qishu}.jpg")
if pic29.headers['Content-Type'] == 'image/jpeg':
    print ('图下29')    
    with open('aomen/pic29.jpg', 'wb') as f:
        f.write(pic29.content)
    files = {'files': open('aomen/pic29.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url29 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic29.jpg'
    else:
        url29= "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url29)
else:
    print ('error')
    url29 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic29.jpg'
    
#获取财神到玄机 https://49152c.com/#/picture/28111
pic30 = requests.get(f"https://tk2.sycccf.com:4949/col/{qishu}/mfpy.jpg")
if pic30.headers['Content-Type'] == 'image/jpeg':
    print ('图下30')    
    with open('aomen/pic30.jpg', 'wb') as f:
        f.write(pic30.content)
    files = {'files': open('aomen/pic30.jpg', 'rb')}
    r = requests.post("https://telegra.ph/upload", files=files).json()
    err = r[0].get("error")
    if err:
        print(f"Failed to upload. Reason: {err}")
        url30 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic30.jpg'
    else:
        url30= "https://2img.net/h/telegra.ph" + r[0].get("src")
        print(url30)
else:
    print ('error')
    url30 = 'https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/pic30.jpg'
    

#保存html文本
htmlconten = f'<div align="center" class="imgblock"><a href="{url01}" target="_blank"><img src="{url01}" / ><a href="{url19}" target="_blank"><img src="{url19}" / ></div><div align="center" class="imgblock"><a href="{url03}" target="_blank"><img src="{url03}" / ><a href="{url04}" target="_blank"><img src="{url04}" / ></div><div align="center" class="imgblock"><a href="{url05}" target="_blank"><img src="{url05}" / ><a href="{url06}" target="_blank"><img src="{url06}" / ></div><div align="center" class="imgblock"><a href="{url07}" target="_blank"><img src="{url07}" / ><a href="{url08}" target="_blank"><img src="{url08}" / ></div><div align="center" class="imgblock"><a href="{url09}" target="_blank"><img src="{url09}" / ><a href="{url10}" target="_blank"><img src="{url10}" / ></div><div align="center" class="imgblock"><a href="{url11}" target="_blank"><img src="{url11}" / ><a href="{url12}" target="_blank"><img src="{url12}" / ></div><div align="center" class="imgblock"><a href="{url13}" target="_blank"><img src="{url13}" / ><a href="{url14}" target="_blank"><img src="{url14}" / ></div><div align="center" class="imgblock"><a href="{url15}" target="_blank"><img src="{url15}" / ><a href="{url16}" target="_blank"><img src="{url16}" / ></div><div align="center" class="imgblock"><a href="{url17}" target="_blank"><img src="{url17}" / ><a href="{url18}" target="_blank"><img src="{url18}" / ></div><h1 align="center" style="color:red ; font-size:50px">香港图片</h1><div align="center" class="imgblock"><a href="{url02}" target="_blank"><img src="{url02}" /></div><div align="center" class="imgblock"><a href="{url20}" target="_blank"><img src="{url20}" / ><a href="{url21}" target="_blank"><img src="{url21}" / ></div></body></html>'
title = '<!DOCTYPE html><html><head><meta charset="utf-8"><title>澳门图片</title></head><body><style type="text/css">.imgblock img{width:50%;height:500px;flost:left;}</style><h1 align="center" style="color:red ; font-size:50px">澳门图片</h1>'
html = title+htmlconten
print('写入html')
with open('aomen/html.txt','w') as f:
    f.write(html)

#保存日期配置
pz = str(qishu + "|" + day + "|" + xg + "|")

with open('aomen/time.txt', 'w') as f:
    f.write(pz)

