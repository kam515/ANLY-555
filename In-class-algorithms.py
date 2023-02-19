#* Katie Mead
#* 2/13/2023

#* Answer the following:
#* 1. Implement a function printRightTriangle(height) which print an ascii triangle (using "*"s) of height height.
#* For example, printRightTriangle(4) should print:
#* *
#* **
#* ***
#* ****
#* 2. CONSTRAINT: The only print statements that can be used are print("*", end="") and print("\n").
#* Theory: Derive a step count function T(h) where h is height. Note that h is the value of the input
#* and not the size of the input, thus we will not do a best, worse, and average case analysis.
#* Determine a tight-fit upper bound for T(h) using Big-O notation.
#* 3. Practical: 
#* using the time module, measure the runtime of printrighttriangle(h) and plot the relationship between
#* the runtime and h. h vs. runtime in seconds.
#* Run multiple simulations at a variety of values of h to confirm your derivation from #2 Theory section above.
#* 4. Present and demo your code and results to the class as a big group.

def printRightTriangle(height):
    for i in range(1, height + 1): # 2h steps
        for j in range(i): # 2h steps
            print('*', end='') # up to h steps
        print("\n") # 1 step

# 4h^2 + h + 1 

printRightTriangle(4)
    
# STEP COUNT FUNCTION: 
#Tofh = (2 + h) * h / 2

#"O(n^2) where n = height"
#"quadratic" because of nested for loops 2h * 2h

import time
import matplotlib.pyplot as plt
import numpy as np
h_values = [int(i) for i in np.linspace(1, 100)] # list of heights to test
runtimes = [] # list of runtimes, to be appended

for h in h_values: # loop through heights
    start_time = time.time() # start timer
    printRightTriangle(h) # run algorithm
    end_time = time.time() # end timer
    runtimes.append(end_time - start_time) # append runtime to list?GYTH

plt.plot(h_values, runtimes)
plt.xlabel('height')
plt.ylabel('runtime (s)')
plt.show()

# save the figure as a .png file

# display 
        
