class Task:
    __is_done = False
    def __init__(self, name, is_done=False):
        self.__title = name
        self.__is_done = is_done

    def mark_done(self):
        self.__is_done = True

    @property
    def title(self):
        return self.__title

    @property
    def is_done(self):
        return 'Выполнена' if bool(self.__is_done) is True else 'Не выполнена'