# Function 1: Filter and sort even numbers
def filter_and_sort_evens(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    return sorted(evens)


# Function 2: Count character frequency (case-insensitive)
def count_character_frequency(text):
    text = text.lower()
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq


# Example calls
if __name__ == "__main__":
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Even numbers sorted:", filter_and_sort_evens(nums))

    sample_text = "Hello World"
    print("Character frequencies:", count_character_frequency(sample_text))
