# Airline Programming Project
# This program will read in a data file with flight information, show the user a list of options, and show results based on what the user choose

# This function asks the user to enter a data file and checks if it is valid
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Please enter a file name: ")
        try:
            dataFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid file name try again...")
    return dataFile

# This function reads from the data file, puts them into lists, and returns those lists
def getData():
    airlineList = []
    flightNumberList = []
    departureTimeList = []
    arrivalTimeList = []
    priceList = []
    infile = openFile()
    line = infile.readline()
    line = line.strip()
    while line != "":
        airline,flight,departure,arrival,price = line.split(",")
        airlineList.append(airline)
        flightNumberList.append(flight)
        departureTimeList.append(departure)
        arrivalTimeList.append(arrival)
        priceList.append(price)
        line = infile.readline()
        line = line.strip()
    infile.close()
    return airlineList, flightNumberList, departureTimeList, arrivalTimeList, priceList

# This function takes the lists and converts them
# It does departure and arrival lists from strings of hours:minutes into intergers of minutes
# It does the price list from strings of prices into intergers of prices and removes the $
# It returns those new lists
def convertingLists(departureTimeList, arrivalTimeList, priceList):
    minutesDepartureTimeList = []
    for i in range (len(departureTimeList)):
        time = departureTimeList[i]
        minutes = 0
        if len(time) == 5:
            minutes = minutes + int(time[0])*600
            minutes = minutes + int(time[1])*60
            minutes = minutes + int(time[3])*10
            minutes = minutes + int(time[4])
        elif len(time) == 4:
            minutes = minutes + int(time[0])*60
            minutes = minutes + int(time[2])*10
            minutes = minutes + int(time[3])
        minutesDepartureTimeList.append(minutes)
    minutesArrivalTimeList = []
    for i in range (len(arrivalTimeList)):
        time = arrivalTimeList[i]
        minutes = 0
        if len(time) == 5:
            minutes = minutes + int(time[0])*600
            minutes = minutes + int(time[1])*60
            minutes = minutes + int(time[3])*10
            minutes = minutes + int(time[4])
        elif len(time) == 4:
            minutes = minutes + int(time[0])*60
            minutes = minutes + int(time[2])*10
            minutes = minutes + int(time[3])
        minutesArrivalTimeList.append(minutes)
    intPriceList = []
    for i in range (len(priceList)):
        number = priceList[i].replace("$","")
        intPriceList.append(int(number))
    return minutesDepartureTimeList, minutesArrivalTimeList, intPriceList

# This function asks the user to enter an airline and a flight number
# If the user enters in something that does not exists, the program lets the user know
# It then finds that flight and returns the index of their specific flight
def findSpecificFlight(airlineList, flightNumberList):
    airlineFound = False
    while airlineFound == False:
        airlineName = input("Enter airline name: ")
        for i in range (len(airlineList)):
            if airlineList[i] == airlineName:
                airlineFound = True
        if airlineFound == False:
            print("Invalid input -- try again")
    flightFound = False
    while flightFound == False:
        flightNumber = input("Enter flight number: ")
        for i in range (len(flightNumberList)):
            if flightNumberList[i] == flightNumber:
                flightFound = True
        if flightFound == False:
            print("Invalid input -- try again")
    specificIndex = 0
    for i in range(len(airlineList)):
        if (airlineList[i] == airlineName) and (flightNumberList[i] == flightNumber):
            specificIndex = i
    return specificIndex

# This function asks the user for maximum flight duration
# If the user enters something wrong, the program lets the user know
# It then finds all flights whose duration is less or equal to the maximum and returns all thoose indexes
def findShorterFlights(minutesDepartureTimeList, minutesArrivalTimeList):
    duration = False
    while duration == False:
        try:
            maxDuration = int(input("Enter maximum duration (in minutes): "))
            duration = True
        except ValueError:
            print("Entry must be a number")
    durationList = []
    for i in range (len(minutesDepartureTimeList)):
        durationTime = minutesArrivalTimeList[i] - minutesDepartureTimeList[i]
        durationList.append(durationTime)
    shorterIndexes = []
    for i in range (len(durationList)):
        if durationList[i] <= maxDuration:
            shorterIndexes.append(i)
    return shorterIndexes

