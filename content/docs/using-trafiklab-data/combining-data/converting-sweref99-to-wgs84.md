---
title: Converting SWEREF99 to WGS84 
aliases: 
  - /konvertering-swref99-wgs84
---

The old trafikverkets API, and some other Swedish datasets as well, make use of the SWEREF99 coordinate system. This is
Swedens national coordinate system, and can only be used in and around Sweden. In order to use these coordinates
together with software that works with the WGS84 coordinate system, or in order to combine data with other data that
uses the WGS84 coordinate system, conversion is needed.

## Converting SWEREF99 to WGS84

In order to convert SWEREF99 coordinates to WGS84, a Gauss-Kreuger projection is used.

The following parameters are used when converting to/from `sweref 99 tm`:

```text
axis = 6378137;
flattening = 003352810681182319D;
central_meridian = 15;
scale = 0.9996D;
false_northing = 0;
false_easting = 500000;
```

The complete projection looks like this

```text
e2 = this.flattening * (2 - this.flattening)
n = this.flattening / (2 - this.flattening)
a_roof = this.axis / (1 + n) * (1 + n * n / 4 + n * n * n * n / 64)
delta1 = n / 2 - 2 * n * n / 3 + 37 * n * n * n / 96 - n * n * n * n / 360
delta2 = n * n / 48 + n * n * n / 15 - 437 * n * n * n * n / 1440
delta3 = 17 * n * n * n / 480 - 37 * n * n * n * n / 840
delta4 = 4397 * n * n * n * n / 161280
Astar = e2 + e2 * e2 + e2 * e2 * e2 + e2 * e2 * e2 * e2
Bstar = -(7 * e2 * e2 + 17 * e2 * e2 * e2 + 30 * e2 * e2 * e2 * e2) / 6
Cstar = (224 * e2 * e2 * e2 + 889 * e2 * e2 * e2 * e2) / 120
Dstar = -(4279 * e2 * e2 * e2 * e2) / 1260
deg_to_rad = 017453292519943295D
lambda_zero = this.central_meridian * deg_to_rad
xi = (x - this.false_northing) / (this.scale * a_roof)
eta = (y - this.false_easting) / (this.scale * a_roof)
xi_prim = xi - delta1 * sin(2 * xi) * cosh(2 * eta) - delta2 * sin(4 * xi) * cosh(4 * eta) - delta3 * sin(6 * xi) * cosh(6 * eta) - delta4 * sin(8 * xi) * cosh(8 * eta)
eta_prim = eta - delta1 * cos(2 * xi) * sinh(2 * eta) - delta2 * cos(4 * xi) * sinh(4 * eta) - delta3 * cos(6 * xi) * sinh(6 * eta) - delta4 * cos(8 * xi) * sinh(8 * eta)
phi_star = Math.asin(sin(xi_prim) / cosh(eta_prim))
delta_lambda = atan(sinh(eta_prim) / cos(xi_prim))
lon_radian = lambda_zero + delta_lambda
lat_radian = phi_star + sin(phi_star) * cos(phi_star) * (Astar + Bstar * sin(phi_star)^2 + Cstar * sin(phi_star)^4 + Dstar * sin(phi_star)^6)
longitude = lat_radian * 180 / 3.141592653589793D
latitude = lon_radian * 180 / 3.141592653589793D
```

Since this conversion is quite complicated, we recommend you use a library to do the heavy lifting.

### Libraries

There are multiple libraries which you can use to convert coordinates from SWEREF99 to WGS84:

* .Net - [MightyLittleGeodesy](https://github.com/bjornsallarp/MightyLittleGeodesy)
* Java - [CoordinateTransformationLibrary](https://github.com/goober/coordinate-transformation-library)
* PHP - [CoordinateTransformationLibrary](https://github.com/david-xelera/CoordinateTransformationLibrary)
* JavaScript - [latlong.mellifica.se](http://latlong.mellifica.se)

Check the licenses and don't forget to give credit where credit is due when using one of them.

### Further reading

You can read more about SWEREF99
at [lantmäteriverkets website (Swedish)](https://www.lantmateriet.se/sv/Kartor-och-geografisk-information/gps-geodesi-och-swepos/Referenssystem/Tredimensionella-system/SWEREF-99/) [(English)](https://www.lantmateriet.se/en/maps-and-geographic-information/gps-geodesi-och-swepos/Referenssystem/Tredimensionella-system/SWEREF-99/)
or on [Wikipedia (Swedish)](http://sv.wikipedia.org/wiki/SWEREF_99).
