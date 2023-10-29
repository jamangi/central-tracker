from data_gardevoir import GARDEVOIR_DATA, GARDEVOIR_CONSISTENCY_TUPLES
from data_rhodon import RHODON_DATA, RHODON_CONSISTENCY_TUPLES
from shauntal_tracker.consistency_tracker import calculate_consistency, save_plot


gardevoir_consistency = calculate_consistency(GARDEVOIR_CONSISTENCY_TUPLES)
rhodon_consistency = calculate_consistency(RHODON_CONSISTENCY_TUPLES)
save_plot("Gardevoir Consistency Score", gardevoir_consistency, "gardevoir_score_plot.png")
save_plot("Rhodon Consistency Score", rhodon_consistency, "rhodon_score_plot.png")
