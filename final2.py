import csv

def HandleData():
    ChartOpen = open('./charts.csv', 'r')
    data = csv.DictReader(ChartOpen)
    return data

def HandleChoice(menuOption):
    match(menuOption):
        case 1:
            Option1()
        case 2:
            Option2()
        case 3:
            Option3()
        case 4:
            print("TBA")
        case 5:
            print("TBA")
        case 6:
            print("\033[91m" + "Exiting..." + "\033[0m")
            exit()
        case _:
            print("\n\n\033[91m" + "Error: " + "\033[0m" + "Invalid Selection Made, Please Try Again!")
            print("TBA")


# Option 1 technical execution and return.
def SpecifedDate(CompletedYear, ReturnedData):
    entries = []
    for data in ReturnedData:
        if data['date'] == CompletedYear:
            entries.append(data)
    print("\n\033[4m" + "Top 5 Songs on " + CompletedYear + "\033[0m\n")
    for d in entries[:5]:
        print("Rank:", d['rank'])
        print("Song:", d['song'])
        print("Artist:", d['artist'], "\n")
    restartOption = int(input("\n\nNext action:\n1) Try Again.\n2) Main Menu\n3) Exit\nSelection: "))
    if restartOption == 1:
        Option1()
    elif restartOption == 2:
        Start()
    elif restartOption == 3:
        print("\033[91m" + "Exiting..." + "\033[0m")
        exit()
    else:
        print("\033[91m" + "Unknown entry entered, exiting..." + "\033[0m")
        exit()

# Option 1 setup
def Option1():
    print("\n\033[4m" + "Top 5 Songs By Day:" + "\033[0m\n")
    ReturnedData = HandleData()
    Year = (input("Enter a Year: "))
    Month = (input("Enter a Month: "))
    Day = (input("Enter a Day: "))
    CompletedYear = str(Year) + "-" + str(Month) + "-" + str(Day)
    SpecifedDate(CompletedYear, ReturnedData)

# Option 2 setup
def Option2():
    print("\n\033[4m" + "Most Successful Artist:" + "\033[0m\n")
    ReturnedData = HandleData()
    MostSuccessfulArtist(ReturnedData)

#Option 2 Technical Execution and Return.
def MostSuccessfulArtist(ReturnedData):
    entries = []
    for d in ReturnedData:
        peakRankCount = int(d['peak-rank'])
        if peakRankCount == 1:
            entries.append(d['artist'])
    SuccessChart = {}
    for e in entries:
        if (e in SuccessChart):
            SuccessChart[e] += 1
        else:
            SuccessChart[e] = 1
    SortedChart = sorted(SuccessChart.items(), key=lambda x: x[1], reverse=True)
    print(SortedChart[0][0], "with", SortedChart[0][1], "number 1 hits")
    restartOption = int(input("\n\nNext action:\n1) Try Again.\n2) Main Menu\n3) Exit\nSelection: "))
    if restartOption == 1:
        Option2()
    elif restartOption == 2:
        Start()
    elif restartOption == 3:
        print("\033[91m" + "Exiting..." + "\033[0m")
        exit()
    else:
        print("\033[91m" + "Unknown entry entered, exiting..." + "\033[0m")
        exit()


# Option 3 setup
def Option3():
    print("\n\033[4m" + "Top 5 Longest Charters:" + "\033[0m\n")
    ReturnedData = HandleData()
    LongestCharters(ReturnedData)

# Option 3 Technical Execution and Return.
def LongestCharters(ReturnedData):
    entries = []
    for data in ReturnedData:
        entries.append(data)
    SortedRuns = sorted(entries, key=lambda x: int(x['weeks-on-board']), reverse=True)
    FinalList = []
    SongSet = set()
    for d in SortedRuns[:100]:
        value = d['song']
        if value not in SongSet:
            FinalList.append(d)
            SongSet.add(value)
    for d in FinalList[:5]:
        print("Song:", d['song'])
        print("Artist:", d['artist'])
        print("Charted duration:", d['weeks-on-board'], "weeks\n")
    restartOption = int(input("\n\nNext action:\n1) Try Again.\n2) Main Menu\n3) Exit\nSelection: "))
    if restartOption == 1:
        Option3()
    elif restartOption == 2:
        Start()
    elif restartOption == 3:
        print("\033[91m" + "Exiting..." + "\033[0m")
        exit()
    else:
        print("\033[91m" + "Unknown entry entered, exiting..." + "\033[0m")
        exit()
        
def Start():
    print("\n\033[4m" + "Billboard Top 100 Songs Search:" + "\033[0m\n")
    menuOption = int(input("Please choose your action to take (in the format of 1-6):\n1) Top 5 Songs By Day\n2) Most Successful Artist\n3) Top 10 Longest Charters\n4) Most Improved Song\n5) Top Songs\n6) Exit\n" + "\033[1m" + "\nSelection: " + "\033[1m"))
    HandleChoice(menuOption)

Start()