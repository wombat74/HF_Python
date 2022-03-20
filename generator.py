import requests

urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com', 'http://gmail.com', 'http://google.com')

# for resp in [requests.get(url) for url in urls]:
#     print(len(resp.content), '->', resp.status_code, '->', resp.url)

for resp in (requests.get(url) for url in urls):
    print(len(resp.content), '->', resp.status_code, '->', resp.url)