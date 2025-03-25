def get_user_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")