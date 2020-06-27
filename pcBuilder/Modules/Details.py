# Базовый класс "Деталь"
class Detail():
    def __init__(self, cost, name):
        self.cost = cost    # Цена компонента
        self.name = name    # Название компонента


# Процессор
class Porcessor(Detail):
    def __init__(self, cost, name, socket, freq, tdp, graphics):
        super().__init__(cost, name)
        self.socket = socket    # Сокет процессора
        self.freq = freq        # Частота процессора
        self.tdp = tdp          # Тепловыделение
        self.graphics = graphics  # Есть ли встроенный графический чип

# Кулер
class Cooler(Detail):
    def __init__(self, cost, name, tdp, height):
        super().__init__(cost, name)
        self.tdp = tdp
        self.height = height

# Материнская плата
class Motherboard(Detail):
    def __init__(self, cost, name, socket, ramSupport, mFormat):
        super().__init__(cost, name) 
        self.socket = socket            # Поддерживаемый CPU сокет
        self.ramSupport = ramSupport    # Поддерживаемый формат оперативной памяти
        self.mFormat = mFormat          # Формат платы (MicroATX, ATX, ...)

# Видеокарта
class Videocard(Detail):
    def __init__(self, cost, name, vRAM, maxPowConsumption, length):
        super().__init__(cost, name)
        self.vRAM = vRAM                           # Объем видеопамяти
        self.maxPowConsumption = maxPowConsumption # Максимальное энергопотребление
        self.length = length                       # Длина видеокарты

# Оперативная память
class RAM(Detail):
    def __init__(self, cost, name, memType, volume, freq, power):
        super().__init__(cost, name)
        self.memType = memType  # Тип используемой памяти (DDR3, DDR4, ...)
        self.volume = volume    # Объем памяти
        self.freq = freq        # Частота
        self.power = power      # Питание

# Корпус
class Body(Detail):
    def __init__(self, cost, name, mFormat, maxVideo, maxCooler):
        super().__init__(cost, name)
        self.mFormat = mFormat      # Формат поддерживаемой материнской платы
        self.maxVideo = maxVideo    # Максимальная длина видеокарты
        self.maxCooler = maxCooler  # Максимальная высота процессорного кулера
        
# Диск
class Drive(Detail):
    def __init__(self, cost, name, volume):
        super().__init__(cost, name)
        self.volume = volume

# Винчестер
class HDD(Drive):
    def __init__(self, cost, name, volume, spinSpeed, maxPower):
        super().__init__(cost, name, volume)
        self.spinSpeed = spinSpeed  # Скорость вращения шпинделя
        self.maxPower = maxPower    # Максимальное энергопотребление
        
        
# Твердотельный накопитель
class SSD(Drive):
    def __init__(self, cost, name, volume, maxIn, maxOut):
        super().__init__(cost, name, volume)
        self.maxIn = maxIn      # Максимальная скорость записи
        self.maxOut = maxOut    # Максимальная скорость чтения

# Блок питания
class PowSuply(Detail):
    def __init__(self, cost, name, maxPower, eEfficiency):
        super().__init__(cost, name)
        self.maxPower = maxPower        # Максимальная мощность
        self.eEfficiency = eEfficiency  # Сертификат 80+ 
