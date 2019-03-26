import sys
import requests

# try:
#     servername = 'http://' + sys.argv[1:]
# except:
#     servername = 'http://khatangatao.com'
#
# print(servername)

target = 'http://khatangatao.com/api/entry/'
headers = {"Authorization": "Bearer 56a4f78b7f4a6990d3ae6c223a73249b8765c0c1"}

r = requests.get(target, headers=headers)
print(r.status_code)

print(r.text)