---
title: SL Nearby stops v2.0 (Närliggande hållplatser 2)
weight: 310
date: 2019-01-14
aliases:
  - /api/sl-narliggande-hallplatser-2
  - /api/sl-narliggande-hallplatser-2/dokumentation
  - /api/sl-narliggande-hallplatser-2/nivaer
  - /api/sl-narliggande-hallplatser-2/konsol
  - /node/25595
  - /node/25595/dokumentation
  - /node/25595/nivaer
  - /node/25595/konsol
---

## Beskrivning

Med detta API kan du få information om närliggande hållplatser till en försedd plats baserad på lat och long.

## URL

`https://journeyplanner.integration.sl.se/v1/nearbystopsv2.<FORMAT>?key=<DIN NYCKEL>&originCoordLat=<LAT>&originCoordLong=<LONG>&maxNo=<MAX ANTAL SVAR>&r=<RADIUS I METER>`

{{% warning %}}
Den tidigare
länken `https://api.sl.se/api2/nearbystopsv2.<FORMAT>?key=<DIN NYCKEL>&originCoordLat=<LAT>&originCoordLong=<LONG>&maxNo=<MAX ANTAL SVAR>&r=<RADIUS I METER>`
har ändrats den 4:e december, och kommer sluta fungera den 15e mars 2024.
Parametrar, svarsstrukturer och API nycklar är oförändrade.
{{% /warning %}}

### API-nyckelnivåer

| Nivå   | Max anrop/minut | Max anrop/månad |
|--------|-----------------|-----------------|
| Brons  | 30              | 10 000          |
| Silver | 60              | 500 000         |
| Guld   |                 | Efter behov     |

<h2>Format</h2>
<p>Json eller xml enligt ändelse till serviceanropet.</p>
<h3>Parametrar</h3>
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
			<p>Key</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Ja</p>
			</td>
			<td>
			<p>Din API nyckel.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>originCoordLat</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Ja</p>
			</td>
			<td>
			<p>Lat</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>originCoordLong</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Ja</p>
			</td>
			<td>
			<p>Long</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>maxNo</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Nej</p>
			</td>
			<td>
			<p>Maximalt antal resultat som önskas. 9 är default, max är 1000.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>r</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Nej</p>
			</td>
			<td>
			<p>Radius runt försedd koordinat som närliggande hållplatser skall hämtas ut för. 1000 är default, max är 2000.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>products</p>
			</td>
			<td>
						</td>
			<td>
			<p>Nej</p>
			</td>
			<td>
			<p>Produktfilter, Kombinationsvärde av önskade trafikslag om inte alla ska användas vid utsökning av resor.</p>
			<p>Bitmask enligt följande:<br />
			Pendeltåg (1)<br />
			Tunnelbana (2)<br />
			Lokalbana/spårvagn (4)<br />
			Buss (8)<br />
			Ej i bruk (16)<br />
			Ej i bruk (32)<br />
			Båt typ (64)<br />
			Närtrafik (128)</p>
			<p>Värdes anges som heltalsvärdet av den kombinerade bitmasken, ex Buss och båt, 8+64 = 72</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>type</p>
			</td>
			<td>
						</td>
			<td>
			<p>Nej</p>
			</td>
			<td>
			<p>Typfilter för platser,<br />
			S: sök efter endast stationer,<br />
			P: Sök efter endast POI<br />
			SP: Sök efter stationer och POI</p>
			</td>
		</tr>
	</tbody>
</table>
<h2>Resultat</h2>
<h3>Svarsstruktur</h3>
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
			<p>serverVersion</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Versionsinformation.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>dialectVersion</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Versionsinformation.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>requestId</p>
			</td>
			<td>
			<p>Long</p>
			</td>
			<td>
			<p>En id som identifierar anropen.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>stopLocationOrCoordLocation</p>
			</td>
			<td>
			<p>StopLocation</p>
			</td>
			<td>
			<p>Innehåller själva svarsdata från tjänsten. Se ”Svarsdata” nedan.</p>
			</td>
		</tr>
	</tbody>
</table>
<h3>Svarsdata</h3>
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
			<p>stopLocationOrCoordLocation</p>
			</td>
			<td>
			<p>Lista av element</p>
			</td>
			<td>
			<p>Lista med de platser som hittats. Se ”StopLocation” och ”CoordLocation” nedan.</p>
			</td>
		</tr>
		<tr>
			<td>
						</td>
			<td>
						</td>
			<td>
						</td>
		</tr>
	</tbody>
