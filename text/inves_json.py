import json
# import requests

f = open('jsn', 'r', encoding='utf-8')
# regex = r'アクセス:\s+(.*)\s+'
lis = []
i = 0

js = json.loads(f.read())
print(len(js))


# for elm in js['data']['list']:
#     if elm['vehicleImage'] is not None:
#         sc = requests.get(elm['vehicleImage']).status_code
#         if sc != 200:
#             print(sc)
#             print(elm['vehicleImage'])
