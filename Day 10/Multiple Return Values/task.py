def formated_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Wrong input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Results: {formated_f_name} {formated_l_name}"

print(formated_name(input("What is your name?: "), input("What is your last name?: ")))
