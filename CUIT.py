import requests
import json
import re

Hm_Ivt = input("输入Hm_Ivt:")
Hm_Ipvt = input("输入Hm_Ipvt:")
S1_rman_sid = input("输入S1_rman_sid:")
fs_session_id = input("输入fs_session_id:")
url = 'https://kczx.cuit.edu.cn/learn/v1/learningsituation'
cookies = 'Hm_lvt_312a66906c417600cd2bcfeb41146eaa='+Hm_Ivt+'; '+'Hm_lpvt_312a66906c417600cd2bcfeb41146eaa='+Hm_Ipvt+'; '+'S1_rman_sid='+S1_rman_sid+'; '+'fs_session_id='+fs_session_id+'; '

def Match(Learn_url):
    match = re.search(r'/(\w+)/(\w+)\?', Learn_url)
    if match:
        course_id = match.group(1)
        subsection_id = match.group(2)
    return course_id,subsection_id

def GetId(course_id,subsection_id,cookies):
    session = requests.Session()
    # 设置 headers
    headers = {
        'Host': 'kczx.cuit.edu.cn',
        'Cookie': cookies,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json; charset=utf-8',
        'Origin': 'https://kczx.cuit.edu.cn',
        'Referer': 'https://kczx.cuit.edu.cn/learn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Te': 'trailers'
        }
    payload = '{"courseId":"'+course_id+'","courseType":2,"subsectionId":"'+subsection_id+'","status":1,"resourceType":"video"}'
    response = requests.post(url,headers=headers,data=payload)
    json_data = json.loads(response.content)
    id = json_data["data"]["id"]
    return id

def submit(id,cookies):
    finish_url = 'https://kczx.cuit.edu.cn/learn/v1/learningsituation/status?id='+id+'&status=2'
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close",
        "Referer": "http://kczx.cuit.edu.cn",
        "Cookie": cookies
    }
    response2 = requests.get(finish_url,headers=headers)
    str = b'{"status":200,"message":"OK"}'
    if(response2.content == str):
        print("成功完成")
    else:
        print("出错了")





def Main():
    while(1):
        Learn_url = input("输入需要学习的视频链接:")
        course_id,subsection_id = Match(Learn_url=Learn_url)
        id = GetId(course_id=course_id,subsection_id=subsection_id,cookies=cookies)
        submit(id=id,cookies=cookies)

Main()