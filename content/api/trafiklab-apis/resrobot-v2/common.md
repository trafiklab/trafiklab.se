---
title: ResRobot data types 
weight: 990
---

The different ResRobot API endpoints have different response structures, but some parts of the response are shared among
all endpoints. In order to ensure that all documentation is correct, and to be able to go more into detail, we have
collected these common data types here.

{{% warning %}}
**New version available**

A new version, version 2.1, of ResRobot is available. Existing apps should migrate to the new version,
and it is no longer possible to build new apps on version 2.0.

**Version 2.0, which you are currently looking at, will be discontinued at June 30th, 2022.**   
{{% /warning %}}

## Product

{{% tabs %}}
{{% tab "json" %}}
```json
"Product": {
  "name": "Regional Tåg 231",
  "num": "231",
  "catCode": "2",
  "catOutS": "JRE",
  "catOutL": "Regional Tåg",
  "operatorCode": "74",
  "operator": "SJ",
  "operatorUrl": "http://www.sj.se"
},
```
{{% /tab %}}
{{% tab "xml" %}}
```xml
<Product catCode="7" 
         catOutL="Länstrafik - Buss" 
         catOutS="BLT" 
         name="Länstrafik - Buss Grön X" 
         num="Grön X" operator="Västtrafik"
         operatorCode="279" 
         operatorUrl="http://www.vasttrafik.se/"/>
```
{{% /tab %}}
{{% /tabs %}}

| **Name**              | **Data type**           | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ----------------------- | ----------------------|
| Product.name          | String                  | catOutL + num |
| Product.num           | String                  | Line or train number |
| Product.operator      | String                  | Operator name. For example: “SL”, ”Skånetrafiken”.                                                                                                                                                                                                                                                                                                                      | |
| Product.catOutS       | String                  | Transport type code, see below  |
| Product.catOutL       | String                  | Category name <br>Example: "Buss", "Tåg", "Intercity", "Tunnelbana", "Arlanda Express","Regional","InterCity", ”PågaTåg”                                                                                                                                                                                                                                              |
| Product.catCode       | Integer                 | Category code, identical to catOutS                                           |
| Product.operator      | String                  | Operator name. For example: “SL”, ”Skånetrafiken”.                                                                                                                                                                                                                                                                                                                      | |
| Product.operatorCode  | String                  | Operator code. For example: “256”, "289".

### Response product categories

{{% warning %}}
**Careful!**

Request category codes for filtering differ from response category codes. These are response product category codes. Request category codes are described in the next section.
{{% /warning %}}

**String representation**

|Abbreviation| Name|
| ------------------- | ----------------------|
|BLT | Regional bus |
|BXB | Express bus |
|ULT | Metro |
|JAX | Arlanda Express |
|JLT | Local train |
|JRE | Regional train |
|JIC | InterCity train |
|JPT | PågaTåg |
|JEX | Express train |
|SLT | Tram |
|FLT | Lokal ferry |
|FUT | International ferry |

**Numeric representation**

|Name| Numeric value|
| ------------------- | ----------------------|
|High speed trains, Snabbtåg, Arlanda Express|1|
|Regional trains, InterCity trains|2| 
|Express busses, Flygbussar|3| 
|Local trains Tåg, PågaTåg, Öresundståg|4| 
|Metro, such as tunnelbanan|5| 
|Tram such as Spårvagn, Tvärbanan | 6|
|Busses| 7|
|Ferries and international ferries | 8|
|Taxi|9|

### Request product category codes

{{% warning %}}
**Careful!**

Request category codes for filtering differ from response category codes. These are request product category codes. Response category codes are described in the section above.
{{% /warning %}}

|Name| Numeric value|
| ------------------- | ----------------------|
|Air traffic|1|
|High speed trains, Snabbtåg, Arlanda Express|2|
|Local trains Tåg, PågaTåg, Öresundståg|4|
|Express busses, Flygbussar|8|
|Regional trains, InterCity trains|16|
|Metro, such as tunnelbanan|32|
|Tram such as Spårvagn, Tvärbanan |64|
|Busses|128|
|Ferries and international ferries |256|
|Taxi|512|

In order to select multiple products, these values can be added up.