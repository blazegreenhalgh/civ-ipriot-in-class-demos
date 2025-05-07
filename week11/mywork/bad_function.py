unit = 'c'
temperature = 38.8


def convert_temp(unit, temp):
    if unit.lower() == 'f':
        converted_temp = (temp - 32) * 5 / 9
    else:
        converted_temp = temp * 9 / 5 + 32
    return converted_temp

print("Hello")
print(convert_temp(unit,temperature))
