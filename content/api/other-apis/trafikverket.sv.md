---
title: Trafikverket Öppet API 
layout: "single"
weight: 90 
summary: Aktuell trafikinformation från Trafikverket om både tåg- och vägtrafik.
date: 06-02-2014
image: '/media/2024/09/banner_inlandsbanan.jpg'
image_position: 'bottom'
aliases:
  - /sv/api/trafiklab-apis/trafikverket/
---
Strukturen skiljer sig en hel del från andra APIer på Trafiklab. Hämtning av data görs med ett HTTP-anrop. En fråga
skickas med i POST-metoden som beskriver vilket data som efterfrågas samt innehållandes eventuella filter.

## Dataformat

XML eller JSON, anges via suffix.

Om något värde saknas i svaret returneras inte detta element i svaret.

## API Nyckel

En API nyckel krävs. En API nyckel kan skapas kostnadsfritt i [Trafikverkets eget dataportal](https://data.trafikverket.se/oauth2/Account/register).
Mer information hittas i [vår snabbstartsguide](https://www.trafiklab.se/docs/getting-started/using-trafiklab/).

## Metoder

Hämtning av data görs med ett HTTP-anrop. En fråga skickas med i POST-metoden som beskriver vilket data som efterfrågas
samt innehållandes eventuella filter. Frågan måste även inkludera en giltig API-nyckel.

Tillgängliga datatyper är:

- **TrainMessage** - Tågtrafikmeddelande, exempelvis information kring banarbete, tågfel, anläggningsfel och dylikt.
- **TrainStation** - Trafikplatser, både med och utan resandeutbyte.
- **TrainAnnouncement** - Tidtabellsinformation, d.v.s information om tåg på trafikplatser (stationer, hållplatser)
  varje post motsvarar ett visst tåg vid respektive trafikplats.Innehåller inte godståg.
- **Icon** - Ikoner, exempelvis för användning i grafiska användargränssnitt och kartor.
- **RoadCondition** – Väglag
- **RoadConditionOverview** – Väglagsöversikter
- **Situation** - Situationer innehållandes händelser och störningar, exempelvis: Viktig information, Olyckor,
  Bärighetsnedsättning, Evenemang, Avvikande färjetider, Kolonnkörning, Kövarning, Oförutsedda hinder, Vägarbete.
- **WeatherStation** - Väderstationer med mätdata

## Koordinatsystem

Trafikverket använder sig av det svenska nationella
koordinatsystemet [SWEREF 99 TM](/docs/using-trafiklab-data/combining-data/converting-sweref99-to-wgs84/). All
geometridata publiceras dock även i koordinatsystemet WGS 84.<em></em>

## Detaljerad dokumentation

Detaljerad dokumentation hittar du på Trafikverkets informationssida för API:et, se nedan.

Den detaljerade dokumentationen innehåller bland annat information om:

- uppbyggnad av frågan som bifogas anropet
- svarets utformning
- felmeddelanden
- tillgänglig datamodell
- exempelkod och vanliga användningsfall
- en API-konsol för testkörning

Observera att du som är Trafiklabs-medlem **inte** behöver registrera dig på Trafikverkets sida utan kan hämta en nyckel
direkt här på Trafiklab.

För mer information se ”[Trafikverkets öppna API för trafikinformation](http://api.trafikinfo.trafikverket.se/)”


