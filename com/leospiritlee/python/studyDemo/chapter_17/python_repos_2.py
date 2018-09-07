import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LC

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
resp = requests.get(url)

status_code = resp.status_code

print('Status Code:', status_code)

resp_json = resp.json()

print('Total repositories:', resp_json['total_count'])

resp_items = resp_json['items']

names, stars = [],[]

for resp_item in resp_items:
    names.append(resp_item['name'])
    stars.append(resp_item['stargazers_count'])

my_style = LC('#333366', base_style=LCS)

chart = pygal.Bar(style=my_style, x_lable_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos_2.svg')




