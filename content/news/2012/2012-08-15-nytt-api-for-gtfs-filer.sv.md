---
title: Nytt API för GTFS-filer
date: 2012-08-15
aliases:
- "/post/64944546086/nytt-api-för-gtfs-filer"

---
I samband med Sweden Social Web Camp lanserar vi ett nytt API på Trafiklab. Genom det nya APIet kan du ladda ner information om all planerad kollektivtrafik i Sverige som GTFS-format. GTFS står för General Transit Feed Specification och är en internationell standard för kollektivtrafikinformation.


Vi har fått flera förfrågningar om tillgång till informationen som samlats in för att skapa olika typer av tjänster. Utifrån behoven hos dessa aktörer och internationell praxis har vi valt att tillgängliggöra informationen i filformatet GTFS (General Transit Feed Specification). Det finns en rad open source verktyg som hanterar detta format och vi på Trafiklab ser detta som ett stort steg framåt för en mer öppen och lättillgänglig information om den samlade kollektivtrafiken i Sverige.

 Ett exempel på vad man kan göra med GTFS-filerna är projektet restidskarta som är skapat av Hannes. Genom denna applikation kan du på ett överskådligt sätt se hur långt du kommer med kollektivtrafiken från en viss punkt i Sverige. Arbetet med att tillgängliggöra informationen i genom GTFS-filer stödjs av Vinnova.

## Samtrafiken - en nod för information om Sveriges kollektivtrafik

Informationen som publiceras genom det nya APIet kommer från Samtrafiken i Sverige AB (som även står bakom Trafiklab). Samtrafiken har sedan årsskiftet ansvar för att samla in information om planerad kollektivtrafik (tidtabeller) för all kollektivtrafik som bedrivs i Sverige. Detta samlas i ett _gemensamt trafikinformationssystem_ (GTI). Uppdraget regleras i en föreskrift från Transportstyrelsen och är en konsekvens av en ny lagstiftning för kollektivtrafik i Sverige. Samtrafiken har hittills endast haft möjlighet att tillgängliggöra informationen genom den nationella reseplaneraren ResRobot, i appar och genom ett  API till reseplaneraren. Sedan årsskiftet har vi dock arbetat för att hitta en möjlighet att tillgängliggöra informationen på ett sätt som inte kräver att frågor ställs till ResRobot, vilket nu resulterat i detta API. 