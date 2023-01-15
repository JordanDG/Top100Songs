import csv

# Cache imported data from 'charts.csv', provides reading privileges, returns data.
def HandleData():
    ChartOpen = open('./charts.csv', 'r')
    data = csv.DictReader(ChartOpen)
    # Data return via function enables reuse.
    return data

# Option 1 setup (Search by specific date)
def Option1():
    # Title and multiple inputs to form date.
    print("\n\033[4m" + "Top 5 Songs By Day:" + "\033[0m\n")
    ReturnedData = HandleData()
    Year = (input("Enter a Year: "))
    Month = (input("Enter a Month: "))
    Day = (input("Enter a Day: "))
    # Concatination of variables to generate search date.
    CompletedYear = str(Year) + "-" + str(Month) + "-" + str(Day)
    # New empty list to populate with results.
    Entries = []
    # If data is returned, add to list.
    for data in ReturnedData:
        if data['date'] == CompletedYear:
            Entries.append(data)
    # If no entries are returned, throw error and restart.
    if len(Entries) == 0:
        print("\n\n\033[91m" + "Error: " + "\033[0m" + "Invalid Search Made, Please Try Again!")
        Option1()
    # Print formatted top 5 results, automatically sorted by rank.
    print("\n\033[4m" + "Top 5 Songs on " + CompletedYear + "\033[0m\n")
    for d in Entries[:5]:
        print("Rank:", d['rank'])
        print("Song:", d['song'])
        print("Artist:", d['artist'], "\n")
    # Restart menu to either repeat function, exit or return to menu
    restartOption = int(input("Next action:\n1) Try Again.\n2) Main Menu\n3) Exit\nSelection: "))
    if restartOption == 1:
        Option1()
    elif restartOption == 2:
        print("\033[91m" + "Returning To Main Menu..." + "\033[0m")
    elif restartOption == 3:
        print("\033[91m" + "Exiting..." + "\033[0m")
        quit()
    else:
        print("\n\033[91m" + "Error: " + "\033[0m" + "Invalid Selection Made, Exiting...")
        quit()

# Option 2 setup (Most Successful Artist).
def Option2():
    # Title.
    print("\n\033[4m" + "Most Successful Artist:" + "\033[0m\n")
    ReturnedData = HandleData()
    # New empty list to populate with results.
    Entries = []
    # If data is returned, add to list.
    for d in ReturnedData:
        peakRankCount = int(d['peak-rank'])
        if peakRankCount == 1:
            Entries.append(d['artist'])
    SuccessChart = {}
    for e in Entries:
        if (e in SuccessChart):
            SuccessChart[e] += 1
        else:
            SuccessChart[e] = 1
    # Automatically sorted by rank.
    SortedChart = sorted(SuccessChart.items(), key=lambda x: x[1], reverse=True)
    print("Artist:", SortedChart[0][0])
    print("Total Number One Hits:", SortedChart[0][1])
    # Restart menu to either repeat function, exit or return to menu
    restartOption = int(input("\nNext action:\n1) Try Again.\n2) Main Menu\n3) Exit\nSelection: "))
    if restartOption == 1:
        Option2()
    elif restartOption == 2:
        print("\033[91m" + "Returning To Main Menu..." + "\033[0m")
    elif restartOption == 3:
        print("\033[91m" + "Exiting..." + "\033[0m")
        quit()
    else:
        print("\n\033[91m" + "Error: " + "\033[0m" + "Invalid Selection Made, Exiting...")
        quit()

