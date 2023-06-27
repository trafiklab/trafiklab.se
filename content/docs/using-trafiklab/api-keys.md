---
title: "API keys"
weight: 50
aliases:
  - /docs/using-trafiklab/creating-api-keys/
  - /docs/using-trafiklab/upgrading-api-keys/
---

## Creating API keys

In order to create an API key, navigate to the project and select the API to add. Every API can only be added once to a
project.

![The new key option](/media/2023/create-API-key.png)

Keys are created with a default profile, allowing you to test the API and build applications for home use. If you need
more API requests than allowed in the standard profile, you can create a request to upgrade the key for free.

## Upgrading API keys

When your application needs more API calls than your API key quota allow, you can upgrade your keys to a higher level.
Upgrading API keys is completely free of charge, and only needed to ensure all Trafiklab users can keep using the
service for
free.
![Screenshot of an api key with an upgrade link](/media/2023/upgrade-quota.png)

In order to upgrade your API key, go to your project and click on the "Upgrade quota" button next to the API key that
you want
to upgrade.

![Screenshot of the key upgrade dialog](/media/2023/request-key-upgrade.png)

Fill out the request form by choosing which level you would like to have from the dropdown and write a motivation. 
Your motivation should include:

* A short description of the project
* An estimate of the number of requests your will need
* How many users/travelers will use your application

Your request will be approved within one or two workdays. If your request is declined, or if more information is needed,
you will receive email on your registered email address. You can see all your pending and closed requests on the page "My 
key upgrades" under Projects & Keys.

### Requests which will not be approved

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

{{% page-ref "frequently-asked-questions" %}}