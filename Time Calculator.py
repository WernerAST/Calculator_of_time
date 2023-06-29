import re
instruction=print("It is a time calculator, you can sum any time requested to the hour and minutes you would like. \nPlease follow the next instructions:")
hour =input("Hour, minutes and if it is am or pm (separated by space): ")
addingtm= input("How many hours and minutes would you like to add?: ")
day1= input("Would you like to add a day? if that is the case please type in the name of the day or  NO if you do not want to:  ")

hoursp= hour.split()
#print(hoursp, lenh)
addtmsp= addingtm.split(":")

operand1 = 0
operand2 = 0
separator= ":"
partofday= " ---am/pm---"

if len (hour) == 8 or len (hour) ==7:
    for i in range(len(hoursp)):
        hour2 = hoursp[i]
           # print ("I'm here 1")
            #print(hour2)
        if ":" in hour2:
            operand1, operand2= hour2.split(":")
            separator = ":"
            #    print ("I'm here 2")
        elif "am" in hour2 or "AM" in hour2 :
            partofday= "am"
        elif "pm" in hour2 or "PM" in hour2:
            partofday= "pm"
        else:
            print("Sorry the input is not correct, try again.")
else:
    print("sorry input not recognized, try again")

addop1= "hour2"
addop2= "min2"

if len (addingtm) <=4:        
        if ":" in addingtm:
            addop1, addop2 = addingtm.split(":")
        else:
             addop1 = addingtm
else:
    print("sorry input not recognized, try again")

hrtl=0
mintl=0
operand11=int(operand1) 
operand22= int(operand2)
addop11=int(addop1)
try:
    addop22=int(addop2)
except:
    addop22=0

if operand11 <=23 and addop11 <=23:
    hrtl= operand11+addop11
    if operand22<=60 and addop22 <=60:
        mintl = operand22+addop22
        if mintl >=60:
            hrtl= hrtl+1
            mintl = mintl-60
else:
    print("It is not a avilable hour.")
if operand11 <=23 and addop11 <=23:
    if "NO" in day1 or "no" in day1:
        print(hrtl,separator,mintl, partofday)
    else:
        print(hrtl,separator,mintl, partofday, day1)
else:
    print("try again please.")