</table>
<h4>StopLocation</h4>
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
			<p>Id</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Reconstruction Id, se reseplanerarens dokumentation</p>
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
			<p>Namn för hållplats.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>extId</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>HafasId för hållplatsen. Läs mer om HafasId i sektionen HafasId och SiteId.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Lat</p>
			</td>
			<td>Double</td>
			<td>
			<p>Lat.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Lon</p>
			</td>
			<td>
			<p>Double</p>
			</td>
			<td>
			<p>Long.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Weight</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Anger hur mycket en station används, ju högre värde desto större användning.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Dist</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Distans i meter från försedd koordinat i anropet.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Products</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Se beskrivning för anropsparametrar</p>
			</td>
		</tr>
	</tbody>
</table>
<h4>CoordLocation</h4>
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
			<p>Id</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Reseplanerar reconstruction Id, se reseplanerarens documentation</p>
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
			<p>Namn för POI.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Lat</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Lat.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Lon</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Long.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Dist</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Distans i meter från försedd koordinat i anropet.</p>
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
			<p>Visar i nuläget endast ”POI”</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>LocationNotes</p>
			</td>
			<td>
			<p>Lista av element</p>
			</td>
			<td>
			<p>Se nedan</p>
			</td>
		</tr>
	</tbody>
</table>
<h4>LocationNote</h4>
<p>Namn/värde lista.</p>
<p>Dessa värden gäller för närvarande men kan komma att ändras utan att information skickas i förväg.</p>
<table>
	<tbody>
		<tr>
			<td>
			<p><strong>Key</strong></p>
			</td>
			<td>
			<p><strong>Value</strong></p>
			</td>
		</tr>
		<tr>
			<td>
			<p>PI</p>
			</td>
			<td>
			<p>Unikt id</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>PC</p>
			</td>
			<td>
			<p>POI kategori:<br />
			Amenity, Historic, Leisure, Shop eller Tourism<br />
			</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>PT</p>
			</td>
			<td>
			<p>POI typ: Hospital, School, Theatre, University, Castle, Park, Library, Mall, Attraction, Chalet, Museum, Viewpoint eller Zoo</p>
						</td>
		</tr>
		<tr>
			<td>
			<p>CN</p>
			</td>
			<td>
			<p>Namnet på kommunen som POI:en befinner sig i.</p>
			</td>
		</tr>
	</tbody>
</table>
<h3>HafasId och SiteId</h3>
<p>Information om hur HafasId byggs på SiteId, StopId och StopAreaId.<br />
HafasId nyttjas bland annat i Reseplanerar api’et.</p>
<table>
	<tbody>
		<tr>
			<td>
			<p><strong>Typ</strong></p>
			</td>
			<td>
			<p><strong>Beskrivning</strong></p>
			</td>
			<td>
			<p><strong>Exempel</strong></p>
			</td>
		</tr>
		<tr>
			<td>
			<p>SiteId</p>
			</td>
			<td>
			<p>3FG1EDCBA där där FGEDCBA är de 7 sista sifforna i site.number utfyllt med nollor.</p>
			</td>
			<td>
			<p>SiteId: 9600</p>
			<p>HafasId: 300109600</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>StopId</p>
			</td>
			<td>
			<p>4FG1EDCBA där GFEDCBA är journeyPatternPoint utfyllt med nollor.</p>
			</td>
			<td>
			<p>JourneyPatternPoint.Number: 56789</p>
			<p>HafasId: 400156789</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>StopAreaId</p>
			</td>
			<td>
			<p>2FG1EDCBA där FEDCBA är stopArea.number utfyllt med nollor</p>
			</td>
			<td>
			<p>StopArea.number: 81025</p>
			<p>HafasId: 200181025</p>
			</td>
		</tr>
	</tbody>
</table>
<h3>XSD</h3>
<h4>Url</h4>
<p>Exempel:<br />
https://api.sl.se/api2/nearbystops/xsd.xml?key=&lt;DIN API NYCKEL&gt;&amp;xsdname= hafasRestLocation.xsd</p>
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
			<p>Nyckel har ej skickats med.</p>
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
	</tbody>
</table>
<h2>Övriga felmeddelanden</h2>
<p>Felmeddelanden från api’et är idag på svenska eller engelska beroende på vilket språk som efterfrågats i urlanropet.</p>
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
			<p>R0001</p>
			</td>
			<td>
			<p>Unknown service method</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>R0002</p>
			</td>
			<td>
			<p>Invalid or missing request parameters.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>R0007</p>
			</td>
			<td>
			<p>Internal communication error.</p>
			</td>
		</tr>
	</tbody>
</table>
