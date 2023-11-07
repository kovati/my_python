empty_tuple = ()  # empty_tuple = tuple()
print(type(empty_tuple))
print(len(empty_tuple))
single_tuple = "alma",
print(type(single_tuple))
print(len(single_tuple))
print(single_tuple[-1])
# single_tuple[0] = "korte" # exception mivel immutable tipus
wrong_tuple = ([2, 3, 4], "word", True)
print(wrong_tuple)
wrong_tuple[0].append(45)  # wrong_tuple[0] -> megkaptam a listat es annak a append metodusta hivtam meg
print(wrong_tuple)
