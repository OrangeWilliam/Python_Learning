import re
import time
import xml.dom.minidom
import sys
ENCODE="gbk"

def pipei(str):
    pattern = re.compile('\<\?xml version=\"1\.0\" encoding=\"GBK\"\?\>.*?\<\/Root\>',re.S)
    return pattern.findall(str)

def readFile():
    with open("400121.TXT", "r", encoding=ENCODE) as f:
        context = f.read()
        #print(context)
        return context

def writrFilre(str):
    with open("output.TXT", "a", encoding=ENCODE) as f:
        f.write(str)

def praseXml(str):
    xml_dom = xml.dom.minidom.parseString(str)
    collection = xml_dom.documentElement
    bodys = collection.getElementsByTagName("Body")
    #Heads = collection.getElementsByTagName("Head")
    #for head in Heads:
        #if(not head.getElementsByTagName('retCode')):
            #print(str)
    for body in bodys:
        if(body.getElementsByTagName('KEHUXM')):
            str1=body.getElementsByTagName('ZH1HAO')[0].childNodes[0].data
            str2=body.getElementsByTagName('KEHUXM')[0].childNodes[0].data
            str3=body.getElementsByTagName('ZHIYEE')[0].childNodes[0].data
            str4=""
            if(body.getElementsByTagName('SHMING')[0].childNodes):
                str4=body.getElementsByTagName('SHMING')[0].childNodes[0].data
            writrFilre(str1+"|"+str2+"|"+str3+"|"+str4+'\n')

def parseContent(str):
    pass

if __name__=="__main__":
    startTime=time.time()
    for i in pipei(readFile()):
        praseXml(i)

    endTime=time.time()
    print(endTime-startTime)