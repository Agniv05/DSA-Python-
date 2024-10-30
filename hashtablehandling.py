#  In Python, a hashmap is commonly referred to as a dictionary. It is a built-in data structure that allows you to store data in key-value pairs. Here’s a breakdown of its features and how it works:

#  Key Features of Hashmaps (Dictionaries)
#  Key-Value Pairs: Each entry in a dictionary consists of a key and its associated value. You can use any immutable data type (like strings, numbers, or tuples) as keys.

#  Fast Access: Dictionaries are implemented using hash tables, which allow for average time complexity of O(1) for lookups, insertions, and deletions.

#  Dynamic Size: Dictionaries can grow and shrink as needed, allowing you to add or remove entries without needing to specify an initial size.

#  Unordered: As of Python 3.7, dictionaries maintain the insertion order of keys, but they are still considered unordered collections because they do not have a fixed position for elements.

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # Output: Alice
my_dict["age"] = 26  # Update age
my_dict["country"] = "USA"  # Add new key-value pair
del my_dict["city"]  # Removes the key 'city'
for key, value in my_dict.items():
    print(f"{key}: {value}")
if "name" in my_dict:
    print("Name exists")
# Create a dictionary
student = {
    "name": "John",
    "age": 20,
    "courses": ["Math", "Science"]
}

# Access a value
print(student["name"])  # Output: John

# Add a new key-value pair
student["graduated"] = False

# Update a value
student["age"] = 21

# Remove a key-value pair
del student["courses"]

# Iterate through the dictionary
for key, value in student.items():
    print(f"{key}: {value}")


class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    



class HashTable:  
    def __init__(self):
        # Initialize the maximum size of the hash table
        self.MAX = 10
        # Create a list of empty lists to represent the hash table
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        # Initialize the hash value to 0
        hash = 0
        # Calculate the hash value by summing the ASCII values of each character in the key
        for char in key:
            hash += ord(char)
        # Return the hash value modulo the maximum size to ensure it fits within the array bounds
        return hash % self.MAX
    
    def __getitem__(self, key):
        # Get the index in the array using the hash of the key
        arr_index = self.get_hash(key)
        # Iterate through the key-value pairs in the bucket
        for kv in self.arr[arr_index]:
            # If the key matches, return the corresponding value
            if kv[0] == key:
                return kv[1]
            
    def __setitem__(self, key, val):
        # Get the hash index for the key
        h = self.get_hash(key)
        found = False  # Flag to check if the key already exists
        # Iterate through the existing elements in the bucket
        for idx, element in enumerate(self.arr[h]):
            # If the key is found, update its value
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)  # Update the key's value
                found = True  # Set the flag to True
        # If the key was not found, append the new key-value pair to the bucket
        if not found:
            self.arr[h].append((key, val))
        
    def __delitem__(self, key):
        # Get the index in the array using the hash of the key
        arr_index = self.get_hash(key)
        # Iterate through the key-value pairs in the bucket
        for index, kv in enumerate(self.arr[arr_index]):
            # If the key matches, delete the key-value pair
            if kv[0] == key:
                print("del", index)  # Optional: print the index of the deleted item
                del self.arr[arr_index][index]  # Remove the item from the list
