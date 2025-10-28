---
title: "Använda Trafiklab.se"
weight: 10
layout: "single"
sidebar: true
aliases:
  - "/hur-gor-jag"
  - "/docs/using-trafiklab/creating-a-project"
  - /docs/using-trafiklab/getting-api-keys/
  - /docs/using-trafiklab/upgrading-api-keys/
  - /docs/using-trafiklab/getting-started/
  - /docs/using-trafiklab/creating-an-account/
  - /docs/using-trafiklab/projects/
  - /docs/using-trafiklab/api-keys/
---

## Kom igång

All data på Trafiklab tillhandahålls kostnadsfritt för alla som är intresserade. Vi behöver dock säkerställa att tjänsterna är tillförlitliga för alla användare,
och hålla våra egna kostnader under kontroll. För att göra detta begränsar vi antalet förfrågningar till varje tjänst genom API‑nycklar och kvoter.

{{% info %}} Alla API:er kräver inte en API‑nyckel. När ingen API‑nyckel behövs kan du hoppa över hela den här guiden och använda API:et direkt utan konto, projekt eller nycklar. {{% /info %}}

För att få API‑nycklar behöver du följa dessa steg:
1. Du måste skapa ett konto
2. Du kan skapa ett projekt för att hålla API‑nycklarna strukturerade
3. Du måste skapa en API‑nyckel

Följande avsnitt guidar dig genom processen för att skapa konto och hjälper dig att komma igång med ditt första projekt och dina första API‑nycklar.

## 1. Skapa ett konto

Att skapa ett konto på Trafiklab krävs för att kunna skapa projekt och API‑nycklar.

