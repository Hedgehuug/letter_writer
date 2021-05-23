import data_access.data_access as da
import stringify.stringify as stringify
import user_inputs.user_inputs as ui
from functools import reduce

file_path = 'data/data.json'


if __name__ == "__main__":

    main_data = da.File_Access.create_access(file_path)

    introductions = main_data.introductions
    bodies = main_data.bodies
    endings = main_data.endings

    # First iteration of the main loop
    # Most of this will be spread out between multiple files
    # Need to add the close of the letter
    def create_motivation_letter(introductions,bodies,endings):

        print("\n\n\nFirst comes the Introduction, prompts will come up for inputs and you have to enter inputs into the chosen template(ID):\n")
        intro = introductions[ui.get_id_input("Intro ID: ",len(introductions))]
        introduction = stringify.check_list(intro['text'],intro['inputs'])
        introduction = reduce(stringify.reduce_list,introduction)
        print(f"Introduction: \n{introduction}\n")



        print("Now for the Body: ")
        body = bodies[ui.get_id_input('Body ID: ',len(bodies))]
        # main_body = stringify.check_list(body['text'],body['inputs'])
        main_body = reduce(stringify.reduce_list,stringify.check_list(body['text'],body['inputs']))
        print(f"Body: \n{main_body}\n")


        print("The Ending: ")
        end = endings[ui.get_id_input("Ending ID: ",len(bodies))]
        # main_body = stringify.check_list(body['text'],body['inputs'])
        ending = reduce(stringify.reduce_list,stringify.check_list(ending['text'],ending['inputs']))
        print(f"Ending: \n{ending}\n")

        return f"{introduction}\n{main_body}\n{ending}"
        

    motivational_letter = create_motivation_letter(introductions,bodies,endings)
    print(motivational_letter)


    








        

        




    # I am excited to work on this project, it's going to be unnecesserily complicated but maybe reusable for more things later on


    