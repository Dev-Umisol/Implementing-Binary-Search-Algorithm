def binary_search(search_list, value):
    path_to_target = []
    low = 0
    high = len(search_list) - 1 # <-- Accounts for the last index in the list being searched
    
    while low <= high:
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)
        
        if value == value_at_middle:
            return path_to_target, f"Value found at index {mid}"
        elif value > value_at_middle: # <-- Checks right half
            low = mid + 1
        else: # <-- Left half
            high = mid - 1
    
    return [], "Value not found"

# --> Example Usage <--
print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))
print(binary_search([1, 3, 5, 9, 14, 22], 10))