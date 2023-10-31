import util

GARDEVOIR_DATA = [
    {"date": "2023-10-29", "gains": 2, "time_minutes": 60, "name": "Gardevoir"},
{"date": "2023-10-30", "gains": 1, "time_minutes": 90, "name": "Gardevoir"}
]

GARDEVOIR_CONSISTENCY_TUPLES = [(datum['time_minutes'], util.to_date(datum['date'])) for datum in GARDEVOIR_DATA]
