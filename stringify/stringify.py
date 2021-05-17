



def check_list(text,inputs_list):
        # I will use a counter to Index the User inputs defined under 'inputs' in the json file
        split_text = text.split(' ')
        counter = 0
        final_list = []
        for item in split_text:
            if '(INPUT)' in item:
                item = input(inputs_list[counter])
                counter += 1
            final_list.append(item)
        return final_list

        # I need to access this from main, so I need to create a string list first

# Combines the outputted list:
def reduce_list(str_a, str_b):
    return f"{str_a} {str_b}"