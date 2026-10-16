---
title: "Ändringar i GTFS Regional-API:et"
date: "2020-02-20"

---

De regionala API:erna blir snart stabila. Innan vi kan släppa dem som stabila behöver vi dock göra en sista ändring av
URL-strukturen. Ändringen innebär att du som dataanvändare behöver göra en mindre ändring i din klient för att kunna
fortsätta använda våra data.

## Varför vi gör detta

För att kunna garantera att URL:erna blir permanenta behöver vi se till att de är framtidssäkra. Genom att lägga till
datatypen i varje URL (gtfs, gtfs-rt, netex) säkerställer vi att alla URL:er är konsekventa, läsbara och ger flexibilitet
i serverimplementationen. På så sätt kan vi fortsätta förbättra våra API:er utan att behöva ändra URL:erna.

## Vilka ändringar som behövs i klienter

När du hämtar statiska GTFS-filer (zip-filer) behöver du ändra bas-URL:en från
opendata.samtrafiken.se till opendata.samtrafiken.se/gtfs. Till exempel blir
https://opendata.samtrafiken.se/ul/ul.zip https://opendata.samtrafiken.se/gtfs/ul/ul.zip

När du hämtar GTFS-filer med realtidsdata (protobuf-filer) behöver du ändra bas-URL:en från
opendata.samtrafiken.se till opendata.samtrafiken.se/gtfs-rt. Till exempel blir
https://opendata.samtrafiken.se/ul/TripUpdates.pb https://opendata.samtrafiken.se/gtfs-rt/ul/TripUpdates.pb.

Dokumentationen på Trafiklab har uppdaterats med de nya URL:erna, så du hittar all information där också.

## Övergångsperiod för de nya URL:erna

Vi vidarebefordrar automatiskt alla anrop till en gammal adress till den nya adressen fram till den 31 mars 2020. Efter
den 31 mars slutar de gamla URL:erna att fungera.

Frågor Tveka inte att kontakta oss om du har några frågor. Du når oss alltid på info@trafiklab.se. 
 




