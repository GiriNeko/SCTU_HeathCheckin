from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup

r = requests.session()
r.headers.update={
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
}

def searchdata(raw):
    rawsoup = BeautifulSoup(raw,"html.parser")
    data = {}
    for array in rawsoup.find_all("input",type="hidden"):
        data[array.get('name')]=array.get('value')
    return data


loginurl = "http://health.sctu.edu.cn:56666/login.aspx"
checkinurl = "http://health.sctu.edu.cn:56666/jktb2_all9.aspx"
userid=""      #用户名
passwd=""     #密码
headers = {
    'Host': "health.sctu.edu.cn:56666",
    'Referer': "http://health.sctu.edu.cn:56666/login.aspx",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    }
headers2 = {
    'Host': 'health.sctu.edu.cn:56666',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://health.sctu.edu.cn:56666',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'http://health.sctu.edu.cn:56666/jktb2_all9.aspx',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}
default = r.get(url=loginurl,headers=headers)
login_data=searchdata(default.text)
login_data["__EVENTTARGET"]='Submit'
login_data["TextBox1"]=userid
login_data["TextBox2"]=passwd
login_data["TextBox3"]=''


res = r.post(url=loginurl,data=login_data,headers=headers)

checkin_data=searchdata(res.text)

#提交数据
checkin_data['jsnum']=''
checkin_data['jsxx']=''
checkin_data['sjh']=''
checkin_data['lxr']=''
checkin_data['lxrsjh']=''
checkin_data['szd']=''
checkin_data['r21']=''
checkin_data['prov']=''
checkin_data['ss11']=''
checkin_data['city']=''
checkin_data['ss12']=''
checkin_data['country']=''
checkin_data['ss13']=''
checkin_data['jtdz1']=''
checkin_data['r22']=''
checkin_data['prov2']=''
checkin_data['ss21']=''
checkin_data['city2']=''
checkin_data['ss22']=''
checkin_data['country2']=''
checkin_data['ss23']=''
checkin_data['jtdz2']=''
checkin_data['lxr2']=''
checkin_data['lxrsjh2']=''
checkin_data['qsh']=''
checkin_data['yy2']=''
checkin_data['prov3']=''
checkin_data['ss31']=''
checkin_data['city3']=''
checkin_data['ss32']=''
checkin_data['country3']=''
checkin_data['ss33']=''
checkin_data['jtdz3']=''
checkin_data['tw']=''
checkin_data['tw2']=''
checkin_data['tw3']=''
checkin_data['r4']=''
checkin_data['ms4']=''
checkin_data['r5']=''
checkin_data['sj5']=''
checkin_data['yy5']=''
checkin_data['r888']=''
checkin_data['btnfile']=''
checkin_data['img11']=''
checkin_data['czcs5']=''
checkin_data['r6']=''
checkin_data['prov4']=''
checkin_data['ss41']=''
checkin_data['city4']=''
checkin_data['ss42']=''
checkin_data['country4']=''
checkin_data['ss43']=''
checkin_data['jtdz6']=''
checkin_data['prov5']=''
checkin_data['ss51']=''
checkin_data['city5']=''
checkin_data['ss52']=''
checkin_data['country5']=''
checkin_data['ss53']=''
checkin_data['jtdz62']=''
checkin_data['jtfs7']=''
checkin_data['r7']=''
checkin_data['sj7']=''
checkin_data['prov6']=''
checkin_data['ss61']=''
checkin_data['city6']=''
checkin_data['ss62']=''
checkin_data['country6']=''
checkin_data['ss63']=''
checkin_data['jtdz7']=''
checkin_data['r8']=''
checkin_data['qkms8']=''
checkin_data['r9']=''
checkin_data['yy9']=''
checkin_data['dd9']=''
checkin_data['jt9']=''
checkin_data['r12']=''
checkin_data['yy12']=''
checkin_data['f13']=''
checkin_data['jzsj2']=''
checkin_data['cj1']=''
checkin_data['cj20']=''
checkin_data['cj2']=''
checkin_data['btnfile2']=''
checkin_data['img21']=''
checkin_data['r13']=''
checkin_data['r11']=''
checkin_data['sj11']=''
checkin_data['startsj']=''
checkin_data['endsj']=''
checkin_data['startsj2']=''
checkin_data['endsj2']=''
checkin_data['jt11_2']=''
checkin_data['jtfs11']=''
checkin_data['f12']=''
checkin_data['fyy12']=''
checkin_data['f14']=''
checkin_data['tj']=''



rescheckin = r.post(url=checkinurl,data=checkin_data,headers=headers2)
resultraw = BeautifulSoup(rescheckin.text,"html.parser")
result=resultraw.find_all("script")


print(result)






