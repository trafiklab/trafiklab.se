---
title: Nyheter i SL Hållplatser och linjer 2
date: 2018-10-16
aliases: "/post/179106057483/nyheter-i-sl-hållplatser-och-linjer-2"
draft: true

---

Sedan några veckor tillbaks är det möjligt att filtrera på trafikslag i SL Hållplatser och linjer 2. Detta för att kunna särskilja när samma linjenummer används på flera olika trafikslag.
Exempelvis så har det ibland förekommit krockar i linjenummer mellan Waxholmsbolagets linjer och SLs linjer. Se problemet som beskrivs [här](https://kundo.se/org/trafiklabse/d/apier-for-tunnelbanors-stoppnamn/)
3.5 Filtrering av data
För modellerna line och jour är det önskvärt att kunna särskilja vilken trafiktyp datat avser. Detta kan åstadkommas genom att skicka med den valfria parametern DefaultTransportModeCode som kan innehålla någon av de Transportmode-värdena som returneras vid anrop till modellen transportmode, ex ”BUS” eller ”METRO”
 Ex:
[https://api.sl.se/api2/linedata.xml?key=[nyckel]&amp;model=line&amp;DefaultTransportModeCode=METRO](http://api.sl.se/api2/linedata.xml?key=%5bnyckel%5d&amp;model=line&amp;DefaultTransportModeCode=METRO)
[https://api.sl.se/api2/linedata.xml?key=[nyckel]&amp;model=jour&amp;DefaultTransportModeCode=BUS](http://api.sl.se/api2/linedata.xml?key=%5bnyckel%5d&amp;model=jour&amp;DefaultTransportModeCode=BUS)
 
