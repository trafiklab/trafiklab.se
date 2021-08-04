---
title: SL Departures (Realtidsinformation 4)
---<h2>Beskrivning</h2>
<p lang="sv-SE">Realtidsinformation gällande buss, tunnelbana, pendeltåg och lokalbana.</p>

{{% info %}}SL will replace this API with a new, similar API in the near future. The documentation for the current API
has therefore not been translated {{% /info %}}

<h2>URL</h2>
<p>https://api.sl.se/api2/realtimedeparturesV4.&lt;FORMAT&gt;?key=&lt;DIN API NYCKEL&gt;&amp;siteid=&lt;SITEID&gt;&amp;timewindow=&lt;TIMEWINDOW&gt;</p>
<h2>Format</h2>
<p>Json eller xml enligt ändelse till serviceanropet.</p>
<h2>Parametrar</h2>
<table>
	<tbody>
		<tr>
			<td>
			<p><strong>Parametrar</strong></p>
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
			<p>Format</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Ja</p>
			</td>
			<td>
			<p>Format på svarsdatat. Giltiga värden är “json” eller “xml”.</p>
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
			<p>Ja</p>
			</td>
			<td>
			<p>Unikt identifikationsnummer för den plats som aktuella avgångar skall hämtas för, t.ex. 9192 för Slussen.Detta id fås från tjänsten SL Platsuppslag.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>TimeWindow</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Ja</p>
			</td>
			<td>
			<p>Hämta avgångar inom önskat tidsfönster. Där tidsfönstret är antalet minuter från och med nu. Max 60.</p>
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
			<p>En giltig API-nyckel.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Bus</p>
			</td>
			<td>Boolean</td>
			<td>Nej</td>
			<td>Default = true. Om false, så exkluderas trafikslaget från svaret.</td>
		</tr>
		<tr>
			<td>
			<p>Metro</p>
			</td>
			<td>Boolean</td>
			<td>Nej</td>
			<td>Default = true. Om false, så exkluderas trafikslaget från svaret.</td>
		</tr>
		<tr>
			<td>
			<p>Train</p>
			</td>
			<td>Boolean</td>
			<td>Nej</td>
			<td>Default = true. Om false, så exkluderas trafikslaget från svaret.</td>
		</tr>
		<tr>
			<td>
			<p>Tram</p>
			</td>
			<td>Boolean</td>
			<td>Nej</td>
			<td>Default = true. Om false, så exkluderas trafikslaget från svaret.</td>
		</tr>
		<tr>
			<td>
			<p>Ship</p>
			</td>
			<td>Boolean</td>
			<td>Nej</td>
			<td>Default = false. Om true inkluderas information om osäker prognos.</td>
		</tr>
		<tr>
			<td>
			<p>EnablePrediction</p>
			</td>
			<td>Boolean</td>
			<td>Nej</td>
			<td>Default = true. Om false, så exkluderas trafikslaget från svaret.</td>
		</tr>
	</tbody>
</table>
<h2>Resultat</h2>
<p lang="sv-SE">Resultat från realtidssökning. Vid xml-format är rotelementets namn ResponseOfDepartures.</p>
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
			<p>Departure</p>
			</td>
			<td>
			<p>Innehåller själva svarsdata från tjänsten. Se ”Svarsdata” nedan.</p>
			</td>
		</tr>
	</tbody>
</table>
<p>Svarsdata/ResponseData</p>
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
			<p>LatestUpdate</p>
			</td>
			<td>
			<p>DateTime</p>
			</td>
			<td>
			<p>Anger när realtidsinformationen (DPS) senast uppdaterades.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>DataAge</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Antal sekunder sedan tidsstämpeln LatestUpdate.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Buses</p>
			</td>
			<td>
			<p>List</p>
			</td>
			<td>
			<p>Lista över samtliga bussavgångar för givet siteId, se svarsstruktur</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Metros</p>
			</td>
			<td>
			<p>List</p>
			</td>
			<td>
			<p>Lista över samtliga tunnelbaneavgångar för givet siteId, se svarsstruktur</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Trains</p>
			</td>
			<td>
			<p>List</p>
			</td>
			<td>
			<p>Lista över samtliga pendeltågsavgångar för givet siteId, se svarsstruktur.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Trams</p>
			</td>
			<td>
			<p>List</p>
			</td>
			<td>
			<p>Lista över samtliga lokalbaneavgångar för givet siteId, se svarsstruktur</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Ships</p>
			</td>
			<td>
			<p>List</p>
			</td>
			<td>
			<p>Lista över samtliga båtavgångar för givet siteId, se svarsstruktur</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>StopPointDeviations</p>
			</td>
			<td>
			<p>List</p>
			</td>
			<td>
			<p>Lista över hållplatsområdesspecifika avvikelser/störningar. D.v.s. störningar som inte är knutna till en specifik avgång</p>
			</td>
		</tr>
	</tbody>
