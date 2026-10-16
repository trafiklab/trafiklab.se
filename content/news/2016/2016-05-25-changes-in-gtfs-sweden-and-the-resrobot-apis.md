---
title: "Changes in GTFS Sweden and the ResRobot APIs"
date: 2016-05-25
draft: true

---

**Samtrafiken is finally putting its new national database for national traffic information (Riksdatabasen) into production! The new Riksdatabas is hosted by a new supplier ([IVU](http://www.ivu.com/)) and the change affects several of Samtrafiken's feeds. On Trafiklab, GTFS Sweden and the ResRobot APIs are affected. Below is information about how the APIs on Trafiklab are affected.**

**GTFS Sweden is replaced by GTFS Sweden 2**

On the first of June, GTFS Sweden 2 will be put into production. The new API has been available as a beta version on Trafiklab for some time, but now that it goes into production you can switch to the new extract for live services. Both the new and the old GTFS APIs will be available in production until 30 August.

Those of you who use the GTFS extract must switch to the new GTFS extract GTFS Sweden 2 before 30 August to ensure that your services have up-to-date information. GTFS Sweden 2 requires a new key, which you get on Trafiklab as usual. Make sure to add the GTFS Sweden 2 API to the project you use in order to get a key.

**New version suffix in ResRobot – Reseplanerare and Stolptidstabeller 2.**

From 1 June, ResRobot - Reseplanerare and Stolptidtabeller 2 can be called with a version suffix **/v2** in the request. The request then becomes, for example, [https://api.resrobot.se/v2/trip](https://api.resrobot.se/v2/trip) instead of the current [https://api.resrobot.se/trip](https://api.resrobot.se/trip).

No new key is needed to call the v2 version. From 1 June to 30 August, both the old request and the new request with the version suffix will work. During the transition period, the number of requests allowed per key is doubled, since requests to both versions are added together in the statistics. On 30 August, the keys' request quotas return to their previous levels.

In the new version of the API, some codes and texts will change slightly (more information about this can be found in the documentation for the APIs on Trafiklab). The single biggest change, however, is that stop IDs now have nine digits. If stop IDs are hard-coded in a service, this may cause problems.

Conversion is done by adding 00 at positions 3 and 4 after the country code, for example 7412345 (old stop ID) becomes 740012345 in the new version of the API.

**Support**

If you have questions or run into problems during the transition, you can always [contact us](https://kundo.se/org/trafiklabse/).

At our upcoming meetup on 2 June, we will also talk about these changes, and there will be an opportunity to ask questions to those of us who work with Trafiklab. [Read more and sign up here]({{< relref "/news/2016/2016-05-19-packed-agenda-at-upcoming-meet-up-with-trafiklab.md" >}}).
