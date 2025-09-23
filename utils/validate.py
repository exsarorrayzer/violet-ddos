from utils.colors import color

def validate_input(prompt, min_val, max_val, input_type=int):
    while True:
        try:
            value = input_type(input(color(prompt, "blue")))
            if min_val <= value <= max_val:
                return value
            print(color(f"[!] Value must be between {min_val} and {max_val}.", "red"))
        except ValueError:
            print(color("[!] Invalid input. Please enter a number.", "red"))