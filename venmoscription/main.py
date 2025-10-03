import math
import json
import sys
import logging
import os
from datetime import datetime
from venmo_api import Client
from venmoscription.default_config import settings

logging.basicConfig(
    level=logging.INFO,  # Show INFO messages and above
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

client = Client(access_token=settings.venmo_token)
friend_ids = [
    friend.id
    for friend in client.user.get_user_friends_list(user_id=client.my_profile().id)
]


def round_up(money):
    money *= 100
    money = math.ceil(money)
    return money / 100


def get_user_id(username):
    user = client.user.get_user_by_username(username)
    return user.id


def is_friend(user_id):
    return user_id in friend_ids


venmo_config_path = os.path.join(os.path.dirname(__file__), "venmo_config.json")
with open(venmo_config_path, "r") as f:
    venmo_config: dict = json.load(f)

now = datetime.now()
curr_month = f"{now.month}/{now.year}"

test = sys.argv[1].lower() == "test"
not_friends = set()
for service, details in venmo_config.items():
    amt_per_person = round_up(details["total"] / len(details["usernames"]))

    for username in [
        uname for uname in details["usernames"] if uname != "wannabe-rich"
    ]:
        user_id = get_user_id(username)
        if not is_friend(user_id):
            not_friends.add(username)
            continue
        service_name = service.replace("_", " ")
        description = f"{service_name} {curr_month}"
        if test:
            logger.info(msg=f"description:\"{description}\" username:{username} user_id:{user_id}")
        else:
            client.payment.request_money(amt_per_person, description, user_id)

if len(not_friends) > 0:
    raise RuntimeError(f"{not_friends} are not my friends on venmo")
raise RuntimeError("test error")