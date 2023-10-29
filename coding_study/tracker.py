from data_astrid import ASTRID_DATA, ASTRID_CONSISTENCY_TUPLES
from data_cirrus import CIRRUS_DATA, CIRRUS_CONSISTENCY_TUPLES
from shauntal_tracker.consistency_tracker import calculate_consistency, save_plot


astrid_consistency = calculate_consistency(ASTRID_CONSISTENCY_TUPLES)
cirrus_consistency = calculate_consistency(CIRRUS_CONSISTENCY_TUPLES)
save_plot("Astrid Consistency Score", astrid_consistency, "astrid_score_plot.png")
save_plot("Cirrus Consistency Score", cirrus_consistency, "cirrus_score_plot.png")
