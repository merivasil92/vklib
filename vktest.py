import vk
import _mysql

session = vk.Session()
api = vk.API(session)

user = api.users.get(user_ids=1, fields=('career', 'status'))[0]
print user
print user['status']
print user['career']
print user['first_name']
print user['last_name']

followers = api.users.getFollowers(user_id=user['uid'], count=1)
count = followers['count']
offset = 0
while offset <= count:
    followers = api.users.getFollowers(user_id=user['uid'], offset=offset, count=1000)
    for uid in followers['items']:
        print uid
        follower = api.users.get(user_ids=uid, fields=('career', 'status'))[0]
        print follower.get('status', '')
    offset += 1000

try:
    con = _mysql.connect('127.0.0.1', 'admin', '', 'VK')
    con.query("SELECT VERSION()")
    result = con.use_result()
    print "MYSQL version: %s" % result.fetch_row()[0]
except _mysql.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
finally:
    if con:
        con.close()