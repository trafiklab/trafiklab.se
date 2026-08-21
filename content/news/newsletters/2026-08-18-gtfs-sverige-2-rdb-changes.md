---
description: "Directed email"
hidden: true 
layout: "single"
---


# Action required: GTFS Sverige 2 IDs will change on September 15, 2026

On September 15, 2026, we will replace one of the software solutions used to produce GTFS Sverige 2 and Samtrafiken
Sales data. As a result, IDs in the GTFS Sverige 2 feed will change and may contain letters and hyphens instead of only
numbers. This change will enable us to continue improving the quality of these datasets.

## What you need to do

Before September 15, please make sure that your system:

- treats all GTFS IDs as strings;
- accepts alphanumeric IDs containing letters and hyphens; and
- does not rely on IDs remaining unchanged when processing data published after the change.

The GTFS standard allows alphanumeric IDs, and commonly used GTFS libraries should already support them. However, we
recommend checking your imports, database schemas, validation rules, integrations, and any code that parses or stores
GTFS IDs.

If you have any questions about this change, please contact us through the
[Trafiklab support forum](https://support.trafiklab.se).

## Consider switching to GTFS Sweden 3

In recent years, we have invested heavily in improving our open data. GTFS Sverige 2 will remain available for the
foreseeable future, but the newer GTFS Sweden 3 dataset may be better suited to your needs.

GTFS Sweden 3 covers all Swedish regions and trains and includes more detailed stops, platform numbers, and realtime
information. The `stop_areas.txt` file maps its more granular stops to the stop IDs used in GTFS Sverige 2.

[Read more about GTFS Sweden 3 on Trafiklab](https://www.trafiklab.se/api/gtfs-datasets/gtfs-sweden/).

