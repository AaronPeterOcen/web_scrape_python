import requests
from bs4 import BeautifulSoup

resp = requests.get('https://news.ycombinator.com/newest')
# print(resp.text)
# using Beautiful Soup
sp = BeautifulSoup(resp.text, 'html.parser')
# print(sp)
# print(sp.find_all('a'))
# bs selectors
links = sp.select('.titleline')
votes = sp.select('.score')

# print(votes[0].get('id'))

def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        hn.append(title)
    return hn

print(create_custom_hn(links, votes))
