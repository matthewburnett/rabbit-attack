# Rabbit Attack!
def start():
    print("#############################")
    print("# Welcome to RABBIT ATTACK! #")
    print("#############################")


def end():
    print("################################")
    print("# Goodbye. Thanks for playing! #")
    print("################################")


def confirm(question):
    while True:
        answer = input(f"{question} [Y]es or [N]o:").lower()

        if answer in ["y", "yes"]:
            return True
        elif answer in ["n", "no"]:
            return False


def play():
    num_knights = 5
    rabbit_is_alive = True

    print("Look, a cute little bunny rabbit.")

    while rabbit_is_alive and num_knights > 0:
        use_grenade = confirm("Shall we use the Holy Hand Grenade?")

        if use_grenade:
            print("1... 2... 5... No, 3!\nBoom!")
            rabbit_is_alive = False
        else:
            num_knights -= 1
            print("Oh, no! The rabbit just killed one of the knights!\n"
                  f"Only {num_knights} remain.")

    if num_knights > 0:
        print("The killer rabbit has been defeated. You win!")
    else:
        print("All of the knights are dead. You lose.")


start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to play again?")

end()
