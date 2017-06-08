#This function is used to compare the cost to work between staying and moving to a new house
#In this function I will use n to stand for the distance to work if I move to another location


distance = 52.0     # the distance to work right now is 52 km, one way
litre = 65          # my car has a 65 litres gas tank
gas = 80.0          # It costs me 80 bucks to get my gas tank full
distance2 = 450.0   # With a full gas tank I can drive for 450km
etr1 = 7.66         # I need to pay 11.5 bucks if I get on 407 in the morning
etr2 = 10.53        # I need to pay 13.5 bucks if I get on 407 in the afternoon
day = 22            # Total working days in one month



# Calculate how much I need to pay the 407 bills based on the usage
def etr(): 
    print "How many days I get on 407 in the morning?"
    x = int(raw_input("> "))
    
    print "How many days I get on 407 in the afternoon?"
    y = int(raw_input("> "))
    
    total = x*etr1 + y*etr2
    print "\nI need to spend %d on 407 bill each month." %total
    return total
    

# Calculate the gas cost each month
def gascost():
    cost = ((distance*2*day)/distance2)*gas
    print "The gas cost for each month will be %d" %cost
    return cost
    
    

# Calculate the cost if move to a new place, assuming no need to get on 407
def newcost():

    costnow = etr() + gascost()
    
    print "\nThe distance from the new house to work: "
    n = int(raw_input("> "))    
    costnew = ((n*2*day)/distance2)*gas
    print "\nThe gas cost for each month will be %d" %costnew
    diff = costnow - costnew
    
    print "\nThe new cost will be %d, and the current cost is %d." %(costnew, costnow)
    print "\nI can save %d each month on traffic if move to a closer location." %diff
    
    
newcost()
