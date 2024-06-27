def calculate_structure_sum(data):
    summ = 0
    if isinstance(data, (list, tuple, set)):
        for i in data:
            summ += calculate_structure_sum(i)
    elif isinstance(data, dict):
        for i,j in data.items():
            summ += calculate_structure_sum(i) + calculate_structure_sum(j)
    elif isinstance(data, str):
        summ += len(data)
    elif isinstance(data, (int, float)):
        summ += data
    return summ
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)