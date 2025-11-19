import json
from modules.Task import Task

class TaskManager:
    def __init__(self):
        self.__tasks = []

    def add_task(self, title):
        task = Task(title)
        self.__tasks.append(task)
        print(f'Задача "{title}" успешна добавлена.')

    def mark_task_done(self, title):
        found = False
        for task in self.__tasks:
            if task.title == title:
                found = True
                task.mark_done()
                print(f'Задача "{title}" отмечена как выполненная.')
                break
        if not found:
            print(f'Нет задачи с именем "{title}"')

    def show_tasks(self):
        len_tasks = len(self.__tasks)
        if len_tasks != 0:
            for i in range(len_tasks):
                print(f'{i+1}. {self.__tasks[i].title} - {self.__tasks[i].is_done}')
        else:
            print('Нет задач.')

    def save_to_file(self):
        tasks = []
        for task in self.__tasks:
            tasks.append({'title': task.title, 'is_done': task.is_done})
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file)
        print('Данные сохранены. Программа завершена.')

    def load_from_file(self):
        try:
            tasks = {1: 2}
            with open('tasks.json') as file:
                tasks = json.load(file)
            for task in tasks:
                self.__tasks.append(Task(task['title'], task['is_done'] == 'Выполнена'))
            print(f'Данные успешно загружены. Всего задач {len(self.__tasks)}.')
        except FileNotFoundError:
            print('Файл не найден, список задач пуст.')
        except json.decoder.JSONDecodeError:
            print('Файл некорректно сохранён, список задач пуст.')
