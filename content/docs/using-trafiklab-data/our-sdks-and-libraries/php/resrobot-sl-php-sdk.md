---
title: ResRobot PHP SDK
---

We created a PHP SDK to easily use the ResRobot APIs. This way you don't need to worry about making
requests, caching, or parsing responses. All responses are parsed and returned as PHP classes.

## Installation

Installing can be done by using Composer:

`composer require trafiklab/resrobot-php-sdk`

## Requirements

The following software is required to use this SDK:

* PHP 7.1 or higher
* PHP Curl extension
* PHP JSON extension

## Usage

In order to use the ResRobot Timetable and Routeplanning APIs, you need to obtain an API key
from [Trafiklab](https://trafiklab.se) first.

### Getting Timetables (departures or arrivals from a stop)

#### Timetables

**Request**

The following code example illustrates how you can retrieve a timetable for a certain stop.

```php
$wrapper = new ResRobotWrapper();

// Create a new routeplanning object. The wrapper will instantiate an object of the interface type.
$wrapper = $wrapper->createTimeTableRequestObject();
$wrapper->setStopId("740000001");
$wrapper->setTimeTableType(TimeTableType::DEPARTURES);

$wrapper->setUserAgent("<YOUR_USER_AGENT>");
$wrapper->setTimeTablesApiKey("<YOUR_API_KEY>");
$response = $resRobotWrapper->getTimeTable($departuresRequest);
```

`<YOUR_API_KEY>` is obtained from [Trafiklab](https://trafiklab.se). `<YOUR_USER_AGENT>` is a string which identifies
your application. While this is not enforced in any way, it is good practice to use a clear user agent. An example could
be `MyDemoApp/1.0.0 (mail@example.com)`. If you don't want to send a user agent, you can just leave out this line.

Detailed information about ResRobot request parameters can be found at
the [ResRobot departures/arrivals API page](https://www.trafiklab.se/api/our-apis/resrobot-reseplanerare). Only the most
important/most used request parameters are implemented in the SDK, in order to reduce clutter, and to ensure that we can
keep the SDK unchanged in case of changes to the API. If you believe we have missed an important field, please create an
issue so we can review this.

**Response**

In order to use the data returned by your request, you can simply call getTimeTable() on the response object. This
method returns an array of TimeTableEntry instances, each of which describes one departure or arrival. You can look at
the code and PHPDoc in order to get up-to-date information on which fields are available. Detailed information about
ResRobot responses can be found at
the [ResRobot departures/arrivals API page](https://www.trafiklab.se/api/our-apis/resrobot-reseplanerare).

The following code gives a quick idea on how the SDK is used.

```php
$entry = $response->getTimetable()[0]; // Get the first result
// Type of transport, one of the constants in Trafiklab\Common\Model\Enum\TransportType
$entry->getTransportType();
// The name of the stop location
$stop = $timeTableEntry->getStopName()
// The number of the line
$lineNumber = $timeTableEntry->getLineNumber();
// The direction of the vehicle
$direction = $timeTableEntry->getDirection();
// The scheduled departure time at the stop
$scheduledStopTime = $timeTableEntry->getScheduledStopTime();
```

#### Routeplanning

**Request**

The following code example illustrates how you can plan a route from A to B

```php
$queryTime = new DateTime();
$queryTime->setTime(18, 0);

$wrapper = new ResRobotWrapper();

// Create a new routeplanning object. The wrapper will instantiate an object of the interface type.
$wrapper = $wrapper->createRoutePlanningRequestObject();
$wrapper->setOriginId("740000001");
$wrapper->setDestinationId("740000002");
$wrapper->setDateTime($queryTime);

$wrapper->setUserAgent(("<YOUR_USER_AGENT>");
$wrapper->setRoutePlanningApiKey("<YOUR_API_KEY>");
$response = $resRobotWrapper->getRoutePlanning($routePlanningRequest);
```

**Response**

In order to use the data returned by your request, you can simply call getTrips() on the response object. This method
returns an array of Trip instances, each of which describes one departure or arrival. You can look at the code and
PHPDoc in order to get up-to-date information on which fields are available. Detailed information about ResRobot
responses can be found at
the [ResRobot departures/arrivals API page](https://www.trafiklab.se/api/our-apis/resrobot-reseplanerare).

The following code gives a quick idea on how the SDK is used.

```php
$trip = $response->getTrips()[0]; // Get the first result

// Tell the user about every leg in their journey.
foreach ($trip->getLegs() as $leg) {

   // There are two types of legs (at this moment): Vehicle journeys, where a vehicle is used, or walking parts
   // where a user walks between two stations. Not all fields are available for walking parts, so we need to handle them differently.

   if ($leg->getType() == RoutePlanningLegType::VEHICLE_JOURNEY) {
       $leg->getVehicle()->getType();
       $leg->getVehicle()->getNumber();
       $leg->getDirection();
       $leg->getDeparture()->getStopName();
       $leg->getDeparture()->getScheduledDepartureTime()->format("H:i");
       $leg->getDeparture()->getScheduledDepartureTime()->getTimestamp();
       $leg->getArrival()->getScheduledArrivalTime()->getTimestamp();
       $leg->getArrival()->getStopName();
       // More fields are available
   } else if ($leg->getType() == RoutePlanningLegType::WALKING) {
       // Limited fields when walking!
       $leg->getDeparture()->getStopName(); // origin
       $leg->getArrival()->getStopName(); // destination
   }
}
```
