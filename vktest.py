import vk

session = vk.Session()
api = vk.API(session)
user = api.users.get(user_ids=1)[0]
print user['first_name']
print user['last_name']
print user['uid']
print api.users.getFollowers(user_id=user['uid'])
print
