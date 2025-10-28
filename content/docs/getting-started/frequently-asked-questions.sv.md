---
title: "Vanliga frågor"
weight: 99
layout: "single"
sidebar: true
aliases:
  - /docs/using-trafiklab/frequently-asked-questions/
---

## Trafiklab

#### Varför behöver jag API-nycklar? Skulle det inte vara enklare utan?

Vi håller med om att det vore enklare, men vi behöver API-nycklarna för att kunna erbjuda den här datan. Varje API-anrop och varje GTFS-hämtning kostar oss pengar. Med hjälp av API-nycklar kan vi förhindra att man laddar ner samma GTFS-fil var 15:e eller 30:e minut, samtidigt som vi är tydliga med att filen bara uppdateras en gång per dag.

Oroa dig inte om du behöver en uppgradering – i de flesta fall beviljas den.

#### Vad händer när ett API avvecklas?

Vi avvecklar sällan API:er. När en förändring är på gång informeras användare i god tid (ofta flera månader i förväg).

## Data

#### Fordon visas i realtidsdata trots att de inte finns i den statiska datan. Varför?

Det kan vara hög belastning på en viss busslinje, varpå operatören kan välja att sätta in en eller flera extrabussar. Dessa bussar är inte kopplade till en planerad tur, men visas ändå i realtidsdatan.

Fordonspositionsdata kan också omfatta parkerade fordon, fordon på väg till sin startpunkt eller på väg tillbaka efter sitt sista stopp.

#### Får jag stresstesta API:erna?

Nej. Om du undrar om våra API:er klarar en viss belastning, kontakta oss i stället.

#### Varför ökar inte användningsstatistiken när jag gör anrop med min API-nyckel?

Statistiken uppdateras bara en gång per dag. För vissa API:er kan det ta upp till 48 timmar innan statistiken blir synlig för Trafiklabs användare.

#### Varför nekades min begäran om uppgradering av API-nyckeln?

Du får ett meddelande som beskriver orsaken när en uppgradering av en API-nyckel nekas. Vanligtvis beror det på magic-mirror-lösningar som vill använda mer än 10 000 API-anrop per månad, eller på att fel datatyp används, varpå vi pekar på hur annan data kan underlätta (till exempel när man använder ett API för analys/massfrågor i stället för våra GTFS/GTFS-RT-data).

## Jag har fortfarande frågor

Tveka inte att höra av dig! Du kan göra det genom att posta i vårt supportforum: [https://support.trafiklab.se](https://support.trafiklab.se)
