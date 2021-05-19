import sys
sys.path.append('..')
import data_access

# This is a module used for taking user-inputs for the data we will be processing
# I don't really care if this is messy, haven't done it a lot before


def get_id_input(input_text,length):
    print(f"Enter Values between 0-{length-1} (representing the number of saved items)")
    return_item = input(input_text)
    try:
        if int(return_item) > length-1:
            raise IndexError
        return int(return_item)
    except (ValueError,TypeError) as err:
        print(f"'{return_item}' is not a valid INT, and cannot be used for ID: {err}")
        print("\nPlease enter a valid ID")
        return get_id_input(input_text,length)
    except IndexError:
        print(f"No item exists at ID: {return_item}, please enter a valid ID\n")
        return get_id_input(input_text,length)


    





