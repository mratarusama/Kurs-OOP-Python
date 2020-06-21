from enum import Enum

# Форматы материнский плат
class MotherFormats(Enum):
    miniITX  = 1 # 170 × 170
    microATX = 2 # 244 × 244
    mBTX     = 3 # 264 × 267
    ATX      = 4 # 305 × 244
    EATX     = 5 # 305 × 330

# Типы оперативной памяти
class MemType(Enum):
    SIMM = 1
    DIMM = 2
    DDR  = 3
    DDR2 = 4
    DDR3 = 5
    DDR4 = 6

# Сертефикаты энергоэффективности 80+
class energyCert(Enum):
    Titanium = 0.91
    Platinum = 0.91
    Silver   = 0.85
    Gold     = 0.88
    Bronze   = 0.81
    Standart = 0.8