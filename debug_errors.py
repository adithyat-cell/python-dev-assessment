# Task 2.3: Debugging & Error Handling

# Function to calculate average of a list with error handling for empty lists
def calculate_average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        print("Warning: Empty list provided. Returning 0 as average.")
        return 0

# Function to safely get a list element
def get_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print(f"Error: Index {index} is out of bounds for the list.")
        return None
    except TypeError:
        print(f"Error: Provided input {my_list} is not a list.")
        return None

# Example calls for calculate_average
data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []  # This will now be handled gracefully

print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")  # No error now

print("-" * 40)

# Example calls for get_list_element
example_list = [100, 200, 300]

print("Element at index 1:", get_list_element(example_list, 1))  # Valid
print("Element at index 5:", get_list_element(example_list, 5))  # Out of bounds
print("Element from invalid input:", get_list_element("not a list", 0))  # Type error
