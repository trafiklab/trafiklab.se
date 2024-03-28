---
title: SL Reseplanerare 3.1
weight: 100
date: 2019-01-14
---

## Beskrivning

Med detta API kan du få reseförslag från A till B inom Stockholms län med SLs trafik. I SLs reseplanerare finns även Waxholmsbolagets trafik. APIet kan användas
för att beräkna reseförslag mellan valfri kombination av position och/eller stoppställe. APIet returnerar reseförslag från ”bästa matchning” av det som läggs
in.

I reseplaneraren finns det fyra olika funktioner som kan anropas:</p>

- Trip: Räknar ut en resa från en startpunkt till en destination. Dessa kan vara stations-id eller
  koordinater baserade på adresser eller ”intressepunkter.
- JourneyDetail: Returnerar detaljerad information om en del av en resa med ett fordon.
  Den returnerar en lista på alla stop/stationer inklusive alla ankomst- och avgångstider med realtidsdata(om det finns tillgängligt).<
- Reconstruction: Används för att återskapa en kopia av en Trip med hjälp av ett rekonstruktionskontext. Resultatet
  kommer att vara en fullständig kopia givet att underliggande data inte har ändrats.<
- GisRoute: Tjänsten används för att få detaljerad information om färdväg.
- XSD: Returnerar en xsd för ovanstående service-svar.

Reseplaneraren anropas med en GET-request per tjänst med UTF-8 url-kodade GET-parametrar.

## Förändringar sedan tidigare version

En ändring har genomförts som kan påverka implementerande applikationer. För version 3.1 av reseplaneraren så har svarsformatet avseende crd-elementen i den
polyline som beskriver detaljerad färdväg ändrats. Punkterna representeras i denna version av double-tal jämfört med version 3.0 som representerade dem som
heltal.

Tidigare version (3.0): *<crd>17973032</crd><crd>59360501</crd><crd>9</crd> <crd>18</crd>*

Travelplanner 3.1: *<crd>17.973032</crd><crd>59.360501</crd><crd>9.0E-6</crd><crd>1.8E-5</crd>*

## URL

- Trip: `https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/trip.<FORMAT>?key=<DIN API NYCKEL>&amp;<parametrar>`
- Journey detail: `https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/journeydetail.<FORMAT>?key=<DIN API NYCKEL>&<referensparameter>`
- Recontruction: `https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/Reconstruction.<FORMAT>?key=<DIN API NYCKEL>&<referensparameter>`
- Gisroute: https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/gisroute.<FORMAT>?key=<DIN APINYCKEL>&<parametrar>
- TTI: https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/tti?key=<DIN API NYCKEL>
- XSD: `https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/xsd.xml?key=<DIN API NYCKEL>`

{{% warning %}}
Den tidigare domänen och bas-URL:en `https://api.sl.se/api2/TravelplannerV3_1/` har ändrats den 15:e januari, och kommer sluta fungera den 15e mars 2024.
Parametrar, svarsstrukturer och API nycklar är oförändrade.
{{% /warning %}}

### API-nyckelnivåer

| Nivå   | Max anrop/minut | Max anrop/månad |
|--------|-----------------|-----------------|
| Brons  | 30              | 10 000          |
| Silver | 60              | 500 000         |
| Guld   |                 | Efter behov     |

## Format

Json eller Xml enligt ändelse till serviceanropet.

## Trip

### Parametrar

{{% warning %}}
**Ändring av Site-ID som används som sökparameter**

Efter en oväntad brytande förändring i februari 2024 så har värdet för SiteId, som förväntas av SL Reseplanerare 3.1 API, ändrats.
Dessa värden ändrades i februari men matchar fortfarande med SiteId-värden som returneras från SL Stop lookup APIet (förutsatt att båda API:erna nås genom domänen integration.sl.se).

Om du använder site-ID:n som du tidigare lagrat bör du konvertera dessa korta (4–7 siffror) site-ID:n i form av ABCDEFG (utfyllt med nollor på vänster sida) till
3BA1CDEFG. Till exempel 9001 blir 300109001.
{{% /warning %}}

| Namn              | Beskrivning                                      | Kommentar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lang              | Språk (en/sv/de)                                 | Språk i svar, default de.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| originExtId       | Startpunkt, id (9 siffror)                       | SiteId från närliggande hållplatser eller platsuppslag. Exempel: 300109001. En startpunkt måste anges med ett av originId, originExtId eller orgiginCoordLat/originCoordLong                                                                                                                                                                                                                                                                                                                                                                                                                    |
| originCoordLat    | Latitud för startpunkt. WGS84.                   | Måste anges tillsammans med originCoordLong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| originCoordLong   | Longitud för startpunkt. WGS84.                  | Måste anges tillsammans med originCoordLat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| destExtId         | Destination, id (9 siffror)                      | SiteId från närliggande hållplatser eller platsuppslag. Exempel: 300109001. En destination måste anges med ett av originId, originExtId eller orgiginCoordLat/originCoordLong                                                                                                                                                                                                                                                                                                                                                                                                                   |
| destCoordLat      | Latitud för destination. WGS84.                  | Måste anges tillsammans med destinationCoordLong.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| destCoordLong     | Longitud för destination. WGS84.                 | Måste anges tillsammans med destinationCoordLat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Via               | Lista av specification av stationer att passera. | Valfritt Separeras av ; i följande format: `viaId\|vänttid\|status\|produkter` <ul><li>viaId, internt eller extert id på hållplats/station att passera</li><li>vänttid, minuter att stanna på passerad hållplats/station (valfritt)</li><li>status, ett av EXR (av- och påstigning krävs), NER (påstigning krävs ej), NXR (avstigning krävs ej), NEXR (av och påstigning krävs ej). Valfritt, EXT är default.</li><li>produkter, trafikslag för via, se Produkt</li></ul> Ex1. via två hållplatser, 9001;9117 Ex2, via två hållpatser med 15 respektive 10 minuters väntetid, 9001\|15;9117\|10 |
| viaId             | Id för station att passera                       | Valfritt Enskilt id för en hållplats/station att resa via, ex 9001.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| viaWaitTime       | Vänttid för passerad station                     | Valfritt Antal minuter som ska spenderas på via-station angiven med viaId.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Avoid             | Lista av stationer att undvika att resa via.     | Valfritt Separeras av ; i följande format: `avoidId\|avoidStatus` <ul><li>avoidId, internt eller externt id för hållplats/ station att undvika</li><li>avoidStatus, ett av NPAVO (passera ej), NCAVO (byt ej vid)</li></ul> Valfritt.                                                                                                                                                                                                                                                                                                                                                           |
| avoidID           | Id för station att undvika                       | Valfritt Internt eller externt id för hållplats/station att undvika för byten                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| changeTimePercent | Utökad bytestid, procentuell (100-500)           | Valfritt Procentuell utökning av ursprungligt beräknad tid för att hantera ett byte. Ex, 200 dubblar tiden som systemet kommer använda för att resenären ska hinna med ett byte. Default 100.                                                                                                                                                                                                                                                                                                                                                                                                   |
| minChangeTime     | Minsta bytestid (min)                            | Valfritt Minsta antal minuter som ska användas vid byten.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| maxChangeTime     | Högsta bytestid                                  | Valfritt Flest antal minuter som ska användas vid byten.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| addChangeTime     | Utökad bytestid                                  | Valfritt Antal minuter som läggs till beräknad bytestid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| maxChange         | Max antal byten (0-11)                           | Högst antal byten på föreslagna resor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Date              | Datum åååå-MM-DD                                 | Valfritt. Datum för resa. Default är dagens datum (servertid)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Time              | Klockslag TT:MM                                  | Valfritt Klockslag för resa. Default är aktuellt klockslag (servertid)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| searchForArrival  | 0 eller 1                                        | Valfritt. Om 1 används angivna date och time för ankomsttid istället för avgångstid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| numF              | 0-6                                              | Valfritt Min antal resor efter angiven starttid, default 4. numF och numB tillsammans kan ej överstiga 6.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| numB              | 0-6                                              | Valfritt. Min antal resor före angiven starttid, default 1. numF och numB tillsammans kan ej överstiga 6.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Products          | Trafikslag, heltal                               | Valfritt Kombinationsvärde av önskade trafikslag om inte alla ska användas vid utsökning av resor. Bitmask enligt följande: Pendeltåg (1) Tunnelbana (2) Lokalbana/spårvagn (4) Buss (8) Ej i bruk (16) Ej i bruk (32) Båt typ (64) Närtrafik (128) Värdes anges som heltalsvärdet av den kombinerade bitmasken, ex Buss och båt, 8+64 = 72                                                                                                                                                                                                                                                     |
| Lines             | Inkluderade filtrering av linjer.                | Linje eller linjer, separerade med kommatecken som ska användas för att filtrera resultat, utropstecken används för exkludering av linjer. Ex: lines=55,122 (endast linje 55 och 122) lines=!19 (Ej linje 19)                                                                                                                                                                                                                                                                                                                                                                                   |
| Context           | Tidigare eller senare resor                      | Valfritt. Parameter som anger startpunkt för att söka senare eller tidigare resor. Värdet fås av resultatvärdet srcF eller srcB i ett anrop till trip-tjänsten. Se 2.4.2                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Poly              | 0 eller 1                                        | Valfritt. Anger om detaljerade färdvägar ska beräknas för resultaten. För beskrivning av polyline se 2.4.5. Default 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Passlist          | 0 eller 1                                        | Valfritt Anger om hållplatser/stationer som passeras på resan ska hämtas. Default 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| originWalk        | 0 eller 1 + detaljering                          | Valfritt, Default 1 Anger om en resa ska kunna inledas med en gångsträcka. För detaljering av avstånd kan min och max antal metrar och anges som `1,[minavstånd],[maxavstånd],[hastighet],[fågelväg]` Hastighet anges som följande: &lt; 100: snabbare = 100: normalt (default) &gt; 100: lågsammare Fågelväg: 1= på 0= av Ex. `1,0,1000,0,1` Tillåt snabb gång men maximalt 1000 meter med fågelväg.                                                                                                                                                                                           |
| destWalk          | 0 eller 1 + detaljering                          | Valfritt. Som originWalk fast för destination.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| originBike        |                                                  | Valfritt. Som originWalk Kommentar: För att få ut korrekt resultat så behöver man inaktivera sökning med gång, dvs sätta parametern originWalk=0                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| destBike          |                                                  | Valfritt. Som originWalk Kommentar: För att få ut korrekt resultat så behöver man inaktivera sökning med gång, dvs sätta parametern destWalk=0                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| originCar         |                                                  | Används ej i dagsläget                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| destCar           |                                                  | Används ej i dagsläget                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| originTaxi        |                                                  | Används ej i dagsläget                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| destTaxi          |                                                  | Används ej i dagsläget                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| originPark        |                                                  | Används ej i dagsläget Möjliggör &ldquo;Parkera och åk&rdquo; I början av en resa. För att finjustera avståndet till nästa station, se originWalk                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| destPark          |                                                  | Används ej i dagsläget Möjliggör &ldquo;Parkera och åk&rdquo; I slutet av en resa. För att finjustera avståndet till nästa station, se originWalk                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### Sökning efter tidigare eller senare resor

