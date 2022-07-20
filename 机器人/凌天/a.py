import requests


def get_data(sya):
    access_token = '24.8ae617c9be3d5810152384b8e47d3be5.2592000.1660661260.282335-26727598'
    url = 'https://aip.baidubce.com/rpc/2.0/unit/service/v3/chat?access_token=' + access_token
    post_data = {
        "version": "3.0",
        "service_id": "S72336",
        "session_id": " ",
        "log_id": "7758521",
        "request": {"terminal_id": "88888",
                    "query": sya}
    }

    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, json=post_data, headers=headers)
    data = response.json()['result']['responses'][0]['actions'][0]['say']

    return data


da = get_data('hhh')
print(da)