# Converting SWEREF99 to WGS84

The old trafikverkets API, and some other Swedish datasets as well, make use of the SWEREF99 coordinate system. This is
Swedens national coordinate system, and can only be used in and around Sweden. In order to use these coordinates
together with software that works with the WGS84 coordinate system, or in order to combine data with other data that
uses the WGS84 coordinate system, conversion is needed.

### Libraries

There are multiple libraries which you can use to convert coordinates from SWEREF99 to WGS84:

* .Net - [MightyLittleGeodesy](https://github.com/bjornsallarp/MightyLittleGeodesy)
* Java - [CoordinateTransformationLibrary](https://github.com/goober/coordinate-transformation-library)
* PHP - [CoordinateTransformationLibrary](https://github.com/david-xelera/CoordinateTransformationLibrary)
* JavaScript - [latlong.mellifica.se](http://latlong.mellifica.se)

Check the licenses and don't forget to give credit where credit is due when using one of them.

### Further reading

You can read more about SWEREF99
at [lantmäteriverkets website \(Swedish\)](https://www.lantmateriet.se/sv/Kartor-och-geografisk-information/gps-geodesi-och-swepos/Referenssystem/Tredimensionella-system/SWEREF-99/) [\(English\)](https://www.lantmateriet.se/en/maps-and-geographic-information/gps-geodesi-och-swepos/Referenssystem/Tredimensionella-system/SWEREF-99/)
or on [Wikipedia \(Swedish\)](http://sv.wikipedia.org/wiki/SWEREF_99).

