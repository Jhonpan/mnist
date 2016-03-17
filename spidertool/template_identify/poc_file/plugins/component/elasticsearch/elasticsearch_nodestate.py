#!/usr/bin/env python
# encoding: utf-8
from t import T

import requests,urllib2,json,urlparse
class P(T):
    def __init__(self):
        T.__init__(self)
    def verify(self,head='',context='',ip='',port='',productname='',keywords='',hackinfo=''):
        target_url = "http://"+ip+":9200/_nodes/stats"
        result = {}
        result['result']=False
        try:
            r=requests.get(url=target_url,timeout=2)
            if r.status_code==200:
                result['result']=True
                result['VerifyInfo'] = {}
                result['VerifyInfo']['type']='information unclosed'
                result['VerifyInfo']['URL'] =ip+":9200/_nodes/stats"
                result['VerifyInfo']['payload']='IP:9200/_nodes/stats'
                result['VerifyInfo']['result'] =r.text
            else:
                pass
        except Exception,e:
            print e.text
        finally:
            return result
if __name__ == '__main__':
    print P().verify(ip='42.120.7.130',port='9200')          
