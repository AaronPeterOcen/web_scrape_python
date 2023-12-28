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
subtext = sp.select('.subtext')

# print(votes[0].get('id'))

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        
        # getting the links  using href
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            print(points)
            hn.append({'title': title, 'link': href})
    return hn

(create_custom_hn(links, subtext))
