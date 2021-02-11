# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# 5. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# 6. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from abc import ABC, abstractmethod


class Warehouse:
    storage = {'Printers': list(), 'Scanners': list(), 'Copiers': list()}
    subdivisions = ['admin', 'counting', 'hr']

    @classmethod
    def start(cls):
        while True:
            action = input("\n't' - take, 'g' - give, 's' - see storage: ")
            if action == 't':
                try:
                    print("Describe equipment with important parameters:")
                    unit_name, paper_size, arg1, arg2 = input().split()
                except ValueError:
                    print("Value error. Check input data")
                    continue
                if unit_name == 'printer':
                    if Printer.check_enter(paper_size, arg1, arg2):
                        Warehouse.take(Printer(paper_size=paper_size,
                                               paper_cap=int(arg1),
                                               print_tech=arg2))
                    else:
                        continue

                elif unit_name == 'scanner':
                    if Scanner.check_enter(paper_size, arg1, arg2):
                        Warehouse.take(Scanner(paper_size=paper_size,
                                               dpi=int(arg1),
                                               lamp=arg2))
                    else:
                        continue

                elif unit_name == 'copier':
                    if Copier.check_enter(paper_size, arg1, arg2):
                        arg2 = True if arg2 == 'analog' else False
                        Warehouse.take(Copier(paper_size=paper_size,
                                              mode=arg1,
                                              copy_type=arg2))
                    else:
                        continue
                else:
                    print("Check equipment name")
                    continue

            elif action == 'g':
                try:
                    print("Describe equipment with important parameters:")
                    subdivision, unit_name, paper_size, arg1, arg2 = input().split()
                except ValueError:
                    print("Value error. Check input data")
                    continue
                if (unit_name == 'printer' and Printer.check_enter(paper_size, arg1, arg2) or
                        unit_name == 'scanner' and Scanner.check_enter(paper_size, arg1, arg2) or
                        unit_name == 'copier' and Copier.check_enter(paper_size, arg1, arg2)):
                    Warehouse.give_away(subdivision, unit_name, paper_size, arg1, arg2)

            elif action == 's':
                print('\n.:WAREHOUSE:.')
                for k, v in Warehouse.storage.items():
                    print(k)
                    for el in v:
                        print(el)
                    print()

    @classmethod
    def take(cls, unit):
        if unit.name == 'printer':
            cls.storage['Printers'].append(unit)
        elif unit.name == 'scanner':
            cls.storage['Scanners'].append(unit)
        elif unit.name == 'copier':
            cls.storage['Copiers'].append(unit)
        print("Unit has been successfully added to warehouse!")

    @classmethod
    def give_away(cls, subdivision, unit_name, paper_size, arg1, arg2):
        if subdivision in cls.subdivisions:
            if unit_name == 'printer':
                paper_cap = int(arg1)
                print_tech = arg2
                for p in Warehouse.storage.get('Printers'):
                    if p.paper_size == paper_size and p.paper_cap == paper_cap and p.print_tech == print_tech:
                        Warehouse.storage.get('Printers').remove(p)
                        return p

            elif unit_name == 'scanner':
                dpi = int(arg1)
                lamp = arg2
                for s in Warehouse.storage.get('Scanners'):
                    if s.paper_size == paper_size and s.dpi == dpi and s.lamp == lamp:
                        Warehouse.storage.get('Scanners').remove(s)
                        return s

            elif unit_name == 'copier':
                mode = arg1
                copy_type = True if arg2 == 'analog' else False
                for c in Warehouse.storage.get('Copiers'):
                    if c.paper_size == paper_size and c.mode == mode and c.copy_type == copy_type:
                        Warehouse.storage.get('Copiers').remove(c)
                        return c

            print(f"We don't have what '{subdivision}' need. Please check request.")
        else:
            print(f"We haven't subdivision '{subdivision}'.")


class OfficeEquipment(ABC):
    _paper_sizes = ['Letter', 'Legal', 'Executive', 'A3', 'A4', 'A5']

    def __init__(self, name, paper_size):
        self.name = name
        self.paper_size = paper_size

    @abstractmethod
    def __str__(self):
        pass


class Printer(OfficeEquipment):
    __printing_technology = ['laser', 'LED', 'inkjet']

    def __init__(self, paper_size, paper_cap, print_tech, name='printer'):
        super(Printer, self).__init__(name, paper_size)
        self.paper_cap = paper_cap
        self.print_tech = print_tech

    def __str__(self):
        return f'{self.paper_size}, {self.paper_cap}, {self.print_tech}'

    @classmethod
    def check_enter(cls, paper_size, paper_cap, print_tech):
        ok = 0

        if paper_size in super()._paper_sizes:
            ok += 1
        else:
            print(f"Printers don't have '{paper_size}' paper size")

        try:
            paper_cap = int(paper_cap)
            ok += 1
        except ValueError:
            print("You've entered NaN to paper capacity of printer")

        if print_tech in cls.__printing_technology:
            ok += 1
        else:
            print(f"Printers don't have '{print_tech}' printing technology")

        if ok == 3:
            return True
        else:
            return False


class Scanner(OfficeEquipment):
    __dpi_list = [300, 600, 900, 1200]
    __lamps = ['xenon', 'fluorescent', 'LED']

    def __init__(self, paper_size, dpi, lamp, name='scanner'):
        super(Scanner, self).__init__(name, paper_size)
        self.dpi = dpi
        self.lamp = lamp

    def __str__(self):
        return f'{self.paper_size}, {self.dpi}, {self.lamp}'

    @classmethod
    def check_enter(cls, paper_size, dpi, lamp):
        ok = 0

        if paper_size in super()._paper_sizes:
            ok += 1
        else:
            print(f"Scanners don't have '{paper_size}' paper size")

        try:
            if int(dpi) in cls.__dpi_list:
                ok += 1
            else:
                print("You've entered incorrect dpi")
        except ValueError:
            print("You've entered NaN to paper capacity of printer")

        if lamp in cls.__lamps:
            ok += 1
        else:
            print(f"Scanners don't have '{lamp}' lamps")

        if ok == 3:
            return True
        else:
            return False


class Copier(OfficeEquipment):
    __modes = ['wb', 'c', 'g']

    def __init__(self, paper_size, mode, copy_type, name='copier'):
        super(Copier, self).__init__(name, paper_size)
        self.mode = mode
        self.copy_type = copy_type

    def __str__(self):
        return f'{self.paper_size}, {self.mode}, {self.copy_type}'

    @classmethod
    def check_enter(cls, paper_size, mode, copy_type):
        ok = 0

        if paper_size in super()._paper_sizes:
            ok += 1
        else:
            print(f"Copier don't have '{paper_size}' paper size")

        if mode in cls.__modes:
            ok += 1
        else:
            print(f"Copier don't have '{mode}' mode")

        if copy_type == 'analog' or copy_type == 'digital':
            ok += 1
        else:
            print("Check copy type. Analog or digital?")

        if ok == 3:
            return True
        else:
            return False


Warehouse.take(Printer('A4', 300, 'laser'))
Warehouse.take(Printer('A5', 500, 'inkjet'))
Warehouse.take(Printer('A3', 200, 'LED'))
Warehouse.take(Scanner('Letter', 900, 'fluorescent'))
Warehouse.take(Scanner('Executive', 300, 'xenon'))
Warehouse.take(Copier('A4', 'wb', 'digital'))
Warehouse.give_away('admin', 'printer', 'A3', 200, 'LED')
Warehouse.start()
