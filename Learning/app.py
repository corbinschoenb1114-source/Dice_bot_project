import utils

player = utils.Dice()
request = ""
while request != "QUIT":
    try:
        request = str.upper(input("please enter command >"))
        check = request
        check = check.replace("ADV", "")
        check = check.replace("DIS", "")
        check = check.split("D")

        if "SKILLS" in request:
            number_of_skills = input("How many Skills? >")
            player.skill_generation(int(number_of_skills))

        elif request == "QUIT":
            break

        elif "ADV" in request:
            # print(True)
            request = request.replace("ADV", "")
            # print(request)
            request = request.split("D")
            # print(request)
            amount_of_dice = int(request[0])
            number_of_faces = int(request[1])
            player.rolls(amount_of_dice, number_of_faces, "adv")

        elif "DIS" in request:
            # print(True)
            request = request.replace("DIS", "")
            # print(request)
            request = request.split("D")
            # print(request)
            amount_of_dice = int(request[0])
            number_of_faces = int(request[1])
            player.rolls(amount_of_dice, number_of_faces, "dis")

        elif request != ("QUIT" and "SKILLS" and "ADV" and "DIS"):
            request = request.split("D")
            # print(request)
            amount_of_dice = int(request[0])
            number_of_faces = int(request[1])
            player.rolls(amount_of_dice, number_of_faces, "")

        else:
            break

    except ValueError:
        pass


