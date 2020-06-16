import requests

from urllib.parse import urlencode


OAUTH = 'https://oauth.vk.com/authorize'
params_dict = {
    'client_id': 7508143,
    'display_page': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v' : 5.89
}

# print('?'.join((OAUTH,urlencode(params_dict))))

TOKEN_VALUE = 'e8a677cf963590ae4fce6e2d23e0ee33c04ba5a9280120ad940ca05f5ad60c0d4fbfb46f4318ccb740753'

params = {
    'source_uid' : 96387738,
    'access_token': TOKEN_VALUE,
    'target_uid': '7508143',
    'v': 5.89
}

response = requests.get('https://api.vk.com/method/friends.getMutual',params)

# print(response.json()['response'])


class Users:
    def __init__(self,id = str ,token = str)-> None:
        self.token = token
        self.id = id
        self.v = 5.89

    def __and__(self, other_user):
        params = {
            'source_uid': self.id,
            'access_token': self.token,
            'target_uid': other_user.id,
            'v': 5.89
        }

        mutal_user_list = []

        response = requests.get('https://api.vk.com/method/friends.getMutual', params)

        ids = response.json()['response']
        for values in ids:
            mutal_user_list.append(Users(str(values),TOKEN_VALUE))
        return mutal_user_list

    def print(self):
        string = 'https://vk.com/id'
        print(string+self.id)

Alex = Users('344671718',TOKEN_VALUE)
Slava = Users('96387738', TOKEN_VALUE)

for values in Alex & Slava:
    values.print()
