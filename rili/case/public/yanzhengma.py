import base64
import requests

def yzm():
    url='https://aip.baidubce.com/oauth/2.0/token'
    data={
    'grant_type':'client_credentials',
        'client_id':'tdoDwXucO18NcUCXH6bOQWlr',
        'client_secret':'FaXK1LehGxGEWbNCMt8DEeVSrEFKNdqK'
    }
    response = requests.post(url=url, data=data).json()
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    f = open('canvas.png', 'rb')
    img = base64.b64encode(f.read())
    params = {"image":img}
    access_token = response['access_token']
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response1 = requests.post(request_url, data=params, headers=headers)
    if response1:
        return (response1.json()['words_result'][0]['words'])
if __name__ == '__main__':
    print(yzm())