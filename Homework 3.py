def gate_and(input1, input2):
    """ an AND gate (input1 ^ input2) """
    gate1 = input1 and input2
    return bool(gate1)
                

# Homework 3: Z-Score Python Script (Group Homework)

#################
#  SAMPLE DATA  #
#################
# First data set: a list of positive integers (not a normal distribution)
population1 = [14, 28, 96, 97, 21, 29, 29, 4, 58, 
               42, 25, 97, 49, 33, 75, 53, 14, 53, 
               45, 87, 75, 66, 62, 55, 57, 44, 44, 
               94, 19, 96, 12, 59, 86, 88, 61, 68, 
               37, 64, 19, 46, 68, 98, 19, 54, 65, 
               30, 1, 82, 76, 3]

# Second data set: a list of negative and positive integers (normal distribution)
population2 = [-16, 10, -15, -6, -5, -20, -11, 9, -9,
               -7, 5, -14, 6, -10, -22, -19, 21, 11, 
               -18, -13, -24, -21, 14, 19, 20, 13, 16, 
               8, 4, 3, 18, 22, 17, 7, -12, -3, 
               23, -8, 2, -2, -4, 1, 12, -25, -1,
               15, 0, -23, -17, 24]

# Third data set: a list of positive integers (normal distribution)
population3 = [125, 475, 275, 550, 350, 325, 575, 
               25, 225, 150, 425, 75, 175, 650, 
               600, 625, 675, 250, 100, 0, 375, 
               500, 400, 450, 300, 525, 50, 200]

#################
#  FUNCTIONS    #
#################

def mean(data_set):
    """
    This function will return the mean of the data_set(population)
    **Do not change this function**
    """
    return sum(data_set)/len(data_set)

def stdev(data_set, avg):
    """
    This function will return the standard deviation of the data_set(population), given the mean of the data_set (avg)
    **Do not change this function**
    """
    variance = sum([(integer - avg) ** 2 for integer in data_set])/len(data_set)
    # return the square root of the variance calculation 
    return variance ** .5
	
def least(data_set):
    """
    Returns the least value in the data_set(population)
    **Do not change this function**
    """
    return min(data_set)
	
def greatest(data_set):
    """
    Returns the greatest value in the data_set(population)
    **Do not change this function**
    """
    return max(data_set)

# Your grader will use this function to help them verify your code
def test_z_score_function():
    pop1_avg = mean(population1)
    pop1_sd = stdev(population1, pop1_avg)
    
    mean_z_score_p1 = z_score(pop1_avg, pop1_avg, pop1_sd)
    
    pop2_greatest = greatest(population2)
    pop2_avg = mean(population2)
    pop2_sd = stdev(population2, pop2_avg)
    
    greatest_z_score_p2 = z_score(pop2_greatest, pop2_avg, pop2_sd)
    
    print("The z-score of the mean of population1 is", mean_z_score_p1)
    print("The z-score of the greatest value of population2 is", greatest_z_score_p2)
  

#######################################################
# YOUR CODE GOES BELOW THIS BOX.                      #
#                                                     #
# Complete the following z_score function.            #
# You may call the functions above,	              #
#   but do not define any others (except for testing) #
# You may use arithmetic operators                    #
#  (i.e., +, -, *, **, /) but not Python Boolean      #
#  (call the provided functions instead)              #
#                                                     #
# Be sure to include names of the group members that  #
# participated in the group assignment work           #
#######################################################

def z_score(x, mu, sigma):
    """
    x is the population item
    mu is the population mean
    sigma is the population standard deviation
    
    Returns the z-score of x
    """
    
    # Participating group member names go in this comment 
    # Logan Fish
    # Arianna Flores
    # Ben Kanaras

    # Your code goes between this comment and the return statement
    z = (x - mu) / sigma

    return z # Place the calculated z-score result between the return statement and this comment so it will be returned by the z_score function

# This code gives entire z-score list for all the data sets to cross check test tables in Excel
p1_scores = [z_score(x, mean(population1),stdev(population1, mean(population1))) for x in population1]
p2_scores = [z_score(x, mean(population2),stdev(population2, mean(population2))) for x in population2]
p3_scores = [z_score(x, mean(population3),stdev(population3, mean(population3))) for x in population3]

print("P1-score:", p1_scores)

print("P2-score:", p2_scores)

print("P3-score:", p3_scores)

# This test function was used to check indiviual z-scores
def test_function(population1,population2,population3):
    pop1_avg = mean(population1)
    pop1_max = greatest(population1)
    pop1_sd = stdev(population1,pop1_avg)

    mean_score_p1 = z_score(pop1_max,pop1_avg,pop1_sd)

    pop2_avg = mean(population2)
    pop2_sd = stdev(population2,pop2_avg)

    mean_score_p2 = z_score(pop2_avg,pop2_avg,pop2_sd)

    pop3_min = least(population3)
    pop3_avg = mean(population3)
    pop3_sd = stdev(population3,pop3_avg)

    mean_score_p3 = z_score(pop3_min,pop3_avg,pop3_sd)

    return mean_score_p1, mean_score_p2, mean_score_p3


#mean_score_p1, mean_score_p2, mean_score_p3 = test_function(population1,population2,population3)
#print("The Z-Score of the mean of population1 is", mean_score_p1)
#print("The Z-Score of the mean of population2 is", mean_score_p2)
#print("The Z-Score of the mean of population3 is", mean_score_p3)

#print(z_score(14,mean(population1),stdev(population1,mean(population1))))
#print(z_score(-16,mean(population2),stdev(population2,mean(population2))))
#print(z_score(125,mean(population3),stdev(population3,mean(population3))))
# I used this just as a means of testing the z-score function as well 