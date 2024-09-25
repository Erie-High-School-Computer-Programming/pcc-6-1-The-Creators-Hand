# Chapter 6 Dictionaries

# Exercise 6.1
def vocabulary():
    # Dictionaries are ___ - value pairs
    # Return the word that would go in the blank in the above sentence
    # All lowercase as a string
    return "key"

# Exercise 6.2
def retrieve_from_dict()->int:
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    # Retrieve the value associated with the key 'b'
    return dictionary["b"]

# Exercise 6.3
def add_to_dict() -> dict:
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    # Add a new key-value pair to the dictionary: 'd' with the value 4
    # Return the dictionary
    dictionary["d"] = 4
    return dictionary

# Exercise 6.4
def update_dict() -> dict:
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    # Update the value associated with the key 'b' to 5
    # Return the dictionary
    dictionary["b"] = 5
    return dictionary

# Exercise 6.5
def delete_from_dict() -> dict:
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    # Delete the key-value pair with the key 'b'
    # Return the dictionary
    if "b" in dictionary:
        del dictionary["b"]
    return dictionary

# Exercise 6.6
def in_dict(dictionary) -> bool:
    
    # Check if the key 'b' is in the dictionary
    # Return True if it is, False if it is not
    if "b" in dictionary:
        return True
    else:
        return False

# Exercise 6.7
def loop_over_dict(dictionary) -> list:
    # Loop over the dictionary and return a list of all the keys
    dict_keys = []
    for key in dictionary.keys():
        dict_keys.append(key)
    return dict_keys

# Exercise 6.8
def loop_over_dict_values(dictionary) -> list:
    # Loop over the dictionary and return a list of all the values
    dict_values = []
    for value in dictionary.values():
        dict_values.append(value)
    return dict_values

# Exercise 6.9
def dictionary_of_lists(dictionary) -> dict:
    # The dictionary contains keys with a list of values
    # Return the value last value of the list associated with the key 'b'
    return dictionary["b"][2]

# Exercise 6.10
def dictionary_of_dictioaries(dictionary) -> dict:
    # The dictionary contains keys with a dictionary of values
    # Return the value associated with the key 'b' and the key 'c'
    return dictionary['b']['c']