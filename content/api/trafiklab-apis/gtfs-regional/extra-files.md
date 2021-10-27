---
title: Extra files
weight: 100
---

Extra files are files which provide additional information about the information in the GTFS files. They are not part of
the GTFS standard, but contain the information which is needed to link the GTFS files to internal operator systems, or
other data which is delivered by the operator.

## Fetching extra files

The extra files can be fetched by taking the URL to a normal GTFS zip file, and adding \__extra_ in the filename. For
example, the file "otraf.zip" becomes "_otraf\_extra.zip_". These files use the same API key as the static data, and
count against the same quota.

### trips\_dated\_vehicle\_journey.txt

This file links every GTFS trip\_id to their source GID in the Noptis data. This file is meant for those who want to
combine or integrate their systems with internal systems of transport agencies. Note that this data is only correct for
operators who deliver data to Samtrafiken in the Noptis DOI or Noptis DII format.
