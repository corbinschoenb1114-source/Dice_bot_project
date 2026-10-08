import random


def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


def replace_at_index(text, index, new_char):
    # Slice up to the index, add the new character, and slice everything after the index
    return text[:index] + new_char + text[index + 1:]


class Dice:
    def rolls(self, amount_of_dice, number_of_faces, vantage):
        if vantage == "":
            result = []
            for i in range(amount_of_dice):
                result.append(random.randint(1, number_of_faces))
            total = 0
            for item in result:
                total += item
            if amount_of_dice > 1 and vantage == "":
                print(f"Total: {total} | Results {result}")
            elif vantage == "":
                print(f"Result: {total}")

        elif "adv" in vantage and amount_of_dice != 2:
            print("Advantage can only be used with two dice")
            pass

        elif "dis" in vantage and amount_of_dice != 2:
            print("disadvantage can only be used with two dice")
            pass

        elif "adv" in vantage:
            result = []
            for item in range(amount_of_dice):
                result.append(random.randint(1, number_of_faces))
            minimum_string = str(min(result))
            # print(minimum_string)
            maximum_string = str(max(result))
            # print(maximum_string)
            minimum_string = '\u0336'.join(minimum_string) + '\u0336'
            # print(minimum_string)

            print(f"({minimum_string}, {maximum_string}) Result: {maximum_string}")

        elif "dis" in vantage:
            result = []
            for item in range(amount_of_dice):
                result.append(random.randint(1, number_of_faces))
            minimum_string = str(min(result))
            # print(minimum_string)
            maximum_string = str(max(result))
            # print(maximum_string)
            maximum_string = '\u0336'.join(maximum_string) + '\u0336'
            # print(minimum_string)

            print(f"({maximum_string}, {minimum_string}) Result: {minimum_string}")

    def skill_generation(self, number_of_skills):
        for i in range(number_of_skills):
            result = []
            result_string = ""
            total = 0
            for number in range(4):
                result.append(random.randint(1, 6))
                # print(result)
            for item in result:
                result_string += str(item) + ", "
                total += item
                # print(result_string)
            minimum = min(result)
            minimum_index = result_string.find(str(minimum))
            strikethrough_number = '\u0336'.join(result_string[minimum_index]) + '\u0336'
            result_string = replace_at_index(result_string, minimum_index, strikethrough_number)
            total = total - minimum
            modifier = int((total - 10) / 2)
            if modifier > 0:
                modifier_string = "+" + str(modifier)
            elif modifier == 0:
                modifier_string = " " + str(modifier)
            else:
                modifier_string = str(modifier)
            if len(str(total)) == 2:
                print(f"({result_string[0:-2]}) Total: {total} | Modifier: {modifier_string}")
            else:
                print(f"({result_string[0:-2]}) Total: {total}  | Modifier: {modifier_string}")

# number = "1 2 3 4 5 1"
# strikethrough_number = '\u0336'.join(number[0]) + '\u0336'
# number = number.replace(number[0], strikethrough_number)
# print(f"({number})")

# word = "banana"
#
# updated_word = utils.replace_at_index(word, 3, "O")
#
# print(updated_word)