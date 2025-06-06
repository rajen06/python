dict_data = {"name": "Alice", "age": 30, "city": "New York"}


dict_comp = {key:value * 2 for key, value in dict_data.items() if isinstance(value, int)}
print(dict_comp)