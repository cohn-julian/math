#Telling what plane the angle will be in. Allows input in Radians and Degrees.

import math

def deg_to_rad(deg):
    return ( (deg*math.pi)/180 ) #rad/deg = pi/180

def find_pos_quad(rad): #Need to change boundries to be RADIANS!
    if rad < 0:
        return find_neg_quad(rad)
    if (0 < rad < (math.pi/2)):
        return "First Quadrant"
    elif rad == (math.pi/2):
        return "Positive Y-Axis"
    elif ( (math.pi/2) < rad < math.pi):
        return "Second Quadrant"
    elif rad == math.pi:
        return "Negative X-Axis"
    elif (math.pi) < rad < (3*math.pi/2):
        return "Third Quadrant"
    elif rad == (3*math.pi/2):
       return "Negative Y-Axis"
    elif (3*math.pi/2)< rad < (2*math.pi):
        return "Fourth Quadrant"
    elif rad == (math.pi*2) or rad == 0:
        return "Positive X-axis"
    elif rad > (math.pi*2):
        return find_pos_quad(rad - (math.pi *2) )

def find_neg_quad(rad):
    if rad > 0:
        return find_pos_quad(rad)
    if (0 > rad > -(math.pi/2)):
        return "Fourth Quadrant"
    elif rad == -(math.pi/2):
        return "negative Y-Axis"
    elif ( -(math.pi/2) > rad > -math.pi):
        return "Third Quadrant"
    elif rad == -math.pi:
        return "Negative X-Axis"
    elif -(math.pi) > rad > -(3*math.pi/2):
        return "Second Quadrant"
    elif rad == -(3*math.pi/2):
       return "Posative Y-Axis"
    elif -(3*math.pi/2)> rad > -(2*math.pi):
        return "First Quadrant"
    elif rad == -(math.pi*2) or rad == 0:
        return "Positive X-axis"
    elif rad < -(math.pi *2):
        return find_neg_quad(rad + (math.pi*2))

def user():
    d_or_r = raw_input("""
    would you like to enter your angle in
    1) Degrees
    2) Radians\n""")
    print d_or_r

    if d_or_r.lower() == "1" or d_or_r.lower()=="degrees":
        deg = raw_input("What is your angle (In Degrees)? : ")
        try:
            deg = float(deg)
        except:
            print "invadil value"
            return user()
        print find_pos_quad(deg_to_rad(deg))
    elif d_or_r.lower()=="2" or d_or_r.lower() == "radians":
        numerator = raw_input("What is your NUMERATOR for your ratio of pi. EX: for 3/2 pi enter 3 now. \n")
        denominator = raw_input("What is your DENOMINATOR for your ration of pi. EX. for 3/2 pi enter 2 now. \n")
        try:
            numerator = float(numerator)
            denominator = float(denominator)
        except:
            print "invalid input"
            return user()
        rad = (numerator/denominator) * math.pi
        print find_pos_quad(rad)
    else:
        print "That was not a valid answer"
        user()

user()
