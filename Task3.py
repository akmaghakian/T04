#Firstly we ask the user to input the diferent times variables for each sport: These are Swimming, Cycling and Running.
swimming_time=input("Please insert the swimming time in minutes")

cycling_time=input("Please insert the cycling time in minutes")

running_time=input("Please insert the running time in minutes")

#Secondly we convert these to a numerical value, so that we can apply an addition operator

swimming_minutes_time = float(swimming_time)
cycling_minutes_time = float(cycling_time)
running_minutes_time = float(running_time)

#Thirdly we create a new variable called total_time which is the total sum in minutes for all 3 sports and print it.

total_time = swimming_minutes_time + cycling_minutes_time + running_minutes_time

print(total_time) #This prints the total sum in munutes of the 3 sports

#Fourthly, once that the total time in minutes has been given, it is subject to the following conditions, which will then assign the relevant award or no award

if total_time < 100 :      # Within Qualifying 100 minutes
       print("Provincial Colours")

if 100 <= total_time <=105 :      # between 5 and 10 minutes of qualifying time it is provincial half colours
       print("Provincial Half Colours")

if 105< total_time <= 110 :      # within 10 minutes of qualifying time it is Provicial Scroll
       print("Provincial Scroll" )

if total_time > 110:        # more than 10 minutes within qualifying time there is no award
       print("No Award")