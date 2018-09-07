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

my_config = pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.lable_font_size=24
my_config.major_lable_font_size=18
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000



chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos_3.svg')




