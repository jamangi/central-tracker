import util

ASTRID_DATA = [
    {"date": "2023-09-20", "tasks_completed": 2.61, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-09-21", "tasks_completed": 2.64, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-09-23", "tasks_completed": 2.84, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-09-25", "tasks_completed": 2.32, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-09-27", "tasks_completed": 2.67, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-09-29", "tasks_completed": 2.79, "time_minutes": 83, "name": "Astrid"},
    {"date": "2023-10-01", "tasks_completed": 1.62, "time_minutes": 56, "name": "Astrid"},
    {"date": "2023-10-02", "tasks_completed": 2.49, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-10-04", "tasks_completed": 2.12, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-10-05", "tasks_completed": 1.99, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-10-07", "tasks_completed": 2.48, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-10-09", "tasks_completed": 2.84, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-10-11", "tasks_completed": 2.75, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-10-12", "tasks_completed": 2.71, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-10-14", "tasks_completed": 1.37, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-10-16", "tasks_completed": 2.84, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-10-18", "tasks_completed": 2.56, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-10-19", "tasks_completed": 2.42, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-10-21", "tasks_completed": 3.01, "time_minutes": 30, "name": "Astrid"},
    {"date": "2023-10-23", "tasks_completed": 2.80, "time_minutes": 30, "name": "Astrid"},
]

ASTRID_CONSISTENCY_TUPLES = [(datum['time_minutes'], util.to_date(datum['date'])) for datum in ASTRID_DATA]
