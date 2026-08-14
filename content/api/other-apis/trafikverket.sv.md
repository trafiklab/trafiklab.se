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
## Vad är Trafikverkets öppna API?

Trafikverkets öppna API är ett API för att hämta information om väg- och tågtrafik.

## Hur använder jag Trafikverkets öppna API?

En giltig API-nyckel krävs. Nya användare måste hämta en nyckel från [Trafikverkets eget dataportal](https://data.trafikverket.se/oauth2/Account/register). Trafiklab utfärdar inte längre nya nycklar för detta API, men befintliga nycklar som utfärdats via Trafiklab fortsätter att fungera.

API:et har flera versioner som alla använder samma API-nyckel. Använd den senaste tillgängliga endpointen, men befintliga applikationer kan fortsätta använda tidigare versioner.

{{% tabs %}} {{% tab "Json" %}}

```text
https://api.trafikinfo.trafikverket.se/v2/data.json
```

{{% /tab %}}

{{% tab "Xml" %}}

```text
https://api.trafikinfo.trafikverket.se/v2/data.xml
```

{{% /tab %}} {{% /tabs %}}

Trafikverkets öppna API används genom att skicka en POST-förfrågan som innehåller en XML-förfrågan. Förfrågan beskriver vilken data som ska hämtas och kan även innehålla filter. API-nyckeln skickas i `LOGIN`-elementet som attributet `authenticationkey`. Lägg inte in en riktig API-nyckel i källkod och dela den inte offentligt.

Samma innehåll i förfrågan kan skickas till någon av endpointsen ovan. Suffixet `.json` eller `.xml` avgör om svaret returneras som JSON eller XML. Spara till exempel XML-förfrågan nedan som `request.xml` och kör:

```bash
curl --request POST \
  --url https://api.trafikinfo.trafikverket.se/v2/data.json \
  --header 'Content-Type: application/xml' \
  --data-binary @request.xml
```

I `QUERY`-elementet väljer `objecttype` datatyp, `schemaversion` versionen av datatypen och `limit` begränsar antalet returnerade poster. `FILTER`-elementet är valfritt. Filtret `EQ` i exemplet begränsar resultatet till poster där `SomeDataField` är lika med `2`. Tillgängliga fält, schemaversioner, filteroperatorer och svarsstruktur dokumenteras för varje datatyp i Trafikverkets dokumentation.

En förfrågan kan se ut så här:

```xml
<REQUEST>
  <LOGIN authenticationkey="YourApiKey" />
  <QUERY objecttype="SomeObjectType" schemaversion="SomeObjectVersion" limit="10">
  <FILTER>
    <EQ name="SomeDataField" value="2" />
  </FILTER>
  </QUERY>
</REQUEST>
```

{{% info %}}
Om ett efterfrågat fält saknar värde inkluderas fältet inte i svaret.
{{% /info %}}

Följande datatyper finns tillgängliga:

| Data type | Beskrivning |
|-----------|-------------|
| TrainMessage | Meddelanden om arbeten på järnvägen, tekniska problem och liknande. |
| TrainStation | Trafikplatser, inte bara för passagerare utan även för gods och gränser. |
| TrainAnnouncement | Tidtabellsinformation, det vill säga information om tåg vid trafikplatser eller stationer. Innehåller inte godståg. |
| Icon | Ikoner för användning på kartor eller i användargränssnitt. |
| RoadCondition | Väglag. |
| RoadConditionOverview | Översikt över väglag. |
| Situation | Beskriver aktuella situationer på vägarna, till exempel incidenter och störningar i den normala trafiken. Det kan handla om viktig information, vägarbeten, olyckor, köer, evenemang eller ändrade färjetider. |
| WeatherStation | Rapporter från väderstationer längs vägarna. |

### Koordinater

API:et använder det svenska nationella koordinatsystemet SWEREF 99 TM. All geometrisk data publiceras även i WGS 84. [Läs mer om konvertering från SWEREF 99](/docs/using-trafiklab-data/combining-data/converting-sweref99-to-wgs84/).

## Detaljerad dokumentation

Fullständig och uppdaterad dokumentation finns i Trafikverkets [Data Exchange Portal](https://data.trafikverket.se/documentation/datacache/intro). Portalen är Trafikverkets centrala webbplats för dokumentation om datautbytestjänster och innehåller bland annat:

- mer information om hur förfrågningar konstrueras
- mer information om svarsstrukturer
- felmeddelanden
- exempelkod
- en interaktiv konsol för testning

Om du redan har en API-nyckel som utfärdats via Trafiklab kan du fortsätta använda den. Nya nycklar måste hämtas från Trafikverkets eget dataportal.

Trafikverkets dokumentation finns här: [https://data.trafikverket.se/documentation/datacache/intro](https://data.trafikverket.se/documentation/datacache/intro)
