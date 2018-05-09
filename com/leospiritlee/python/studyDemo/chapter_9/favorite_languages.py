from collections import  OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['tim'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

print(favorite_languages)

for name,language in favorite_languages.items():
    print(name.title() + ' favorite language is ' + language.title())