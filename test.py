import data_access.data_access as data_access
import user_inputs.user_inputs
import data

file_path = 'data/data.json'

# Testing for the functionality of File_Access() in data_access

# Testing the creation of a new object
testing_file_access = data_access.File_Access.create_access(file_path)
# print(testing_file_access.file)
# Output: 
# JSON File with all introductions, bodies, and closing remarks


# Testing the fetching of groups:
print(list(map(lambda item: item,testing_file_access.file)))
# Output:
# ['introductions', 'body']

# Same thing but with the contents of the groups
print(list(map(lambda item: item,testing_file_access.file.values())))






