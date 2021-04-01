---
title: Extra files
---

{% hint style="info" %} For technical details about HTTP headers, URLs, and response structures, please use the Open-API
Specification available on our developer portal. {% endhint %}

Extra files are files which provide additional information about the information in the GTFS files. They are not part of
the GTFS standard, but contain the information which is needed to link the GTFS files to internal operator systems, or
other data which is delivered by the operator. These files can be downloaded without an API key.

### **feed\_info.txt**

URL: [**https://api.resrobot.se/samtrafiken/gtfs/feed\_info.txt**](https://api.resrobot.se/samtrafiken/gtfs/feed_info.txt)

This file is included in the GTFS standard, but is also offered as a separate download. This way you can check if the
feed has been updated before downloading it.

### **trafikverket\_stops.txt**

URL: [**https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/trafikverket\_stops.txt**](https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/trafikverket_stops.txt)

This file contains a mapping between national stop IDs \(rikshållplatser\) and Trafikverkets signatures. For example,
CST -&gt; 740000001. Only for train stations.

### **agency\_stops.txt**

URL: [**https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/agency\_stops.txt**](https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/agency_stops.txt)

This file contains a mapping between the operators' local IDs and the national ids \(rikshållplatser\). For example, the
following mapping means that operator `275` uses the id `41063` for the stop with national id `740066331` .

```text
agency_id,stop_id,agency_stop_id
275,740066331,41063
```

In the GTFS `agency.txt` file, we find that agency\_id 275 corresponds to SL. In other words, SL uses id `41063` for the
stop with national id `740066331` .

```text
agency_id,stop_id,agency_stop_id
275,SL,http://www.sl.se,Europe/Stockholm,sv
```

One or more operators have a local id for each national id. Not every local id corresponds to a national id.

{% hint style="info" %} The local stop id for SL \(id 275, Stockholms Lokaltrafik\) is used by SL for _Stop-Area_. You
can use SLs API [SL Hållplatser och Linjer 2](https://www.trafiklab.se/api/sl-hallplatser-och-linjer-2/dokumentation) to
translate it to a SiteID used in other SL APIs**.**
{% endhint %}

### **agency\_stops\_&lt;AGENCY\_ID&gt;.txt**

URL: [**https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/agency\_stops\_&lt;AGENCY\_ID&gt;.txt**](https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/agency_stops_AGENCY_ID.txt?key=YOUR_API_KEY)

This file contains the same information as the agency\_stops.txt file described above, but is already filtered on a
given operator. Replace `<agency_id>` with the operator id of your choice.

### **routes\_technical.txt**

URL: [**https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/routes\_technical.txt**](https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/routes_technical.txt?key=YOUR_API_KEY)

This file maps route ids to their _technical route number_ used by their operator. A technical route number is unique
within an agency.

### **trips\_technical.txt**

URL: [**https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/trips\_technical.txt**](https://api.trafiklab.se/v2/samtrafiken/gtfs/extra/trips_technical.txt?key=YOUR_API_KEY)

This file contains a mapping between trip ids and their corresponding technical trip numbers. The technical trip number
is unique for a route in an agency. In other words, the combination of the 3 values agency\_id, technical\_route\_number
and technical\_trip\_number is unique. Train numbers always have their train number as technical trip number, even if
the train has a public line number \(for example Pendeltåg 40 i Stockholm\)