# This function asks the user to enter an airline
# If the user enters it something that does not exists, the program lets the user know
# It then finds the cheapest price flown by that airline and returns its index
def findCheapestFlight(airlineList, intPriceList):
    cheapestIndex = 0
    cheapest = intPriceList[0]   
    airlineFound = False
    while airlineFound == False:
        airlineName = input("Enter airline name: ")
        for i in range (len(airlineList)):
            if airlineList[i] == airlineName:
                airlineFound = True
                if intPriceList[i] < cheapest:
                    cheapest = intPriceList[i]
                    cheapestIndex = i
        if airlineFound == False:
            print("Invalid input -- try again")         
    return cheapestIndex

# This function asks the user to enter a time
# If the user did not enter a time, the program lets the user know
# It then finds all flighst that depart after that time and returns those indexes
def findDepartingFlights(minutesDepartureTimeList):
    earliestDeparture = input("Enter earliest departure time: ")
    early = False
    while early == False:
        try:
            if len(earliestDeparture) == 5:
                if int(earliestDeparture[0]) in [0,1,2]:
                    if int(earliestDeparture[1]) in [0,1,2,3,4,5,6,7,8,9]:
                        if earliestDeparture[2] == ":":
                            if int(earliestDeparture[3]) in [0,1,2,3,4,5,6]:
                                if int(earliestDeparture[4]) in [0,1,2,3,4,5,6,7,8,9]:
                                    early = True
            else:
                earliestDeparture = input("Invalid time - Try again ")
        except ValueError:
            earliestDeparture = input("Invalid time - Try again ")
    earliestMinutes = 0
    earliestMinutes = earliestMinutes + int(earliestDeparture[0])*600
    earliestMinutes = earliestMinutes + int(earliestDeparture[1])*60
    earliestMinutes = earliestMinutes + int(earliestDeparture[3])*10
    earliestMinutes = earliestMinutes + int(earliestDeparture[4])
    departingIndexes = []
    for i in range (len(minutesDepartureTimeList)):
        if minutesDepartureTimeList[i] > earliestMinutes:
            departingIndexes.append(i)
    return departingIndexes

# This function finds the average price of all flights
# It then returns that average
def findAveragePriceFlights(intPriceList):
    averagePrice = 0
    for i in range (len(intPriceList)):
        averagePrice = averagePrice + intPriceList[i]
    averagePrice = round(averagePrice/(len(intPriceList)),2)
    return averagePrice

# This function creates a list of indexes that is sorted based on the order of departure time
# It then creates an output file and writes to the file the flights based on the list of indexes
# It returns nothing
def sortFlights(minutesDepartureTimeList, airlineList, flightNumberList, departureTimeList, arrivalTimeList, priceList):
    sortedIndexes = []
    for i in range (len(minutesDepartureTimeList)):
        sortedIndexes.append(i)
    for i in range(len(minutesDepartureTimeList)):            
        min = i
        for j in range(i + 1, len(minutesDepartureTimeList)):
            if minutesDepartureTimeList[j] < minutesDepartureTimeList[min]:
                min = j
        minutesDepartureTimeList[i], minutesDepartureTimeList[min] = minutesDepartureTimeList[min], minutesDepartureTimeList[i]
        sortedIndexes[i], sortedIndexes[min] = sortedIndexes[min], sortedIndexes[i]
    outFile = open("time-sorted-flights.csv", 'w')
    for i in range(len(sortedIndexes)):
        outFile.write(airlineList[sortedIndexes[i]] + "," + flightNumberList[sortedIndexes[i]] + "," + departureTimeList[sortedIndexes[i]] + "," + arrivalTimeList[sortedIndexes[i]] + "," + priceList[sortedIndexes[i]] + '\n')
    outFile.close()
    return

