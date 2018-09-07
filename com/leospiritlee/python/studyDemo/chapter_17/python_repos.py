import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
resp = requests.get(url)

print("Status code :",resp.status_code)

resp_dict = resp.json()

print(resp_dict.keys())

# dict_keys(['total_count', 'incomplete_results', 'items'])

total_count_key = resp_dict['total_count']

print("Total repositories:", total_count_key)

item_key = resp_dict['items']

print('Repositories returned:', len(item_key))

item_1 = item_key[0]
print('\nkeys_1:', len(item_1))

# for key in sorted(item_1.keys()):
#     print(key)

# print("\nSelected information about first repository:")
# print('Name:', item_1['name'])
# print('Owner:', item_1['owner']['login'])
# print('Stars:', item_1['stargazers_count'])
# print('Repository:', item_1['html_url'])
# print('Created:', item_1['created_at'])
# print('Updated:', item_1['updated_at'])
# print('Description:', item_1['description'])


for item in item_key:
    print('\nName:', item['name'])
    print('Owner:', item['owner']['login'])
    print('Stars:', item['stargazers_count'])
    print('Repository:', item['html_url'])
    print('Created:', item['created_at'])
    print('Updated:', item['updated_at'])
    print('Description:', item['description'])


