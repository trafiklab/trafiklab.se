---
title: SL Stop lookup v1.0 (Platsuppslag)
weight: 300
date: 2014-03-14
---
<h2>Beskrivning</h2>
<p>Med detta API kan du få information om en plats genom att skicka in delar av platsens namn. Du kan välja mellan att bara söka efter hållplatsområden eller hållplatser, adresser och platser.</p>

{{% info %}}SL will replace this API with a new, similar API in the near future. The documentation for the current API
has therefore not been translated for the new Trafiklab website. {{% /info %}}

<h2>URL</h2>

`https://api.sl.se/api2/typeahead.<FORMAT>?key=<DIN NYCKEL>%&searchstring=<SÖKORD>%&stationsonly=<ENDAST STATIONER>&maxresults<MAX ANTAL SVAR>`

<h2>Format</h2>
<p>Json eller xml enligt ändelse till serviceanropet.</p>
<h2>Parametrar</h2>
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
			<p>SearchString</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Ja</p>
			</td>
			<td>
			<p>Söksträngen. (Max 20 tecken)</p>
			</td>
		</tr>
		<tr>
			<td>
			<p class="notranslate">StationsOnly</p>
			</td>
			<td>
			<p>Boolean</p>
			</td>
			<td>
			<p>Nej</p>
			</td>
			<td>
			<p>Om ”True” returneras endast hållplatser. True = default.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>MaxResults</p>
			</td>
			<td>
			<p>Integer</p>
			</td>
			<td>
			<p>Nej</p>
			</td>
			<td>
			<p>Maximalt antal resultat som önskas. 10 är default, det går inte att få mer än 50.</p>
			</td>
		</tr>
		<tr>
			<td>type</td>
			<td>String</td>
			<td>Nej</td>
			<td>
			<p>Typfilter för platser:</p>
			<p>S: sök efter endast stationer<br />
			P: Sök efter endast POI<br />
			A: Sök endast efter adresser<br />
			SP: Sök efter stationer och POI<br />
			SA: Sök endas efter stationer och Adresser<br />
			AP: Sök endast på adresser och POI<br />
			ALL: adresser, stationer och POI</p>
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
			<p class="notranslate">StatusCode</p>
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
			<p>Sites</p>
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
			<p>Sites</p>
			</td>
			<td>
			<p>List</p>
			</td>
			<td>
			<p>Lista med de platser som hittats. Se ”Site” nedan.</p>
			</td>
		</tr>
	</tbody>
</table>
<h4>Site</h4>
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
			<p>Namnet på platsen.</p>
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
			<p>Id för hållplatsområde.</p>
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
			<p>Typ av plats: ”Station”, ”Address” eller ”Poi” (Point of interest).</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>X</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>X-koordinat för placering.</p>
			</td>
		</tr>
		<tr>
			<td>
			<p>Y</p>
			</td>
			<td>
			<p>String</p>
			</td>
			<td>
			<p>Y-koordinat för placering.</p>
			</td>
		</tr>
	</tbody>
</table>
<h2>Felmeddelanden</h2>
<p>Än så länge finns inga felmeddelanden.</p>
<h2 id="support">Support</h2>
<p>Räcker inte dokumentationen så<a href="http://kundo.se/org/trafiklabse/posts/">sök gärna bland alla de hundratals inlägg som finns på vårt supportforum</a>. Det är troligt att någon redan har hittat och löst samma problem som du har.</p>
<p>Hittar du fortfarande inte svar på din fråga så<a href="http://kundo.se/org/trafiklabse/">skriv ett eget inlägg på forumet</a>så hjälper vi dig.</p>
