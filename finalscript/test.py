def get_float(pair):
    return pair[1]

def arrange_by_float_descending(inputs):
    sorted_pairs = sorted(inputs, key=get_float, reverse=True)
    return sorted_pairs

# Example inputs: list of [name, float] pairs
input_list = [["Alice", 8.5], ["Bob", 9.2], ["Charlie", 7.8], ["David", 9.8]]
sorted_output = arrange_by_float_descending(input_list)

for name, value in sorted_output:
    print(f"Name: {name}, Float: {value}")