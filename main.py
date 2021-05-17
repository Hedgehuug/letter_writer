import data_access.data_access as da
import stringify.stringify as stringify
from functools import reduce

file_path = 'data/data.json'


if __name__ == "__main__":

    main_data = da.File_Access.create_access(file_path)

    introductions = main_data.file['introductions']
    bodies = main_data.file['bodies']

    # First iteration of the main loop
    # Most of this will be spread out between multiple files
    # Need to add the close of the letter
    def create_motivation_letter(introductions,bodies):

        print("First comes the Introduction, prompts will come up for inputs and you have to enter inputs into the chosen template(ID): ")
        intro = introductions[int(input("Intro ID: "))]
        introduction = stringify.check_list(intro['text'],intro['inputs'])
        introduction = reduce(stringify.reduce_list,introduction)
        print(f"Introduction: \n{introduction}\n")



        print("Now for the Body: ")
        body = bodies[int(input("Body ID: "))]
        # main_body = stringify.check_list(body['text'],body['inputs'])
        main_body = reduce(stringify.reduce_list,stringify.check_list(body['text'],body['inputs']))
        print(f"Body: \n{main_body}\n")

        return f"{introduction}\n{main_body}"
        

    motivational_letter = create_motivation_letter(introductions,bodies)
    print(motivational_letter)


    








        

        




    # I am excited to work on this project, it's going to be unnecesserily complicated but maybe reusable for more things later on


    