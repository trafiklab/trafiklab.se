---
title: Tjuvstart för nytt Reseplanerings-API
date: 2017-06-22
aliases:
  - "/post/162117351103/tjuvstart-för-nytt-reseplanerings-api"
draft: true

---

**Nu finns ett nytt test-API från SL ute på Trafiklab. APIet heter SL Reseplanerare 3 och innehåller ett antal nya funktioner. **
Det nya APIet kommer under sommaren finnas tillgängligt för testkörningar, men först efter sommaren går det in i skarp drift. Detta nya API kommer på sikt att ersätta SL Reseplanerare 2, men i ett första läge kommer det enbart finnas tillgängligt för tester och relativt få anrop per nyckel. För en smidig övergång kommer båda versionerna finnas i skarp drift parallellt under minst 3 månader. Det innebär att SL Reseplanerare 2 kommer släckas tidigast i november 2017. Vi återkommer med exakta tidpunkter efter sommaren.
Nedan beskriver vi några highlights från det nya APIet. Den fullständiga dokumentationen hittar du på [trafiklab.se](http://www.trafiklab.se/). Där kan du även plocka ut en API-nyckel till det nya APIet, ställa frågor och lämna synpunkter. Vi kommer försöka svara på frågor och hantera eventuella fel löpande, men pga semesterledigheter kan det finnas perioder med längre svarstid. 
**Nya möjligheter i Reseplanerare 3**
<ul><li>Mellanliggande hållplatser
För att veta vilka hållplatser som passeras under en resa är man i version 2 tvungen att anropa journeyDetail efter en sökning med trip. Detta är i v3 inte längre nödvändigt, genom att ange passlist=1 fås denna information direkt av trip.</li><li>Detaljerade färdvägar
Även resans detaljerade färdväg i form av geografiska koordinater kan fås direkt av trip/reconstruction/journeyDetail  genom att ange poly=1.</li><li>Prisinformation
I version 3 presenteras de faktiska biljettpriserna för en resa, inte bara som tidigare zon-information.</li><li>Tidigare/senare resor
För att ”skrolla” tidigare och senare resor efter ett sök med trip finns möjligheten att skicka in samma sökning, kompletterat med en skroll-parameter från det tidigare svaret för att få nästkommande eller föregående resor (se api-dokumentation)</li><li>Dela resa
Den nya tjänsten reconstruction gör det enklare att dela ett reseresultat, inte bara en sökning (som kan ge ett annat resultat vid annat tillfälle)</li></ul>
**Nyckelnivå**
Det kommer under sommaren endast finnas en nyckelnivå att tillgå: ”test”. Tillåtna anrop: 5.000 per månad och 15 per minut.
 
