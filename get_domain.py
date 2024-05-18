import requests
from lxml import etree

# 发送请求
# response = requests.get('https://www.dxsbb.com/news/1396.html')
# # 设置正确的字符编码
# response.encoding = 'utf-8'  # 或者其他正确的字符编码
# # 解析 HTML
# html = etree.HTML(response.text)
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,vi;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.aizhan.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'linux',
}
# 使用 XPath 定位标签
sum=0
# for i in range(2,789):
#     result = html.xpath('/html/body/div[5]/div[1]/div[1]/div[2]/div/table/tbody/tr['+str(i)+']/td[2]')
#                   /html/body/div[5]/div[1]/div[1]/div[2]/div/table/tbody/tr[3]/td[2]
#                   /html/body/div[5]/div[1]/div[1]/div[2]/div/table/tbody/tr[788]/td[2]
# 输出结果
    #title=result[0].text
with open('./主体单位.txt','r',encoding='utf-8') as company:
    for title in company:
        title=title.replace('\n','')
        #print(title)
        url='https://icp.aizhan.com/reverse-icp/?q='+str(title)+'&t=company'
        #print(url)
    
        try:
            #pass
            response1=requests.get(url=url,headers=headers)

            html1=etree.HTML(response1.text)

            result1 = html1.xpath('/html/body/div[4]/div[3]/div/div[2]/table/tbody/tr/td[3]/a')
            #print(result1)
            domain=result1[0].text
           # print(domain)
            if domain!='':
                sum+=1
                with open('./result.txt','a') as file:
                    file.write(domain+'\n')
                    print(result1[0].text)

        except:
            pass
# print("共计:",sum,'条域名')
