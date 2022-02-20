from datetime import datetime
from zoneinfo import ZoneInfo
from venmo_api import Client
import os
import math

# getting the current time in PST
local_tz = ZoneInfo("US/Pacific")
utc_time = datetime.utcnow()
local_time = utc_time.astimezone(local_tz)

# authenticating with venmo API
client = Client(access_token = os.environ.get('venmo_token'))

# dict of user_ids to usernames
# hopefully I can refactor this into a web dashboard
user_dict = {
    '2507792346775552606': 'yourtriggered', 
    '2828373562753024707': 'mangekyomaster', 
    '3151324359163904454': 'yu_xxincheng', 
    '2313403662073856986': 'axie846', 
    '2275877610061824186': 'jyun1700'
}

# the amount that I have to charge
amount = 15.99

# function to check if the users I'm charging are also my friends on venmo
def users_are_friends(user_ids):
    """
    check if users from list of user_ids are in your friends list
    :param user_ids: <list[str]> a list of user_ids

    :return: <bool> true if all are friends, false if not
    """

    print("checking if users are friends on venmo...")
    
    friends = client.user.get_user_friends_list(
        user_id = client.my_profile().id
    )

    # algo:
    # iterate through friends list, and if i see an ID that's in
    # my to-charge list, I remove it.  
    user_ids_cpy = set(user_ids)
    for friend in friends:
        if friend.id in user_ids:
            user_ids_cpy.remove(friend.id)
    
    # if there are any IDs that are left, that means they are not in
    # my friends list. Log it, and maybe send me an email
    # TODO: send me an email if ID not in friends list
    if len(user_ids_cpy) != 0:
        for user_id in user_ids_cpy:
            # log that the user is not my friend on venmo
            print(f"User [{user_id} : {user_dict[user_id]}] is not in your venmo friends list!")
    else:
        print("all good!")

    return len(user_ids_cpy) == 0

# for rounding up to the nearest cent
def round_up(money):
    """
    round up money to the nearest cent
    ex: 
    $2.6666 => $2.67
    $3.1111 => $3.12

    :param money: <float> amount of money in dollars

    :return: <float> the money rounded up to the nearest cent
    """
    money *= 100
    money = math.ceil(money)
    return money / 100

# for my purposes only, only charge for spotify
# on every 27th of the month
if local_time.day == 27:
    # log that it is the 27th
    print("It is the 27th!!!!")

    user_ids = list(user_dict.keys())

    amount_per_person = round_up(amount / len(user_ids))
    
    # we'll deal with what happpens if a person is not a friend later...
    are_friends = users_are_friends(user_ids)
    
    for user_id in user_ids:
        client.payment.request_money(
            amount_per_person, 
            "🤖beep boop🤖 spotify premium for family", 
            user_id
        )
else:
    print("It is not the 27th")

print("fin")