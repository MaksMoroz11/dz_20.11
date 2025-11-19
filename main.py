from modules.TaskManager import TaskManager

task_manager = TaskManager()
task_manager.load_from_file()

while (command := input('Введите команду: ')) and command != 'exit':
    if command == 'add':
        name_task = input('Введите название задачи: ')
        task_manager.add_task(name_task)
    elif command == 'done':
        name_task = input('Введите название задачи: ')
        task_manager.mark_task_done(name_task)
    elif command == 'show':
        task_manager.show_tasks()
    else:
        print('Неизвестная команда.')
    print()

task_manager.save_to_file()