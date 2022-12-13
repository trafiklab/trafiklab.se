---
title: SL Stops and lines v2.0 (Hållplatser och linjer 2)
weight: "400"
date: 2015-03-02
aliases:
- "/api/sl-hallplatser-och-linjer-2"
- "/api/sl-hallplatser-och-linjer-2/documentation"
- "/api/sl-hallplatser-och-linjer-2/nivaer"
- "/api/sl-hallplatser-och-linjer-2/console"
- "/node/13609"
- "/node/13609/documentation"
- "/node/13609/nivaer"
- "/node/13609/console"

---
Listning av hållplatser och linjer i Stockholms län.

{{% info %}}SL will replace this API with a new, similar API in the near future. The documentation for the current API
has therefore not been translated for the new Trafiklab website.{{% /info %}}

<p>För att kunna beskriva trafikinformation på ett konsekvent sätt, är det nödvändigt att ingående begrepp och definitioner är klara och tydliga. De viktigaste begreppen för denna tjänst presenteras nedan.</p>

<table>
<tbody>
<tr>
<td>
<p><strong>Begrepp</strong></p>
</td>
<td>
<p><strong>Beskrivning</strong></p>
</td>
</tr>
<tr>
<td>
<p>Site</p>
</td>
<td>
<p>Site är en gruppering av StopAreas som används för att förenkla sökningen i reseplaneraren.</p>
</td>
</tr>
<tr>
<td>
<p>StopArea</p>
</td>
<td>
<p>StopArea är en gruppering av StopPoints med samma trafikslag och namn inom ett avgränsat geografiskt område, exempelvis en terminal.</p>
</td>
</tr>
<tr>
<td>
<p>StopPoint</p>
</td>
<td>
<p>En StopPoint är ett stoppställe och ingår i en StopArea</p>
</td>
</tr>
<tr>
<td>
<p>Line</p>
</td>
<td>
<p>Linje annonserad mot resenär</p>
</td>
</tr>
<tr>
<td>
<p>JourneyPattern</p>
</td>
<td>
<p>En unik körväg för en linje</p>
</td>
</tr>
<tr>
<td>
<p>JourneyPatternPointOnLine</p>
</td>
<td>
<p>Innehåller samtliga stoppställen som trafikeras av en viss linje</p>
</td>
</tr>
<tr>
<td>
<p>Transportmode</p>
</td>
<td>
<p>Trafikslag</p>
</td>
</tr>
</tbody>
</table>
<p>API</p>
<h2>Åtkomst</h2>
<p>URL:er för anrop finns specificerade nedan:</p>
<p>Produktionsmiljö</p>

`https://api.sl.se/api2/LineData.xml?model=[model]&key=[key]`

`https://api.sl.se/api2/LineData.json?model=[model]&key=[key]`

<p>Observera att det är extension i anropet som avgör formateringen av svaret.</p>
<h2>API-nycklar, behörighet</h2>
<p>API-nycklar kan införskaffas via Trafiklabs utvecklareportal</p>
<p>En API-nyckel ska användas i URL:en för ett API anrop.</p>

`https://api.sl.se/api2/LineData.xml?model=[model]&key=[key]`

<h3>Nyckelnivåer</h3>
<table>
<tbody>
<tr>
<td>
<p><strong>Nivå</strong></p>
</td>
<td>
<p><strong>Max anrop/minut</strong></p>
</td>
<td>
<p><strong>Max anrop/månad</strong></p>
</td>
</tr>
<tr>
<td>
<p>Brons</p>
</td>
<td>
<p>5</p>
</td>
<td>
<p>500</p>
</td>
</tr>
</tbody>
</table>

<h2>Format</h2>
<p>API:et har support för XML och JSON dataformatering.</p>
<p>Önskad formatering anges i URL:en för ett API anrop.</p>

`api.sl.se/api2/LineData.xml?model=[model]&key=[key]`

