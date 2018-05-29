import earth_distance as ed 
import random


def read_cities(file_name): #Reads in list of cities 
    with open(file_name, 'r') as f:
        data = f.readlines()
        data = [x.strip() for x in data]
        data = [x.split('\t') for x in data]
        t = []
        for i in data:
            t.append(tuple(i))
        return t
  
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, that is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """

def print_cities(road_map):#Prints cycle to two decimal places 
    for i in range(len(road_map)):
        for y in range(len(road_map[i])):
            try:
                print(round(float(road_map[i][y]),2), end = ' ')
            except ValueError:
                print(road_map[i][y], end = ' ')
        print()
                

def compute_total_distance(road_map): #Returns total sum of all distances in the cycle. Distance is shown in Miles
    distcnt = 0.00
    for i in range(len(road_map)):
        for y in range(1):
            if i+1 == len(road_map):
                distcnt += ed.distance(float(road_map[i][2]), float(road_map[i][3]), float(road_map[0][2]), float(road_map[0][3]))
                break
            else:
                distcnt += ed.distance(float(road_map[i][2]), float(road_map[i][3]), float(road_map[i+1][2]), float(road_map[i+1][3])) 
    return distcnt

    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """

def swap_adjacent_cities(road_map, index): #Swaps two Adjacent Cities or first and last of cycle 
    new1 = road_map
    tempi = new1[index]
    if index + 1 == len(road_map):
        new1[index] = new1[0]
        new1[0] = tempi
    else:     
        new1[index] = new1[index+1]
        new1[index +1] = tempi
    newroad_map = (new1, compute_total_distance(new1))
    return newroad_map 

    """
    Take the city at location `index` in the `road_map`, and the city at 
    location `index+1` (or at `0`, if `index` refers to the last element 
    in the list), swap their positions in the `road_map`, compute the 
    new total distance, and return the tuple 

        (new_road_map, new_total_distance)
    """

def swap_cities(road_map, index1, index2):
    if index1 == index2:
        return swap_adjacent_cities(road_map, index1)
    else:    
        new2 = road_map
        tempi = new2[index1]
        new2[index1] = new2[index2]
        new2[index2] = tempi
        newroad_map2 = (new2, compute_total_distance(new2))
        return newroad_map2
    
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """

def find_best_cycle(road_map):
    dist = compute_total_distance(road_map)
    
    count = 0
    bestroad_map = 0
    print('Finding Best Cycle')
    for i in range(100):
        count += 1
        print(count)
        t_road_map = swap_cities(road_map, random.randint(0, len(road_map)-1), random.randint(0, len(road_map)-1))
        if t_road_map[1] < dist:
            dist = t_road_map[1]
            road_map = t_road_map[0]
            bestroad_map = tuple()
            bestroad_map = t_road_map
            print('Best Distance Is:', dist)
            print('FOUND BEST!')
            print(bestroad_map[1])
        else:
            road_map = t_road_map[0]
            print(compute_total_distance(road_map))
    print('Printing first index')
    print(bestroad_map[0])
    print('printing second index')
    print(bestroad_map[1])
    optcycle = bestroad_map[0]
    print(optcycle)
    return optcycle

   
    """Using a combination of `swap_cities` and `swap_adjacent_cities`, 
    try `10000` swaps, and each time keep the best cycle found so far. 
    After `1000   0` swaps, return the best cycle found so far. """


def print_map(road_map):
    print('Please find your calculated optimum journey as follows:')
    for i in range(len(road_map)):
        if i+1 == len(road_map):
            print('Journey', i+1,':')
            print(road_map[i][1], ' -> ' , road_map[0][1])
            print(round(ed.distance(float(road_map[i][2]), float(road_map[i][3]), float(road_map[0][2]), float(road_map[0][3]))),"Miles")
        else:
            print('Journey', i+1,':')
            print(road_map[i][1], ' -> ' , road_map[i+1][1])
            print('Distance is:', round(ed.distance(float(road_map[i][2]), float(road_map[i][3]), float(road_map[i+1][2]), float(road_map[i+1][3]))),"Miles")
    print('Total Travel Distance is', round(compute_total_distance(road_map), ),'Miles')
        
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """


def main():
    road_map = read_cities('city-data.txt')
    print('Please find the list of cities you need to travel to:')
    print_cities(road_map)
    bestcycle = find_best_cycle(road_map)
    print(compute_total_distance(bestcycle))
    print_map
    
    
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    
    
if __name__ == "__main__":
    main()
