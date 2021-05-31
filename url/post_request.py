import requests
import json

makeDto = {}


def notify():
    res = requests.get('http://localhost:8085/vehicle/v1/admin/makes?pageSize=1000')
    for make in res.json()['data']['list']:
        print(make['makeId'])
        makeDto['makeCode'] = make['makeCode']
        makeDto['makeName'] = make['makeName']
        makeDto['active'] = 'true'
        print(makeDto)
        print('http://localhost:8085/vehicle/v1/admin/makes/' + make['makeId'])
        requests.put('http://localhost:8085/vehicle/v1/admin/makes/' + make['makeId'], data=json.dumps(makeDto),headers={'Content-Type': 'application/json'})

    # requests.post('https://localhost:8085/vehicle/v1/admin/makes/', data=json.dumps({
    #     'text': content,  # 投稿するテキスト
    #     'username': u'me',  # 投稿のユーザー名
    #     'icon_emoji': u':ghost:',  # 投稿のプロフィール画像に入れる絵文字
    #     'link_names': 1,  # メンションを有効にする
    # }))


if __name__ == '__main__':
    notify()
