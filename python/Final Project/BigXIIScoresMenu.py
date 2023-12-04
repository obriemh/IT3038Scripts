import subprocess


# This part is self explanatory and allows the user to pick the sport they would like the current schedule and wins/losses on. 
def main():
    
    print("We're officially in the Big XII! Please select a sport below to find out how our Bearcats are doing in their inaugural season!")
    print("#1 Football (Ouch)")
    print("#2 Men's Basketball")
    print("#3 Women's Basketball")
    option = input("Make a selection:")
    
    #This is a simple loop to allow the user to pick and then subsequently launch the appropriate sport they were interested in.
    if option == "1":
        subprocess.run(["python", "CFBScoreScraper.py"])
    elif option == "2":
        exec(open("MBBScoreScraper.py").read())
    elif option == "3":
        exec(open("WBBScoreScraper.py").read())
    else:
        print("Ouch. Please use 1, 2, or 3 only.")

    
if __name__ == "__main__":
    main()