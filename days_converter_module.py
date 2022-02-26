user_input_message = "*****************************\nHey user, enter number of days and conversion unit\n"


def days_to_units(num_of_days, conversion_unit):
        if conversion_unit == "hours":
            return f"{num_of_days} days are {num_of_days * 24} hours"
        elif conversion_unit == "minutes":
            return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
        else:
            return "unsupported uint!"


def validate_and_execute(days_and_unit_dict):
    try:
        user_input_in_number = int(days_and_unit_dict["days"])

        # we want to conversion only for positive integers
        if user_input_in_number > 0:
            calculated_value = days_to_units(user_input_in_number, days_and_unit_dict["unit"])
            print(calculated_value)
        elif user_input_in_number == 0:
            print("you enter a 0, please enter a positive number!")
        else:
            print("you enter a negative number, no conversion for you!")
    except ValueError:
        print("you input is not a valid number, don't ruin my program")

