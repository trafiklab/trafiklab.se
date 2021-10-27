---
title: Trafikverket Öppet API 
layout: "single"
weight: 90 
summary: Aktuell trafikinformation från Trafikverket om både tåg- och vägtrafik.
date: 06-02-2014
---
<p>Strukturen skiljer sig en hel del från andra APIer på Trafiklab. Hämtning av data görs med ett HTTP-anrop. En fråga skickas med i POST-metoden som beskriver vilket data som efterfrågas samt innehållandes eventuella filter.</p>

<p><strong>Dataformat</strong></p>

<p>XML eller JSON, anges via suffix.</p>

<p>Om något värde saknas i svaret returneras inte detta element i svaret.</p>



<p><strong>API Nyckel</strong></p>

<p>Det krävs en giltig API nyckel som skickas med anropet. En API nyckel får man genom att skapa ett projekt som använder detta API.<a href="http://www.trafiklab.se/apis/dokumentation/nycklar">Mer om hur du skapar och använder API nycklar hittar du här</a>. För att få en API nyckel så måste man godkänna APIets<a href="http://www.trafiklab.se/apis/trafikverket-trainexport-api/dokumentation-trafikverket-trainexport#api-license">licensvillkor</a>.</p>

<p><strong>Metoder</strong></p>

<p>Hämtning av data görs med ett HTTP-anrop. En fråga skickas med i POST-metoden som beskriver vilket data som efterfrågas samt innehållandes eventuella filter. Frågan måste även inkludera en giltig API-nyckel.</p>

<p>Tillgängliga datatyper är:</p>

<p><strong>TrainMessage</strong> - Tågtrafikmeddelande, exempelvis information kring banarbete, tågfel, anläggningsfel och dylikt.</p>

<p><strong>TrainStation</strong> - Trafikplatser, både med och utan resandeutbyte.</p>

<p><strong>TrainAnnouncement</strong> - Tidtabellsinformation, d.v.s information om tåg på trafikplatser (stationer, hållplatser) varje post motsvarar ett visst tåg vid respektive trafikplats.Innehåller inte godståg.</p>

<p><strong>Icon</strong>- Ikoner, exempelvis för användning i grafiska användargränssnitt och kartor.</p>

<p><strong>    RoadCondition</strong>– Väglag</p>

<p><strong>RoadConditionOverview</strong>– Väglagsöversikter</p>

<p><strong>    Situation</strong>- Situationer innehållandes händelser och störningar, exempelvis: Viktig information, Olyckor, Bärighetsnedsättning, Evenemang, Avvikande färjetider, Kolonnkörning, Kövarning, Oförutsedda hinder, Vägarbete.</p>

<p><strong>    WeatherStation</strong>- Väderstationer med mätdata</p>

<p><strong>Koordinatsystem</strong></p>

<p>Trafikverket använder sig av det svenska nationella koordinatsystemet SWEREF 99 TM. All geometridata publiceras dock även i koordinatsystemet WGS 84.<em></em></p>

<p><strong>Detaljerad dokumentation</strong></p>

<p>Detaljerad dokumentation hittar du på Trafikverkets informationssida för API:et, se nedan.</p>

<p>Den detaljerade dokumentationen innehåller bland annat information om:</p>

<ul>
	<li>uppbyggnad av frågan som bifogas anropet</li>
	<li>svarets utformning</li>
	<li>felmeddelanden</li>
	<li>tillgänglig datamodell</li>
	<li>exempelkod och vanliga användningsfall</li>
	<li>en API-konsol för testkörning</li>
</ul>

<p>Observera att du som är Trafiklabs-medlem <strong>INTE</strong> behöver registrera dig på Trafikverkets sida utan kan hämta en nyckel direkt här på Trafiklab.</p>

<p>För mer information se ”<a href="http://api.trafikinfo.trafikverket.se/">Trafikverkets öppna API för trafikinformation</a>”</p>