I resultat från trip kommer två utdataparametrar, scrB och scrF, som kan användas för att söka tidigare (scrB) eller senare (scrF) avgångar. Detta görs genom
att skicka in samma sökning till trip med parametern _context_ satt till värdet av den av de två som vill användas.

### Anmärkningar

I sökresultaten finns olika typer av anmärkningar.

Fasta anmärkningar är inlagda som ”notes”. Fasta anmärkningar är anmärkningar kopplade till avgången i tidtabellen, som tex förhandsbokning på telefon.

Störningsmeddelanden ligger inlagda som ”Messages”.

### Priser

Priser för en resa kommer i ”TariffResult”, priserna är angivna som heltal i ören. Exempelvis:

```xml

<TariffResult>
    <fareSetItem name="ONEWAY" desc="SL">
        <fareItem name="Reskassa" desc="Helt pris" cur="SEK" price="3100"/>
        <fareItem name="övriga försäljningsställen" desc="Helt pris" cur="SEK" price="4400"/>
        <fareItem name="Konduktör på Spårväg City" desc="Helt pris" cur="SEK" price="6200"/>
        <fareItem name="Reskassa" desc="Reducerat pris" cur="SEK" price="2100"/>
        <fareItem name="övriga försäljningsställen" desc="Reducerat pris" cur="SEK" price="3000"/>
        <fareItem name="Konduktör på Spårväg City" desc="Reducerat pris" cur="SEK" price="4100"/>
    </fareSetItem>
</TariffResult>
```

### Detaljerade färdvägar

Trip och journeyDetail kan leverera en detaljerad färdväg för resultatet i ”Polyline”, exempelvis:

```xml

<Polyline type="WGS84" delta="true" dim="2" crdEncS="NNNNNN">
    <crd>18.06199</crd>
    <crd>59.332455</crd>
    <crd>2.7E-5</crd>
    <crd>-9.0E-6</crd>
    <crd>-1.8E-5</crd>
    <crd>9.0E-6</crd>
</Polyline>
```

Koordinatlistan består av en startlongitud och latitud, och följande differenser från föregående punkt. Dvs i exemplet ovan en linje bestående av punkterna (
longitud, latitud):  
(18.061711,59.331331),( 18.062017, 59.332446),( 18.061999, 59.332455)

### Realtid

Realtid finns för nuvarande för bussar, pendeltåg, tvärbanan och roslagsbanan.

Realtiden är en prognos, dvs, den är ungefärlig.

Om det finns realtid så anges detta i separata fält. För realtidstider i reseförslaget så läggs ”rtTime” och ”rtDate” till i svaret. De gamla fälten ”time” och
”date” är kvar så att man vet vad det ändrats från/till.

I denna version av api:et är realtid inte parameterstyrt utan levereras alltid om data finns tillgängligt.

### Svarsformat

API:et kan returnera både xml och json.  
Json-innehållet är automatiskt konverterat från xml enligt följande regler:

* Elementnamn blir objektegenskaper
* Text (PCDATA) blir en objektegenskap med namnet "$"  
  <a>foo</a> blir { "a": { "$" : "foo" } }
* Nestlade element blir nestlade egenskaper:  
  <a><b>foo</b><c>foo</c></a>  
  blir  
  { "a": { "b" : { "$": "foo" }, "c": { "$": "foo"} } }
