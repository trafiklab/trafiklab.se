---
title: SL Traffic status v2.0 (Trafikläget 2)
weight: 600
date: 2014-03-14
aliases:
  - /apis/sl-trafiklaget-2
  - /apis/sl-trafiklaget-2/documentation
  - /apis/sl-trafiklaget-2/nivaer
  - /apis/sl-trafiklaget-2/console
  - /node/12603
  - /node/12603/documentation
  - /node/12603/nivaer
  - /node/12603/console
---

## Beskrivning

Med detta API kan du få information om den aktuella statusen för SLs trafikläge. Detta är information på en övergripande
nivå om aktuell status för respektive trafikslag. Den information som ligger till grund för detta API hittar du på
startsidan av sl.se under rubriken "Trafikläget kl. xx:xx". API’et har endast en metod som returnerar en översiktlig
bild över hur trafiksituationen ser ut just nu, med avseende på störningar som kan påverka resenärerna. Det som
returneras är en lista med ett antal trafikslag, varje trafikslag har en sammanfattande status och ett antal (0 eller
fler) händelser. Det finns 3 olika status som händelser kan ha:

- ”Inga större störningar”
- ”Stor påverkan”
- ”Avstängt”

En händelse påverkar sitt trafikslag, så att trafikslagets sammanfattande status är lika med den sämsta statusen som
finns ibland just nu aktiva händelser tillhörande trafikslaget. En händelse kan utöver statusen dessutom vara planerad.

{{% info %}}SL will replace this API with a new, similar API in the near future. The documentation for the current API
has therefore not been translated for the new Trafiklab website. {{% /info %}}

## URL

`https://api.sl.se/api2/trafficsituation.<FORMAT>?key=<DIN API NYCKEL>`

## Format

Json eller xml enligt ändelse till serviceanropet.

## Parametrar

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
	</tbody>
</table>

## Resultat

### Svarsstruktur

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
			<p>TrafficStatus</p>
			</td>
			<td>
			<p>Innehåller själva svarsdata från tjänsten. Se ”Svarsdata” nedan.</p>
			</td>
		</tr>
	</tbody>
</table>

### Svarsdata

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
			<p>TrafficTypes</p>
			</td>
			<td>
			<p>List</p>
			</td>
			<td>
			<p>Ett TrafficType objekt för varje trafikslag.</p>
			</td>
		</tr>
	</tbody>
</table>

### TrafficType

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
			<p>Name</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Namn på trafikslag: "Tunnelbana", "Pendeltåg", etc.</p>
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
			<p>"metro", "train", "local", "tram", "bus" eller "fer".</p>
			<p>fer = Båt</p>
			<p>local = Lokalbana</p>
			<p>tram = Spårvagn</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>StatusIcon</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Hjälpinformation som indikerar vilken ikon som ska visas i webben.</p>
			<p>Möjliga värden:</p>
			<ul>
				<li>EventMajor: "Avstängt"</li>
				<li>EventMinor: "Stor påverkan"</li>
				<li>EventGood: "Inga större störningar"</li>
				<li>EventPlanned: "Planerad händelse"</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>
			<p>Expanded</p>
			</td>
			<td>
			<p>Boolean</p>
			</td>
			<td>
			<p>Hjälpinformation som indikerar om informationen har hög prioritet eller inte.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>HasPlannedEvent</p>
			</td>
			<td>
			<p>Boolean</p>
			</td>
			<td>
			<p>Hjälpinformation som indikerar om det finns planerade händelser.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Events</p>
			</td>
			<td>
			<p>List</p>
			</td>
			<td>
			<p>Ett TrafficEvent objekt för varje händelse.</p>
			</td>
		</tr>
	</tbody>
</table>

### TrafficEvent

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
			<p>EventId</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Löpnummer på händelsen.</p>
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
			<p>Meddelande gällande störningen/händelsen.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Expanded</p>
			</td>
			<td>
			<p>Boolean</p>
			</td>
			<td>
			<p>Hjälpinformation som indikerar om informationen har hög prioritet eller inte.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Planned</p>
			</td>
			<td>
			<p>Boolean</p>
			</td>
			<td>
			<p>Hjälpinformation som indikerar om händelsen är planerad eller inte.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>SortIndex</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Sorteringsordning på händelsen.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>StatusIcon</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Hjälpinformation som indikerar vilken ikon som ska visas i webben.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>LineNumbers</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Linjenummer som händelsen berör, en kommaseparerad String t.ex. ”177, 69K, 508”.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>LineNumbers/InputDataIsOptional</p>
			</td>
			<td>
			<p>Boolean</p>
			</td>
			<td>
			<p>Är alltid satt till True och indikerar att linjenummer är frivilligt.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>TrafficLine</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Namn på den bana som händelsen påverkar. Kan saknas, om händelsen påverkar hela trafikslaget eller banor inte finns (typ bussar).</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>EventInfoUrl</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Länk till storningsinformation.sl.se, eller till specifik sida med information om händelsen.</p>
			</td>
		</tr>
	</tbody>
</table>

### Felmeddelanden

Än så länge finns inga felmeddelanden.

## Support

Räcker inte dokumentationen så<a href="https://kundo.se/org/trafiklabse/posts/">sök gärna bland alla de hundratals
inlägg som finns på vårt supportforum</a>. Det är troligt att någon redan har hittat och löst samma problem som du har.
Hittar du fortfarande inte svar på din fråga så<a href="https://kundo.se/org/trafiklabse/">skriv ett eget inlägg på
forumet</a>så hjälper vi dig.
