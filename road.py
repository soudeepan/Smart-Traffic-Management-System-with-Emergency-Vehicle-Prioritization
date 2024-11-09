import database
import numpy as np
import time
import detection

class Road:
    def __init__(self, name, vehicle_count, capacity, total_time, rate_of_increase, file_path=None):
        """
        Initializes a new Road instance with the specified attributes.
        Calculates initial green light time based on vehicle count and capacity.
        """
        self.next = Road  # Placeholder for linking roads in a network
        # Calculate initial green time based on current vehicle count and capacity
        green_time = vehicle_count / capacity * total_time
        # Add road data to database and store the assigned road id
        self.id = database.add_road(name, green_time, vehicle_count, capacity, total_time, False, file_path)
        self.rate_of_increase = rate_of_increase  # Rate at which vehicle count increases when red
        self.is_green = False  # Current traffic light state
        self.emergency_triggered_at = None  # Timestamp for emergency vehicle trigger

    def get_vehicle_count(self):
        """Returns the current vehicle count from the database."""
        return database.get_vehicle_count(self.id)

    def get_name(self):
        """Returns the name of the road."""
        return database.get_name(self.id)

    def get_green_time(self):
        """Returns the current green light duration for this road."""
        return database.get_green_time(self.id)

    def get_hasEmergencyVehicle(self):
        """Returns whether an emergency vehicle is currently detected on this road."""
        return database.get_hasEmergencyVehicle(self.id)

    def turn_red(self):
        """Sets the traffic light state to red."""
        self.is_green = False

    def turn_green(self):
        """Sets the traffic light state to green."""
        self.is_green = True

    def update(self):
        """
        Updates the road status including vehicle count and green light time.
        Also manages random emergency vehicle triggers with a reset time.
        """
        # Retrieve current vehicle count, capacity, and total time from the database
        vehicle_count = database.get_vehicle_count(self.id)
        capacity = database.get_capacity(self.id)
        total_time = database.get_total_time(self.id)
        
        # Adjust vehicle count based on traffic light state
        if self.is_green:
            # Decrease vehicle count if the light is green, simulating vehicle clearance
            vehicle_count -= int(capacity / 3600 * (1 + np.random.uniform(-0.1, 0.1)))  # Randomized clearance rate
        else:
            # Increase vehicle count if the light is red, simulating vehicle arrival
            vehicle_count += int(self.rate_of_increase * (1 + np.random.uniform(-0.2, 0.2)))  # Randomized increase rate
        
        # Update the vehicle count in the database
        database.update_vehicle_count(self.id, vehicle_count)

        # Recalculate and update green time based on new vehicle count
        green_time = vehicle_count / capacity * total_time
        database.update_green_time(self.id, green_time)

        # Trigger emergency vehicle randomly with a low probability and only if no emergency is active
        if np.random.rand() < 0.005 and self.emergency_triggered_at is None:  # 0.5% chance
            print(f"Emergency vehicle triggered on {self.get_name()} for a few seconds.")
            database.update_hasEmergencyVehicle(self.id, True)
            self.emergency_triggered_at = time.time()  # Record emergency trigger time

        # Check if the emergency vehicle duration has passed and reset if necessary
        if self.emergency_triggered_at:
            elapsed_time = time.time() - self.emergency_triggered_at
            if elapsed_time > 5:  # Clear emergency status after 5 seconds
                print(f"Emergency vehicle cleared from {self.get_name()} after 5 seconds.")
                database.update_hasEmergencyVehicle(self.id, False)
                self.emergency_triggered_at = None  # Reset emergency trigger

    def cam_update(self):
        """
        Updates the vehicle count and emergency status based on real-time camera detection.
        Uses detection module to assess the current frame for vehicles and emergency vehicles.
        """
        # Get real-time data from camera detection for the specified road's file path
        vehicle_count, hasEmergencyVehicle = detection.get_vehicle_condition(database.get_file_path(self.id))
        
        database.update_vehicle_count(self.id, vehicle_count)
        database.update_hasEmergencyVehicle(self.id, hasEmergencyVehicle)