Börja med att gå till [registreringssidan](https://developer.trafiklab.se/register) eller klicka på knappen "Mitt konto" ovan.

Du behöver fylla i en giltig e‑postadress, ett användarnamn och ett lösenord. Denna e‑postadress används för att kontakta dig om vi gör ändringar
i ett API du använder. Din e‑postadress görs inte offentlig om du inte delar ett projekt med andra användare,
i vilket fall din e‑postadress kommer att vara synlig för de andra medlemmarna i projektet.

Om du har ett GitHub‑konto kan du välja att registrera dig och logga in via GitHub. För att göra det klickar du bara på
knappen "Registrera med GitHub".

![Skärmdump av fälten för e‑postadress och användarnamn](/media/2024/10/developer-trafiklab-se-login.png)

Efter att du fyllt i din information behöver du acceptera användarvillkoren.

Klicka på registreringsknappen längst ned på sidan så får du ett e‑postmeddelande med en länk för att verifiera din e‑postadress.
Efter verifiering är du redo att skapa ditt första projekt.

## 2. Skapa ett projekt

Efter inloggning omdirigeras du till [din projektsida](https://developer.trafiklab.se/project/list) där du
kan skapa ditt allra första projekt. För att göra detta klickar du på den lila knappen "New project" uppe till höger och fyller i
ett bra namn, projekttyp och en kort beskrivning av ditt nästa projekt. Du kan också lägga till valfri information som webbplats och
öppen källkods‑repo. Tryck på spara‑knappen.

Om du behöver ändra några detaljer senare klickar du bara på redigeringsknappen uppe till höger.

### Projekt med flera användare

Du kan lägga till eller ta bort användare i ett projekt genom att kontakta Trafiklab‑teamet på info@trafiklab.se

Längst ned på sidan ser du alla användare som är kopplade till projektet. En användare kan ha en av tre olika behörighetsnivåer:
* **Read Only**: Användaren har åtkomst till projektets innehåll men kan inte göra några ändringar
* **Read/Write**: Användaren har samma behörighet som Read Only men med möjlighet att ändra innehåll, t.ex. API‑nycklar
* **Project Owner**: Användaren har samma behörighet som Read/Write samt möjlighet att ta bort projekt och hantera projektmedlemmar

## 3. Skapa API‑nycklar

Efter att du skapat ditt projekt kan du börja lägga till API‑nycklar. Välj vilka API:er du vill använda i rullgardinslistan och
klicka på knappen "Add API key to project". Oroa dig inte om du fortfarande är osäker på vilka du behöver – du kan komma
tillbaka och lägga till eller ta bort nycklar och andra inställningar när som helst.

För att skapa en API‑nyckel går du till projektet och väljer vilket API som ska läggas till. Varje API kan bara läggas till en gång per
projekt.

![Alternativet för ny nyckel](/media/2024/10/developer-trafiklab-se-add-key.png "Rullgardinsmenyn 'add key'")

Nycklar skapas med en standardprofil som låter dig testa API:et och bygga applikationer för hemmabruk. Om du behöver
fler API‑anrop än vad som tillåts i standardprofilen kan du skapa en begäran om att uppgradera nyckeln utan kostnad.

{{% page-ref page="/api/" %}}

## 4. Uppgradera API‑nycklar

När din applikation behöver fler API‑anrop än vad kvoten för din API‑nyckel tillåter kan du uppgradera dina nycklar till en högre nivå.
Att uppgradera API‑nycklar är helt kostnadsfritt och behövs bara för att säkerställa att alla Trafiklab‑användare kan fortsätta använda
tjänsten gratis.
![Skärmdump av en API‑nyckel med uppgraderingslänk](/media/2024/10/developer-trafiklab-se-key.png "Uppgraderingsknappar kan ses för nycklar som kan uppgraderas")

För att uppgradera din API‑nyckel går du till ditt projekt och klickar på knappen "Upgrade quota" bredvid den API‑nyckel som
du vill uppgradera.

![Skärmdump av dialogrutan för nyckeluppgradering](/media/2024/10/developer-trafiklab-se-key-upgrade.png "Formuläret för begäran om nyckeluppgradering")

Fyll i begäran genom att välja vilken nivå du vill ha i rullgardinslistan och skriv en motivering.
Din motivering bör innehålla:

* En kort beskrivning av projektet
* En uppskattning av hur många förfrågningar du kommer att behöva
* Hur många användare/resenärer som kommer att använda din applikation

Din begäran godkänns inom en till två arbetsdagar. Om din begäran avslås, eller om mer information behövs,
kommer du att få e‑post till din registrerade e‑postadress. Du kan se alla dina väntande och stängda begäranden på sidan "Mina
nyckeluppgraderingar" under Projekt & Nycklar.

### Begäran som inte kommer att godkännas

Vi strävar efter att erbjuda transportdata till så många användare som möjligt. I vissa fall kan dock din uppgraderingsbegäran nekas.
Följande begäran kommer alltid att nekas:

* **Silver eller högre för avgångstavlor som används i Magic Mirror och andra icke‑offentliga projekt.** Anledningen är
  att bronsnivån erbjuder tillräckligt med API‑anrop för att visa nästa avgångar hela dagen. Bättre kodning är mer
  effektivt än att polla ett API var 30:e sekund eller
  minut. [Se Justera uppdateringsfrekvensen under dagen ](./../using-trafiklab-data/best-practices/limiting-requests.md#adjusting-the-update-frequency-during-the-day)
  i våra best practices för att lära dig hur du kan göra detta.
* **Uppgraderingar av reseplanerings‑API:er i syfte att få fram analyser som isokronkartor och restider mellan alla städer,
  alla aktuella förseningar.** Vi vill att du använder rätt verktyg för uppgiften. Vi kommer att neka alla begäranden där målet är att
  skrapa API‑resultat för att bygga analyser. Som tumregel, om du behöver göra mer än 10 förfrågningar för att få fram
  den data du behöver, bör du i stället
  [använda GTFS och GTFS‑RT](../../public-transport-data/our-data-and-apis/gtfs/). Resultatet blir bättre analyser som dessutom
  tar kortare tid att generera – en win‑win.
* **Stresstester m.m.** är inte tillåtna och kommer aldrig att godkännas. Kontakta oss om du har särskilda behov för din applikation.
