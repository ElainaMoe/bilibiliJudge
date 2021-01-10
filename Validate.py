import requests as r

validate_url='http://api.bilibili.com/x/credit/jury/jury'
def Validate(access_key):
    params={'access_key': access_key}
    info=r.get(validate_url,params=params)
    return info