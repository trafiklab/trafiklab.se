---
title: Extra files
weight: 100
---

Extra files are files which provide additional information about the information in the GTFS files. They are not part of
the GTFS standard, but contain the information which is needed to link the GTFS files to internal operator systems, or
other data which is delivered by the operator.

The extra files can be fetched by taking the URL to a normal GTFS zip file, and adding \__extra_ in the filename. For
example, the file "otraf.zip" becomes "_otraf\_extra.zip_". These files use the same API key as the static data, and
count against the same quota.

In order to retrieve the static data you need an API key. Technical details for fetching the data can be found in the
API's OpenAPI specification. Trafiklabs GTFS documentation can help you to get started with GTFS files.

{{% note %}}
**Where to download**

The dataset can be accessed through the following URL:
[https://opendata.samtrafiken.se/gtfs/{operator}/{operator}_extra.zip?key={apikey}](https://opendata.samtrafiken.se/gtfs/{operator}/{operator}_extra.zip?key=APIKEY).

Replace `{operator}` with the abbreviation of the operator you want to download. These abbreviations can be found in the
OpenAPI specification, but are also listed on the [static data documentation page](static.md). Replace `{apikey}` with your own API key.
{{% /note %}}

## Included data

### trips\_dated\_vehicle\_journey.txt

This file links every GTFS trip\_id to their source GID in the Noptis data. This file is meant for those who want to
combine or integrate their systems with internal systems of transport agencies. Note that this data is only correct for
operators who deliver data to Samtrafiken in the Noptis DOI or Noptis DII format.
