# Enum is special data type that will let us define a set of named values and they are unique
# Example
# from enum import Enum
# class Color(Enum):
#     RED = "Red"
#     GREEN = "Green"
#     BLUE = "Blue"
# print(Color.RED.name)
# print(Color.RED.value)

# write an enum called AccountPrivilege with values Premium, Gold, Silver
from enum import Enum


class Privilege(Enum):
    PREMIUM = "PREMIUM"
    GOLD = "GOLD"
    SILVER = "SILVER"
