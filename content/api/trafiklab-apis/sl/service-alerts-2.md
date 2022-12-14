---
title: SL Service alerts v2.0 (Störningsinformation 2)
weight: 500
date: 2014-03-14
aliases: 
  - /api/sl-storningsinformation-2
  - /api/sl-storningsinformation-2/documentation
  - /api/sl-storningsinformation-2/nivaer
  - /api/sl-storningsinformation-2/console
  - /api/sl-storningsinformation-2/konsol
  - /node/12605
  - /node/12605/documentation
  - /node/12605/nivaer
  - /node/12605/console
  - /node/12605/konsol
---
<h2>Beskrivning</h2>
<p>Med detta API kan du få fram information om aktuella och planerade störningar i SL-trafiken. Med API ‘et kan du ställa frågor om störningar på till exempel en viss linje eller ett visst trafikslag. Svaret består av störningsmeddelanden med viss metainformation.</p>
<p>För att se informationen som returneras av detta API, se <a href="https://api.sl.se/ta">https://api.sl.se/ta</a> (detta är en störningsinformationssida som är anpassad för SL:s interna behov och inte avsedd att användas av resenärerna).</p>

{{% info %}}SL will replace this API with a new, similar API in the near future. The documentation for the current API
has therefore not been translated for the new Trafiklab website. {{% /info %}}

<p>Om ingen av parametrarna ”TransportMode”, ”LineNumber” och ”SiteId” skickas med anropet skickas samtliga avvikelser tillbaks som svar.</p>
<p>Är du intresserad av Störningar här och nu i SL trafiken se<a href="https://sl.se/sv/find/?query=St%c3%b6rningsinformation">https://sl.se/sv/find/?query=St%c3%b6rningsinformation</a></p>

### API-nyckelnivåer

| Nivå   | Max anrop/minut | Max anrop/månad |
|--------|-----------------|-----------------|
| Brons  | 30              | 10 000          |
| Silver | 60              | 100 000         |
| Guld   |                 | Efter behov     |

<h2>Metod deviations</h2>
<p>URL</p>

`https://api.sl.se/api2/deviations.<FORMAT>?key=<DIN API NYCKEL>&transportMode=<TRANSPORTMODE>&lineNumber=<LINENUMBER>&siteId=<SITEID>&fromDate=<FROMDATE>&toDate=<TODATE>`

<p>Format</p>
<p>Json eller xml enligt ändelse till serviceanropet.</p>
<p>Parametrar</p>
<table>
	<tbody>
		<tr>
			<td>
			<p><strong>Namn</strong></p>
			</td>
			<td>
			<p><strong>Typ</strong></p>
			</td>
			<td>
			<p><strong>Tvingande</strong></p>
			</td>
			<td>
			<p><strong>Beskrivning</strong></p>
			</td>
		</tr>
		<tr>
			<td>
			<p>TransportMode</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Nej</p>
			</td>
			<td>
			<p>Aktuella trafikslag. Tillåtna värden är bus, metro, train, shipoch tram. Kommaseparerad sträng.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>LineNumber</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Nej</p>
			</td>
			<td>
			<p>Max 10 linjer. Kommaseparerad sträng.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>SiteId</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Nej</p>
			</td>
			<td>
			<p>Id för sökt hållplatsområde.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>FromDate</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Nej default, men Ja om ToDate angivits</p>
			</td>
			<td>
			<p>Startdatum för aktuell giltighetsperiod.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>ToDate</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Nej default, men Ja om FromDate angivits</p>
			</td>
			<td>
			<p>Slutdatum för aktuell giltighetsperiod.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Key</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Ja</p>
			</td>
			<td>
			<p>Din API nyckel. Under mockupdataperioden så kan nyckeln vara vad som helst.</p>
			</td>
		</tr>
	</tbody>
</table>
<p>Resultat</p>
<p>Svarsstruktur</p>
<table>
	<tbody>
		<tr>
			<td>
			<p><strong>Namn</strong></p>
			</td>
			<td>
			<p><strong>Datatyp</strong></p>
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
			<p>Integer</p>
			</td>
			<td>
			<p>Innehåller statuskod för det eventuella meddelandet.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Message</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Innehåller eventuellt anropsrelaterade meddelanden som t.ex. felmeddelanden. Se ”Felmeddelanden” nedan.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>ExecutionTime</p>
			</td>
			<td>
			<p>long</p>
			</td>
			<td>
			<p>Anger hur lång tid (i ms) det tog för servern att generera svaret.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>ResponseData</p>
			</td>
			<td>
			<p>Deviations</p>
			</td>
			<td>
			<p>Innehåller själva svarsdata från tjänsten. Se ”Svarsdata” nedan.</p>
			</td>
		</tr>
	</tbody>
