import sys 
import requests

# https://gihyo.jp/dp とかテストがてらに使い勝手良い

url = sys.argv[1]

r = requests.get(url)
print(f'encoding:{r.encoding}',file=sys.stderr)
print(r.text)