</table>
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
			<p>TransportMode</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Trafikslag: ”BUS”,"METRO", ”TRAIN”, ”TRAM” eller ”SHIP”.</p>
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
			<p>Linjebeteckning/nummer.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Destination</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Namn på linjens ändhållplats.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>JourneyDirection</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Reseriktnings-id. 0 vid okänd riktning, annars 1 eller 2.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>GroupOfLine</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p><strong>För buss:</strong> Anger om det är en blå buss. Om det är en blå buss står det ”blåbuss”, annars saknas elementet(xml) eller är null(json).</p>
			<p><strong>För lokalbana:</strong> Linjegrupp, t.ex. “Tvärbanan” eller “Roslagsbanan”.</p>
			<p><strong>För tunnelbana:</strong> Linjegruppering. Röd/grön/blå linje.</p>
			<p><strong>För båt:</strong> Anger om det är pendlarbåt eller Waxholmsbolaget.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>StopAreaName</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Hållplatsnamn.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>StopAreaNumber</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Id för aktuell hållplats.</p>
			<p>Tunnelbana före övergång: 0</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>StopPointNumber</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Id för aktuellt stoppställe.</p>
			<p>Tunnelbana före övergång: 0</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>StopPointDesignation</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Ytterligare identifierare för stoppställe, t.ex. bokstav för busskur eller spår för pendeltåg.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>TimeTabledDateTime</p>
			</td>
			<td>
			<p>DateTime</p>
			</td>
			<td>
			<p>Avgångstid enligt tidtabell.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>ExpectedDateTime</p>
			</td>
			<td>
			<p>DateTime</p>
			</td>
			<td>
			<p>Förväntad avgångstid. Om det finns tillhörande störning med tillräckligt hög prioritet så kan denna ha null/tomt värde. Detta fram till ett par minuter innan avgång.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>DisplayTime</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Avgångstid för presentation. Kan anta formaten x min, HH:mm eller Nu. Om det finns tillhörande störning med tillräckligt hög prioritet så kan denna ha värdet ”-”. Detta fram till ett par minuter innan avgång.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>JourneyNumber</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Turnummer för avgången.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Deviations</p>
			</td>
			<td>
			<p>List</p>
			</td>
			<td>
			<p>Innehåller typen ”Deviation” nedan. Denna kan vara tom, eller innehålla 1 till flera avvikelser.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>SecondaryDestinationName</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p><strong>Finns bara för:</strong>Pendeltåg.</p>
			<p>Namn på delmål</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>PredictionState</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p><strong>Kan ha tre olika värden, NORMAL, UNRELIABLE, UNKNOWN. UNRELIABLE betecknar en osäker prognos</strong></p>
			<p>Namn på delmål</p>
			</td>
		</tr>
	</tbody>
</table>
<p>Deviation</p>
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
			<p>Consequence</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Konsekvensbeskrivning för aktuell avvikelse.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>ImportanceLevel</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Signifikationsnivå för aktuell avvikelse. 0-9 där 9 är mest allvarlig.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Text</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Beskrivning av aktuell avvikelse.</p>
			</td>
		</tr>
	</tbody>
</table>
<p>StopPointDeviations</p>
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
			<p>StopInfo</p>
			</td>
			<td>
			<p>StopInfo</p>
			</td>
			<td>
			<p>StopInfo. Kan vara tom. Se StopInfo</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Deviation</p>
			</td>
			<td>
			<p>Deviation</p>
			</td>
			<td>
			<p>Deviation. Kan vara tom. Se Deviation.</p>
			</td>
		</tr>
	</tbody>
</table>
<p>StopInfo</p>
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
			<p>GroupOfLine</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Om TransportMode är ”TRAM” så innehåller noden något av följande värden: ”Lidingöbanan”, ”Nockebybanan”, ”Roslagsbanan”, ”Saltsjöbanan”, ”Spårväg City”, ”Tvärbanan”. Annars blankt (kan komma att ändras).</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>StopAreaName</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Namn på hållplatsen som avvikelsen gäller.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>StopAreaNumber</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Id för hållplatsen som avvikelsen gäller. Är noll om TransportMode inte är BUS.</p>
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
			<p>”METRO”, ”BUS”, ”TRAIN”, ”TRAM” eller ospecificerat.</p>
			</td>
		</tr>
	</tbody>
</table>
<h2>Felmeddelanden</h2>
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
			<p>4001</p>
			</td>
			<td>
			<p>SiteId måste gå att konvertera till heltal.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>5321</p>
			</td>
			<td>
			<p>Kunde varken hämta information från TPI (tunnelbanan) eller DPS (övriga trafikslag).</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>5322</p>
			</td>
			<td>
			<p>Kunde inte hämta information från DPS.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>5323</p>
			</td>
			<td>
			<p>Kunde inte hämta information från TPI.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>5324</p>
			</td>
			<td>
			<p>Kunde varken hämta information från TPI (tunnelbanan) eller DPS (övriga trafikslag) p.g.a. inaktuell DPS-data. Detta uppstår om DPS-datan är äldre än 2 minuter vid svarstillfället.</p>
			</td>
		</tr>
	</tbody>
</table>
<h2 id="support">Support</h2>
<p>Räcker inte dokumentationen så <a href="https://kundo.se/org/trafiklabse/posts/">sök gärna bland alla de 
hundratals inlägg som finns på vårt supportforum</a>. Det är troligt att någon redan har hittat och löst samma problem som du har.</p>
<p>Hittar du fortfarande inte svar på din fråga så<a href="https://kundo.se/org/trafiklabse/">skriv ett eget inlägg på forumet</a>så hjälper vi dig.</p>
