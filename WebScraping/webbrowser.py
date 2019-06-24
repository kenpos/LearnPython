import requests

res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
    res.status_code ==requests.codes.ok
    print('取得成功:{}'.format(res.status_code ))
    
except Exception as exc:
    print('問題発生:{}'.format(exc))
    

print(type(res))
print(res.status_code)
print(len(res.text))
print(res.text[:200])
