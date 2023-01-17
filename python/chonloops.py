##chon
import math


def time_to_accel(accel, distance):#time to accel
    time = math.sqrt(distance/(0.5 * accel))
    time = (time/60)
    return time
    
def dist_while_deaccel(time, deaccel, v_final):#distance while slowing down 
    peak_vel = 0 + (60 * 60 * time)
    dist_deaccel = (v_final**2 - peak_vel**2)/(2 * deaccel)
    return dist_deaccel

print("Enter the list of planes:")#takes in the list of planes 
Planes = input()
x = Planes.split()#separates them into individual strings

i = 0

while i < len(x):#will stay in the loop until it has gone through all of the items in the list
    print("Input the acceleration of", x[i], "in m/s^2")
    accel = int(input())
    print("Input the distance that", x[i], "will travel in km")
    distance = int(input())
    print("Input the rate of deacceleration", x[i], "in m/s^2")
    deaccel = int(input())
    print("Input the final velocity of", x[i], "in km/h")
    v_final = int(input())
    if x[i][0] == ["a","e","i","o","u"]:#if statement for if the plane starts with a vowel or not
        print("An", x[i], "travels", distance, "km in", time_to_accel(accel, distance), "minutes, it decelerates for", dist_while_deaccel(time_to_accel(accel, distance), deaccel, v_final), "km until it reaches a constant speed.")
    else:
        print("A", x[i], "travels", distance, "km in", time_to_accel(accel, distance), "minutes, it decelerates for", dist_while_deaccel(time_to_accel(accel, distance), deaccel, v_final), "km until it reaches a constant speed.")
    i+=1




