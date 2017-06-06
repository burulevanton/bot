import command_system

def hello(text):
   message = 'Привет, друг!\nЯ новый чат-бот.'
   return message, ''

hello_command = command_system.Command()

hello_command.keys = ['привет', 'hello', 'здравствуй', 'здравствуйте']
hello_command.description = 'Поприветствую тебя'
hello_command.process = hello