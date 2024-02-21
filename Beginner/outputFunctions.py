def my_function():
    result = 2 * 3
    return result

output = my_function()

print(output)

def format_name(f_name, l_name):
   formated_f_name = f_name.title()
   formated_l_name = l_name.title()

   return f"{formated_f_name} {formated_l_name}"


formated_string = format_name("austin", "robertson")

print(formated_string)