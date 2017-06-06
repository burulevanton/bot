import vkapi
import re
from settings import admin_token,group_id

ban_dict = {}

def isFive(text):
    t = re.sub('\W', ' ', text).split()
    return len(t)<5


def isNotWeb(text):
    text = re.sub(r'https://','',text)
    text = re.sub(r'http://','',text)
    text = re.sub('www.','',text)
    text = re.match('\w+\.\w+', text)
    return not text==None


def bot(comment):
    text = comment['text']
    if isFive(text) or isNotWeb(text):
        vkapi.wall_delete_comment(token = admin_token, comment_id = comment['id'], owner_id = group_id)
        id = comment['from_id']
        if id not in ban_dict.keys():
            ban_dict[id] = 1
        else:
            ban_dict[id] = ban_dict[id]+1
        if(ban_dict[id] >3):
            ban_dict[id] = 0
            vkapi.ban_user(time = comment['date'], id = id)