</table>
<p>Svarsdata</p>
<table>
	<tbody>
		<tr>
			<td>
			<p><strong>Namn</strong></p>
			</td>
			<td>
			<p><strong>Datatyp</strong></p>
			</td>
			<td>
			<p><strong>Beskrivning</strong></p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Created</p>
			</td>
			<td>
			<p>DateTime</p>
			</td>
			<td>
			<p>När ärendet blev publicerad.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>MainNews</p>
			</td>
			<td>
			<p>Boolean</p>
			</td>
			<td>
			<p>Boolean som indikerar om ärendet är en huvudnyhet.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>SortOrder</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Förslag på sorteringsordning av ärendena. Denna returneras som 1.<br />
			Är man ute efter sortering på prioritet bör denna tas från Deviationsrawdata och återfinns i svarsstrukturen under priority.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Header</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Rubrik.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Details</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Detaljer, samma som presenteras på webbplatsen för resp. ärende.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Scope</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Ett alias för ScopeElements.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>DevCaseGid</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Ärendets id.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>DevMessageVersionNumber</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Anger aktuell version för ärendet.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>ScopeElements</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Beskrivning av vilka linjer eller hållplatser ärendet gäller för.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>FromDateTime</p>
			</td>
			<td>
			<p>DateTime</p>
			</td>
			<td>
			<p>När ärendet börjar vara aktivt.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>UpToDateTime</p>
			</td>
			<td>
			<p>DateTime</p>
			</td>
			<td>
			<p>När ärendet slutar att vara aktivt.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Updated</p>
			</td>
			<td>
			<p>DateTime</p>
			</td>
			<td>
			<p>Senast ärendet blev uppdaterat.</p>
			</td>
		</tr>
	</tbody>
</table>
<h2>Metod deviationsrawdata</h2>
<p>URL</p>
<p>api.sl.se/api2/deviationsrawdata.&lt;FORMAT&gt;?key=&lt;DIN API NYCKEL&gt;&amp;transportMode=&lt;TRANSPORTMODE&gt;&amp;lineNumber=&lt;LINENUMBER&gt;&amp;siteId=&lt;SITEID&gt;</p>
<p>Om ingen av parametrarna ”TransportMode” och ”LineNumber” skickas med anropet skickas samtliga avvikelser tillbaks som svar.</p>
<p>Format</p>
<p>Json eller xml enligt ändelse till serviceanropet.</p>
<p>Parametrar</p>
<table>
	<tbody>
		<tr>
			<td>
			<p><strong>Namn</strong></p>
			</td>
			<td>
			<p><strong>Datatyp</strong></p>
			</td>
			<td>
			<p><strong>Tvingande</strong></p>
			</td>
			<td>
			<p><strong>Beskrivning</strong></p>
			</td>
		</tr>
		<tr>
			<td>
			<p>TransportMode</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Nej</p>
			</td>
			<td>
			<p>Aktuella trafikslag. Tillåtna värden är ”bus”, ”metro”, ”train”, "ship"och ”tram”. Kommaseparerad sträng.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>LineNumber</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Nej</p>
			</td>
			<td>
			<p>Max 10 linjer. Kommaseparerad sträng.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>SiteId</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Nej</p>
			</td>
			<td>
			<p>Id för sökt hållplatsområde.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Key</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Ja</p>
			</td>
			<td>
			<p>Din API nyckel. Under mockupdataperioden så kan nyckeln vara vad som helst.</p>
			</td>
		</tr>
		<tr>
			<td>
			</td>
			<td>
			</td>
			<td>
			</td>
			<td>
			</td>
		</tr>
		<tr>
			<td>
			</td>
			<td>
			</td>
			<td>
			</td>
			<td>
			</td>
		</tr>
	</tbody>
</table>
<h2>Resultat</h2>
<p>Svarsstruktur</p>
<table>
	<tbody>
		<tr>
			<td>
			<p><strong>Namn</strong></p>
			</td>
			<td>
			<p><strong>Datatyp</strong></p>
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
			<p>Integer</p>
			</td>
			<td>
			<p>Innehåller statuskod för det eventuella meddelandet.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Message</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Innehåller eventuellt anropsrelaterade meddelanden som t.ex. felmeddelanden. Se ”Felmeddelanden” nedan.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>ExecutionTime</p>
			</td>
			<td>
			<p>Long</p>
			</td>
			<td>
			<p>Anger hur lång tid (i ms) det tog för servern att generera svaret.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>ResponseData</p>
			</td>
			<td>
			<p>Deviations</p>
			</td>
			<td>
			<p>Innehåller själva svarsdata från tjänsten. Se ”Svarsdata” nedan.</p>
			</td>
		</tr>
	</tbody>
