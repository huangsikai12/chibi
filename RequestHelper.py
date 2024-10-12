import requests
import Constants



def sendPostRequest(url: str):
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'JSESSIONID=' + Constants.JSESSIONID,
    }
    data = {
        "fbsqid": Constants.HD_ID
    }
    response = requests.post(url, json=data, headers=headers)
    return response
