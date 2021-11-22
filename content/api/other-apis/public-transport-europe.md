---
title: Public transport data in Europe
layout: single 
weight: "1"
---
If you're interested in data outside of sweden, this list will help you get on track in finding other publishers.

## National Access Points (NAPs)

|Country|National Access Point|
|----|----|
|🇦🇹 Austria | https://www.mobilitydata.gv.at/ |
|🇧🇪 Belgium | https://www.transportdata.be/en/ |
|🇧🇬 Bulgaria | https://lima.api.bg/ |
|🇭🇷 Croatia | https://www.promet-info.hr/ |
|🇨🇾 Republic of Cyprus | http://www.traffic4cyprus.org.cy/ |
|🇨🇿 Czech Republic | https://data.gov.cz/datov%C3%A9-sady |
|🇩🇰 Denmark | https://nap.vd.dk/ |
|🇪🇪 Estonia | http://www.peatus.ee/|
|🇫🇮 Finland | http://www.finap.fi/ |
|🇫🇷 France | https://transport.data.gouv.fr/ |
|🇩🇪 Germany | https://service.mdm-portal.de/ |
|🇬🇷 Greece | http://www.nap.gov.gr/ |
|🇭🇺 Hungary | https://napportal.kozut.hu/ |
|🇮🇪 Ireland | https://data.gov.ie/ |
|🇮🇹 Italy | http://www.cciss.it/ |
|🇱🇻 Latvia | https://lvceli.lv/en/road-network/statistical-data/transport-sector-open-data/|
|🇱🇹 Lithuania | http://www.visimarsrutai.lt/gtfs |
|🇱🇺 Luxembourg | https://data.public.lu/en/ |
|🇲🇹 Malta | http://news.transport.gov.mt/data/ |
|🇳🇱 Netherlands | https://ndovloket.nl/ |
|🇳🇴 Norway | https://transportportal.atlas.vegvesen.no/no/|
|🇵🇱 Poland | https://dane.gov.pl/pl/dataset/1739,krajowy-punkt-dostepowy-kpd-multimodalne-usugi-informacji-o-podrozach |
|🇵🇹 Portugal | https://nap-portugal.imt-ip.pt/   |
|🇷🇴 Romania | |
|🇸🇰 Slovakia | https://odoprave.info |
|🇸🇮 Slovenia | https://www.ncup.si/en/multimodal |
|🇪🇸 Spain | https://nap.mitma.es/ |
|🇨🇭 Switzerland | https://opentransportdata.swiss/en/ |
|🇸🇪 Sweden | http://www.trafficdata.se/ |

Source:
https://ec.europa.eu/transport/sites/default/files/its-national-access-points.pdf

## GTFS and NeTEx data

|Country|Provider/Attribution|License|GTFS|NeTEx|Comments|
|----|----|----|----|----|----|
|🇧🇪 Belgium|[NMBS/SNCB](https://nmbs.be), [MIVB](https://stip-mivb.be)|Contract (NMBS), custom license (MIVB) |[Registration page NMBS](https://www.belgiantrain.be/en/3rd-party-services/mobility-service-providers/public-data), [Registration page MIVB](https://opendata.stib-mivb.be/store/data)|[Registration page](https://www.belgiantrain.be/en/3rd-party-services/mobility-service-providers/public-data)|Signed contract required for NMBS GTFS data. NeTEx according to Belgian Epip profile.|
|🇩🇰 Denmark|[Rejseplanen](https://rejseplanen.dk)| |[gtfs.zip](http://www.rejseplanen.info/labs/GTFS.zip)| | Account required for developer portal access | 
|🇪🇪 Estonia|[Transpordiamet](https://www.mnt.ee/eng/public-transportation/public-transport-information-system)| |[gtfs.zip](https://peatus.ee/gtfs/gtfs.zip)| | |
|🇫🇮 Finland| | | [National Access Point, regional feeds](https://finap.fi/#/services) | [National Access Point, regional feeds](https://finap.fi/#/services) | |
|🇫🇷 France| | |[Open Data Portal, regional feeds](https://navitia.opendatasoft.com/explore/?sort=modified&q=&refine.geographicarea=France)| | |
|🇩🇪 Germany|[DELFI](https://opendata-oepnv.de)|CC-BY 4.0|[Registration page](https://www.opendata-oepnv.de/ht/de/organisation/delfi/startseite?tx_vrrkit_view%5Bdataset_name%5D=deutschlandweite-sollfahrplandaten-gtfs&tx_vrrkit_view%5Baction%5D=details&tx_vrrkit_view%5Bcontroller%5D=View)|[Registration page](https://www.opendata-oepnv.de/ht/de/organisation/delfi/startseite?tx_vrrkit_view%5Bdataset_name%5D=deutschlandweite-sollfahrplandaten&tx_vrrkit_view%5Bdataset_formats%5D%5B0%5D=ZIP&tx_vrrkit_view%5Baction%5D=details&tx_vrrkit_view%5Bcontroller%5D=View)| The GTFS feed covers ~75% of all public transportation (as of 4/2020), mainly because some regional providers are not included. If this is insufficient for you, consider using the NeTEx feed, which has a higher coverage, or manually combine available regional feeds. Account required.|
|🇮🇪 Ireland|[Transport for Ireland](https://www.transportforireland.ie/transitData/PT_Data.html)|CC-BY 4.0|[gtfs.zip](https://www.transportforireland.ie/transitData/google_transit_combined.zip)||
|🇱🇻 Latvia|Rīgas Satiksme| | [gtfs.zip](http://saraksti.rigassatiksme.lv/riga/gtfs.zip) | | |
|🇱🇹 Lithuania|[Visimarsrutai](https://www.visimarsrutai.lt/gtfs/)| |[gtfs.zip](https://www.visimarsrutai.lt/gtfs/gtfs_all.zip)||
|🇳🇱 Netherlands|[OpenOV, Nationaal Toegangspunt ITS](https://nt.ndw.nu/#/settings/multimodaal-reisinformatie-overview/1)|CC0|[gtfs-openov-nl.zip](http://gtfs.openov.nl/gtfs-rt/gtfs-openov-nl.zip)
|🇳🇴 Norway|[Entur](https://developer.entur.no)|NLOD|[rb_norway-aggregated-gtfs.zip](https://storage.googleapis.com/marduk-production/outbound/gtfs/rb_norway-aggregated-gtfs.zip)|[rb_norway-aggregated-netex.zip](https://storage.googleapis.com/marduk-production/outbound/netex/rb_norway-aggregated-netex.zip)|

Sources:

- https://eu.data.public-transport.earth/
- https://github.com/public-transport/european-transport-operators

### In cooperation with Interreg

This page has been created in cooperation with Stronger Combined, a project by the European Regional Development Fund.

![Stronger Combined, InterReg logo](/media/2021/09/stronger-combined-interreg.png)