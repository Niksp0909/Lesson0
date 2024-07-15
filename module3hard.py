data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data_structure):
    total_sum = 0

    def sum_recursive(element):
        nonlocal total_sum
        if isinstance(element, dict):
            for key, value in element.items():
                sum_recursive(key)
                sum_recursive(value)
        elif isinstance(element, (list, tuple, set)):
            for item in element:
                sum_recursive(item)
        elif isinstance(element, str):
            total_sum += len(element)
        elif isinstance(element, int):
            total_sum += element

    sum_recursive(data_structure)
    return total_sum


result = calculate_structure_sum(data_structure)
print(result)
