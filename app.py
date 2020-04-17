import requests
import json

url = 'https://papermc.io/api/v1/paper/1.15.2'

r = requests.get(url)

versions = json.loads(r.text)
latest = versions['builds']['latest']

print(f'Latest version: {latest}')
print('Downloading')

url += f'/{latest}/download'

r = requests.get(url)

open('./paper.jar', 'w+b').write(r.content)
