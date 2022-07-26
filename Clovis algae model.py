#Program written by Clovis Hatungimana for modeling the growth of the algae population in a river.
# Here, we are modeling by regression the Taylor series polynomial
# representative of the weight y (in pounds) of the algae population in the river.

# We are given the weights of the population for the first few months and are tasked with
# predicting future values of the weight by regression.


# We import modules that will allow us to tackle this challenge.
import matplotlib.pyplot as plt
import math
import numpy as np


# defining variables

an = [1,1,1.5]   # Initiating the list that contains the values of the coefficients of
                 # our nth variables in the polynomial. The list has already three coefficients for
                 # the three first terms of our polynomial.
rate_of_change_in_y =[1,1,3]    # Initiating the list that will contain the higher order derivatives of
                                # our polynomial, evaluated at time t=0.
y=[1,1,3/2]     # The list that contains the varous wheights of algae over time t.

# The nth term is given by (an)*(t^n).
# an = y^n(0)/n! or y^n(0) =y^(n-1)(0)+(n-1)y^(n-2)(0).

# Setting the number of terms for our Taylor polynomial. We can vary this number out of discretion.
number_of_terms=30

# We will use a counter to select previous weight values in our lists and calculate the next values by regression.
# We already have the first three values. So, the counter will start at the fourth value.

counter=3

while counter < number_of_terms:
    
    # Calculating by regression the higher order derivatives of y, evaluated at time t=0.

    next_rate = rate_of_change_in_y[counter-1] + (counter-1)*rate_of_change_in_y[counter-2]
    
    # Calculating by regression the values of the coefficient of the nth term.
    an_next = next_rate/math.factorial(counter)
    
    # Storing obtained values of derivatives and coefficients in our lists.
    rate_of_change_in_y.append(next_rate)
    an.append(an_next)
    
    counter=counter+1

# Creating a list of exponents of time t for each nth term of the polynomial.
i=0   # This is a counter for our while loop.
exponent=[]       # The list that will contain the power/exponents of the nth term.
                  # We can use this (exponent) list as our x-axis for graphing.
listoftime=[]       
while i < len(an):
    exponent.append(i)
    
 # Creating a list that contains multiple duplicates of the number 1
 # This list has the same lenght as that of an (the list of our coefficients an).
 # This list will serve as our list of values of time t
 
    unitary_list=(np.array(an)**0)*i
    listoftime.append(unitary_list)
    
    i=i+1
    
# We create a list that contains values of t (time) raised to the nth power.
t_raised_to_the_power =np.array(listoftime)**exponent

# Creating a list that will contain the total amount of algae (y values) for each time t.
total=[]

# We now create a while loop to multiply t^n (value of t to the nth power) with each coefficient (an).
b=0  # This is a counter for our while loop
while b <len(an):
    
    # Calculating the amount of algae (y values) for each term of our polynomial an*(t^n)
    yn=np.array(an)*t_raised_to_the_power[b]
    
    # Storing the yn values in the list that stores the total amount of algae over time.
    total.append(np.sum(yn))
    
    b=b+1
    

print("Amount of algae: \n", total[:5])

# Now, we plot the values of the total amount of algae (y-axis) and exponent (x-axis)

plt.plot(exponent[:3], total[:3],'g')
plt.axis("square")

plt.title("Amount of algae")
plt.xlabel('Time in years')
plt.ylabel('Weight in pounds')
plt.legend({'y(t)'})
plt.show()




