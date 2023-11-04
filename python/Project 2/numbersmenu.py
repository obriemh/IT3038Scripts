import subprocess

def main():
    
    print("Hello! Please pick a Guess the Numbers game to play!")
    print("#1 Guess a Number (1 - 100.)")
    print("#2 Guess A Number: Extreme (1 - 10,000. 100 Tries.)")
    option = input("Select which version you want to play.")
    
    if option == "1":
        subprocess.run(["python", "guessinggame.py"])
    elif option == "2":
        exec(open("extremenumbers.py").read())
    else:
        print("Ouch. Please use 1 or 2 only.")

    
if __name__ == "__main__":
    main()