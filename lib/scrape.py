import requests



url = 'http://law.lis.virginia.gov/vacode'

response = requests.get(url)
html = response.content
print html