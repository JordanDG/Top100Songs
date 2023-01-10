import csv

def HandleMenuChoice(menuOption):
    match (menuOption):
        case 1:
            TopRankingSongByDay()
        case 2:
            MostSuccessfulArtist()
        case 3:
            Top10LongestCharters()
        case 4:
            TopImprovement()
        case 5:
            TopSongs()
        case 6:
            print("\033[91m" + "Exiting..." + "\033[0m")
            exit()
        case _:
            print("\n\n\033[91m" + "Error: " + "\033[0m" + "Invalid Selection Made, Please Try Again!")
            ScriptStart()




def Option1():
    print("\n\033[4m" + "Top Ranked Song By Day:" + "\033[0m\n")
    print("Please input the following (in a numerical format):")
    # Data inputs to construct date variable
    Year = (input("Enter a Year: "))
    Month = (input("Enter a Month: "))
    Day = (input("Enter a Day: "))
    CompletedYear = str(Year) + "-" + str(Month) + "-" + str(Day)
    csv_file = csv.reader(open("./charts.csv", 'r'))

    for row in csv_file:
        if CompletedYear==row[0] and row[1] == "1":
            print("\n\033[92m" + "Result:" + "\033[0m")
            print("\033[1m" + "Name: " + "\033[0m" + row[2] + "\033[1m" + "\nArtist: " + "\033[0m" + row[3] + "\033[1m" + "\nWeeks Charted: " + "\033[0m" + row[6])
            finalChoice = str(input("\nWhat would like to do next?\n1) Search Another Date\n2) Go Back To Main Menu\n3) Exit\nSelection: "))
            if finalChoice == "1":
                Option1()
            elif finalChoice == "2":
                ScriptStart()
            elif finalChoice == "3":
                exit()
            else:
                print("\n\033[91m" + "Error: " + "\033[0m" + "Invalid selection Made, Restarting.")
                ScriptStart()
        else:
            print("\n\033[91m" + "Error: " + "\033[0m" + "No Results From Given Parameters.")
            finalChoice = str(input("\nWhat would like to do next?\n1) Search Another Date\n2) Go Back To Main Menu\n3) Exit\nSelection: "))
            if finalChoice == "1":
                TopRankingSongByDay()
            elif finalChoice == "2":
                ScriptStart()
            elif finalChoice == "3":
                exit()
            else:
                print("\n\033[91m" + "Error: " + "\033[0m" + "Invalid selection Made, Restarting.")
                ScriptStart()


def MostSuccessfulArtist():
    print("\n\033[4m" + "Most Successful Artist:" + "\033[0m\n")
    csv_file = csv.reader(open("./charts.csv", 'r'))
    data = list(csv_file)
    print(data[1])


def Top10LongestCharters():
    print("Yes")

def TopImprovement():
    print("Yes")

def TopSongs():
    print("Yes")

def ScriptStart():
    print("\n\033[4m" + "Billboard Top 100 Songs Search:" + "\033[0m\n")
    menuOption = int(input("Please choose your action to take (in the format of 1-5):\n1) Top Ranked Song By Day\n2) Most Successful Artist\n3) Top 10 Longest Charters\n4) Most Improved Song\n5) Top Songs\n6) Exit\n" + "\033[1m" + "\nSelection: " + "\033[1m"))
    HandleMenuChoice(menuOption)

ScriptStart()