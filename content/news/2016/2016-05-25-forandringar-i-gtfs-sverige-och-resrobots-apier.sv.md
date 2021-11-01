---
title: Förändringar i GTFS Sverige och ResRobots APIer
date: 2016-05-25
aliases:
  - "/post/144899868373/förändringar-i-gtfs-sverige-och-resrobots-apier"
draft: true

---

**Äntligen produktionssätter Samtrafiken sin nya Riksdatabas för Nationell Trafikinformation! Den nya Riksdatabasen ligger hos en ny leverantör ([IVU](http://www.ivu.com/)) och förändringen påverkar flera flöden hos Samtrafiken. På Trafiklab påverkas GTFS Sverige och Resrobot’s APIer. Nedan följer information om hur APIerna på Trafiklab påverkas.**
**GTFS Sverige byts ut mot GTFS Sverige 2**
Den första juni kommer GTFS Sverige 2 att produktionssättas. Det nya APIet har funnits som betaversion på Trafiklab under en tid, men i och med produktionssättningen går det att gå över till det nya extraktet för skarpa tjänster. Både det nya och det gamla APIerna för GTFS kommer att finnas tillgängliga i produktion fram till den 30 augusti.
Ni som använder GTFS-extraktet måste övergå till att använda det nya GTFS extraktet GTFS Sverige 2 innan 30 augusti för att säkerställa att era tjänster har uppdaterad information. För GTFS Sweden 2 behövs en ny nyckel som man hämtar på Trafiklab som vanligt. Se till att lägga till APIet GTFS Sweden 2 i det projekt ni använder för att kunna hämta en nyckel.
**Nytt versionstillägg i ResRobot – Reseplanerare och Stolptidstabeller 2. **
ResRobot - Reseplanerare och Stolptidtabeller 2 kommer från den 1 juni att kunna anropas med ett versionstillägg **/v2** i anropet. Anropet blir till exempel [https://api.resrobot.se/v2/trip](https://api.resrobot.se/v2/trip) istället för  nuvarande [https://api.resrobot.se/trip. ](https://api.resrobot.se/trip.%C2%A0)
Ingen ny nyckel behövs för att anropa v2-versionen. Den 1 juni till den 30 augusti kommer både det gamla anropet och det nya anropet med versionstillägget att fungera. Under övergångsperioden fördubblas antalet anrop som är tillåtna per nyckel då anropen till bägge versionerna räknas ihop i statistiken. 30 augusti återgår nycklarnas anropsnivåer till tidigare nivåer.
I den nya versionen av APIet kommer vissa koder och texter att förändras marginellt (mer information om detta finns i dokumentationen för APIerna på Trafiklab). Den enskilda största förändringen är dock att hållplatsid nu blir nio-ställiga. Om hållplatsid finns hårdkodat i en tjänst kan detta ställa till problem.
Konvertering sker genom att lägga till 00 på position 3 och 4 efter landsnumret, till exempel så blir 7412345 (gammalt hållplatsid) i den nya versionen av APIet 740012345.
**Support**
Om du har frågor eller stöter på problem under övergången kan du alltid [kontakta oss](https://kundo.se/org/trafiklabse/).
På vår kommande meetup den 2 juni kommer vi också berätta om dessa förändringar och det finns möjlighet att ställa frågor till oss som jobbar med Trafiklab. [Läs mer och anmäl dig här](http://blogg.trafiklab.se/post/144597997813/fullsp%C3%A4ckad-agenda-p%C3%A5-kommande-meet-up-med).
 
