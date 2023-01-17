
import math

def time_to_accel(accel, distance):#time to accel
    time = math.sqrt(distance/(0.5 * accel))
    time = (time/60)
    return time
    
def dist_while_deaccel(time, deaccel, v_final):#distance while slowing down 
    peak_vel = 0 + (60 * 60 * time)
    dist_deaccel = (v_final**2 - peak_vel**2)/(2 * deaccel)
    return dist_deaccel

def traverse(sentance):
    index_space = sentance.find(" ")
    if(index_space<0):
        print(sentance)
    else:
        previous_space = 0
        while (index_space >= 0):
            print(sentance[previous_space: index_space])
            aeroplane = (sentance[previous_space: index_space])
            print("input the accelertiaon of {} in m/s^2" .format(aeroplane))
            acceleration = float(input())
            print("Input the distance of acceleration of {} in km:" .format(aeroplane))
            distance = float(input())
            print("Input deccelration of {} in m/s^2 (-required)" .format(aeroplane))
            deaccel = float(input())
            print("Input the final velocity of {} in m/s:" .format(aeroplane))
            v_final = float(input())
            
            print("A {} travels " + str(distance) + " km in " + str(time_to_accel(acceleration, distance)) + " minutes, it decelerates for " + str(dist_while_deaccel(time_to_accel(acceleration, distance), deaccel, v_final)) + " km until it reaches a constant speed." .format(aeroplane))
            
            
        print(sentance[previous_space: index_space])
        
print("Input the list of airplanes:")
sentance = input()
traverse(sentance)