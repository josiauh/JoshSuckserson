import os
def print_options():
    print("1. Velvet")
    print("You can also type: 1, vel, vl")
    print("2. Veneer")
    print("You can also type: 2, ven, vn")

def display_votes():
    try:
        with open(os.path.dirname(__file__) +"/velvetVotes.txt", "r") as velvet_file:
            velvet_votes = sum(1 for _ in velvet_file)

        with open(os.path.dirname(__file__) +"/veneerVotes.txt", "r") as veneer_file:
            veneer_votes = sum(1 for _ in veneer_file)

        print(f"Votes for Velvet: {velvet_votes}")
        print(f"Votes for Veneer: {veneer_votes}")

    except Exception as e:
        print(f"An error occurred while displaying votes: {e}")

def vote(option):
    velvetOptions = [
        "1",
        "velvet",
        "vel",
        "vl"
    ]
    veneerOptions = [
        "2",
        "veneer",
        "ven",
        "vn"
    ]
    try:
        filename = ""
        if option.lower() in velvetOptions:
            filename = os.path.dirname(__file__) + "/velvetVotes.txt"
            acOption = "Velvet"
        elif option.lower() in veneerOptions:
            filename = os.path.dirname(__file__) + "/veneerVotes.txt"
            acOption = "Veneer"
        else:
            print("Invalid option. Please choose either Velvet or Veneer.")
            return

        with open(filename, "a") as file:
            file.write("1\n")  # Each vote is represented by a line with the value 1

        print(f"Your vote for {acOption} has been recorded.")
        display_votes()

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print_options()
    display_votes()
    user_vote = input("Which option would you like to vote for (Velvet or Veneer)? ").strip()
    vote(user_vote)

if __name__ == "__main__":
    while True:
        main()