* Om det finns multipla element med samma namn så översätts det till en json array ex:  
  <a><b>foo1</b><b>foo2</b></a>  
  blir  
  { "a": { "b" : \[{"$": foo1" }, {"$": "foo2" }\] } }
* Attributnamn blir objektegenskaper  
  <a atb="foo1">foo2</a>  
  blir  
  { "a": { "atb" : "foo1", "$" : "foo2" } }

### Svarsstruktur

I nedan tabell beskrivs den xml struktur som finns. Vissa uppenbara attribut är inte med då det blir väldigt mycket annars, som t.ex. Lat och Lon för att ge en
lättare överblick av det som är mindre självklart.  
För mer information om olika attribut och element så finns också xsd’n hafasRestTrip.xsd.

**Exempel förklaring av nedan struktur i tabellen:**  
element1/element2 => element2 är ett underelement till element1.  
element1.attribut1 => attribut1 är ett attribut till element1.

| Element                                       | Notes                                                                                                                                                                                                                                                                        |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Element                                       | Notes                                                                                                                                                                                                                                                                        |
| Element *Error*                               | Element som innehåller felbeskrivning                                                                                                                                                                                                                                        |
| Complex type *Polyline*                       | Detaljerad färdväg, om poly=1 angivits.                                                                                                                                                                                                                                      |
| Element Product<br>Complex type *ProductType* | Produktkontext, möjliggör åtkomst till intern data.<br>Ex. <br>`<Product name=" " admin="100017" operatorCode="SL"`<br>`operator="Storstockholms Lokaltrafik" num="11297"`<br>`line="17" catOutS="MET" catOutL="TUNNELBANA "`<br>`catOut="METRO " catIn="MET" catCode="1"/>` |
| Element *JourneyDetailRef*                    | Referens till journey detail för ett detta leg-elementet.                                                                                                                                                                                                                    |
| Simple type *PrognosisType*                   | Innehåller typ av prognos. Om den rapporterades in av extern part, räknades ut, eller rättades av systemet.                                                                                                                                                                  |
| Element *Stops*                               | En lista av journey stops/stations, om passlist=1 angivits.                                                                                                                                                                                                                  |
| Complex type *StopType*                       | Elementet stop innehåller namnet, route index, latitude, longitude, departure time/date, arrival time/date, track, realtidsdata för ankomst och avgång sampt track.                                                                                                          |
| Element *Messages*                            | Innehåller en lista av meddelanden för denna trip.                                                                                                                                                                                                                           |
| Element *Names*                               | Lists av journey names                                                                                                                                                                                                                                                       |
| Element *JourneyStatus*                       | Innehåller status för Journey.                                                                                                                                                                                                                                               |
| Element *TripList*                            | Rotelement, innehåller en lista på alla Trips vid anrop till trip. Om ett större fel har inträffat under anrop så innehåller attributen errorCode och errortext felbeskrivning.                                                                                              |
| Element *Trip*                                | Trip-objektet innehåller en lista med Leg-objekt med den uträknade resan.                                                                                                                                                                                                    |
| Element *LegList*                             | Innehåller alla Leg-element för en Trip.                                                                                                                                                                                                                                     |
| Element *Leg*                                 | Leg-objektet är en del av en resa. Det kan vara antingen en gångväg, cykel eller bilväg eller oftast en resa med bus, tåg, eller annat typ av transportmedel.                                                                                                                |
| Element *Origin*                              | Innehåller namn, typ, rout index, realtidsdata för startpunkten för denna resa.                                                                                                                                                                                              |
| Element *Destination*                         | Innehåller namn, typ, rout index, realtidsdata för destinationen för denna resa.                                                                                                                                                                                             |
| Element *GisRef*                              | Referens till en specifik route i ett Leg-element.                                                                                                                                                                                                                           |

### Genererad exempeldata

```xml
<?xml version="1.0" encoding="utf-8"?>
<Trip alternative="false" valid="true" idx="1" tripId="tripId1" ctxRecon="ctxRecon1" duration="P396DT1H1M1S"
      return="false" ecoUrl="ecoUrl1" checksum="checksum1" xmlns="hafas_rest">
    <Messages>
        <Message id="id1" externalId="externalId1" act="true" pub="pub1" head="head1" lead="lead1" text="text1"
                 tckr="tckr1" company="company1" category="category1" priority="1" products="1" icon="icon1"
                 routeIdxFrom="1" routeIdxTo="1" sTime="sTime1" sDate="sDate1" eTime="eTime1" eDate="eDate1"
                 altStart="altStart1" altEnd="altEnd1">
            <affectedProduct name="name1" num="num1" line="line1" catOut="catOut1" catIn="catIn1" catCode="catCode1"
                             catOutS="catOutS1" catOutL="catOutL1" operatorCode="operatorCode1" operator="operator1"
                             admin="admin1"/>
            <affectedProduct name="name2" num="num2" line="line2" catOut="catOut2" catIn="catIn2" catCode="catCode2"
                             catOutS="catOutS2" catOutL="catOutL2" operatorCode="operatorCode2" operator="operator2"
                             admin="admin2"/>
            <affectedProduct name="name3" num="num3" line="line3" catOut="catOut3" catIn="catIn3" catCode="catCode3"
                             catOutS="catOutS3" catOutL="catOutL3" operatorCode="operatorCode3" operator="operator3"
                             admin="admin3"/>
        </Message>
        <Message id="id2" externalId="externalId2" act="false" pub="pub2" head="head2" lead="lead2" text="text2"
                 tckr="tckr2" company="company2" category="category2" priority="-2147483647" products="-2147483647"
                 icon="icon2" routeIdxFrom="-2147483647" routeIdxTo="-2147483647" sTime="sTime2" sDate="sDate2"
                 eTime="eTime2" eDate="eDate2" altStart="altStart2" altEnd="altEnd2">
            <affectedProduct name="name4" num="num4" line="line4" catOut="catOut4" catIn="catIn4" catCode="catCode4"
                             catOutS="catOutS4" catOutL="catOutL4" operatorCode="operatorCode4" operator="operator4"
                             admin="admin4"/>
            <affectedProduct name="name5" num="num5" line="line5" catOut="catOut5" catIn="catIn5" catCode="catCode5"
                             catOutS="catOutS5" catOutL="catOutL5" operatorCode="operatorCode5" operator="operator5"
                             admin="admin5"/>
            <affectedProduct name="name6" num="num6" line="line6" catOut="catOut6" catIn="catIn6" catCode="catCode6"
                             catOutS="catOutS6" catOutL="catOutL6" operatorCode="operatorCode6" operator="operator6"
                             admin="admin6"/>
        </Message>
        <Message id="id3" externalId="externalId3" act="true" pub="pub3" head="head3" lead="lead3" text="text3"
                 tckr="tckr3" company="company3" category="category3" priority="2147483647" products="2147483647"
                 icon="icon3" routeIdxFrom="2147483647" routeIdxTo="2147483647" sTime="sTime3" sDate="sDate3"
                 eTime="eTime3" eDate="eDate3" altStart="altStart3" altEnd="altEnd3">
            <affectedProduct name="name7" num="num7" line="line7" catOut="catOut7" catIn="catIn7" catCode="catCode7"
                             catOutS="catOutS7" catOutL="catOutL7" operatorCode="operatorCode7" operator="operator7"
                             admin="admin7"/>
            <affectedProduct name="name8" num="num8" line="line8" catOut="catOut8" catIn="catIn8" catCode="catCode8"
                             catOutS="catOutS8" catOutL="catOutL8" operatorCode="operatorCode8" operator="operator8"
                             admin="admin8"/>
            <affectedProduct name="name9" num="num9" line="line9" catOut="catOut9" catIn="catIn9" catCode="catCode9"
                             catOutS="catOutS9" catOutL="catOutL9" operatorCode="operatorCode9" operator="operator9"
                             admin="admin9"/>
        </Message>
    </Messages>
    <Eco co2="0.0" part="0.0" partV="0.0" nmhc="0.0" nox="0.0" prime="0.0" so2="0.0"/>
    <ServiceDays planningPeriodBegin="planningPeriodBegin1" planningPeriodEnd="planningPeriodEnd1" sDaysR="sDaysR1"
                 sDaysI="sDaysI1" sDaysB="sDaysB1" routeIdxFrom="1" routeIdxTo="1"/>
    <ServiceDays planningPeriodBegin="planningPeriodBegin2" planningPeriodEnd="planningPeriodEnd2" sDaysR="sDaysR2"
                 sDaysI="sDaysI2" sDaysB="sDaysB2" routeIdxFrom="-2147483647" routeIdxTo="-2147483647"/>
    <ServiceDays planningPeriodBegin="planningPeriodBegin3" planningPeriodEnd="planningPeriodEnd3" sDaysR="sDaysR3"
                 sDaysI="sDaysI3" sDaysB="sDaysB3" routeIdxFrom="2147483647" routeIdxTo="2147483647"/>
    <LegList>
        <Leg idx="anySimpleType" name="name1" number="number1" category="category1" type="type1" cancelled="false"
             partCancelled="false" reachable="true" direction="direction1" duration="P396DT1H1M1S" dist="1">
            <Origin name="name1" type="ST" id="id1" extId="extId1" lon="1" lat="1" routeIdx="1"
                    prognosisType="PROGNOSED" time="time1" date="date1" tz="0" track="track1" rtTime="rtTime1"
                    rtDate="rtDate1" rtTz="0" rtTrack="rtTrack1" hasMainMast="true" mainMastId="mainMastId1"
                    mainMastExtId="mainMastExtId1">
                <Notes>
                    <Note key="key1" type="U" priority="1" routeIdxFrom="1" routeIdxTo="1">Note1</Note>
                    <Note key="key2" type="A" priority="-2147483647" routeIdxFrom="-2147483647"
                          routeIdxTo="-2147483647">Note2
                    </Note>
                    <Note key="key3" type="I" priority="2147483647" routeIdxFrom="2147483647" routeIdxTo="2147483647">
                        Note3
                    </Note>
                </Notes>
            </Origin>
            <Destination name="name1" type="ST" id="id1" extId="extId1" lon="1" lat="1" routeIdx="1"
                         prognosisType="PROGNOSED" time="time1" date="date1" tz="0" track="track1" rtTime="rtTime1"
                         rtDate="rtDate1" rtTz="0" rtTrack="rtTrack1" hasMainMast="true" mainMastId="mainMastId1"
                         mainMastExtId="mainMastExtId1"/>
            <JourneyDetailRef ref="ref1"/>
            <GeometryRef ref="anySimpleType"/>
            <GisRef ref="ref1"/>
            <GisRoute dist="1" durS="P396DT1H1M1S" durR="P396DT1H1M1S" durST="P396DT1H1M1S" durW2C="P396DT1H1M1S"
                      durW2D="P396DT1H1M1S" dirTxt="dirTxt1" dirGeo="1">
                <seg name="name1" rType="U" rNum="rNum1" man="NO" manTx="manTx1" dirTx="dirTx1" ori="U" polyS="1"
                     polyE="1" dist="1"/>
                <seg name="name2" rType="M" rNum="rNum2" man="FR" manTx="manTx2" dirTx="dirTx2" ori="N"
                     polyS="-2147483647" polyE="-2147483647" dist="-2147483647"/>
                <seg name="name3" rType="H" rNum="rNum3" man="TO" manTx="manTx3" dirTx="dirTx3" ori="S"
                     polyS="2147483647" polyE="2147483647" dist="2147483647"/>
                <polyline name="name1" delta="true" dim="2" type="WGS84" crdEncYX="crdEncYX1" crdEncZ="crdEncZ1"
                          crdEncS="crdEncS1">
                    <crd>1</crd>
                    <crd>-2147483647</crd>
                    <crd>2147483647</crd>
                </polyline>
                <altPolyline name="name1" delta="true" dim="2" type="WGS84" crdEncYX="crdEncYX1" crdEncZ="crdEncZ1"
                             crdEncS="crdEncS1">
                    <crd>1</crd>
                    <crd>-2147483647</crd>
                    <crd>2147483647</crd>
                </altPolyline>
                <altPolyline name="name2" delta="false" dim="1" type="WGS84" crdEncYX="crdEncYX2" crdEncZ="crdEncZ2"
                             crdEncS="crdEncS2">
                    <crd>0</crd>
                    <crd>2</crd>
                    <crd>-2147483646</crd>
                </altPolyline>
                <altPolyline name="name3" delta="true" dim="-2147483647" type="PLANAR" crdEncYX="crdEncYX3"
                             crdEncZ="crdEncZ3" crdEncS="crdEncS3">
                    <crd>2147483646</crd>
                    <crd>-1</crd>
                    <crd>3</crd>
                </altPolyline>
            </GisRoute>
            <JourneyStatus>P</JourneyStatus>
            <Product name="name1" num="num1" line="line1" catOut="catOut1" catIn="catIn1" catCode="catCode1"
                     catOutS="catOutS1" catOutL="catOutL1" operatorCode="operatorCode1" operator="operator1"
                     admin="admin1"/>
            <Polyline name="name1" delta="true" dim="2" type="WGS84" crdEncYX="crdEncYX1" crdEncZ="crdEncZ1"
                      crdEncS="crdEncS1">
                <crd>1</crd>
                <crd>-2147483647</crd>
                <crd>2147483647</crd>
            </Polyline>
            <Stops>
                <Stop name="name1" id="id1" extId="extId1" routeIdx="1" lon="1" lat="1" arrPrognosisType="PROGNOSED"
                      depPrognosisType="PROGNOSED" depTime="depTime1" depDate="depDate1" depTz="0" arrTime="arrTime1"
                      arrDate="arrDate1" arrTz="0" passingTime="passingTime1" passingDate="passingDate1" passingTz="0"
                      arrTrack="arrTrack1" depTrack="depTrack1" rtDepTime="rtDepTime1" rtDepDate="rtDepDate1"
                      rtDepTz="0" rtArrTime="rtArrTime1" rtArrDate="rtArrDate1" rtArrTz="0" rtArrTrack="rtArrTrack1"
                      rtDepTrack="rtDepTrack1" rtPassingTime="rtPassingTime1" rtPassingDate="rtPassingDate1"
                      rtPassingTz="0" cancelled="false" hasMainMast="true" mainMastId="mainMastId1"
                      mainMastExtId="mainMastExtId1"/>
                <Stop name="name2" id="id2" extId="extId2" routeIdx="-2147483647" lon="-79228162514264337593543950335"
                      lat="-79228162514264337593543950335" arrPrognosisType="MANUAL" depPrognosisType="MANUAL"
                      depTime="depTime2" depDate="depDate2" depTz="1" arrTime="arrTime2" arrDate="arrDate2" arrTz="1"
                      passingTime="passingTime2" passingDate="passingDate2" passingTz="1" arrTrack="arrTrack2"
                      depTrack="depTrack2" rtDepTime="rtDepTime2" rtDepDate="rtDepDate2" rtDepTz="1"
                      rtArrTime="rtArrTime2" rtArrDate="rtArrDate2" rtArrTz="1" rtArrTrack="rtArrTrack2"
                      rtDepTrack="rtDepTrack2" rtPassingTime="rtPassingTime2" rtPassingDate="rtPassingDate2"
                      rtPassingTz="1" cancelled="true" hasMainMast="false" mainMastId="mainMastId2"
                      mainMastExtId="mainMastExtId2"/>
                <Stop name="name3" id="id3" extId="extId3" routeIdx="2147483647" lon="79228162514264337593543950335"
                      lat="79228162514264337593543950335" arrPrognosisType="REPORTED" depPrognosisType="REPORTED"
                      depTime="depTime3" depDate="depDate3" depTz="-2147483647" arrTime="arrTime3" arrDate="arrDate3"
                      arrTz="-2147483647" passingTime="passingTime3" passingDate="passingDate3" passingTz="-2147483647"
                      arrTrack="arrTrack3" depTrack="depTrack3" rtDepTime="rtDepTime3" rtDepDate="rtDepDate3"
                      rtDepTz="-2147483647" rtArrTime="rtArrTime3" rtArrDate="rtArrDate3" rtArrTz="-2147483647"
                      rtArrTrack="rtArrTrack3" rtDepTrack="rtDepTrack3" rtPassingTime="rtPassingTime3"
                      rtPassingDate="rtPassingDate3" rtPassingTz="-2147483647" cancelled="false" hasMainMast="true"
                      mainMastId="mainMastId3" mainMastExtId="mainMastExtId3"/>
            </Stops>
        </Leg>
        <Leg idx="anySimpleType" name="name2" number="number2" category="category2" type="type2" cancelled="true"
             partCancelled="true" reachable="true" direction="direction2" duration="-P10675199DT2H48M5.477S"
             dist="-2147483647">
            <Origin name="name2" type="ADR" id="id2" extId="extId2" lon="-79228162514264337593543950335"
                    lat="-79228162514264337593543950335" routeIdx="-2147483647" prognosisType="MANUAL" time="time2"
                    date="date2" tz="1" track="track2" rtTime="rtTime2" rtDate="rtDate2" rtTz="1" rtTrack="rtTrack2"
                    hasMainMast="false" mainMastId="mainMastId2" mainMastExtId="mainMastExtId2">
                <Notes>
                    <Note key="key4" type="R" priority="0" routeIdxFrom="0" routeIdxTo="0">Note4</Note>
                    <Note key="key5" type="H" priority="2" routeIdxFrom="2" routeIdxTo="2">Note5</Note>
                    <Note key="key6" type="U" priority="-2147483646" routeIdxFrom="-2147483646"
                          routeIdxTo="-2147483646">Note6
                    </Note>
                </Notes>
            </Origin>
            <Destination name="name2" type="ADR" id="id2" extId="extId2" lon="-79228162514264337593543950335"
                         lat="-79228162514264337593543950335" routeIdx="-2147483647" prognosisType="MANUAL" time="time2"
                         date="date2" tz="1" track="track2" rtTime="rtTime2" rtDate="rtDate2" rtTz="1"
                         rtTrack="rtTrack2" hasMainMast="false" mainMastId="mainMastId2"
                         mainMastExtId="mainMastExtId2"/>
            <JourneyDetailRef ref="ref2"/>
            <GeometryRef ref="anySimpleType"/>
            <GisRef ref="ref2"/>
            <GisRoute dist="-2147483647" durS="-P10675199DT2H48M5.477S" durR="-P10675199DT2H48M5.477S"
                      durST="-P10675199DT2H48M5.477S" durW2C="-P10675199DT2H48M5.477S" durW2D="-P10675199DT2H48M5.477S"
                      dirTxt="dirTxt2" dirGeo="-2147483647">
                <seg name="name4" rType="T" rNum="rNum4" man="ON" manTx="manTx4" dirTx="dirTx4" ori="E" polyS="0"
                     polyE="0" dist="0"/>
                <seg name="name5" rType="T4L" rNum="rNum5" man="LE" manTx="manTx5" dirTx="dirTx5" ori="W" polyS="2"
                     polyE="2" dist="2"/>
                <seg name="name6" rType="T2L" rNum="rNum6" man="RI" manTx="manTx6" dirTx="dirTx6" ori="NE"
                     polyS="-2147483646" polyE="-2147483646" dist="-2147483646"/>
                <polyline name="name2" delta="false" dim="1" type="WGS84" crdEncYX="crdEncYX2" crdEncZ="crdEncZ2"
                          crdEncS="crdEncS2">
                    <crd>0</crd>
                    <crd>2</crd>
                    <crd>-2147483646</crd>
                </polyline>
                <altPolyline name="name4" delta="false" dim="2147483647" type="HAFASGEO" crdEncYX="crdEncYX4"
                             crdEncZ="crdEncZ4" crdEncS="crdEncS4">
                    <crd>-2147483645</crd>
                    <crd>2147483645</crd>
                    <crd>-2</crd>
                </altPolyline>
                <altPolyline name="name5" delta="true" dim="0" type="WGS84" crdEncYX="crdEncYX5" crdEncZ="crdEncZ5"
                             crdEncS="crdEncS5">
                    <crd>4</crd>
                    <crd>-2147483644</crd>
                    <crd>2147483644</crd>
                </altPolyline>
                <altPolyline name="name6" delta="false" dim="2" type="PLANAR" crdEncYX="crdEncYX6" crdEncZ="crdEncZ6"
                             crdEncS="crdEncS6">
                    <crd>-3</crd>
                    <crd>5</crd>
                    <crd>-2147483643</crd>
                </altPolyline>
            </GisRoute>
            <JourneyStatus>R</JourneyStatus>
            <Product name="name2" num="num2" line="line2" catOut="catOut2" catIn="catIn2" catCode="catCode2"
                     catOutS="catOutS2" catOutL="catOutL2" operatorCode="operatorCode2" operator="operator2"
                     admin="admin2"/>
            <Polyline name="name2" delta="false" dim="1" type="WGS84" crdEncYX="crdEncYX2" crdEncZ="crdEncZ2"
                      crdEncS="crdEncS2">
                <crd>0</crd>
                <crd>2</crd>
                <crd>-2147483646</crd>
            </Polyline>
            <Stops>
                <Stop name="name4" id="id4" extId="extId4" routeIdx="0" lon="0.9" lat="0.9" arrPrognosisType="CORRECTED"
                      depPrognosisType="CORRECTED" depTime="depTime4" depDate="depDate4" depTz="2147483647"
                      arrTime="arrTime4" arrDate="arrDate4" arrTz="2147483647" passingTime="passingTime4"
                      passingDate="passingDate4" passingTz="2147483647" arrTrack="arrTrack4" depTrack="depTrack4"
                      rtDepTime="rtDepTime4" rtDepDate="rtDepDate4" rtDepTz="2147483647" rtArrTime="rtArrTime4"
                      rtArrDate="rtArrDate4" rtArrTz="2147483647" rtArrTrack="rtArrTrack4" rtDepTrack="rtDepTrack4"
                      rtPassingTime="rtPassingTime4" rtPassingDate="rtPassingDate4" rtPassingTz="2147483647"
                      cancelled="true" hasMainMast="false" mainMastId="mainMastId4" mainMastExtId="mainMastExtId4"/>
                <Stop name="name5" id="id5" extId="extId5" routeIdx="2" lon="1.1" lat="1.1"
                      arrPrognosisType="CALCULATED" depPrognosisType="CALCULATED" depTime="depTime5" depDate="depDate5"
                      depTz="0" arrTime="arrTime5" arrDate="arrDate5" arrTz="0" passingTime="passingTime5"
                      passingDate="passingDate5" passingTz="0" arrTrack="arrTrack5" depTrack="depTrack5"
                      rtDepTime="rtDepTime5" rtDepDate="rtDepDate5" rtDepTz="0" rtArrTime="rtArrTime5"
                      rtArrDate="rtArrDate5" rtArrTz="0" rtArrTrack="rtArrTrack5" rtDepTrack="rtDepTrack5"
                      rtPassingTime="rtPassingTime5" rtPassingDate="rtPassingDate5" rtPassingTz="0" cancelled="false"
                      hasMainMast="true" mainMastId="mainMastId5" mainMastExtId="mainMastExtId5"/>
                <Stop name="name6" id="id6" extId="extId6" routeIdx="-2147483646" lon="-79228162514264337593543950335"
                      lat="-79228162514264337593543950335" arrPrognosisType="PROGNOSED" depPrognosisType="PROGNOSED"
                      depTime="depTime6" depDate="depDate6" depTz="2" arrTime="arrTime6" arrDate="arrDate6" arrTz="2"
                      passingTime="passingTime6" passingDate="passingDate6" passingTz="2" arrTrack="arrTrack6"
                      depTrack="depTrack6" rtDepTime="rtDepTime6" rtDepDate="rtDepDate6" rtDepTz="2"
                      rtArrTime="rtArrTime6" rtArrDate="rtArrDate6" rtArrTz="2" rtArrTrack="rtArrTrack6"
                      rtDepTrack="rtDepTrack6" rtPassingTime="rtPassingTime6" rtPassingDate="rtPassingDate6"
                      rtPassingTz="2" cancelled="true" hasMainMast="false" mainMastId="mainMastId6"
                      mainMastExtId="mainMastExtId6"/>
            </Stops>
        </Leg>
        <Leg idx="anySimpleType" name="name3" number="number3" category="category3" type="type3" cancelled="false"
             partCancelled="false" reachable="false" direction="direction3" duration="P10675199DT2H48M5.477S"
             dist="2147483647">
            <Origin name="name3" type="POI" id="id3" extId="extId3" lon="79228162514264337593543950335"
                    lat="79228162514264337593543950335" routeIdx="2147483647" prognosisType="REPORTED" time="time3"
                    date="date3" tz="-2147483647" track="track3" rtTime="rtTime3" rtDate="rtDate3" rtTz="-2147483647"
                    rtTrack="rtTrack3" hasMainMast="true" mainMastId="mainMastId3" mainMastExtId="mainMastExtId3">
                <Notes>
                    <Note key="key7" type="A" priority="2147483646" routeIdxFrom="2147483646" routeIdxTo="2147483646">
                        Note7
                    </Note>
                    <Note key="key8" type="I" priority="-1" routeIdxFrom="-1" routeIdxTo="-1">Note8</Note>
                    <Note key="key9" type="R" priority="3" routeIdxFrom="3" routeIdxTo="3">Note9</Note>
                </Notes>
            </Origin>
            <Destination name="name3" type="POI" id="id3" extId="extId3" lon="79228162514264337593543950335"
                         lat="79228162514264337593543950335" routeIdx="2147483647" prognosisType="REPORTED" time="time3"
                         date="date3" tz="-2147483647" track="track3" rtTime="rtTime3" rtDate="rtDate3"
                         rtTz="-2147483647" rtTrack="rtTrack3" hasMainMast="true" mainMastId="mainMastId3"
                         mainMastExtId="mainMastExtId3"/>
            <JourneyDetailRef ref="ref3"/>
            <GeometryRef ref="anySimpleType"/>
            <GisRef ref="ref3"/>
            <GisRoute dist="2147483647" durS="P10675199DT2H48M5.477S" durR="P10675199DT2H48M5.477S"
                      durST="P10675199DT2H48M5.477S" durW2C="P10675199DT2H48M5.477S" durW2D="P10675199DT2H48M5.477S"
                      dirTxt="dirTxt3" dirGeo="2147483647">
                <seg name="name7" rType="TR" rNum="rNum7" man="KL" manTx="manTx7" dirTx="dirTx7" ori="SE"
                     polyS="2147483646" polyE="2147483646" dist="2147483646"/>
                <seg name="name8" rType="NT" rNum="rNum8" man="KR" manTx="manTx8" dirTx="dirTx8" ori="NW" polyS="-1"
                     polyE="-1" dist="-1"/>
                <seg name="name9" rType="CT" rNum="rNum9" man="HL" manTx="manTx9" dirTx="dirTx9" ori="SW" polyS="3"
                     polyE="3" dist="3"/>
                <polyline name="name3" delta="true" dim="-2147483647" type="PLANAR" crdEncYX="crdEncYX3"
                          crdEncZ="crdEncZ3" crdEncS="crdEncS3">
                    <crd>2147483646</crd>
                    <crd>-1</crd>
                    <crd>3</crd>
                </polyline>
                <altPolyline name="name7" delta="true" dim="-2147483646" type="HAFASGEO" crdEncYX="crdEncYX7"
                             crdEncZ="crdEncZ7" crdEncS="crdEncS7">
                    <crd>2147483643</crd>
                    <crd>-4</crd>
                    <crd>6</crd>
                </altPolyline>
                <altPolyline name="name8" delta="false" dim="2147483646" type="WGS84" crdEncYX="crdEncYX8"
                             crdEncZ="crdEncZ8" crdEncS="crdEncS8">
                    <crd>-2147483642</crd>
                    <crd>2147483642</crd>
                    <crd>-5</crd>
                </altPolyline>
                <altPolyline name="name9" delta="true" dim="-1" type="PLANAR" crdEncYX="crdEncYX9" crdEncZ="crdEncZ9"
                             crdEncS="crdEncS9">
                    <crd>7</crd>
                    <crd>-2147483641</crd>
                    <crd>2147483641</crd>
                </altPolyline>
            </GisRoute>
            <JourneyStatus>A</JourneyStatus>
            <Product name="name3" num="num3" line="line3" catOut="catOut3" catIn="catIn3" catCode="catCode3"
                     catOutS="catOutS3" catOutL="catOutL3" operatorCode="operatorCode3" operator="operator3"
                     admin="admin3"/>
            <Polyline name="name3" delta="true" dim="-2147483647" type="PLANAR" crdEncYX="crdEncYX3" crdEncZ="crdEncZ3"
                      crdEncS="crdEncS3">
                <crd>2147483646</crd>
                <crd>-1</crd>
                <crd>3</crd>
            </Polyline>
            <Stops>
                <Stop name="name7" id="id7" extId="extId7" routeIdx="2147483646" lon="79228162514264337593543950335"
                      lat="79228162514264337593543950335" arrPrognosisType="MANUAL" depPrognosisType="MANUAL"
                      depTime="depTime7" depDate="depDate7" depTz="-2147483646" arrTime="arrTime7" arrDate="arrDate7"
                      arrTz="-2147483646" passingTime="passingTime7" passingDate="passingDate7" passingTz="-2147483646"
                      arrTrack="arrTrack7" depTrack="depTrack7" rtDepTime="rtDepTime7" rtDepDate="rtDepDate7"
                      rtDepTz="-2147483646" rtArrTime="rtArrTime7" rtArrDate="rtArrDate7" rtArrTz="-2147483646"
                      rtArrTrack="rtArrTrack7" rtDepTrack="rtDepTrack7" rtPassingTime="rtPassingTime7"
                      rtPassingDate="rtPassingDate7" rtPassingTz="-2147483646" cancelled="false" hasMainMast="true"
                      mainMastId="mainMastId7" mainMastExtId="mainMastExtId7"/>
                <Stop name="name8" id="id8" extId="extId8" routeIdx="-1" lon="0.8" lat="0.8" arrPrognosisType="REPORTED"
                      depPrognosisType="REPORTED" depTime="depTime8" depDate="depDate8" depTz="2147483646"
                      arrTime="arrTime8" arrDate="arrDate8" arrTz="2147483646" passingTime="passingTime8"
                      passingDate="passingDate8" passingTz="2147483646" arrTrack="arrTrack8" depTrack="depTrack8"
                      rtDepTime="rtDepTime8" rtDepDate="rtDepDate8" rtDepTz="2147483646" rtArrTime="rtArrTime8"
                      rtArrDate="rtArrDate8" rtArrTz="2147483646" rtArrTrack="rtArrTrack8" rtDepTrack="rtDepTrack8"
                      rtPassingTime="rtPassingTime8" rtPassingDate="rtPassingDate8" rtPassingTz="2147483646"
                      cancelled="true" hasMainMast="false" mainMastId="mainMastId8" mainMastExtId="mainMastExtId8"/>
                <Stop name="name9" id="id9" extId="extId9" routeIdx="3" lon="1.2" lat="1.2" arrPrognosisType="CORRECTED"
                      depPrognosisType="CORRECTED" depTime="depTime9" depDate="depDate9" depTz="-1" arrTime="arrTime9"
                      arrDate="arrDate9" arrTz="-1" passingTime="passingTime9" passingDate="passingDate9" passingTz="-1"
                      arrTrack="arrTrack9" depTrack="depTrack9" rtDepTime="rtDepTime9" rtDepDate="rtDepDate9"
                      rtDepTz="-1" rtArrTime="rtArrTime9" rtArrDate="rtArrDate9" rtArrTz="-1" rtArrTrack="rtArrTrack9"
                      rtDepTrack="rtDepTrack9" rtPassingTime="rtPassingTime9" rtPassingDate="rtPassingDate9"
                      rtPassingTz="-1" cancelled="false" hasMainMast="true" mainMastId="mainMastId9"
                      mainMastExtId="mainMastExtId9"/>
            </Stops>
        </Leg>
    </LegList>
    <TariffResult>
        <fareSetItem name="name1" desc="desc1">
            <ticketParam name="name1" value="value1"/>
            <ticketParam name="name2" value="value2"/>
            <ticketParam name="name3" value="value3"/>
            <fareItem name="name1" desc="desc1" price="0" cur="cur1" shpCtx="shpCtx1">
                <ticket name="name1" desc="desc1" price="0" cur="cur1" shpCtx="shpCtx1">
                    <ticketParam name="name1" value="value1"/>
                    <ticketParam name="name2" value="value2"/>
                    <ticketParam name="name3" value="value3"/>
                </ticket>
                <ticket name="name2" desc="desc2" price="1" cur="cur2" shpCtx="shpCtx2">
                    <ticketParam name="name4" value="value4"/>
                    <ticketParam name="name5" value="value5"/>
                    <ticketParam name="name6" value="value6"/>
                </ticket>
                <ticket name="name3" desc="desc3" price="-2147483647" cur="cur3" shpCtx="shpCtx3">
                    <ticketParam name="name7" value="value7"/>
                    <ticketParam name="name8" value="value8"/>
                    <ticketParam name="name9" value="value9"/>
                </ticket>
            </fareItem>
            <fareItem name="name2" desc="desc2" price="1" cur="cur2" shpCtx="shpCtx2">
                <ticket name="name4" desc="desc4" price="2147483647" cur="cur4" shpCtx="shpCtx4">
                    <ticketParam name="name10" value="value10"/>
                    <ticketParam name="name11" value="value11"/>
                    <ticketParam name="name12" value="value12"/>
                </ticket>
                <ticket name="name5" desc="desc5" price="0" cur="cur5" shpCtx="shpCtx5">
                    <ticketParam name="name13" value="value13"/>
                    <ticketParam name="name14" value="value14"/>
                    <ticketParam name="name15" value="value15"/>
                </ticket>
                <ticket name="name6" desc="desc6" price="2" cur="cur6" shpCtx="shpCtx6">
                    <ticketParam name="name16" value="value16"/>
                    <ticketParam name="name17" value="value17"/>
                    <ticketParam name="name18" value="value18"/>
                </ticket>
            </fareItem>
            <fareItem name="name3" desc="desc3" price="-2147483647" cur="cur3" shpCtx="shpCtx3">
                <ticket name="name7" desc="desc7" price="-2147483646" cur="cur7" shpCtx="shpCtx7">
                    <ticketParam name="name19" value="value19"/>
                    <ticketParam name="name20" value="value20"/>
                    <ticketParam name="name21" value="value21"/>
                </ticket>
                <ticket name="name8" desc="desc8" price="2147483646" cur="cur8" shpCtx="shpCtx8">
                    <ticketParam name="name22" value="value22"/>
                    <ticketParam name="name23" value="value23"/>
                    <ticketParam name="name24" value="value24"/>
                </ticket>
                <ticket name="name9" desc="desc9" price="-1" cur="cur9" shpCtx="shpCtx9">
                    <ticketParam name="name25" value="value25"/>
                    <ticketParam name="name26" value="value26"/>
                    <ticketParam name="name27" value="value27"/>
                </ticket>
            </fareItem>
        </fareSetItem>
        <fareSetItem name="name2" desc="desc2">
            <ticketParam name="name4" value="value4"/>
            <ticketParam name="name5" value="value5"/>
            <ticketParam name="name6" value="value6"/>
            <fareItem name="name4" desc="desc4" price="2147483647" cur="cur4" shpCtx="shpCtx4">
                <ticket name="name10" desc="desc10" price="3" cur="cur10" shpCtx="shpCtx10">
                    <ticketParam name="name28" value="value28"/>
                    <ticketParam name="name29" value="value29"/>
                    <ticketParam name="name30" value="value30"/>
                </ticket>
                <ticket name="name11" desc="desc11" price="-2147483645" cur="cur11" shpCtx="shpCtx11">
                    <ticketParam name="name31" value="value31"/>
                    <ticketParam name="name32" value="value32"/>
                    <ticketParam name="name33" value="value33"/>
                </ticket>
                <ticket name="name12" desc="desc12" price="2147483645" cur="cur12" shpCtx="shpCtx12">
                    <ticketParam name="name34" value="value34"/>
                    <ticketParam name="name35" value="value35"/>
                    <ticketParam name="name36" value="value36"/>
                </ticket>
            </fareItem>
            <fareItem name="name5" desc="desc5" price="0" cur="cur5" shpCtx="shpCtx5">
                <ticket name="name13" desc="desc13" price="-2" cur="cur13" shpCtx="shpCtx13">
                    <ticketParam name="name37" value="value37"/>
                    <ticketParam name="name38" value="value38"/>
                    <ticketParam name="name39" value="value39"/>
                </ticket>
                <ticket name="name14" desc="desc14" price="4" cur="cur14" shpCtx="shpCtx14">
                    <ticketParam name="name40" value="value40"/>
                    <ticketParam name="name41" value="value41"/>
                    <ticketParam name="name42" value="value42"/>
                </ticket>
                <ticket name="name15" desc="desc15" price="-2147483644" cur="cur15" shpCtx="shpCtx15">
                    <ticketParam name="name43" value="value43"/>
                    <ticketParam name="name44" value="value44"/>
                    <ticketParam name="name45" value="value45"/>
                </ticket>
            </fareItem>
            <fareItem name="name6" desc="desc6" price="2" cur="cur6" shpCtx="shpCtx6">
                <ticket name="name16" desc="desc16" price="2147483644" cur="cur16" shpCtx="shpCtx16">
                    <ticketParam name="name46" value="value46"/>
                    <ticketParam name="name47" value="value47"/>
                    <ticketParam name="name48" value="value48"/>
                </ticket>
                <ticket name="name17" desc="desc17" price="-3" cur="cur17" shpCtx="shpCtx17">
                    <ticketParam name="name49" value="value49"/>
                    <ticketParam name="name50" value="value50"/>
                    <ticketParam name="name51" value="value51"/>
                </ticket>
                <ticket name="name18" desc="desc18" price="5" cur="cur18" shpCtx="shpCtx18">
                    <ticketParam name="name52" value="value52"/>
                    <ticketParam name="name53" value="value53"/>
                    <ticketParam name="name54" value="value54"/>
                </ticket>
            </fareItem>
        </fareSetItem>
        <fareSetItem name="name3" desc="desc3">
            <ticketParam name="name7" value="value7"/>
            <ticketParam name="name8" value="value8"/>
            <ticketParam name="name9" value="value9"/>
            <fareItem name="name7" desc="desc7" price="-2147483646" cur="cur7" shpCtx="shpCtx7">
                <ticket name="name19" desc="desc19" price="-2147483643" cur="cur19" shpCtx="shpCtx19">
                    <ticketParam name="name55" value="value55"/>
                    <ticketParam name="name56" value="value56"/>
                    <ticketParam name="name57" value="value57"/>
                </ticket>
                <ticket name="name20" desc="desc20" price="2147483643" cur="cur20" shpCtx="shpCtx20">
                    <ticketParam name="name58" value="value58"/>
                    <ticketParam name="name59" value="value59"/>
                    <ticketParam name="name60" value="value60"/>
                </ticket>
                <ticket name="name21" desc="desc21" price="-4" cur="cur21" shpCtx="shpCtx21">
                    <ticketParam name="name61" value="value61"/>
                    <ticketParam name="name62" value="value62"/>
                    <ticketParam name="name63" value="value63"/>
                </ticket>
            </fareItem>
            <fareItem name="name8" desc="desc8" price="2147483646" cur="cur8" shpCtx="shpCtx8">
                <ticket name="name22" desc="desc22" price="6" cur="cur22" shpCtx="shpCtx22">
                    <ticketParam name="name64" value="value64"/>
                    <ticketParam name="name65" value="value65"/>
                    <ticketParam name="name66" value="value66"/>
                </ticket>
                <ticket name="name23" desc="desc23" price="-2147483642" cur="cur23" shpCtx="shpCtx23">
                    <ticketParam name="name67" value="value67"/>
                    <ticketParam name="name68" value="value68"/>
                    <ticketParam name="name69" value="value69"/>
                </ticket>
                <ticket name="name24" desc="desc24" price="2147483642" cur="cur24" shpCtx="shpCtx24">
                    <ticketParam name="name70" value="value70"/>
                    <ticketParam name="name71" value="value71"/>
                    <ticketParam name="name72" value="value72"/>
                </ticket>
            </fareItem>
            <fareItem name="name9" desc="desc9" price="-1" cur="cur9" shpCtx="shpCtx9">
                <ticket name="name25" desc="desc25" price="-5" cur="cur25" shpCtx="shpCtx25">
                    <ticketParam name="name73" value="value73"/>
                    <ticketParam name="name74" value="value74"/>
                    <ticketParam name="name75" value="value75"/>
                </ticket>
                <ticket name="name26" desc="desc26" price="7" cur="cur26" shpCtx="shpCtx26">
                    <ticketParam name="name76" value="value76"/>
                    <ticketParam name="name77" value="value77"/>
                    <ticketParam name="name78" value="value78"/>
                </ticket>
                <ticket name="name27" desc="desc27" price="-2147483641" cur="cur27" shpCtx="shpCtx27">
                    <ticketParam name="name79" value="value79"/>
                    <ticketParam name="name80" value="value80"/>
                    <ticketParam name="name81" value="value81"/>
                </ticket>
            </fareItem>
        </fareSetItem>
    </TariffResult>
</Trip>
```

## JourneyDetail

<p>Journeydetail används för att få detaljerad information kring en resa/delresa (<em>Leg</em>)</p>
<p>Detta bygger på att man först anropat trip. (Se 2.4)</p>
<p>I svaret från trip får man en referens, t.ex.</p>

```xml

<JourneyDetailRef ref="1|3598|0|74|13062017">
```

Denna referens använder man när man ska anropa Journeydetail för den specifika resan. Hela linjesträckningen
för angiven resa returneras, önskar man bara information om hållplatser i den del av resa som en sökning
med trip ger rekomenderas att sätta passlist=1 i trip. Detta är en utökning från api-version 2.

### Parametrar

| Namn | Beskrivning                   | Kommentar                                                                                                                 |
|------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| id   | Referensen från Trip, se ovan | It may be necessary to escape the \| character by its URL encoding %7C.                                                   |
| date | åååå-MM-DD                    | Valfritt<br>Ger motsvarande resa annan dag, om möjligt                                                                    |
| poly | 0 eller 1                     | Valfritt.<br>Anger om detaljerade färdvägar ska beräknas för resultaten. För beskrivning av polyline se 2.4.5. Default 0. |

Exempel:

```text
https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/journeydetail.&lt;FORMAT&gt;?key=&lt;DIN API NYCKEL&gt;&amp;id=1|3598|0|74|13062017
```

# Realtid

If there is real-time information, it is indicated in separate extra fields. For real-time times in JourneyDetail, "rtArrTime," "rtArrDate," "rtDepTime," and "
rtDepDate" are added to the response. The old fields "arrTime," "arrDate," "depTime," and "depDate" are retained to track changes.

# Svarsstruktur

In the table below, the XML structure is described. Some obvious attributes are not included to keep it concise, such as Lat and Lon for a clearer overview of
less obvious elements.

**Example explanation of the structure in the table:**

- element1/element2 => element2 is a sub-element to element1.
- element1.attribut1 => attribut1 is an attribute of element1.

| Namn                     | Datatyp   | Beskrivning                                                                                                                     |
|--------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------|
| JourneyDetail            | Element   | Rootelement.                                                                                                                    |
| JourneyDetail/Notes      | Element   | Contains notes to be displayed for the journey.                                                                                 |
| JourneyDetail/Stops      | List      | List of stops for this journey.                                                                                                 |
| Stops/Stop               | Element   | Stop contains the name of the stop, route index, latitude, longitude, departure date and time, arrival date and time.           |
| Stop.id                  | Attribute | Id for the specified location in the list of stops. Can be used for further travel from that point.                             |
| Stop.routeIdx            | Attribute | Used in conjunction with routeIdx in the Trip response in a search, to know which part of the list is relevant for the journey. |
| JourneyDetail/Directions | List      | List of directions.                                                                                                             |
| Directions/Direction     | Element   | Direction information.                                                                                                          |
| JourneyDetail/Types      | List      | List of travel types.                                                                                                           |
| JourneyDetail/Names      | List      | List of elements.                                                                                                               |
| Names/Name               | Element   | Contains the name of the journey.                                                                                               |
| JourneyDetail/Messages   | List      | Contains a list of real-time messages to be displayed.                                                                          |
| Polyline                 | Element   | Detailed route if poly=1 is specified.                                                                                          |

## GisRoute

Tjänsten används för att få detaljerad information om färdväg. Eftersom Trip inte returnerar polyline för gångväg och cykel så används detta framför allt för
att rita ut cykel och gångväg på karta. I svaret från trip fås en delresa:

```xml

<Leg type="WALK" idx="1" dist="464" duration="PT6M" name="">
    <Origin id="A=1@O=Stockholm City@X=18059500@Y=59331143@U=74@L=400105313@" extId="400105313" name="Stockholm City"
            type="ST" lon="18.0595" lat="59.331143" hasMainMast="true"
            mainMastId="A=1@O=Centralen (Stockholm)@X=18057657@Y=59331134@U=74@L=300101002@" mainMastExtId="300101002"
            date="2019-02-12" time="08:45:00"/>
    <Destination id="A=2@O=Stockholm, Drottninggatan 22@l=@X=18065001@Y=59330415@u=0@"
                 name="Stockholm, Drottninggatan 22" type="ADR" lon="18.065001" lat="59.330415" date="2019-02-12"
                 time="08:51:00"/>
    <GisRef ref="G|1|G@F|A=1@O=Stockholm City@X=18059500@Y=59331143@U=74@L=400105313@|A=2@O=Stockholm, Drottninggatan 22@l=@X=18065001@Y=59330415@u=0@|12022019|84500|85100|ft|ft@0@1000@120@-1@100@1@1000@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$§bt@0@2000@120@-1@100@1@1000@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$§tt@0@5000@120@-1@100@1@2500@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$§|"/>
</Leg>
```

Värdet i ref i objektet GisRef är det som används som input till gisroute

### Parametrar

| Namn | Beskrivning                     | Description                                                                      |
|------|---------------------------------|----------------------------------------------------------------------------------|
| ctx  |                                 | Värdet i ctxRecon som fås i svaret från trip.                                    |
| lang | sv = svenska<br />en = engelska |                                                                                  |
| poly | 0 eller 1                       | Valfritt. Anger om detaljerade färdvägar ska beräknas för resultaten. Default 0. |

Exempel:

```text
http://https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/gisroute.&lt;FORMAT&gt;?key=&lt;DIN APINYCKEL&gt;&amp;ctx=G|1|G@F|A=1@O=Stockholm%20City@X=18059500@Y=59331143@U=74@L=400105313@|A=2@O=Stockholm,%20Drottninggatan%2022@l=@X=18065001@Y=59330415@u=0@|12022019|84500|85100|ft|ft@0@1000@120@-1@100@1@1000@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$%C2%A7bt@0@2000@120@-1@100@1@1000@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$%C2%A7tt@0@5000@120@-1@100@1@2500@0@@@@@false@0@-1@$f@$f@$f@$f@$f@$%C2%A7%7C&amp;lang=sv&amp;poly=1
```

### Svarsstruktur

Svaret från gisroute är detsamma som för resultatet från trip, med skillnad att det bara är en resa med i resultatet. Det tillkommer även ett objekt för att
beskriva färdvägen, GisRoute:

```xml

<GisRoute dist="189" durS="PT2M">
    <seg dist="22" man="ST" manTx="Fortsätt på Renstiernas gata" name="Renstiernas gata" ori="N" polyE="10" polyS="7"
         rType="CT"/>
    <seg man="TO" manTx="Ankomst på Renstiernas gata"/>
    <polyline type="WGS84" dim="3" crdEncS="NNNNNHMNNNN" crdEncZ="???????????" delta="true">
        <crd>18.080803</crd>
        <crd>59.315164</crd>
        <crd>0.0</crd>
        <crd>3.45E-4</crd>
        <crd>4.1E-5</crd>
        <crd>0.0</crd>
        <crd>-2.7E-5</crd>
        <crd>6.1E-5</crd>
        <crd>0.0</crd>
        <crd>9.0E-5</crd>
        <crd>1.1E-5</crd>
        <crd>0.0</crd>
        <crd>2.5E-5</crd>
        <crd>2.7E-5</crd>
        <crd>0.0</crd>
        <crd>9.9E-5</crd>
        <crd>4.0E-6</crd>
        <crd>0.0</crd>
        <crd>1.7E-4</crd>
        <crd>1.5E-5</crd>
        <crd>0.0</crd>
        <crd>0.001985</crd>
        <crd>2.48E-4</crd>
        <crd>0.0</crd>
        <crd>8.8E-5</crd>
        <crd>1.1E-5</crd>
        <crd>0.0</crd>
        <crd>4.0E-5</crd>
        <crd>3.5E-5</crd>
        <crd>0.0</crd>
        <crd>-4.9E-5</crd>
        <crd>1.05E-4</crd>
        <crd>0.0</crd>
    </polyline>
</GisRoute>
```

Segmenten beskriver delar ur resan och polyline beskriver koordinater på samma sätt som dokumenteras i Trip.

## Reconstruction

För att återskapa en resa framsökt via tjänsten trip kan tjänsten reconstruction användas (exempelvis för delningsfunktion eller liknande)

I svaret från trip fås:

```xml

<Trip idx="0" ctxRecon="T$A=1@O=T-Centralen@L=400101052@a=128@$A=1@O=Slussen@L=400101012@a=128@$201706140859$201706140902$ $" checksum="774B67E9_4" tripId="C-0"
      duration="PT3M">
```

Värdet i ctxRecon är det som används som input till reconstruction

### Parametrar

| Namn | Beskrivning         | Description                                                                |
|------|---------------------|----------------------------------------------------------------------------|
| ctx  |                     | Värdet i ctxRecon som fås i svaret från trip.                              |
| poly | 0 eller 1           | Valfritt. Anger om detaljerade färdvägar ska beräknas för resultaten.      |
| date | Datum< (ÅÅÅÅ-MM-DD) | Valfritt. Försöker rekonstruera en resa på specificerat datum, om möjligt. |

Exempel:

```text
https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/reconstruction.<FORMAT>?key=<DIN API NYCKEL>&amp;ctx=T%24A%3D1%40O%3DT-Centralen%40L%3D400101052%40a%3D128%40%24A%3D1%40O%3DSlussen%40L%3D400101012%40a%3D128%40%24201706140859%24201706140902%24%20%24
```

## Svarsstruktur

Svaret från reconstruction är detsamma som för resultatet från trip, med skillnad att det bara är en resa med i resultatet.

## XSD

Returnerar en xsd innehållandes definioner för alla de ingående delarna av svarsstrukturerna för tjänsterna i SL Reseplanerare 3.

### Parametrar

Inga specifika parametrar används för denna tjänst.

Exempel:

```text
https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/xsd.xml?key=<DIN API NYCKEL>.xsd
```

## TTI – Time table info

Time table info service visar för vilken tidsperiod det finns tidtabellsdata tillgängligt i reseplaneraren. Informationen kan t ex användas för att markera
sökbar tidsperiod i en kalender.

### Parametrar

Inga specifika parametrar används för denna tjänst.

Exempel:

```text
https://journeyplanner.integration.sl.se/v1/TravelplannerV3_1/tti?key=<DIN API NYCKEL>
```

### Svarsstruktur

Svaret innehåller information om mellan vilka datum som sökning är giltig, i nedanstående fall är datumintervallet 2016-12-11 till 2018-12-08.

```xml

<TimetableInfoList serverVersion="1.7.6" dialectVersion="1.23" requestId="1507536412387"
                   begin="2016-12-11" end="2018-12-08">
    <TimetableInfo ident="7mtpu" date="2017-10-05" time="10:50:08"/>
    <TimetableInfo ident="65wha" date="2017-09-26" time="07:30:36"/>
    <TimetableInfo ident="6jpdq" date="2017-09-14" time="07:50:04"/>
    <TimetableInfo ident="2x6uq" date="2017-07-06" time="09:19:28"/>
</TimetableInfoList>
```

## Felmeddelanden

| Statuskod | Meddelande                                                                      |
|-----------|---------------------------------------------------------------------------------|
| 1001      | Nyckel har ej skickats med.                                                     |
| 1002      | Nyckel är ogiltig                                                               |
| 1003      | Ogiltigt api                                                                    |
| 1004      | Api tillfälligt inte tillgängligt                                               |
| 1005      | Nyckel finns, men ej för detta api<br>problem with request: Invalid api for key |
| 1006      | För många anrop per minut, för den profil som används                           |
| 1007      | För många anrop per månad, för den profil som används                           |

## Skillnader jämfört med TravelPlannerV3

Xsd:n är uppdaterad, men förutom nedanstående ändring så påverkas inte de befintliga funktionerna.

**Ändringar:**

- Formatet på koordinater i polyline i Trip-anropet har ändrats. Numera beskrivs de med double-värden och differensvärden anges med exponent.