# Option 3 setup (Top 5 longest charters)
def Option3():
    # Title.
    print("\n\033[4m" + "Top 5 Longest Charters:" + "\033[0m\n")
    ReturnedData = HandleData()
    # New empty list to populate with results.
    Entries = []
    # If data is returned, add to list.
    for data in ReturnedData:
        Entries.append(data)
    SortedRuns = sorted(Entries, key=lambda x: int(x['weeks-on-board']), reverse=True)
    FinalList = []
    SongSet = set()
    for d in SortedRuns[:100]:
        value = d['song']
        if value not in SongSet:
            FinalList.append(d)
            SongSet.add(value)
    # Print formatted top 5 results, automatically sorted by rank.
    for d in FinalList[:5]:
        print("Song:", d['song'])
        print("Artist:", d['artist'])
        print("Charted duration:", d['weeks-on-board'], "weeks\n")
    # Restart menu to either repeat function, exit or return to menu
    restartOption = int(input("Next action:\n1) Try Again.\n2) Main Menu\n3) Exit\nSelection: "))
    if restartOption == 1:
        Option3()
    elif restartOption == 2:
        print("\033[91m" + "Returning To Main Menu..." + "\033[0m")
    elif restartOption == 3:
        print("\033[91m" + "Exiting..." + "\033[0m")
        quit()
    else:
        print("\n\033[91m" + "Error: " + "\033[0m" + "Invalid Selection Made, Exiting...")
        quit()

# Option 4 setup
def Option4():
    # Title.
    print("\n\033[4m" + "Top 5 biggest climbers:" + "\033[0m\n")
    ReturnedData = HandleData()
    # New empty list to populate with results.
    Entries = []
    # If data is returned, add to list.
    for d in ReturnedData:
        d['climb'] = 1
        Entries.append(d)
    for d in Entries:
        r = int(d['rank'])
        if d['last-week'] == '':
            pos = 101
        else:   
            pos = int(d['last-week'])
        c = int(d['climb'])
        if r < pos:
            climb = pos - r
            d.update({'climb': climb})
    # Print formatted top 5 results, automatically sorted by rank.
    SortedEntries = sorted(Entries, key=lambda x: x['climb'], reverse=True)
    for d in SortedEntries[:5]:
        print("-", "Song:", d['song'])
        print("-", "artist:", d['artist'], "\n")
    # Restart menu to either repeat function, exit or return to menu
    restartOption = int(input("Next action:\n1) Try Again.\n2) Main Menu\n3) Exit\nSelection: "))
    if restartOption == 1:
        Option4()
    elif restartOption == 2:
        print("\033[91m" + "Returning To Main Menu..." + "\033[0m")
    elif restartOption == 3:
        print("\033[91m" + "Exiting..." + "\033[0m")
        quit()
    else:
        print("\n\033[91m" + "Error: " + "\033[0m" + "Invalid Selection Made, Exiting...")
        quit()

# Option 5 setup
def Option5():
    # Title and inputs to form search term.
    print("\n\033[4m" + "Search Number Ones By Song:" + "\033[0m\n")
    SongSearchString = (input("Enter a Song Name: ")).title()
    ReturnedData = HandleData()
    # New empty list to populate with results.
    Entries = []
    # If data is returned, add to list.
    for data in ReturnedData:
        if data['song'] == SongSearchString and data['rank'] == "1":
            Entries.append(data)
    # If no entries are returned, throw error and restart.
    if len(Entries) == 0:
        print("\n\033[91m" + "Error: " + "\033[0m" + "Invalid Search Made, Please Try Again!")
        Option5()
    print("\n\033[4m" + "Search Results For " + SongSearchString + "\033[0m\n")
    # Print formatted top 5 results, automatically sorted by rank.
    for d in Entries[:100]:
        print("-", "Rank:", d['rank'])
        print("-", "Date:", d['date'])
        print("-", "Artist:", d['artist'], "\n")
    # Restart menu to either repeat function, exit or return to menu
    restartOption = int(input("Next action:\n1) Try Again.\n2) Main Menu\n3) Exit\nSelection: "))
    if restartOption == 1:
        Option5()
    elif restartOption == 2:
        print("\033[91m" + "Returning To Main Menu..." + "\033[0m")
    elif restartOption == 3:
        print("\033[91m" + "Exiting..." + "\033[0m")
        quit()
    else:
        print("\n\033[91m" + "Error: " + "\033[0m" + "Invalid Selection Made, Exiting...")
        quit()