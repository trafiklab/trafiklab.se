---
description: "Directed email"
hidden: true 
layout: "single"
---

# Action required: Samtrafiken Sales IDs will change on September 15, 2026

On September 15, 2026, we will replace one of the software solutions used to produce the Samtrafiken Sales data. As a
result, all `ServiceJourney` IDs in the Samtrafiken Sales NeTEx feed will change. This change will enable us to continue
improving the quality of the dataset.

## What you need to do

When importing the first dataset published after the change, please make sure that your system:

- downloads and imports the complete dataset;
- does not rely on `changes.csv` or `changeslines.csv` for an incremental update; and
- removes any previously imported traffic data before loading the new dataset.

After completing this full import, you can resume your usual update process. The file format itself will not change.

The full documentation for the Samtrafiken Sales data is available on the
[Trafiklab website](https://www.trafiklab.se/api/netex-datasets/samtrafiken-sales-data/).

If you have any questions about this change, please contact us through the
[Trafiklab support forum](https://support.trafiklab.se).
