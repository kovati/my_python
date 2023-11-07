empty_list = []  # empty_list = list()
print(len(empty_list))
empty_list.append(31)  # ez mindig a vegehez adja hozza az uj elemet
print(len(empty_list))
print(empty_list[0])
numbers: list[int] = [31, 67, 0, 89, 454, 6545, 67, 31]
numbers.insert(2, 999)  # ez a megadott index (az elso parameter most a 2.) helyre szurja be az elemet
numbers.insert(-356, 0)
print(numbers)
print(numbers[-1])
print(numbers[-len(numbers)])
print(numbers[::-2])
back_second_numbers = numbers[::-2]
print(back_second_numbers)
print(numbers)
del numbers[0]  # index alapjan torli az elemet
print(numbers)
deleted_item = numbers.pop(0)  # index alapjan torli az elemet de annak erteket visszaadja
print(deleted_item)
print(numbers)
numbers.remove(67)  # csak az elso elofordulast torli [67, 67, 67] -> [67, 67]
print(numbers)
another_numbers = [-999, -1, -56]
concat_list = numbers + another_numbers
print(concat_list)
print(numbers * 8)
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)
numbers.sort(reverse=True)
print(numbers)
number_text = str(4567)  # init metodus vagy konstruktor
print(number_text)
print(str(True).upper())
b = bool(2)
print(b)
mixed_list = ["Kovács János", "A,B,C,D,E", 32, 1967, "MindentViszTrans Zrt."]  # anti pattern
print(*mixed_list)  # kicsomagolas print("K J", "kat", 32, 1967, "ceg")

matrix = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
print(matrix)
print(len(matrix))
print(matrix[1][2])  # matrix[sor][oszlop]
last_row = matrix[2]
print(last_row)
print(type(numbers))
print(type(numbers[0]))
print(type(matrix))
print(type(matrix[0]))
print(type(matrix[0][0]))
print(31 in numbers)
print(310 in numbers)
print(310 not in numbers)
print(numbers[0])
numbers[0] = 66666666
print(numbers)
