import math


#part 1
r = 5
vol = 4/3*math.pi*r**3

print("1.) vol = ", vol)


#part 2
price = 24.95
discount = .4
copies = 60

cost = (price*discount)+3+(0.75*copies-1)

print("2.) total wholesale cost = ", cost)

#part3 

easy = 8*60+15 #seconds per mile
tempo = 7*60+12 #seconds per mile

runTime = easy + 3*tempo + easy  #runtime in seconds

hours = 6
minutes = 52
seconds = 00
 
print("3.) Leave house at ", hours, ":", minutes, ":", seconds)

returnHours = hours + (runTime//60+minutes)//60
returnMinutes = (runTime//60+minutes)%60
returnSeconds = runTime//60
print("    RTB at ", returnHours, ":", returnMinutes, ":", returnSeconds)
