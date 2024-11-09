import cv2
from ultralytics import solutions

# Define region points for detection
region_points = [(20, 400), (1080, 404), (1080, 360), (20, 360), (20, 400)]

# Initialize Object Counter with specified region and model
counter = solutions.ObjectCounter(
    show=True,
    region=region_points,
    model="yolo11n.pt",
)

# Function to detect vehicles and emergency vehicles in the current frame of a video
def get_vehicle_condition(filePath):
    # Open the video file
    cap = cv2.VideoCapture(filePath)
    if not cap.isOpened():
        print("Error reading video file")
        return 0, False  # Return zero vehicles and no emergency if the video cannot be read

    # Read the current frame
    success, frame = cap.read()
    cap.release()  # Release video resources immediately since we only need the first frame

    if not success:
        print("Could not read the first frame")
        return 0, False  # Return zero vehicles and no emergency if the first frame is empty

    # Detect vehicles in the first frame
    result = counter.count(frame)
    
    # Get counts for each object class in the region
    detections = result["detections"]
    
    # Calculate vehicle count and check for emergency vehicles
    vehicle_count = sum(1 for d in detections if d["class"] in ["bike", "car", "bus", "truck"])
    has_emergency_vehicle = any(d["class"] in ["cops", "ambulance", "fire truck"] for d in detections)

    return vehicle_count, has_emergency_vehicle

