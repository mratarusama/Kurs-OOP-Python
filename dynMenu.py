from os import system
import curses
import sys

# Класс "Действие" - выполняется при нажатии на Enter
class Action(object):
    def __init__(self, id, method, description, *method_args):
        self.id = id
        self.method = method
        self.description = description
        self.method_args = method_args

    def execute(self):
        if self.method_args == ():
            self.method()
        else:
            self.method(self.method_args)

# Класс "Меню", содержит все поля и предоставляет возможность выберать между ними
class Menu(object):
    def __init__(self, title, prev_menu=None):
        self.title = title         # Заголовок меню
        self.actions = []          # Пункты меню, изначально пустые
        self.prev_menu = prev_menu # Ссылка на предыдущее меню
        self.actions.append(
            Action(
              0,
              self.back,
              "Back"
            )
        )                          # Добавляем кнопку "Назад"
        self.selected = 1          # Выбранный номер в меню
        self.maxEl = 1             # Текущее количество пунктов

    # Добавление нового пункта в меню
    def register_action(self, method, description, *method_args):
        self.actions.append(Action(self.maxEl, method, description, *method_args))
        self.maxEl += 1       

    # Возвращение назад в иерархии меню
    def back(self):
        if self.prev_menu:
            # Если есть указатель на предыдущее меню, то идем туда
            self.prev_menu.start()
        else:
            # Иначе, выходим из программы
            curses.endwin()
            sys.exit(0)

    # Запуск меню
    def start(self):
        while True:
            curses.wrapper(self.print_menu)
            curses.wrapper(self.choice)
    
    # Выбор пунктов в меню
    def choice(self, stdscr):
        while True:
            key = stdscr.getch()
            # Переход выше в меню
            if key in (curses.KEY_UP, ord('w'), ord('ц')) and self.selected > 1:
                self.print_element(self.selected, 0, self.actions[self.selected-1], False, stdscr)
                self.selected -= 1
                self.print_element(self.selected, 0, self.actions[self.selected-1], True, stdscr)
            # Переход ниже в меню
            elif key in (curses.KEY_DOWN, ord('s'), ord('ы')) and self.selected < self.maxEl:
                self.print_element(self.selected, 0, self.actions[self.selected-1], False, stdscr)
                self.selected += 1
                self.print_element(self.selected, 0, self.actions[self.selected-1], True, stdscr) 
            # Выбор выбранного элемента
            elif key == curses.KEY_ENTER or key in [10, 13]:
                break
            stdscr.refresh()
        curses.endwin()
        system("cls")
        self.actions[self.selected-1].execute()
    
    # Начальный вывод всех элементов меню
    def print_menu(self, stdscr):
        stdscr.clear()
        curses.curs_set(0)
        stdscr.addstr(0, 0, self.title)
        
        for i, action in enumerate(self.actions):
            if(i+1 == self.selected): 
                self.print_element(i+1, 0, action, True, stdscr)
            else:
                self.print_element(i+1, 0, action, False, stdscr)
                
        stdscr.refresh()
    
    # Вывод одного элемента меню
    def print_element(self, x, y, action, selected, stdscr):
        if selected:
            stdscr.addstr(x, y, f"{action.id}. {action.description}", curses.A_REVERSE)
        else:
            stdscr.addstr(x, y, f"{action.id}. {action.description}")