<h2>Datatyper</h2>
<p>Alla datatyper representeras alltid i strängform för respektive format.</p>
<p>Typen angiven vid beskrivningar av modeller anger endast en lämplig datatyp att konvertera värdet till i ett givet programmeringsspråk.</p>
<table>
<tbody>
<tr>
<td>
<p><strong>Typ</strong></p>
</td>
<td>
<p><strong>Exempel</strong></p>
</td>
<td>
<p><strong>Beskrivning</strong></p>
</td>
</tr>
<tr>
<td>
<p>Int</p>
</td>
<td>
<p>123</p>
</td>
<td>
<p>Alla datatyper representeras alltid i strängform. Kan dock konverteras till datatypen Int om programmeringsspråket har stöd till det</p>
</td>
</tr>
</tbody>
</table>
<h2>Filtrering av data</h2>
<p>För modellerna line och jour är det önskvärt att kunna särskilja vilken trafiktyp datat avser. Detta kan åstadkommas genom att skicka med den valfria parametern DefaultTransportModeCode som kan innehålla någon av de Transportmode-värdena som returneras vid anrop till modellen transportmode, ex ”BUS” eller ”METRO”</p>
<p>Ex:</p>
`https://api.sl.se/api2/linedata.xml?key=[nyckel]&model=line&DefaultTransportModeCode=METRO`
`https://api.sl.se/api2/linedata.xml?key=[nyckel]&model=jour&DefaultTransportModeCode=BUS`
<h2>Teckenkodning</h2>
<p>UTF-8 används för både XML och Json.</p>
<h2>Prestanda</h2>
<p>Eftersom anrop returnerar relativ stor datamängd är det starkt rekommenderat att anropet innehåller följande HEADER parameter för att möjliggöra GZIP komprimering i svaret.</p>
<table>
<tbody>
<tr>
<td>
<p><strong>Nyckel</strong></p>
</td>
<td>
<p><strong>Värde</strong></p>
</td>
</tr>
<tr>
<td>
<p>Accept-Encoding</p>
</td>
<td>
<p><strong>gzip, deflate</strong></p>
</td>
</tr>
</tbody>
</table>
<h2>Uppdateringsfrekvens</h2>
<p>API portalen uppdaterar data en gång per dygn mellan klockan 0.00-2.00 varje dag.</p>
<h2>API modell</h2>
<p>Anrop till <a href="https://api.sl.se/api2/LineData">https://api.sl.se/api2/LineData</a> returnerar alltid en API modell (basmodell) tillbaka, oavsett vilken specifik datamodell man har begärt i anropet.</p>
<table>
<tbody>
<tr>
<td>
<p><strong>Nyckel</strong></p>
</td>
<td>
<p><strong>Typ</strong></p>
</td>
<td>
<p><strong>Exempel</strong></p>
</td>
<td>
<p><strong>Beskrivning</strong></p>
</td>
</tr>
<tr>
<td>
<p>StatusCode</p>
</td>
<td>
<p>Int</p>
</td>
<td>
<p>0</p>
</td>
<td>
<p>0 om anropet har gått bra, annars en felkod som inte kan åtgärdas via tex ett modifierat anrop</p>
</td>
</tr>
<tr>
<td>
<p>ExecutionTime</p>
</td>
<td>
<p>Int</p>
</td>
<td>
<p>267</p>
</td>
<td>
<p>Antal millisekunder som det har tagit att genererar ett svar på servern</p>
</td>
</tr>
<tr>
<td>
<p>ResponseData</p>
</td>
<td>
<p>Objekt</p>
</td>
<td>
</td>
<td>
<p>Container-objekt som innehåller attribut och data</p>
</td>
</tr>
<tr>
<td>
<p>Version</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>2014-06-27 14:03:39.103</p>
</td>
<td>
<p>Senast ändrad. Uppdateras normalt sett bara en gång per dygn</p>
</td>
</tr>
<tr>
<td>
<p>Type</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>DataModelType</p>
</td>
<td>
<p>Anger typen av datamodellen som svaret innehåller:</p>
<p>Site, StopPoint, Line, JourneyPatternPointOfLine, TransportMode</p>
</td>
</tr>
<tr>
<td>
<p>ResponseData</p>
</td>
<td>
<p>Objekt</p>
</td>
<td>
</td>
<td>
<p>Container-objekt som innehåller typad data</p>
</td>
</tr>
</tbody>
</table>
<h3>API modell för XML</h3>
<p><ResponseOfPwsResult xmlns:xsd=<strong>"https://www.w3.org/2001/XMLSchema"</strong> xmlns:xsi=<strong>"https://www.w3.org/2001/XMLSchema-instance"</strong>> <StatusCode><strong>0</strong></StatusCode> <ExecutionTime><strong>267</strong></ExecutionTime> <ResponseData> <Version xmlns=<strong>"https://api.sl.se/api/pws"</strong>><strong>2014-10-09 01:05</strong></Version> <Type xmlns=<strong>"https://api.sl.se/api/pws"</strong>><strong>DataModelType</strong></Type> <strong><!--DataModel></DataModel></strong> <strong>...</strong> <strong> <DataModel></DataModel--></strong> </ResponseData> </ResponseOfPwsResult></p>
<h3>API modell för JSON</h3>
<p><strong>{</strong> "StatusCode"<strong>:</strong> <strong>0,</strong> "Execut ionTime"<strong>:</strong> <strong>282,</strong> "ResponseData"<strong>:</strong> <strong>{</strong> "Version"<strong>:</strong> <strong>"2014-10-09 01:05"</strong><strong>,</strong> "Type"<strong>:</strong> <strong>"DataModelType"</strong><strong>,</strong> "Result"<strong>:</strong> <strong>\[</strong> <strong>/* DataModel, ..., DataModel */ </strong><strong>\]</strong> <strong>}</strong> <strong>}</strong></p>
<p>Specifikation för datamodeller</p>
<p>API:et tillhandahåller följande datamodeller</p>
<table>
<tbody>
<tr>
<td>
<p><strong>Nyckel</strong></p>
</td>
<td>
<p><strong>Värde</strong></p>
</td>
<td>
<p><strong>Beskrivning</strong></p>
</td>
</tr>
<tr>
<td>
<p>model</p>
</td>
<td>
<p><strong>site</strong></p>
</td>
<td>
<p>Returnerar svar med Site objekt</p>
</td>
</tr>
<tr>
<td>
<p>model</p>
</td>
<td>
<p><strong>stop</strong></p>
</td>
<td>
<p>Returnerar svar med StopPoint objekt</p>
</td>
</tr>
<tr>
<td>
<p>model</p>
</td>
<td>
<p><strong>line</strong></p>
</td>
<td>
<p>Returnerar svar med Line objekt</p>
</td>
</tr>
<tr>
<td>
<p>model</p>
</td>
<td>
<p><strong>jour</strong></p>
</td>
<td>
<p>Returnerar svar med JourneyPatternPointOnLine objekt</p>
</td>
</tr>
<tr>
<td>
<p>model</p>
</td>
<td>
<p><strong>tran</strong></p>
</td>
<td>
<p>Returnerar svar med TransportMode objekt</p>
</td>
</tr>
</tbody>
</table>
<p>Önskad datamodell anges i URL:en för ett API anrop.</p>
<p>api.sl.se/api2/LineData.xml?model=\[model\]&key=\[key\]</p>
<h2>Exempel</h2>
<p>https://api.sl.se/api2/LineData.xml?model=site</p>
<h2>Site</h2>
<h3>Beskrivning</h3>
<p>Site är en gruppering av StopAreas som används för att förenkla sökningen i reseplaneraren.</p>
<h3>Egenskaper</h3>
<table>
<tbody>
<tr>
<td>
<p><strong>Egenskap</strong></p>
</td>
<td>
<p><strong>Kan konverteras till</strong></p>
</td>
<td>
<p><strong>Exempel</strong></p>
</td>
<td>
<p><strong>Beskrivning</strong></p>
</td>
</tr>
<tr>
<td>
<p>SiteId</p>
</td>
<td>
<p>Int</p>
</td>
<td>
<p>1002</p>
</td>
<td>
<p>Unikt identifikationsnummer för en Site</p>
</td>
</tr>
<tr>
<td>
<p>SiteName</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>Centralen</p>
</td>
<td>
<p>Benämning på området</p>
</td>
</tr>
<tr>
<td>
<p>StopAreaNumber</p>
</td>
<td>
<p>Int</p>
</td>
<td>
<p>1051</p>
</td>
<td>
<p>Unikt identifikationsnummer för hållplats</p>
</td>
</tr>
<tr>
<td>
<p>LastModifiedUtcDateTime</p>
</td>
<td>
<p>DateTime</p>
</td>
<td>
<p>2014-06-27 14:03:39.103</p>
</td>
<td>
<p>Senast ändrad</p>
</td>
</tr>
<tr>
<td>
<p>ExistsFromDate</p>
</td>
<td>
<p>DateTime</p>
</td>
<td>
<p>2014-06-28 00:00:00.000</p>
</td>
<td>
<p>Gäller fr.o.m. datum</p>
</td>
</tr>
</tbody>
</table>
<h3>XML objektstruktur</h3>
<p><Site xmlns=<strong>"https://api.sl.se/api/pws"</strong>> <SiteId><strong>1002</strong></SiteId> <SiteName><strong>Centralen</strong></SiteName> <StopAreaNumber><strong>1051</strong></StopAreaNumber> <LastModifiedUtcDateTime><strong>2014-06-27 14:03:39.103</strong></LastModifiedUtcDateTime> <ExistsFromDate><strong>2014-06-28 00:00:00.000</strong></ExistsFromDate> </Site></p>
<h3>JSON objektstruktur</h3>
<p><strong>{</strong> "SiteId"<strong>:</strong> <strong>"1002"</strong><strong>,</strong> "SiteName"<strong>:</strong> <strong>"Centralen"</strong><strong>,</strong> "StopAreaNumber"<strong>:</strong> <strong>"1051"</strong><strong>,</strong> "LastModifiedUtcDateTime"<strong>:</strong> <strong>"2014-06-27 14:03:39.103"</strong><strong>,</strong> "ExistsFromDate"<strong>:</strong> <strong>"2014-06-28 00:00:00.000"</strong> <strong>}</strong></p>
<h2>StopPoint</h2>
<h3>Beskrivning</h3>
<p>StopPoints (Stoppställen) ingår i en StopArea.</p>
<h3>Egenskaper</h3>
<table>
<tbody>
<tr>
<td>
<p><strong>Egenskap</strong></p>
</td>
<td>
<p><strong>Kan konverteras till</strong></p>
</td>
<td>
<p><strong>Exempel</strong></p>
</td>
<td>
<p><strong>Beskrivning</strong></p>
</td>
</tr>
<tr>
<td>
<p>StopPointNumber</p>
</td>
<td>
<p>Int</p>
</td>
<td>
<p>1051</p>
</td>
<td>
<p>Unikt identifikationsnummer för stoppställe</p>
</td>
</tr>
<tr>
<td>
<p>StopPointName</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>T-Centralen</p>
</td>
<td>
<p>Namn på stoppställe</p>
</td>
</tr>
<tr>
<td>
<p>StopAreaNumber</p>
</td>
<td>
<p>Int</p>
</td>
<td>
<p>1051</p>
</td>
<td>
<p>Number för StopArea</p>
<p>Ett stoppställe ingår endast i en StopArea</p>
</td>
</tr>
<tr>
<td>
<p>LocationNorthingCoordinate</p>
</td>
<td>
<p>Double</p>
</td>
<td>
<p>59.3313179695028</p>
</td>
<td>
<p>Koordinat i WGS84-format</p>
</td>
</tr>
<tr>
<td>
<p>LocationEastingCoordinate</p>
</td>
<td>
<p>Double</p>
</td>
<td>
<p>18.0616773959365</p>
</td>
<td>
<p>Koordinat i WGS84-format</p>
</td>
</tr>
<tr>
<td>
<p>ZoneShortName</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>A</p>
</td>
<td>
<p>Taxezon. A, B eller C</p>
<p>Om SLs taxa inte gäller är taxezon null</p>
</td>
</tr>
<tr>
<td>
<p>StopAreaTypeCode</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>METROSTN</p>
</td>
<td>
<p>Användning av hållplatsen. BUSSTERM, TRAMSTN,METROSTN, RAILWSTN, SHIPBER eller FERRYBER</p>
</td>
</tr>
<tr>
<td>
<p>LastModifiedUtcDateTime</p>
</td>
<td>
<p>DateTime</p>
</td>
<td>
<p>2014-06-03 00:00:00.000</p>
</td>
<td>
<p>Senast ändrad</p>
</td>
</tr>
<tr>
<td>
<p>ExistsFromDate</p>
</td>
<td>
<p>DateTime</p>
</td>
<td>
<p>2014-06-03 00:00:00.000</p>
</td>
<td>
<p>Gäller fr.o.m. datum</p>
</td>
</tr>
</tbody>
</table>
<h3>XML objektstruktur</h3>
<p><StopPoint xmlns=<strong>"https://api.sl.se/api/pws"</strong>> <StopPointNumber><strong>1051</strong></StopPointNumber> <StopPointName><strong>T-Centralen</strong></StopPointName> <StopAreaNumber><strong>1051</strong></StopAreaNumber> <LocationNorthingCoordinate><strong>59.3313179695028</strong></LocationNorthingCoordinate> <LocationEastingCoordinate><strong>18.0616773959365</strong></LocationEastingCoordinate> <ZoneShortName><strong>A</strong></ZoneShortName> <StopAreaTypeCode><strong>METROSTN</strong></StopAreaTypeCode> <LastModifiedUtcDateTime><strong>2014-06-03 00:00:00.000</strong></LastModifiedUtcDateTime> <ExistsFromDate><strong>2014-06-03 00:00:00.000</strong></ExistsFromDate> </StopPoint></p>
<p>JSON objektstruktur</p>
<p><strong>{</strong> "StopPointNumber"<strong>:</strong> <strong>"1051"</strong><strong>,</strong> "StopPointName"<strong>:</strong> <strong>"T-Centralen"</strong><strong>,</strong> "StopAreaNumber"<strong>:</strong> <strong>"1051"</strong><strong>,</strong> "LocationNorthingCoordinate"<strong>:</strong> <strong>"59.3313179695028"</strong><strong>,</strong> "LocationEastingCoordinate"<strong>:</strong> <strong>"18.0616773959365"</strong><strong>,</strong> "ZoneShortName"<strong>:</strong> <strong>"A"</strong><strong>,</strong> "StopAreaTypeCode"<strong>:</strong> <strong>"METROSTN"</strong><strong>,</strong> "LastModifiedUtcDateTime"<strong>:</strong> <strong>"2014-06-03 00:00:00.000"</strong><strong>,</strong> "ExistsFromDate"<strong>:</strong> <strong>"2014-06-03 00:00:00.000"</strong> <strong>}</strong></p>
<h2>Line</h2>
<h3>Beskrivning</h3>
<p>Returnerar beskrivning av en linje. Innehåller referenser till trafikslag.</p>
<h3>Egenskaper</h3>
<table>
<tbody>
<tr>
<td>
<p><strong>Egenskap</strong></p>
</td>
<td>
<p><strong>Kan konverteras till</strong></p>
</td>
<td>
<p><strong>Exempel</strong></p>
</td>
<td>
<p><strong>Beskrivning</strong></p>
</td>
</tr>
<tr>
<td>
<p>LineNumber</p>
</td>
<td>
<p>Int</p>
</td>
<td>
<p>3</p>
</td>
<td>
<p>Unikt identifikationsnummer för linje</p>
</td>
</tr>
<tr>
<td>
<p>LineDesignation</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>3</p>
</td>
<td>
<p>Linjebeteckning</p>
</td>
</tr>
<tr>
<td>
<p>DefaultTransportMode</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>blåbuss</p>
</td>
<td>
<p>Gruppering av linjer för presentation</p>
</td>
</tr>
<tr>
<td>
<p>DefaultTransportModeCode</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>BUS</p>
</td>
<td>
<p>Trafikslag</p>
</td>
</tr>
<tr>
<td>
<p>LastModifiedUtcDateTime</p>
</td>
<td>
<p>DateTime</p>
</td>
<td>
<p>2007-08-24 00:00:00.000</p>
</td>
<td>
<p>Senast ändrad</p>
</td>
</tr>
<tr>
<td>
<p>ExistsFromDate</p>
</td>
<td>
<p>DateTime</p>
</td>
<td>
<p>2007-08-24 00:00:00.000</p>
</td>
<td>
<p>Gäller fr.o.m. datum</p>
</td>
</tr>
</tbody>
</table>
<h3>XML objektstruktur</h3>
<p><Line xmlns=<strong>"</strong><strong>https://api.sl.se/api/pws</strong><strong>"</strong>> <LineNumber><strong>3</strong></LineNumber> <LineDesignation><strong>3</strong></LineDesignation> <DefaultTransportMode><strong>blåbuss</strong></DefaultTransportMode> <DefaultTransportModeCode><strong>BUS</strong></DefaultTransportModeCode> <LastModifiedUtcDateTime><strong>2007-08-24 00:00:00.000</strong></LastModifiedUtcDateTime> <ExistsFromDate><strong>2007-08-24 00:00:00.000</strong></ExistsFromDate> </Line></p>
<h3>JSON objektstruktur</h3>
<p><strong>{</strong> "LineNumber"<strong>:</strong> <strong>"3"</strong><strong>,</strong> "LineDesignation"<strong>:</strong> <strong>"3"</strong><strong>,</strong> "DefaultTransportMode"<strong>:</strong> <strong>"blåbuss"</strong><strong>,</strong> "DefaultTransportModeCode"<strong>:</strong> <strong>"BUS"</strong><strong>,</strong> "LastModifiedUtcDateTime"<strong>:</strong> <strong>"2007-08-24 00:00:00.000"</strong><strong>,</strong> "ExistsFromDate"<strong>:</strong> <strong>"2007-08-24 00:00:00.000"</strong> <strong>}</strong></p>
<h2>JourneyPatternPointOnLine</h2>
<h3>Beskrivning</h3>
<p>Returnerar kopplingen mellan stoppställe och linje. Innehåller samtliga stoppställen som trafikeras av en viss linje.</p>
<h3>Egenskaper</h3>
<table>
<tbody>
<tr>
<td>
<p><strong>Egenskap</strong></p>
</td>
<td>
<p><strong>Kan konverteras till</strong></p>
</td>
<td>
<p><strong>Exempel</strong></p>
</td>
<td>
<p><strong>Beskrivning</strong></p>
</td>
</tr>
<tr>
<td>
<p>LineNumber</p>
</td>
<td>
<p>Int</p>
</td>
<td>
<p>1</p>
</td>
<td>
<p>Unikt identifikationsnummer för linje</p>
</td>
</tr>
<tr>
<td>
<p>DirectionCode</p>
</td>
<td>
<p>Int</p>
</td>
<td>
<p>1</p>
</td>
<td>
<p>Linjeriktning</p>
</td>
</tr>
<tr>
<td>
<p>JourneyPatternPointNumber</p>
</td>
<td>
<p>Int</p>
</td>
<td>
<p>10008</p>
</td>
<td>
<p>Unikt identifikationsnummer för stoppställe</p>
</td>
</tr>
<tr>
<td>
<p>LastModifiedUtcDateTime</p>
</td>
<td>
<p>DateTime</p>
</td>
<td>
<p>2012-06-23 00:00:00.000</p>
</td>
<td>
<p>Senast ändrad</p>
</td>
</tr>
<tr>
<td>
<p>ExistsFromDate</p>
</td>
<td>
<p>DateTime</p>
</td>
<td>
<p>2012-06-23 00:00:00.000</p>
</td>
<td>
<p>Gäller fr.o.m. datum</p>
</td>
</tr>
</tbody>
</table>
<h3>XML objektstruktur</h3>
<p><JourneyPatternPointOnLine xmlns=<strong>"https://api.sl.se/api/pws"</strong>> <LineNumber><strong>1</strong></LineNumber> <DirectionCode><strong>1</strong></DirectionCode> <JourneyPatternPointNumber><strong>10008</strong></JourneyPatternPointNumber> <LastModifiedUtcDateTime><strong>2012-06-23 00:00:00.000</strong></LastModifiedUtcDateTime> <ExistsFromDate><strong>2012-06-23 00:00:00.000</strong></ExistsFromDate> </JourneyPatternPointOnLine></p>
<h3>JSON objektstruktur</h3>
<p><strong>{</strong> "LineNumber"<strong>:</strong> <strong>"1"</strong><strong>,</strong> "DirectionCode"<strong>:</strong> <strong>"1"</strong><strong>,</strong> "JourneyPatternPointNumber"<strong>:</strong> <strong>"10008"</strong><strong>,</strong> "LastModifiedUtcDateTime"<strong>:</strong> <strong>"2012-06-23 00:00:00.000"</strong><strong>,</strong> "ExistsFromDate"<strong>:</strong> <strong>"2012-06-23 00:00:00.000"</strong> <strong>}</strong></p>
<h2>TransportMode</h2>
<h3>Beskrivning</h3>
<p>Returnerar tillgängliga trafikslag. Linjedatan refererar till trafikslaget via egenskapen DefaultTransportModeCode.</p>
<h3>Samband mellan TransportModeCode och StopAreaCode</h3>
<table>
<tbody>
<tr>
<td>
<p><strong>DefaultTransportModeCode</strong></p>
</td>
<td>
<p><strong>StopAreaTypeCode</strong></p>
</td>
</tr>
<tr>
<td>
<p>BUS</p>
</td>
<td>
<p>BUSTERM</p>
</td>
</tr>
<tr>
<td>
<p>METRO</p>
</td>
<td>
<p>METROSTN</p>
</td>
</tr>
<tr>
<td>
<p>TRAM</p>
</td>
<td>
<p>TRAMSTN</p>
</td>
</tr>
<tr>
<td>
<p>TRAIN</p>
</td>
<td>
<p>RAILWSTN</p>
</td>
</tr>
<tr>
<td>
<p>SHIP</p>
</td>
<td>
<p>SHIPBER</p>
</td>
</tr>
<tr>
<td>
<p>FERRY</p>
</td>
<td>
<p>FERRYBER</p>
</td>
</tr>
</tbody>
</table>
<h3>Objektegenskaper</h3>
<table>
<tbody>
<tr>
<td>
<p><strong>Egenskap</strong></p>
</td>
<td>
<p><strong>Kan konverteras till</strong></p>
</td>
<td>
<p><strong>Exempel</strong></p>
</td>
<td>
<p><strong>Beskrivning</strong></p>
</td>
</tr>
<tr>
<td>
<p>DefaultTransportModeCode</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>BUS</p>
</td>
<td>
<p>Unik kod för trafikslag</p>
</td>
</tr>
<tr>
<td>
<p>DefaultTransportMode</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>buss</p>
</td>
<td>
<p>Benämning på trafikslag</p>
</td>
</tr>
<tr>
<td>
<p>StopAreaTypeCode</p>
</td>
<td>
<p>String</p>
</td>
<td>
<p>BUSTERM</p>
</td>
<td>
<p>Typkod för hållplatsen</p>
</td>
</tr>
<tr>
<td>
<p>LastModifiedUtcDateTime</p>
</td>
<td>
<p>DateTime</p>
</td>
<td>
<p>2007-08-24 00:00:00.000</p>
</td>
<td>
<p>Senast ändrad</p>
</td>
</tr>
<tr>
<td>
<p>ExistsFromDate</p>
</td>
<td>
<p>DateTime</p>
</td>
<td>
<p>2007-08-24 00:00:00.000</p>
</td>
<td>
<p>Gäller fr.o.m. datum</p>
</td>
</tr>
</tbody>
</table>
<h3>XML objektstruktur</h3>
<p><TransportMode xmlns=<strong>"https://api.sl.se/api/pws"</strong>> <DefaultTransportModeCode><strong>BUS</strong></DefaultTransportModeCode> <DefaultTransportMode><strong>buss</strong></DefaultTransportMode> <StopAreaTypeCode><strong>BUSTERM</strong></StopAreaTypeCode> <LastModifiedUtcDateTime><strong>2007-08-24 00:00:00.000</strong></LastModifiedUtcDateTime> <ExistsFromDate><strong>2007-08-24 00:00:00.000</strong></ExistsFromDate> </TransportMode></p>
<h3>JSON objektstruktur</h3>
<p><strong>{</strong> "DefaultTransportModeCode"<strong>:</strong> <strong>"BUS"</strong><strong>,</strong> "DefaultTransportMode"<strong>:</strong> <strong>"buss"</strong><strong>,</strong> "StopAreaTypeCode"<strong>:</strong> <strong>"BUSTERM"</strong><strong>,</strong> "LastModifiedUtcDateTime"<strong>:</strong> <strong>"2007-08-24 00:00:00.000"</strong><strong>,</strong> "ExistsFromDate"<strong>:</strong> <strong>"2007-08-24 00:00:00.000"</strong> <strong>}</strong></p>
<p>Fullständiga exempel</p>
<h2>Trafikslag XML</h2>
<p><ResponseOfPwsResult xmlns:xsd=<strong>"https://www.w3.org/2001/XMLSchema"</strong> xmlns:xsi=<strong>"https://www.w3.org/2001/XMLSchema-instance"</strong>> <StatusCode><strong>0</strong></StatusCode> <ExecutionTime><strong>277</strong></ExecutionTime> <ResponseData> <Version xmlns=<strong>"https://api.sl.se/api/pws"</strong>><strong>2014-10-09 18:05</strong></Version> <Type xmlns=<strong>"https://api.sl.se/api/pws"</strong>><strong>TransportMode</strong></Type> <TransportMode xmlns=<strong>"https://api.sl.se/api/pws"</strong>> <DefaultTransportModeCode><strong>BUS</strong></DefaultTransportModeCode> <DefaultTransportMode><strong>buss</strong></DefaultTransportMode> <StopAreaTypeCode><strong>BUSTERM</strong></StopAreaTypeCode> <LastModifiedUtcDateTime><strong>2007-08-24 00:00:00.000</strong></LastModifiedUtcDateTime> <ExistsFromDate><strong>2007-08-24 00:00:00.000</strong></ExistsFromDate> </TransportMode> <TransportMode xmlns=<strong>"https://api.sl.se/api/pws"</strong>> <DefaultTransportModeCode><strong>FERRY</strong></DefaultTransportModeCode> <DefaultTransportMode><strong>färja</strong></DefaultTransportMode> <StopAreaTypeCode><strong>FERRYBER</strong></StopAreaTypeCode> <LastModifiedUtcDateTime><strong>2007-08-24 00:00:00.000</strong></LastModifiedUtcDateTime> <ExistsFromDate><strong>2007-08-24 00:00:00.000</strong></ExistsFromDate> </TransportMode> <TransportMode xmlns=<strong>"https://api.sl.se/api/pws"</strong>> <DefaultTransportModeCode><strong>METRO</strong></DefaultTransportModeCode> <DefaultTransportMode><strong>tunnelbana</strong></DefaultTransportMode> <StopAreaTypeCode><strong>METROSTN</strong></StopAreaTypeCode> <LastModifiedUtcDateTime><strong>2007-08-24 00:00:00.000</strong></LastModifiedUtcDateTime> <ExistsFromDate><strong>2007-08-24 00:00:00.000</strong></ExistsFromDate> </TransportMode> <TransportMode xmlns=<strong>"https://api.sl.se/api/pws"</strong>> <DefaultTransportModeCode><strong>SHIP</strong></DefaultTransportModeCode> <DefaultTransportMode><strong>båt</strong></DefaultTransportMode> <StopAreaTypeCode><strong>SHIPBER</strong></StopAreaTypeCode> <LastModifiedUtcDateTime><strong>2007-08-24 00:00:00.000</strong></LastModifiedUtcDateTime> <ExistsFromDate><strong>2007-08-24 00:00:00.000</strong></ExistsFromDate> </TransportMode> <TransportMode xmlns=<strong>"https://api.sl.se/api/pws"</strong>> <DefaultTransportModeCode><strong>TRAIN</strong></DefaultTransportModeCode> <DefaultTransportMode><strong>pendeltåg</strong></DefaultTransportMode> <StopAreaTypeCode><strong>RAILWSTN</strong></StopAreaTypeCode> <LastModifiedUtcDateTime><strong>2007-08-24 00:00:00.000</strong></LastModifiedUtcDateTime> <ExistsFromDate><strong>2007-08-24 00:00:00.000</strong></ExistsFromDate> </TransportMode> <TransportMode xmlns=<strong>"https://api.sl.se/api/pws"</strong>> <DefaultTransportModeCode><strong>TRAM</strong></DefaultTransportModeCode> <DefaultTransportMode><strong>spårvagn/lokalbana</strong></DefaultTransportMode> <StopAreaTypeCode><strong>TRAMSTN</strong></StopAreaTypeCode> <LastModifiedUtcDateTime><strong>2007-08-24 00:00:00.000</strong></LastModifiedUtcDateTime> <ExistsFromDate><strong>2007-08-24 00:00:00.000</strong></ExistsFromDate> </TransportMode> </ResponseData> </ResponseOfPwsResult></p>
<h2>Trafikslag JSON</h2>
<p><strong>{</strong> "StatusCode"<strong>:</strong> <strong>0,</strong> "ExecutionTime"<strong>:</strong> <strong>327,</strong> "ResponseData"<strong>:</strong> <strong>{</strong> "Version"<strong>:</strong> <strong>"2014-10-09 18:05"</strong><strong>,</strong> "Type"<strong>:</strong> <strong>"TransportMode"</strong><strong>,</strong> "Result"<strong>:</strong> <strong>\[{</strong> "DefaultTransportModeCode"<strong>:</strong> <strong>"BUS"</strong><strong>,</strong> "DefaultTransportMode"<strong>:</strong> <strong>"buss"</strong><strong>,</strong> "StopAreaTypeCode"<strong>:</strong> <strong>"BUSTERM"</strong><strong>,</strong> "LastModifiedUtcDateTime"<strong>:</strong> <strong>"2007-08-24 00:00:00.000"</strong><strong>,</strong> "ExistsFromDate"<strong>:</strong> <strong>"2007-08-24 00:00:00.000"</strong> <strong>},</strong> <strong>{</strong> "DefaultTransportModeCode"<strong>:</strong> <strong>"FERRY"</strong><strong>,</strong> "DefaultTransportMode"<strong>:</strong> <strong>"färja"</strong><strong>,</strong> "StopAreaTypeCode"<strong>:</strong> <strong>"FERRYBER"</strong><strong>,</strong> "LastModifiedUtcDateTime"<strong>:</strong> <strong>"2007-08-24 00:00:00.000"</strong><strong>,</strong> "ExistsFromDate"<strong>:</strong> <strong>"2007-08-24 00:00:00.000"</strong> <strong>},</strong> <strong>{</strong> "DefaultTransportModeCode"<strong>:</strong> <strong>"METRO"</strong><strong>,</strong> "DefaultTransportMode"<strong>:</strong> <strong>"tunnelbana"</strong><strong>,</strong> "StopAreaTypeCode"<strong>:</strong> <strong>"METROSTN"</strong><strong>,</strong> "LastModifiedUtcDateTime"<strong>:</strong> <strong>"2007-08-24 00:00:00.000"</strong><strong>,</strong> "ExistsFromDate"<strong>:</strong> <strong>"2007-08-24 00:00:00.000"</strong> <strong>},</strong> <strong>{</strong> "DefaultTransportModeCode"<strong>:</strong> <strong>"SHIP"</strong><strong>,</strong> "DefaultTransportMode"<strong>:</strong> <strong>"båt"</strong><strong>,</strong> "StopAreaTypeCode"<strong>:</strong> <strong>"SHIPBER"</strong><strong>,</strong> "LastModifiedUtcDateTime"<strong>:</strong> <strong>"2007-08-24 00:00:00.000"</strong><strong>,</strong> "ExistsFromDate"<strong>:</strong> <strong>"2007-08-24 00:00:00.000"</strong> <strong>},</strong> <strong>{</strong> "DefaultTransportModeCode"<strong>:</strong> <strong>"TRAIN"</strong><strong>,</strong> "DefaultTransportMode"<strong>:</strong> <strong>"pendeltåg"</strong><strong>,</strong> "StopAreaTypeCode"<strong>:</strong> <strong>"RAILWSTN"</strong><strong>,</strong> "LastModifiedUtcDateTime"<strong>:</strong> <strong>"2007-08-24 00:00:00.000"</strong><strong>,</strong> "ExistsFromDate"<strong>:</strong> <strong>"2007-08-24 00:00:00.000"</strong> <strong>},</strong> <strong>{</strong> "DefaultTransportModeCode"<strong>:</strong> <strong>"TRAM"</strong><strong>,</strong> "DefaultTransportMode"<strong>:</strong> <strong>"spårvagn/lokalbana"</strong><strong>,</strong> "StopAreaTypeCode"<strong>:</strong> <strong>"TRAMSTN"</strong><strong>,</strong> "LastModifiedUtcDateTime"<strong>:</strong> <strong>"2007-08-24 00:00:00.000"</strong><strong>,</strong> "ExistsFromDate"<strong>:</strong> <strong>"2007-08-24 00:00:00.000"</strong> <strong>}\]</strong> <strong>}</strong> <strong>}</strong></p>
<h2 id="support">Support</h2>
<p>Räcker inte dokumentationen så<a href="http://kundo.se/org/trafiklabse/posts/">sök gärna bland alla de hundratals inlägg som finns på vårt supportforum</a>. Det är troligt att någon redan har hittat och löst samma problem som du har.</p>
<p>Hittar du fortfarande inte svar på din fråga så<a href="http://kundo.se/org/trafiklabse/">skriv ett eget inlägg på forumet</a>så hjälper vi dig.</p>