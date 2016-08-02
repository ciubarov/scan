import requests
class VKApi(object):
    
    def __init__(self, uid, token):
        self.token = token
        self.uid = uid
        
    def get_profile_data(self):
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params={
                'access_token': self.token,
                'fields': 'photo_50,sex,bdate,country,city, domain, can_post'
        }).json()
        
        return response.get('profile')
    
    def get_friends_list(self):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'user_id': self.uid,
                'access_token': self.token,
                'fields': 'photo_50,first_name,last_name,can_post'
            }
        ).json()

        return response.get('response')