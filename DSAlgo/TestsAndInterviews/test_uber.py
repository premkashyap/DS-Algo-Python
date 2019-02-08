#minimum time to complete trip. 
def minimum_time(no_of_trips, list_of_cabs):
    no_of_trips_left = no_of_trips
    time_elapsed =0
    while no_of_trips_left >0:
        time_elapsed+=1
        no_of_trips_done = sum([time_elapsed//i for i in list_of_cabs])
        no_of_trips_left = no_of_trips-no_of_trips_done
    return time_elapsed   

#find the no of markings with atleast 1 uber
def no_of_markings_with_uber(ubers):
    min_value, max_value=0,0
    for uber in ubers:
        if uber[0]<min_value:
            min_value=uber[0]
        if uber[1]>max_value:
            max_value=uber[1]
    markings = [0 for i in range(min_value, max_value+1)]
    for uber in ubers:  
        for i in range(uber[0], uber[1]+1):
            markings[i-min_value] = 1
    return sum(markings)



if __name__ == '__main__':
    print(minimum_time(8, [1,2,5]))
    print(no_of_markings_with_uber([[4,7],[5,6],[-1,0]]))