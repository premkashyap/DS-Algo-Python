def cellCompete(states, days):
    for _ in range(days):
        new_state = []
        current_state = [i for i in states]
        for index, _ in enumerate(current_state):
            new_state.append(int((current_state[index-1] if index >0 else 0) != (current_state[index+1] if index < len(states)-1 else 0)))
        states = new_state
    return states


def generalizedGCD(num, arr):
    def gcd(a, b):
        return b if a==0 else gcd(b%a, a)
    result = arr[0]
    for i in range(1, num):
        result = gcd(arr[i], result)
    return result

def nearestVegetarianRestaurant(totalRestaurants, allLocations, numRestaurants):
    def key_func(location):
        return location[0]**2 + location[1]**2
    allLocations.sort(key = key_func)
    return allLocations[:numRestaurants]

def optimalUtilization(deviceCapacity, foregroundAppList, backgroundAppList):
    def sort_key(device):
        return device[1]
    foregroundAppList.sort(key=sort_key, reverse=True)
    backgroundAppList.sort(key=sort_key, reverse=True)
    global_max=0
    current_max=0
    devices = []
    for fore_apps in foregroundAppList:
        if (fore_apps[1] >= deviceCapacity):
            continue
        for back_apps in backgroundAppList:
            if back_apps[1] + fore_apps[1] > deviceCapacity:
                continue
            current_max = back_apps[1] + fore_apps[1]
            if global_max ==0:
                global_max=current_max
                devices.append([fore_apps[0],back_apps[0]])
            elif current_max==global_max:
                devices.append([fore_apps[0],back_apps[0]])
            elif current_max<global_max:
                break
            
    return devices
            

if __name__ == '__main__':
    print(optimalUtilization(20, [[1,8],[2,15],[3,9]], [[1,8],[2,11],[3,12]]))