</table>
<p>Svarsdata</p>
<table>
	<tbody>
		<tr>
			<td>
			<p><strong>Namn</strong></p>
			</td>
			<td>
			<p><strong>Datatyp</strong></p>
			</td>
			<td>
			<p><strong>Beskrivning</strong></p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Created</p>
			</td>
			<td>
			<p>DateTime</p>
			</td>
			<td>
			<p>När ärendet blev publicerad.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>MainNews</p>
			</td>
			<td>
			<p>Boolean</p>
			</td>
			<td>
			<p>Boolean som indikerar om ärendet är en huvudnyhet.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>SortOrder</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Förslag på sorteringsordning av ärendena.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Header</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Rubrik.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Details</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Detaljer, samma som presenteras på webbplatsen för resp. ärende.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Scope</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Ett beskrivande alias för ScopeElements.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>DevCaseGid</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Ärendets id.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>DevMessageVersionNumber</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Anger aktuell version för ärendet.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>ScopeElements</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Uppräkning av vilka linjer eller hållplatser ärendet gäller för.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>FromDateTime</p>
			</td>
			<td>
			<p>DateTime</p>
			</td>
			<td>
			<p>När ärendet börjar vara aktivt.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>UpToDateTime</p>
			</td>
			<td>
			<p>DateTime</p>
			</td>
			<td>
			<p>När ärendet slutar att vara aktivt.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Updated</p>
			</td>
			<td>
			<p>DateTime</p>
			</td>
			<td>
			<p>Senast ärendet blev uppdaterat.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Priority</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Prioriteringsordning för ärendet.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>LineNumber</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Linje där ärendet är gällande.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>SiteId</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Id för hållplatsområde. Kan vara tom.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>TransportMode</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Trafikslag för ärendet.</p>
			</td>
		</tr>
	</tbody>
</table>
<p>Felmeddelanden</p>
<table>
	<tbody>
		<tr>
			<td>
			<p><strong>Statuskod</strong></p>
			</td>
			<td>
			<p><strong>Meddelande</strong></p>
			</td>
		</tr>
		<tr>
			<td>
			<p>1001</p>
			</td>
			<td>
			<p>problem with request: Key is undefined</p>
			<p>Nyckel hare ej skickats med.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>1002</p>
			</td>
			<td>
			<p>problem with request: Key is invalid</p>
			<p>Nyckel är ogiltig</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>1003</p>
			</td>
			<td>
			<p>Invalid api</p>
			<p>Ogiltigt api</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>1004</p>
			</td>
			<td>
			<p>problem with request: This api is currently not available for keys with priority above 2</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>1005</p>
			</td>
			<td>
			<p>Nyckel finns, men ej för detta api</p>
			<p>problem with request: Invalid api for key</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>1006</p>
			</td>
			<td>
			<p>To many requests per minute</p>
			<p>För många anrop per minut, för den profil som används</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>1007</p>
			</td>
			<td>
			<p>To many requests per month</p>
			<p>För många anrop per månad, för den profil som används</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>4002</p>
			</td>
			<td>
			<p>Fråndatum angett utan tilldatum. Båda datumen måste vara angivna vid filtrering på datum.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>4002</p>
			</td>
			<td>
			<p>Tilldatum angett utan fråndatum. Båda datumen måste vara angivna vid filtrering på datum.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>5000</p>
			</td>
			<td>
			<p>Ogiltigt formaterad parameter.</p>
			<p>FEL! Serverfel, var god försök lite senare.</p>
			<p>Ogiltigt formaterat datum, datumet ska formateras YYYY-MM-DD.</p>
			</td>
		</tr>
	</tbody>
</table>
<h2 id="support">Support</h2>
<p>Räcker inte dokumentationen så<a href="https://kundo.se/org/trafiklabse/posts/">sök gärna bland alla de hundratals inlägg som finns på vårt supportforum</a>. Det är troligt att någon redan har hittat och löst samma problem som du har.</p>
<p>Hittar du fortfarande inte svar på din fråga så<a href="https://kundo.se/org/trafiklabse/">skriv ett eget inlägg på forumet</a>så hjälper vi dig.</p>
