import util

RHODON_DATA = [
    {"date": "2023-10-29", "gains": 3.01, "time_minutes": 60, "name": "Rhodon"},
{"date": "2023-10-30", "gains": 0, "time_minutes": 0, "name": "Rhodon"}
]

RHODON_CONSISTENCY_TUPLES = [(datum['time_minutes'], util.to_date(datum['date'])) for datum in RHODON_DATA]
