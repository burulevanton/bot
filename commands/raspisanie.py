import command_system
from answer_pars import rasp_chisl, rasp_today, rasp_znam, rasp_zvon,rasp_exams, rasp_konsul
import datetime

def get_rasp(text):
    numbers = [str(i) for i in range(1, 8)]
    # Расписание на завтра
    if text == 'на завтра':
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        wd = tomorrow.weekday()
        chisl = tomorrow.isocalendar()[1] % 2
        return rasp_chisl[wd] if chisl else rasp_znam[wd]
    # Расписание на день недели
    elif text in numbers:
        i = int(text) - 1
        if rasp_chisl[i] == rasp_znam[i]:
            return rasp_today[i] + rasp_chisl[i]
        else:
            return '%sПервая неделя:\n%s\nВторая неделя:\n%s' % (
                rasp_today[i],
                rasp_chisl[i],
                rasp_znam[i])
    # Расписание звонков
    elif text == 'звонков':
        return rasp_zvon
    # Расписание консультаций
    elif text == 'консультаций':
        return rasp_konsul
    # Расписание звонков
    elif text == 'экзаменов':
        return rasp_exams
    # Расписание на сегодня
    else:
        today = datetime.date.today()
        wd = today.weekday()
        chisl = today.isocalendar()[1] % 2
        return rasp_chisl[wd] if chisl else rasp_znam[wd]


def raspisanie(text):
    text = text.replace('расписание ', '')
    message = get_rasp(text)
    return message, ''

hello_command = command_system.Command()

hello_command.keys = ['расписание']
hello_command.description = 'Расписание'
hello_command.process = raspisanie