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
                'fields': 'photo_100,sex,bdate,country,city, domain, can_post'
        }).json()
        
        return response.get('profile')
    
    def get_friends_list(self):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'user_id': self.uid,
                'access_token': self.token,
                'fields': 'photo_100,first_name,last_name,can_post'
            }
        ).json()

        return response.get('response')

    def wall_post(self, message):
        response = requests.get(
            'https://api.vk.com/method/wall.post',
            params={
                'access_token': self.token,
                'message': message
            }
        ).json()

        return response.get('response')