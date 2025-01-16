def create_age_dict(names, ages):
    if len(names) != len(ages):
        print("Списки имеют разную длину")
        return {}
    return dict(zip(names, ages))

input_age = input("Введите числа через пробел: ")

ages = list(map(float, input_age.split()))

input_name = input("Введите имена через пробел: ")
names = list(input_name.split())

result = create_age_dict(names, ages)
print(result)
