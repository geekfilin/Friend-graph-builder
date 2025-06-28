import vk_api
from vk_api.exceptions import VkApiError

class VKHarvester:
    def __init__(self, api_config):
        self.session = vk_api.VkApi(token=api_config['access_token'], api_version=api_config['api_version'])
        self.api = self.session.get_api()
    
    def get_user_connections(self, user_id):
        try:
            user_info = self.api.users.get(user_ids=user_id, fields="connections")[0]
            connections = {
                "user_id": user_info['id'],
                "username": f"id{user_info['id']}",
                "followers": [],
                "friends": []
            }
            
            followers = self.api.users.getFollowers(user_id=user_info['id'], fields="domain")['items']
            friends = self.api.friends.get(user_id=user_info['id'], fields="domain")['items']
            
            for user in followers:
                connections['followers'].append({
                    "id": user['id'],
                    "username": user.get('domain', f"id{user['id']}")
                })
            
            for user in friends:
                connections['friends'].append({
                    "id": user['id'],
                    "username": user.get('domain', f"id{user['id']}")
                })
                
            return connections
        
        except VkApiError as e:
            print(f"VK API Error: {e}")
            return None