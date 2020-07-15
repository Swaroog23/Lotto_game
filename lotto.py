from random import shuffle


def lotto():

    """Simulation of a Lotto lottery, where you pick 6 numbers and see how many you hve got right"""

    jackpot = list(range(1, 50))
    shuffle(jackpot)
    results = jackpot[:6]

    # Here we set the jackpot with shuffle, where we take 6 numbers form shuffled list

    player_choices = []
    numbers_right = 0
    choice = None

    # choice variable is here to prevent a UnboundLocalError

    while len(player_choices) != 6:
        try:
            choice = int(input("Your number: "))
        except ValueError:
            print("Please input a number")

        if choice not in player_choices and choice in jackpot:
            player_choices.append(choice)

        if choice in results:
            numbers_right += 1

    if numbers_right == 1:
        end_str = "You've hit 1 number!"
    else:
        end_str = f"You've hit {numbers_right} numbers!"

    # the if statement is implemented to make sure grammar is correct in the end screen

    return f"""
Your choices: 
{player_choices}
The jackpot was: 
{results}
{end_str}
"""


print(lotto())