# The main function; the menu and the results of each option being printed is here
def main():
    airlineList, flightNumberList, departureTimeList, arrivalTimeList, priceList = getData()
    minutesDepartureTimeList, minutesArrivalTimeList, intPriceList = convertingLists(departureTimeList, arrivalTimeList, priceList)
    finished = False
    while finished == False:
        print()
        print("Please choose one of the following options:")
        print("1 -- Find flight information by airline and flight number")
        print("2 -- Find flights shorter than a specified duration")
        print("3 -- Find the cheapest flight by a given airline")
        print("4 -- Find flight departing after a specified time")
        print("5 -- Find the average price of all flights")
        print("6 -- Write a file with flights sorted by departure time")
        print("7 -- Quit")
        goodChoice = False
        while goodChoice == False:
            try:
                choice = int(input("Choice ==> "))
                goodChoice = True
            except ValueError:
                print("Entry must be a number")
            if goodChoice == True and (choice > 7 or choice < 1):
                print("Entry must be between 1 and 7")
                goodChoice = False
        if choice == 1:
            print()
            specificIndex = findSpecificFlight(airlineList, flightNumberList)
            print()
            print("The flight that meets your criteria is:")
            print()
            print("AIRLINE".ljust(8), "FLT#".ljust(6), "DEPART".rjust(7), "ARRIVE".rjust(7), "PRICE".rjust(3))
            print(airlineList[specificIndex].ljust(8), flightNumberList[specificIndex].ljust(6), departureTimeList[specificIndex].rjust(7), arrivalTimeList[specificIndex].rjust(7), priceList[specificIndex].rjust(3))
        elif choice == 2:
            print()
            shorterIndexes = findShorterFlights(minutesDepartureTimeList, minutesArrivalTimeList)
            print()
            if shorterIndexes == []:
                print("No flights meet your criteria")
            else:
                print("The flights that meet your criteria are:")
                print()
                print("AIRLINE".ljust(8), "FLT#".ljust(6), "DEPART".rjust(7), "ARRIVE".rjust(7), "PRICE".rjust(3))
                for i in range (len(shorterIndexes)):
                    print(airlineList[shorterIndexes[i]].ljust(8), flightNumberList[shorterIndexes[i]].ljust(6), departureTimeList[shorterIndexes[i]].rjust(7), arrivalTimeList[shorterIndexes[i]].rjust(7), priceList[shorterIndexes[i]].rjust(3))
        elif choice == 3:
            print()
            cheapestIndex = findCheapestFlight(airlineList, intPriceList)
            print()
            print("The flight that meets your criteria is:")
            print()
            print("AIRLINE".ljust(8), "FLT#".ljust(6), "DEPART".rjust(7), "ARRIVE".rjust(7), "PRICE".rjust(3))
            print(airlineList[cheapestIndex].ljust(8), flightNumberList[cheapestIndex].ljust(6), departureTimeList[cheapestIndex].rjust(7), arrivalTimeList[cheapestIndex].rjust(7), priceList[cheapestIndex].rjust(3))
        elif choice == 4:
            print()
            departingIndexes = findDepartingFlights(minutesDepartureTimeList)
            print()
            if departingIndexes == []:
                print("No flights meet your criteria")
            else:
                print("The flights that meet your criteria are:")
                print()
                print("AIRLINE".ljust(8), "FLT#".ljust(6), "DEPART".rjust(7), "ARRIVE".rjust(7), "PRICE".rjust(3))
                for i in range (len(departingIndexes)):
                    print(airlineList[departingIndexes[i]].ljust(8), flightNumberList[departingIndexes[i]].ljust(6), departureTimeList[departingIndexes[i]].rjust(7), arrivalTimeList[departingIndexes[i]].rjust(7), priceList[departingIndexes[i]].rjust(3))
        elif choice == 5:
            print()
            averagePrice = findAveragePriceFlights(intPriceList)
            print("The average price is $", averagePrice)
        elif choice == 6:
            print()
            sortFlights(minutesDepartureTimeList, airlineList, flightNumberList, departureTimeList, arrivalTimeList, priceList)
            print("Sorted data has been written to file: time-sorted-flights.csv")
        elif choice == 7:
            print()
            print("Thank you for flying with us")
            finished = True
