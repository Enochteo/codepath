from collections import deque

def track_scene_transitions(scenes):
    j = 0
    i = 1
    while i < len(scenes):
        print(f"Transition from {scenes[j]} to {scenes[i]}")
        i += 1
        j += 1
"""
    scenes_queue = deque(scenes)

    while len(scenes_queue) > 1:
        element1 = scenes_queue.popleft()
        element2 = scenes_queue[0]
        print(f"Transition from {element1} to {element2}")
"""

    

scenes = ["Opening", "Rising Action", "Climax", "Falling Action", "Resolution"]
track_scene_transitions(scenes)

scenes = ["Introduction", "Conflict", "Climax", "Denouement"]
track_scene_transitions(scenes)




def organize_scene_data_by_date(scene_records):
    dates = []
    for key in scene_records:
        date = key.split("-")
        result = "".join(date)
        result_date = int(result)
        dates.append(result_date)
    return sorted(dates)
    return sorted(scene_records, key=lambda x: x[0])

    20240820

scene_records = [
    ("2024-08-15", "Climax"),
    ("2024-08-10", "Introduction"),
    ("2024-08-20", "Resolution"),
    ("2024-08-12", "Rising Action")
]
print(organize_scene_data_by_date(scene_records))

scene_records = [
    ("2023-07-05", "Opening"),
    ("2023-07-07", "Conflict"),
    ("2023-07-01", "Setup"),
    ("2023-07-10", "Climax")
]
print(organize_scene_data_by_date(scene_records))