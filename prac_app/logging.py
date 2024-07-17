def process_logs(logs):
    """
    Input: logs is a list of tuples (timestamp, vehicle_id, event_type)
    Output: A dictionary with event types as keys and their counts as values
    """
    # Implement your solution here
    logging = {"timestamp": " ", "vehicle_id": " ", "event_type": " "}
    for log in logs:
        logging["timestamp"] = log[0]
        logging["vehicle_id"] = log[1]
        logging["event_type"] = log[2]
        print(logging)

# Example usage
logs = [
    (1621234567, "AV001", "STARTUP"),
    (1621234568, "AV002", "SENSOR_CHECK"),
    (1621234569, "AV001", "MOVE"),
    (1621234570, "AV003", "STARTUP"),
    (1621234571, "AV002", "MOVE"),
]
result = process_logs(logs)