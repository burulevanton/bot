import command_system
import vkapi
import re
from plotsystem import plot_system

def sub(text):
    text = re.sub('https://vk.com/','',text)
    return vkapi.get_id(text)


def plot(text):
    text = text.split()
    if len(text)<2:
        return 'неверные данные', ''
    count = text[1]
    if int(count)<1 or int(count)>100:
        return 'Неправильно задан параметр количество записей, максимум 100', ''
    if len(text)==3:
        owner_id = sub(text[2])
        plot_system(vkapi.get_wall(count=count, owner_id = owner_id))
    else:
        plot_system(vkapi.get_wall(count=count))
    message = ''
    attachment = vkapi.upload_photo('likes')
    attachment = attachment + ',' + vkapi.upload_photo('views')
    attachment = attachment + ',' + vkapi.upload_photo('comments')
    return message, attachment


plot_command = command_system.Command()

plot_command.keys = ['график']
plot_command.description = 'График для администратора'
plot_command.process = plot
