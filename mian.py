def reverse_string(input_str):
    return input_str[::-1]

result = reverse_string("hello")
print(result)


def is_palindrome(input_str):
    cleaned_str = ''.join(char.lower() for char in input_str if char.isalnum())
    return cleaned_str == cleaned_str[::-1]

print(is_palindrome("sosa"))
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True



def remove_duplicates(input_list):
    unique_elements = []
    for element in input_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

result = remove_duplicates([3, 2, 2, 4, 5])
print(result)


def list_sum(input_list):
    return sum(input_list)

result = list_sum([5, 5, 5])
print(result)



def remove_element(input_list, element_to_remove):
    return [element for element in input_list if element != element_to_remove]

original_list = [1, 2, 6, 5, 3]
element_to_remove = 3

result = remove_element(original_list, element_to_remove)
print(result)






