---
title: ResRobot data types 
weight: 990
date: 2021-10-12
---

The different ResRobot API endpoints have different response structures, but some parts of the response are shared among
all endpoints. In order to ensure that all documentation is correct, and to be able to go more into detail, we have
collected these common data types here.

## Product

{{% note %}}
**Changes compared to ResRobot v2.0:**

- `operatorUrl` is no longer available
- Several fields have been added
{{% /note %}}

{{% tabs %}}
{{% tab "json" %}}
```json
"Product": {
    "name": "Länstrafik - Tåg 40",
    "internalName": "Länstrafik - Tåg 40",
    "displayNumber": "40",
    "num": "40",
    "line": "40",
    "lineId": "1275000000036",
    "catOut": "JLT",
    "catIn": "JLT",
    "catCode": "4",
    "cls": "16",
    "catOutS": "JLT",
    "catOutL": "Länstrafik - Tåg",
    "operatorCode": "275",
    "operator": "SL",
    "admin": "275___",
    "routeIdxFrom": 0,
    "routeIdxTo": 1
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
         />
```
{{% /tab %}}
{{% /tabs %}}

| **Name**              | **Data type**               | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ------------------------- | ----------------------|
| Product.name          | String                  | Public name, matches catOutL + num |
| Product.internalName  | String                  | Internal name, matches catOutL + num|
| Product.displayNumber | String                  | Publicly announced number (train or line number) |
| Product.num           | String                  | Internal product number (e.g. train number) |
| Product.line          | String                  | Publicly announced line name, if available |
| Product.lineId        | String                  | Line id for use in further requests |
| Product.catCode       | Integer                 | Category code, see _Response product categories > Numeric representation_ below |
| Product.cls           | String                  | Category class, same codes as used in requests, see below |
| Product.catIn         | String                  | Transport type code for the vehicle when it arrives, in string format. Typically identical to catOut. |
| Product.catOut        | String                  | Same as catOutS|
| Product.catOutS       | String                  | Transport type code for the vehicle when it departs, in string format. See _Response product categories > String representation_ below. |
| Product.catOutL       | String                  | Transport type name for the vehicle when it departs, depending on language parameter <br>Example: "Buss", "Tåg", "Tunnelbana"                                                                                                                                                                                                                                          |
| Product.operator      | String                  | Operator name. For example: “SL”, ”Skånetrafiken”.                                                                                                                                                                                                                                                                                                                      | |
| Product.operatorCode  | String                  | Operator code. For example: “256”, "289".                                                                                                                                                                                                                                                                                                                      | |

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