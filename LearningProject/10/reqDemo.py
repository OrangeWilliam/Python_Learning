import requests
def search_Douban(keyword):
    url="https://www.douban.com/search"
    params={
        "q":keyword
    }
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
    }
    resp=requests.request("GET",url,params=params,headers=headers)
    #print(resp)
    #print(resp.text)
    return resp

if __name__=='__main__':
    req_jd("你好李焕英")