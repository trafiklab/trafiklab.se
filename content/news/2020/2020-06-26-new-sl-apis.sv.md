---
title: Nytt SL-API ”Kollektivtrafikinformation Region Stockholm” ersätter dagens 7 SL-API:er på Trafiklab 
date: 2020-06-26 
image: /media/2020/06/sl-inverse.jpg
---

**Det nya SL-API:et har försenats till Q1 2021. Vi uppdaterar dig när vi vet mer.**

SL lanserade sina första öppna API:er 2014 och i dag finns det 7 API:er vars funktionalitet successivt har
utökats. Tjänsterna har använts flitigt, och SL har fått värdefull återkoppling som har använts som en del av
underlaget för utformningen av det nya öppna SL-API:et.

Ledorden vid utformningen av det nya API:et har varit enkelhet, konsekvens, standardisering och större omfattning. Det nya
SL-API:et ersätter de nuvarande 7 API:erna och erbjuder en enhetlig datamodell genom hela API:et.

Du behöver inte längre veta att Slussen har id 9192 för att hitta nästa avgång. Sök bara på
Slussen så får du nästa avgång, avvikelser och de aktuella linjerna. Sökningen kan göras för hela stationen eller
för en enskild hållplatsposition.

API:et är RESTful och stöder [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS), vilket ger enklare felhantering och
navigering i informationen.

API:ets struktur är framtidssäker och gör det enklare att lägga till trafikinformation som entréer,
fordonspositioner med mera. Dokumentation och versionshantering förbättras också – du behöver inte hämta en ny nyckel
för varje ny version av API:et.

Sammanfattning:

- API:ets funktioner
    - Reseplanering
    - Hållplatsområden och linjer
    - Avvikelser
    - Nästa avgång
    - Autokomplettering
- RESTful (med stöd för HATEOAS)
- Enhetlig datamodell
- Förbättrad dokumentation
- Mer precisa och standardiserade felmeddelanden
- En enda API-nyckel oavsett endpoint eller API-version
- Möjliggör snabbare förändringar i applikationer som använder API:et

Applikationer som i dag använder SL:s API:er kan migreras under en övergångsperiod på 4 månader då
dessa API:er finns parallellt med det nya SL-API:et. Därefter är endast det nya SL-API:et tillgängligt.

Vi håller dig uppdaterad med mer information om tidplanen för det nya SL-API:et, dess parametrar och
motsvarande svarsdata. Har du frågor är du välkommen att kontakta Trafiklab via Kundo
på [support.trafiklab.se](https://support.trafiklab.se).
