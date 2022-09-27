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
if pic01.status_code == 200:
    print ('图下01')    
    with open('aomen/pic01.jpg', 'wb') as f:
        f.write(pic01.content)
else:
    print ('error')

#获取香港挂牌玄机 https://49152c.com
pic02 = requests.get(f"https://tk.sycccf.com:4949/col/{xg}/n1.jpg")
if pic02.status_code == 200:
    xg = str(int(xg)+1)
    print ('图下02')   
    with open('aomen/pic02.jpg', 'wb') as f:
        f.write(pic02.content)
else:
    print ('error')

#获取东成西就 https://49152c.com
pic03 = requests.get(f"https://tk2.sycccf.com:4949/col/{qishu}/dcxj.jpg")
if pic03.status_code == 200:
    print ('图下03')    
    with open('aomen/pic03.jpg', 'wb') as f:
        f.write(pic03.content)
else:
    print ('error')

#获取石狮镇码 https://49152c.com
pic04 = requests.get(f"https://tk2.sycccf.com:4949/col/{qishu}/sszm.jpg")
if pic04.status_code == 200:
    print ('图下04')    
    with open('aomen/pic04.jpg', 'wb') as f:
        f.write(pic04.content)
else:
    print ('error')

#获取绝杀五肖霸王杀五肖 https://www.353583.com/
pic05 = requests.get(f"https://www.353583.com/tutu/faf{qishu}.jpg")
if pic05.status_code == 200:
    print ('图下05')    
    with open('aomen/pic05.jpg', 'wb') as f:
        f.write(pic05.content)
else:
    print ('error')

#获取二肖二码 https://www.353583.com/
pic06 = requests.get(f"https://www.353583.com/tutu/fgmc{qishu}.jpg")
if pic06.status_code == 200:
    print ('图下06')    
    with open('aomen/pic06.jpg', 'wb') as f:
        f.write(pic06.content)
else:
    print ('error')

#获取六肖12码 https://www.353583.com/
pic07 = requests.get(f"https://www.353583.com/tutu/6i12m{qishu}.jpg")
if pic07.status_code == 200:
    print ('图下07')    
    with open('aomen/pic07.jpg', 'wb') as f:
        f.write(pic07.content)
else:
    print ('error') 

#获取天书三肖 https://www.353583.com/
pic08 = requests.get(f"https://www.353583.com/tutu/gd{qishu}.jpg")
if pic08.status_code == 200:
    print ('图下08')    
    with open('aomen/pic08.jpg', 'wb') as f:
        f.write(pic08.content)
else:
    print ('error') 

#获取四肖八码 https://www.353583.com/
pic09 = requests.get(f"https://www.353583.com/tutu/lhwt{qishu}.jpg")
if pic09.status_code == 200:
    print ('图下09')    
    with open('aomen/pic09.jpg', 'wb') as f:
        f.write(pic09.content)
else:
    print ('error') 

#获取四肖四码 https://www.353583.com/
pic10 = requests.get(f"https://www.353583.com/tutu/ugyf{qishu}.jpg")
if pic10.status_code == 200:
    print ('图下10')    
    with open('aomen/pic10.jpg', 'wb') as f:
        f.write(pic10.content)
else:
    print ('error')

#获取看图找生肖 https://49629a.com/
pic11 = requests.get(f"https://49629a.com/img/ktzsx{qishu}.jpg")
if pic11.status_code == 200:
    print ('图下11')    
    with open('aomen/pic11.jpg', 'wb') as f:
        f.write(pic11.content)
else:
    print ('error')

#获取澳门精准四肖12码 https://49629a.com/
pic12 = requests.get(f"https://49629a.com/img/amhg{qishu}.jpg")
if pic12.status_code == 200:
    print ('图下12')    
    with open('aomen/pic12.jpg', 'wb') as f:
        f.write(pic12.content)
else:
    print ('error')

#获取西游家野 三肖中特 https://49629a.com/
pic13 = requests.get(f"https://49629a.com/img/zbxyb{qishu}.jpg")
if pic13.status_code == 200:
    print ('图下13')    
    with open('aomen/pic13.jpg', 'wb') as f:
        f.write(pic13.content)
else:
    print ('error')

#获取澳门内幕 四肖四码 https://49629a.com/
pic14 = requests.get(f"https://49629a.com/img/nm4x8m{qishu}.jpg")
if pic14.status_code == 200:  
    print ('图下14')  
    with open('aomen/pic14.jpg', 'wb') as f:
        f.write(pic14.content)
else:
    print ('error')

#获取三肖六码 https://123186.com
pic15 = requests.get(f"https://123186a.com/gsbtu/baoma{qishu}.jpg")
if pic15.status_code == 200:
    print ('图下15')    
    with open('aomen/pic15.jpg', 'wb') as f:
        f.write(pic15.content)
else:
    print ('error')

#获取皇道吉日 https://123186.com
pic16 = requests.get(f"https://123186a.com/gsbtu/hdjr{qishu}.jpg")
if pic16.status_code == 200:
    print ('图下16')    
    with open('aomen/pic16.jpg', 'wb') as f:
        f.write(pic16.content)
else:
    print ('error')


#获取马经 https://666.003123.me/js8/tu/ktzsx.png
page = requests.get("https://777.003123.me/index.php?c=5").text
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

pic17 = requests.get("https://777.003123.me/InterPhoto.image.php"+m2[0],headers=headers)
if pic17.status_code == 200:
    print ('图下17')    
    with open('aomen/pic17.jpg', 'wb') as f:
        f.write(pic17.content)
else:
    print ('error')

#获取守护幸福 https://777.003123.me/index.php?c=2
page = requests.get("https://777.003123.me/index.php?c=2").text
pattern = re.compile('Title: <a href="(.*?)">No Title')
m =  re.findall(pattern, page)
page2 = requests.get(m[0]).text

pattern2 = re.compile('InterPhoto.image.php(.*?)"')
m2 =  re.findall(pattern2, page2)
headers = {
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
    'Referer': 'https://777.003123.me/InterPhoto.php?id=64384',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

pic18 = requests.get("https://777.003123.me/InterPhoto.image.php"+m2[0],headers=headers)
if pic18.status_code == 200:
    print ('图下18')    
    with open('aomen/pic18.jpg', 'wb') as f:
        f.write(pic18.content)
else:
    print ('error')

#保存日期配置
pz = str(qishu + "|" + day + "|" + xg + "|")

with open('aomen/time.txt', 'w') as f:
    f.write(pz)
