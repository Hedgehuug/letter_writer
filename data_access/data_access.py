import sys
sys.path.append('..')
import json
import data


# Context Manager is just for opening files, I thought I'd put it here since this is the file for that
class ContextManager:
        def __init__(self,filename):
            self.file = open(filename)

        def __enter__(self):
            return self.file

        def __exit__(self, type, value, traceback):
            self.file.close()


# This is the primary class for creating a new piece of text
class File_Access:
    def __init__(self,json_file):
        self.file = json_file
        self.introductions = json_file['introductions']
        self.bodies = json_file['bodies']
        self.endings = json_file['endings']

    @classmethod
    def create_access(self,file_name):
        with ContextManager(file_name) as the_file:
            import_file = json.loads(the_file.read())
        final_return = File_Access(import_file)
        return final_return

    # I need to find out what this does
    def fetch_group(self,group):
        return self.file[group]
        


if __name__ == "__main__":
    file_path: str = '../data/data.json'
    file_access = File_Access.create_access(file_path)
    introductions = file_access.file['introductions']

    split_list = []
    for item in introductions:
        split_list = item['text'].split(' ')

    # I'm going to try and reduce the list
    from functools import reduce

    # Takes 2 inputs, one a split up version of the list of words in the 'text' section, and an index to indicate which text to use
    def check_list(list_input,intro_index):
        # I will use a counter to Index the User inputs defined under 'inputs' in the json file
        counter = 0
        final_list = []
        for item in list_input:
            if '(INPUT)' in item:
                item = input(introductions[intro_index]['inputs'][counter])
                counter += 1
            final_list.append(item)
        return final_list


    # I actually implemented Reduce, that's incredible
    def reduce_list(str_a, str_b):
        return f"{str_a} {str_b}"

    print(reduce(reduce_list,check_list(split_list,0)))
    # print(check_list(split_list,0))


    

