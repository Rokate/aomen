import aiohttp
import asyncio
import aiofiles
import requests
import time
import re
import os 

async def parseurl(url,sem):
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                picurl = (await response.json())['data']['largePictureUrl']
                #print(picurl)
                imagelist.append(picurl)
    
async def downloadpic(url,sem):
    async with sem:        
        max_retries = 3
        attempt = 0
        while True:
            try:
                async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
                    async with session.get(url, timeout=10) as resp:
                        picname = url.split("/")[-1]                        
                        if resp.headers['Content-Type'] == 'image/jpeg':
                            async with aiofiles.open(f'aomen/{picname}', 'wb') as f:
                                while True:
                                    chunk = await resp.content.read(1024)
                                    if not chunk:
                                        break
                                    await f.write(chunk) 
                                print(f'{url}<==>{picname}下载成功')           
                            break
                        else:
                           print (f'{picname}下载失败')
                           break     
            except aiohttp.ClientConnectorError as e:
                if attempt < max_retries:
                    print("{}times:{}".format(picname, attempt),str(e))
                    attempt += 1
                else:
                    raise

async def downloadamimg(imagelist):
    y = 0
    for url in imagelist:
        pic = str(y)
        y = y+1
        max_retries = 3
        attempt = 0
        while True:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as resp:
                        page = await resp.text()
                        pattern = re.compile('Title: <a href="(.*?)">No Title')
                        m =  re.findall(pattern, page)
                        
                        async with session.get(m[0]) as resp:
                            page2 = await resp.text()
                        pattern2 = re.compile('InterPhoto.image.php(.*?)"')
                        m2 =  re.findall(pattern2, page2)
                        headers = {
                            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
                            'Referer': m[0],
                            'sec-ch-ua-mobile': '?0',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36',
                            'sec-ch-ua-platform': '"Windows"',}
                        picfile = await session.get("https://amtutu.003123.club/yjjy/InterPhoto.image.php"+m2[0],headers=headers)
                        async with aiofiles.open(f'aomen/ampic{pic}.jpg', 'wb') as f:
                            while True:
                                chunk = await picfile.content.read(1024)
                                if not chunk:
                                    break
                                await f.write(chunk)        
                        break
            except aiohttp.ClientConnectorError as e:
                if attempt < max_retries:
                    print("{}times:{}".format(picname, attempt),str(e))
                    attempt += 1
                else:
                    raise           
                        
async def downloadxgmj():
    max_retries = 3
    attempt = 0
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://xgtutu.003123.club/yjjy/index.php?c=16') as resp:
                    page = await resp.text()
                    pattern = re.compile('Title: <a href="(.*?)">马经')
                    m =  re.findall(pattern, page)
                    async with session.get(m[0]) as resp:
                        page2 = await resp.text()
                    pattern2 = re.compile('InterPhoto.image.php(.*?)"')
                    m2 =  re.findall(pattern2, page2)
                    headers = {
                            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
                            'Referer': m[0],
                            'sec-ch-ua-mobile': '?0',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36',
                            'sec-ch-ua-platform': '"Windows"',}
                    picfile = await session.get("https://xgtutu.003123.club/yjjy/InterPhoto.image.php"+m2[0],headers=headers)
                    async with aiofiles.open(f'aomen/xgmj.jpg', 'wb') as f:
                        while True:
                            chunk = await picfile.content.read(1024)
                            if not chunk:
                                break
                            await f.write(chunk)        
                    break
        except aiohttp.ClientConnectorError as e:
            if attempt < max_retries:
                print("{}times:{}".format(picname, attempt),str(e))
                attempt += 1
            else:
                raise

async def downloadxgsh():
    max_retries = 3
    attempt = 0
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://xgtutu.003123.club/yjjy/index.php?c=17') as resp:
                    page = await resp.text()
                    pattern = re.compile('Title: <a href="(.*?)">守护幸福')
                    m =  re.findall(pattern, page)
                    async with session.get(m[0]) as resp:
                        page2 = await resp.text()
                    pattern2 = re.compile('InterPhoto.image.php(.*?)"')
                    m2 =  re.findall(pattern2, page2)
                    headers = {
                            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
                            'Referer': m[0],
                            'sec-ch-ua-mobile': '?0',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36',
                            'sec-ch-ua-platform': '"Windows"',}
                    picfile = await session.get("https://xgtutu.003123.club/yjjy/InterPhoto.image.php"+m2[0],headers=headers)
                    async with aiofiles.open(f'aomen/xgsh.jpg', 'wb') as f:
                        while True:
                            chunk = await picfile.content.read(1024)
                            if not chunk:
                                break
                            await f.write(chunk)        
                    break
        except aiohttp.ClientConnectorError as e:
            if attempt < max_retries:
                print("{}times:{}".format(picname, attempt),str(e))
                attempt += 1
            else:
                raise

async def downloadxggp():
    picurl = requests.get('https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=10870').json()['data']['largePictureUrl']
    pic = requests.get(picurl)
    if pic.headers['Content-Type'] == 'image/jpeg':
        with open('aomen/xgn1.jpg', 'wb') as f:
            f.write(pic.content)
    else:
        print ('xggp下载失败')
        
async def get49tkimgurl():    
    task_list = []
    sem = asyncio.Semaphore(3)
    for url in tk49_imgurl:
        task = asyncio.create_task(parseurl(url,sem))
        task_list.append(task)
    await asyncio.gather(*task_list)

