import util

ASTRID_DATA = [
    {"date": "2023-10-14", "tasks_completed": 1, "time_minutes": 90, "name": "Astrid"},
    {"date": "2023-10-15", "tasks_completed": 1, "time_minutes": 90, "name": "Astrid"},
{"date": "2023-10-16", "tasks_completed": 1, "time_minutes": 90, "name": "Astrid"},
{"date": "2023-10-17", "tasks_completed": 1, "time_minutes": 90, "name": "Astrid"},
{"date": "2023-10-19", "tasks_completed": 1, "time_minutes": 90, "name": "Astrid"},
{"date": "2023-10-20", "tasks_completed": 1, "time_minutes": 90, "name": "Astrid"},
{"date": "2023-10-21", "tasks_completed": 1, "time_minutes": 0, "name": "Astrid"},
{"date": "2023-10-22", "tasks_completed": 1, "time_minutes": 90, "name": "Astrid"},
{"date": "2023-10-23", "tasks_completed": 1, "time_minutes": 0, "name": "Astrid"},
{"date": "2023-10-24", "tasks_completed": 1, "time_minutes": 0, "name": "Astrid"},
{"date": "2023-10-26", "tasks_completed": 1, "time_minutes": 90, "name": "Astrid"},
{"date": "2023-10-27", "tasks_completed": 1, "time_minutes": 90, "name": "Astrid"},
{"date": "2023-10-28", "tasks_completed": 1, "time_minutes": 0, "name": "Astrid"},
{"date": "2023-10-29", "tasks_completed": 1, "time_minutes": 90, "name": "Astrid"},
{"date": "2023-10-30", "tasks_completed": 1, "time_minutes": 90, "name": "Astrid"},
{"date": "2023-10-31", "tasks_completed": 0, "time_minutes": 90, "name": "Astrid"},
]

ASTRID_CONSISTENCY_TUPLES = [(datum['time_minutes'], util.to_date(datum['date'])) for datum in ASTRID_DATA]
