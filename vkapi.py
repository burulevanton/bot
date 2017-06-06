import vk
import requests
from settings import token,admin_token,group_id,message

session = vk.Session()
api = vk.API(session, v=5.64)


def send_message(user_id, token, message, attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment)

def wall_delete_comment(token, comment_id, owner_id):
    api.wall.deleteComment(access_token = token, comment_id = comment_id, owner_id = owner_id)

def get_id(group_id):
    return '-'+str(api.groups.getById(access_token = token, group_id = group_id)[0]['id'])


def get_wall(count,owner_id='-29534144'):
    result = api.wall.get(access_token = admin_token, owner_id=owner_id, count=count)
    result = result['items']
    return result

def ban_user(time, id):
    api.groups.banUser(access_token = admin_token, user_id = id, group_id = 147133771, end_date = time+300, comment = message, comment_visible = 1)

def upload_photo(name):
    url = api.photos.getMessagesUploadServer(access_token = token)
    upload_url = url.get('upload_url')
    file_ = {'photo': (name+'.png', open(name+'.png', 'rb'))}
    r = requests.post(url=upload_url, files=file_)
    result = r.json()
    result = api.photos.saveMessagesPhoto(access_token = token, photo=result['photo'], server=result['server'], hash=result['hash'])
    owner_id = str(result[0]['owner_id'])
    id = str(result[0]['id'])
    return 'photo'+owner_id+'_'+id


def upload_file():
    url = api.docs.getUploadServer(access_token = admin_token,group_id = group_id.replace('-',''), type='audio_message')
    upload_url = url.get('upload_url')
    file = {'file': ('audio.ogg', open('audio.ogg', 'rb'))}
    r = requests.post(url=upload_url, files=file)
    file = r.json()['file']
    result = api.docs.save(access_token = admin_token, file=file)
    owner_id = str(result[0]['owner_id'])
    id = str(result[0]['id'])
    return 'doc'+owner_id+'_'+id