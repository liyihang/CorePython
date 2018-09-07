from enum import Enum

# 枚举类型不可更改
#不能重名
class VIP(Enum):
    YELLOW = 1
    RED = 2
    RED_ALIAS = 2
    GREEN = 3
    BLACK = 4

class Common():
    YELLOW = 1

for v in VIP.__members__.items():
    print(v)