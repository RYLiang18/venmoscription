from venmo_api import Client
import os
import sys

client = Client(access_token = os.environ.get('venmo_token'))


def is_friend(user_id):
    my_friends = client.user.get_user_friends_list(
        user_id = client.my_profile().id
    )

    my_friend_ids = [friend.id for friend in my_friends]
    return user_id in my_friend_ids

user= client.user.get_user_by_username(username=sys.argv[1])
print("========================================")
print(f"id: {user.id}")
print(f"username: {user.username}")
print(f"is_friend: {is_friend(user.id)}")
print("========================================")




