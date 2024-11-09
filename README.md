
# Smart Traffic Management System with Emergency Vehicle Prioritization

**Tagline:** Efficient and Intelligent Traffic Control to Prioritize Emergency Vehicles and Reduce Congestion.

## 1. Project Description

### Overview
This project is a smart traffic management system designed to optimize traffic light cycles based on real-time data, with special prioritization for emergency vehicles. By dynamically adjusting green-light timings, it aims to reduce congestion and enable emergency vehicles to navigate intersections more efficiently.

### Problem Statement
Urban areas face significant traffic congestion, often resulting in delays for emergency vehicles at intersections. This project addresses this problem by automatically adjusting traffic lights to prioritize emergency vehicles and manage vehicle density more effectively.

## 2. Features

- **Real-Time Traffic Control:** Dynamically adjusts traffic light timings based on real-time vehicle density at each intersection.
- **Emergency Vehicle Detection and Prioritization:** Detects emergency vehicles on the road and grants them a green signal to pass through without delay.
- **Adaptive Timing Mechanism:** Uses the vehicle count and rate of increase on each road to calculate optimized green-light durations.
- **Data Persistence with SQLite:** Efficiently stores and retrieves road traffic data for analysis of ongoing traffic patterns.

## 3. Tech Stack

- **Programming Language:** Python
- **Database:** SQLite for efficient data storage and retrieval
- **Libraries:**
  - `ultralytics` for computer vision applications
  - `sqlite3` for database interactions
  - `numpy` for statistical adjustments in vehicle density calculations
  - Additional libraries like `time` for managing timing intervals

## 4. How It Works

### Database Schema
The database includes a table for each road, containing fields like:
- **`green_time`** - Duration of green light in seconds
- **`vehicle_count`** - Current count of vehicles in the road region
- **`capacity`** - Total capacity of vehicles the road can hold

### Road and Traffic Management Logic
- **Road Class:** Models each road's behavior, tracks traffic data, and handles updates.
- **Process Loop:** Monitors vehicle counts, calculates optimized green times, and switches active roads to ensure optimal traffic flow.
  
### Emergency Vehicle Handling
The system continuously checks for emergency vehicles using YOLO-based detection. When an emergency vehicle is detected, the traffic light state updates to provide immediate green light access to that vehicle.

## 5. Challenges and Solutions

- **Dynamic Traffic Data Management:** Efficiently handling and storing dynamic traffic data presented a challenge. Implementing SQLite provided a lightweight solution, balancing functionality with performance for real-time updates.
  
## 6. Future Improvements

- **Machine Learning for Traffic Prediction:** Integrate machine learning models to forecast traffic patterns based on historical data.
- **Real-Time Camera Integration:** Add direct camera data processing for enhanced vehicle counting accuracy.
- **Multi-Intersection Traffic Management:** Scale the system to handle a network of intersections for comprehensive traffic optimization.
