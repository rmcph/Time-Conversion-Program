#ask user for number of seconds
seconds = int(input("What is the number of seconds in total?" ))

#convert seconds to hours, minutes, and seconds
hoursRemaining = seconds // 3600
secsStillRemaining = seconds % 3600
minutesRemaining = secsStillRemaining // 60
secondsRemaining = secsStillRemaining % 60

#print the result
print((str(hoursRemaining) + ("hr.")) + (str(minutesRemaining) + ("min.")) + (str(secondsRemaining) + ("sec.")))
                                                    
