import time
from road import Road
import database

database.create_database()  # Ensure the database is initialized

# Initialize roads and link them
road1 = Road("Road 1", 40, 1000, 300, 1)
road2 = Road("Road 2", 60, 800, 300, 2)
road3 = Road("Road 3", 70, 1100, 300, 1.7)
road4 = Road("Road 4", 30, 700, 300, 1.2)

road1.next = road2
road2.next = road3
road3.next = road4
road4.next = road1

roads = [road1, road2, road3, road4]
active_road = road1
start_time = time.time()

road_timestamp = None
camera_timestamp = None


while True:
    curr_time = time.time()

    # Initializing timestamps if they're None
    if road_timestamp is None:
        road_timestamp = curr_time

    if camera_timestamp is None:
        camera_timestamp = curr_time

    # Check if green time has passed, switch active road if necessary
    if curr_time - start_time > active_road.get_green_time():
        print(f"Switching green light from {active_road.get_name()} to {active_road.next.get_name()}")
        active_road.turn_red()
        active_road = active_road.next
        active_road.turn_green()
        start_time = curr_time

    # Check for emergency vehicles and prioritize the road if any is found
    for road in roads:
        if road.get_hasEmergencyVehicle():
            print(f"Emergency vehicle detected on {road.get_name()}, prioritizing this road.")
            if active_road != road:
                active_road.turn_red()
                active_road = road
                active_road.turn_green()
                start_time = curr_time
                print(f"Switched to road with emergency: {active_road.get_name()}")
            break

    # Update vehicle count every second
    if curr_time - road_timestamp > 1:
        print("\nUpdating vehicle counts:")
        for road in roads:
            road.update()
            print(f"Road {road.get_name()} - Vehicle count: {road.get_vehicle_count()}")
        road_timestamp = curr_time


        
        print(f"Active road: {active_road.get_name()}")
        print(f"Time since last switch: {curr_time - start_time:.2f} seconds")
        print(f"Road statuses:")
        for road in roads:
            print(f"  {road.get_name()} - Green: {road.is_green}, Emergency: {road.get_hasEmergencyVehicle()}")

        print(f"\n----------------------------------------------")


    # Camera updates every 10 seconds
    if curr_time - camera_timestamp > 10:
        print("\nUpdating camera data:")
        for road in roads:
            road.cam_update()
            print(f"Road {road.get_name()} - Camera updated.")
        camera_timestamp = curr_time


