---
title: "Upgrading API keys"
weight: 50
---
When your application needs more API calls than your API key quota allow, you can upgrade your keys to a higher level.
Upgrading API keys is completely free, and only needed to ensure all Trafiklab users can keep using the service for
free.

{{% warning %}}  Disable browser plugins like Google Translate when creating a project. They are known to
cause issues on the developer portal, when logging in, creating accounts and creating projects. {{% /warning %}}

![Screenshot of an api key with an upgrade link](/media/2020/05/key-visible.png)

In order to upgrade your API key, click the "Uppgradera" link and fill out the form.

![Screenshot of the key upgrade dialog](/media/2020/05/upgrade-key.png)

Change the level you'd like from the dropdown list. Write a motivation below. Your motivation should include:

* A short description of the project
* An estimate of the number of requests your will need
* How many users/travelers will use your application

Your request will be approved within one or two workdays. If your request is declined, or if more information is needed,
you will receive email on your registered email address.

### Requests which will not approved

We aim to offer transport data to as many users as possible. However, in some cases your upgrade request may be denied.
The following requests will always be denied:

* **Silver or higher for departure boards used in Magic Mirror and other non-public projects.** The reason for this is
  that the bronze level offers enough API calls to show the next departures all day long. Better coding is more
  effecient than polling an API every 30 seconds or
  minute. [See Adjusting the update frequency during the day ](./../using-trafiklab-data/best-practices/limiting-requests.md#adjusting-the-update-frequency-during-the-day)
  in our best practices to learn how you can do this.
* **Upgrades on journey planning APIs in order to get analytics like isochrone maps and travel times between all cities,
  all current delays.** We want you to use the right tool for the job. We will deny all requests where the goal is to
  scrape API results in order to build analytics. As a rule of thumb, if you need to make more than 10 requests in order
  to get the data you need, you should
  be [using GTFS and GTFS-RT instead](../../public-transport-data/our-data-and-apis/gtfs/). As a result, you will be
  able to build better analytics, and they will take less time to generate, so this is a win-win.
* **Stress tests etc** Are not allowed and will never be approved. Ask us if you have special needs for your application.

{{% note %}} Right now, the developer portal is not available in English yet. While these guides should help you to get
started, the following list of common Swedish words should help you to get around on the developer portal.

* **Spara**: Save/Submit
* **Tillbaka**: Back
* **Radera**: Delete
* **Hämta**: Fetch
* **Skapa**: Create
* **Nyckel**: (API) key
* **Nivå**: Level
* **Konto**: Account
  {{% /note %}}

{{% page-ref "frequently-asked-questions" %}}