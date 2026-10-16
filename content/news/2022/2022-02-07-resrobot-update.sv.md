---
title: "Resrobot uppdateras till 2.1 med ändringar som inte är bakåtkompatibla"
date: "2022-02-07"
image: /media/2021/10/ResRobot-header.png 
image_credit: Samtrafiken
---

Vårt Resrobot-API har fått en välförtjänt uppdatering! Efter mer än 6 år med Resrobot 2.0 finns nu Resrobot 2.1
tillgängligt. Underhållsuppdateringen fokuserar på uppdateringar av plattformens backend och åtgärdar flera buggar. Till
exempel har den långlivade buggen med svarshuvudet HTTP content-encoding åtgärdats, vilket bör göra API:et enklare att
använda med standardverktyg och bibliotek.

Nackdelen är att vi inte kunde undvika vissa ändringar som inte är bakåtkompatibla, till exempel ny bas-URL och nya
API-nycklar, några ändrade standardparametrar och något förändrade svarsstrukturer. Vi har tagit fram en
migreringsguide som beskriver alla ändringar i anrops- och svarsformaten, tillsammans med en kort repetition av hur du
lägger till de nya API-nycklarna i dina befintliga projekt.

På grund av tekniska problem blir endpoints för närliggande hållplatser och hållplatsuppslag tyvärr tillgängliga först den
24 mars 2022. Migreringsguiden och den uppdaterade dokumentationen finns redan, så den som vill kan sätta sig in i de nya
specifikationerna redan nu, innan dessa endpoints finns på plats.

## Tidplan 

De två versionerna fungerar parallellt fram till den 30 juni 2022, då de nuvarande Resrobot-API:erna stängs ner. Se till
att uppdatera ditt projekt före detta datum.

## Använder du vårt SDK?

Om du använder [vårt Resrobot PHP SDK](https://github.com/trafiklab/resrobot-php-sdk) behöver du bara uppdatera
SDK-versionen i din applikation för att börja använda den nya versionen. Vårt mål är att göra dessa SDK:er tillgängliga i
fler programspråk i framtiden.

Om du har fler frågor, tveka inte att kontakta oss på [info@trafiklab.se](mailto:info@trafiklab.se) eller att
skapa ett supportärende på [support.trafiklab.se](https://support.trafiklab.se).

Med vänliga hälsningar, Team Trafiklab

