import sqlite3
from typing import Optional

def get_connection():
    """Establishes a connection to the database and returns the connection and cursor."""
    # Connect to 'road.db' database (creates if it doesn't exist)
    con = sqlite3.connect("road.db")
    # Create a cursor for executing SQL commands
    cur = con.cursor()
    return con, cur

def close_connection(con, cur):
    """Commits changes and closes the database connection."""
    # Close the cursor
    cur.close()
    # Commit any changes to the database
    con.commit()
    # Close the database connection
    con.close()

def create_database():
    """Creates the 'road' table if it doesn't already exist."""
    con, cur = get_connection()
    # Create table with columns for road data if not already created
    cur.execute("""
        CREATE TABLE IF NOT EXISTS road (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            green_time INTEGER,
            vehicle_count INTEGER,
            capacity INTEGER,
            total_time INTEGER,
            hasEmergencyVehicle BOOLEAN,
            filePath TEXT
        )
    """)
    close_connection(con, cur)

def add_road(name: str, green_time: int, vehicle_count: int, capacity: int, total_time: int, has_emergency_vehicle: bool, file_path: Optional[str] = None) -> int:
    """
    Adds a new road record to the database.
    Returns the id of the inserted row.
    """
    con, cur = get_connection()
    # Insert a new road record with given parameters
    cur.execute("""
        INSERT INTO road (name, green_time, vehicle_count, capacity, total_time, hasEmergencyVehicle, filePath) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, green_time, vehicle_count, capacity, total_time, has_emergency_vehicle, file_path))
    # Get the id of the last inserted row
    road_id = cur.lastrowid
    close_connection(con, cur)
    return road_id

def update_hasEmergencyVehicle(road_id: int, has_emergency_vehicle: bool):
    """Updates the emergency vehicle presence for a specific road by id."""
    con, cur = get_connection()
    # Update 'hasEmergencyVehicle' column for the specified road id
    cur.execute("""
        UPDATE road 
        SET hasEmergencyVehicle = ? 
        WHERE id = ?
    """, (has_emergency_vehicle, road_id))
    close_connection(con, cur)

def update_green_time(road_id: int, green_time: int):
    """Updates the green light duration for a specific road by id."""
    con, cur = get_connection()
    # Update 'green_time' column for the specified road id
    cur.execute("""
        UPDATE road 
        SET green_time = ? 
        WHERE id = ?
    """, (green_time, road_id))
    close_connection(con, cur)

def update_vehicle_count(road_id: int, vehicle_count: int):
    """Updates the vehicle count for a specific road by id."""
    con, cur = get_connection()
    # Update 'vehicle_count' column for the specified road id
    cur.execute("""
        UPDATE road 
        SET vehicle_count = ? 
        WHERE id = ?
    """, (vehicle_count, road_id))
    close_connection(con, cur)

def update_file_path(road_id: int, file_path: str):
    """Updates the file path for the traffic data source of a specific road by id."""
    con, cur = get_connection()
    # Update 'filePath' column for the specified road id
    cur.execute("""
        UPDATE road 
        SET filePath = ? 
        WHERE id = ?
    """, (file_path, road_id))
    close_connection(con, cur)

def get_green_time(road_id: int) -> Optional[int]:
    """Retrieves the green light duration for a specific road by id."""
    con, cur = get_connection()
    # Retrieve 'green_time' column for the specified road id
    cur.execute("SELECT green_time FROM road WHERE id = ?", (road_id,))
    result = cur.fetchone()
    close_connection(con, cur)
    # Return green_time if record exists, else None
    return result[0] if result else None

def get_vehicle_count(road_id: int) -> Optional[int]:
    """Retrieves the vehicle count for a specific road by id."""
    con, cur = get_connection()
    # Retrieve 'vehicle_count' column for the specified road id
    cur.execute("SELECT vehicle_count FROM road WHERE id = ?", (road_id,))
    result = cur.fetchone()
    close_connection(con, cur)
    # Return vehicle_count if record exists, else None
    return result[0] if result else None

def get_capacity(road_id: int) -> Optional[int]:
    """Retrieves the capacity for a specific road by id."""
    con, cur = get_connection()
    # Retrieve 'capacity' column for the specified road id
    cur.execute("SELECT capacity FROM road WHERE id = ?", (road_id,))
    result = cur.fetchone()
    close_connection(con, cur)
    # Return capacity if record exists, else None
    return result[0] if result else None

def get_total_time(road_id: int) -> Optional[int]:
    """Retrieves the total time data for a specific road by id."""
    con, cur = get_connection()
    # Retrieve 'total_time' column for the specified road id
    cur.execute("SELECT total_time FROM road WHERE id = ?", (road_id,))
    result = cur.fetchone()
    close_connection(con, cur)
    # Return total_time if record exists, else None
    return result[0] if result else None

def get_name(road_id: int) -> Optional[str]:
    """Retrieves the name of a specific road by id."""
    con, cur = get_connection()
    # Retrieve 'name' column for the specified road id
    cur.execute("SELECT name FROM road WHERE id = ?", (road_id,))
    result = cur.fetchone()
    close_connection(con, cur)
    # Return name if record exists, else None
    return result[0] if result else None

def get_file_path(road_id: int) -> Optional[str]:
    """Retrieves the file path for the traffic data source of a specific road by id."""
    con, cur = get_connection()
    # Retrieve 'filePath' column for the specified road id
    cur.execute("SELECT filePath FROM road WHERE id = ?", (road_id,))
    result = cur.fetchone()
    close_connection(con, cur)
    # Return filePath if record exists, else None
    return result[0] if result else None

def get_hasEmergencyVehicle(road_id: int) -> Optional[bool]:
    """Retrieves the emergency vehicle presence status for a specific road by id."""
    con, cur = get_connection()
    # Retrieve 'hasEmergencyVehicle' column for the specified road id
    cur.execute("SELECT hasEmergencyVehicle FROM road WHERE id = ?", (road_id,))
    result = cur.fetchone()
    close_connection(con, cur)
    # Return hasEmergencyVehicle if record exists, else None
    return result[0] if result else None