async def downloadimglist():    
    task_list = []
    sem = asyncio.Semaphore(4)
    for url in imagelist:        
        task = asyncio.create_task(downloadpic(url,sem))
        task_list.append(task)
    await asyncio.gather(*task_list)

if __name__ == '__main__':
    start = time.time()
    os.mkdir('aomen')
    qishu = requests.get('https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=28854').json()['data']['period']
    imagelist = [
        f"https://www.353583.com/tutu/faf{qishu}.jpg",
        f"https://www.353583.com/tutu/fgmc{qishu}.jpg",
        f"https://www.353583.com/tutu/6i12m{qishu}.jpg",
        f"https://www.353583.com/tutu/gd{qishu}.jpg",
        f"https://www.353583.com/tutu/lhwt{qishu}.jpg",
        f"https://www.353583.com/tutu/ugyf{qishu}.jpg",
        f"https://49629a.com/img/amhg{qishu}.jpg",
        f"https://49629a.com/img/zbxyb{qishu}.jpg",
        f"https://49629a.com/img/nm4x8m{qishu}.jpg",
        f"https://123186a.com/gsbtu/baoma{qishu}.jpg",
        f"https://123186a.com/gsbtu/hdjr{qishu}.jpg",
        f"https://49629a.com/img/jl3x{qishu}.jpg",
        f"https://www.353583.com/tutu/ujcc{qishu}.jpg",
        f"https://www.29761a.com/img/djpt{qishu}.jpg",
        f"https://49629a.com/img/1xzt{qishu}.jpg",]   

    tk49_imgurl = [
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=28854',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=209232',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=209244',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=209362',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=316981',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=28247',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=209347',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=209351',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=28096',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=28111',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=416992',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=28628',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=10344',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=10346',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=10348',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=10350',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=10815',
        'https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=15819',]

    amimg = [
        'https://amtutu.003123.club/yjjy/index.php?c=5',
        'https://amtutu.003123.club/yjjy/index.php?c=2'
    ]
    print("获取49图片")
    asyncio.run(get49tkimgurl())
    print("开始下载图片")
    asyncio.run(downloadimglist())

    '''
    loop = asyncio.get_event_loop()
    loop.run_until_complete(downloadamimg(amimg))
    '''
    print("获取香港图片")
    asyncio.run(downloadxggp())
    asyncio.run(downloadxgmj())
    asyncio.run(downloadxgsh())
    print("获取澳门图片")
    asyncio.run(downloadamimg(amimg))
    htmlconten = f'<div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/n1.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/n1.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/rv.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/rv.jpg" / ></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/dcxj.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/dcxj.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/sszm.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/sszm.jpg" / ></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/faf{qishu}.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/faf{qishu}.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/fgmc{qishu}.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/fgmc{qishu}.jpg" / ></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/6i12m{qishu}.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/6i12m{qishu}.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/gd{qishu}.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/gd{qishu}.jpg" / ></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/lhwt{qishu}.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/lhwt{qishu}.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/ugyf{qishu}.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/ugyf{qishu}.jpg" / ></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/ktzsx.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/ktzsx.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/amhg{qishu}.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/amhg{qishu}.jpg" / ></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/zbxyb{qishu}.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/zbxyb{qishu}.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/nm4x8m{qishu}.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/nm4x8m{qishu}.jpg" / ></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/baoma{qishu}.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/baoma{qishu}.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/hdjr{qishu}.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/hdjr{qishu}.jpg" / ></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/ampic0.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/ampic0.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/ampic1.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/ampic1.jpg" / ></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/tt38.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/tt38.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/amffh.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/amffh.jpg" / ></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/amfql.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/amfql.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/twqp.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/twqp.jpg" / ></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/jl3x{qishu}.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/jl3x{qishu}.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/ujcc{qishu}.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/ujcc{qishu}.jpg" / ></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/djpt{qishu}.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/djpt{qishu}.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/1xzt{qishu}.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/1xzt{qishu}.jpg" / ><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/lhlxsm.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/lhlxsm.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/b8.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/b8.jpg" / ></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/mfpy.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/mfpy.jpg" / ></div><iframe src="https://zhibo.chong0123.com:777/" height="150" width=100% title="香港开奖"></iframe><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/xgn1.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/xgn1.jpg" /></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/xgmj.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/xgmj.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/xgsh.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/xgsh.jpg" / ></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/b002.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/b002.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/b004.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/b004.jpg" / ></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/b006.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/b006.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/b008.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/b008.jpg" / ></div><div align="center" class="imgblock"><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/j11.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/j11.jpg" / ><a href="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/qlb.jpg" target="_blank"><img src="https://ghproxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/aomen/qlb.jpg" / ></div></body></html>'
    title = '<!DOCTYPE html><html><head><meta charset="utf-8"><title>澳门图片</title></head><body><style type="text/css">.imgblock img{width:50%;height:500px;flost:left;}</style><h1 align="center" style="color:red ; font-size:50px">澳门图片</h1><iframe src="https://zhibo.aoyoushop.com:777/" height="180" width=100% title="澳门开奖"></iframe>'
    html = title+htmlconten
    print('写入html')
    with open('aomen/html.txt','w') as f:
        f.write(html)

    end = time.time()
    print(f'一共耗时：{end - start}')
