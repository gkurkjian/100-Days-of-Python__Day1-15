# PAUSE 1
# Create a function called format_name() that takes two inputs: f_name and `l_name'.

# PAUSE 2
# Use the title() function to modify the f_name and l_name parameters into Title Case.

def format_name(f_name, l_name):
    formated_f_temp_name = f_name.title()
    formated_l_temp_name = l_name.title()
    return f"{formated_f_temp_name} {formated_l_temp_name}"

the_out_put = format_name("geOrGe", "KURKJIAN")
print(the_out_put)
