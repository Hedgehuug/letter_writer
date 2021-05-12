import data_access.data_access as data_access
import user_inputs.user_inputs
import data

file_path = 'data/data.json'

def create_new_intro(filepath):
    # I will first fetch the data
    return_object = data_access.File_Access.create_access(file_path)


create_new_intro(file_path)
