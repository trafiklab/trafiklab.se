---
title: Oxyfi Vehicle positions
---

Oxyfi Vehicle Positions is a Push-API which provides real-time vehicle positions for public transport vehicles.
Information is provided by Oxyfi's onboard internet system.

### API Overview

Positions are represented by GPS data that is generated locally onboard each train-set. The current position is
transmitted as a message every second to Oxyfi’s real-time server on shore.

Besides storing the message for future use the server customizes messages on the fly by tagging it with additional
information and passes them on to subscribers. One such subscriber is the WebSocket API service.

The Trainpos API is one such subscriber. It subscribes on messages that contains the _NMEA version 2.2_ specification of
the _$GPRMC_ sentence tagged with vehicleId and train number (tågnummer), both public and internal train numbers.

VehicleId is a unique number assigned to every train-set or carriage in Sweden, this number is typically written on the
vehicle and is never changed. The train number on the other hand identifies a specific route, the train number is
typically found on tickets, billboards and timetables. A train can serve 0 or more train identities at any one time, see
further information below

![](https://docs.google.com/drawings/d/syxOJ1JeO4zisbX6X1rSkSw/image?w=708&h=417&rev=397&ac=1)

The Trainpos API will redistribute the real-time positions to all Trainpos subscribers. A Trainpos API subscriber is
typically some form of server that in turn is responsible to distribute positions to all of its clients. In other words,
the clients should not try to subscribe directly from the Trainspos API. In fact, the API key is only valid for one
subscriber, if a new subscribe request arrives at the API, it will close any open WebSocket with the same API key.

The total delay from position generation onboard until it is sent out from the real-time server is typically less than
100 ms. The vast majority of this delay is occurring in the mobile network that connects the vehicle to the internet.

Each train-set or carriage reports its position every second so you should get a message per second for each vehicle
that currently has both power and radio coverage.

### Message Details

A message sent from the real-time server to a subscriber is encoded as an ASCII-string and sent over the subscribers
WebSocket.

The message format is based on the NMEA specification version 2.2 and contains the GPRMC sentence followed by a number
of additional fields as explained in Table 1. Each message begins with $GP and fields are separated by comma. Time zone
will always be UTC.

This is a sample message:

```xml
$GPRMC,142937,A,5948.7028,N,01307.9771,E,49.53,349.7,101212,1.8,E*3A,,1421.trains.se,,8955.public.trains.se@2012-12-10;8957.public.trains.se@2012-12-10,oxyfi
```

#### **Table 1 message Specification**

| No | Field example | Explanation |
| :--- | :--- | :--- |
| 1 | RMC | Recommended Minimum sentence C |
| 2 | 142937 | Fix taken at 14:29:37 UTC |
| 3 | A | Status A=active or V=Void |
| 4 | 5948.7028 | Latitude 59 deg 48.7028' |
| 5 | N | Latitude hemisphere N for northern and S for southern |
| 6 | 01307.9771 | Longitude 13 deg 07.9771' |
| 7 | E | Longitude direction, E for east of the meridian 0° and W for west   |
| 8 | 49.53 | Speed over ground in knots |
| 9 | 349.7 | Track angle in degrees True |
| 10 | 101212 | Date – 10th of December 2012 |
| 11 | 1.8 | Magnetic Variation |
| 12 | E | Magnetic deviation direction, E for east of the meridian 0° and W for west |
| 13 | \*3A | The checksum data, always begins with \* |
| 14 | n/a | Not used |
| 15 | 1421.trains.se | Identifies the vehicle, 1421 in this case (Värmlandstrafik) |
| 16 | n/a | Not used |
| 17 | 8955.public.trains.se@2012-12-10; 8957.public.trains.se@2012-12-10 | Train numbers concatenated with semicolon if more than one is present. See more details about how this string is built up in section "A Note on Train Numbers". |
| 18 | oxyfi | Data origin |

#### **A Note on Train Numbers**

A train-set or carriage may carry more than one train number at a time, each being either announced (public) or
technical (internal). The string in the message field that carries train number is therefore built up like
domain-names concatenated together with semicolon. For instance, train number 8955 is the announced train number and
thus “tagged” with public resulting in 8955.public.trains.se. If there had been a corresponding technical only train
number too, say 8845, that would have resulted in the following string 8955.public.trains.se;8845.internal.trains.se.

In addition to the above, if a train-set or carriage is running late so that the current train number becomes
overlapping with the next planned number, both those numbers will be presented in the field. As the message sample
shows, at the time when the message was intercepted that particular train served both 8955 and 8957, thus the train
number field is 8955.public.trains.se@2012-12-10;8957.public.trains.se@2012-12-10.

To give subscribers a head start, the train number is applied 5 minutes before the actual train starts to serve it.

### How to Subscribe

In order to receive updates, you need to subscribe to the websocket steam.

`wss://api.oxyfi.com/trainpos/listen?v=1&key=YOUR-KEY-HERE`

{{% tabs %}} {{% tab "Python 3" %}}

```python
#Uses https://github.com/websocket-client/websocket-client
import websocket

def on_message(ws, message):
    print(message)

ws = websocket.WebSocketApp("wss://api.oxyfi.com/trainpos/listen?v=1&key=YOUR-KEY-HERE",on_message = on_message)
ws.run_forever()
```

{{% /tab %}}

{{% tab "NodeJS" %}}

```javascript
// Uses https://github.com/websockets/ws
const WebSocket = require('ws');
const ws = new WebSocket('wss://api.oxyfi.com/trainpos/listen?v=1&key=YOUR-KEY-HERE');
ws.on('message', function incoming(data) { console.log(data); })
```

{{% /tab %}} {{% /tabs %}}

### Usage

A Trainpos API subscriber is typically some form of server that in turn is responsible to distribute positions to all of
its clients. In other words, the clients should not try to subscribe directly from the Trainspos API. In fact, the API
key is only valid for one subscriber at the time, if a new websocket request is made, the Trainpos API will close any
open websocket with the same API key.

Here are some suggestion of libraries that can be used to parse NMEA formatted data to objects or data structures:

* JS: [https://www.npmjs.com/package/nmea-0183](https://www.npmjs.com/package/nmea-0183)
* Python: [https://github.com/Knio/pynmea2](https://github.com/Knio/pynmea2)
* Java: [http://nmealib.sourceforge.net/](http://nmealib.sourceforge.net/)
*
C\#: [https://github.com/amezcua/GPS-NMEA-Parser/blob/master/C%23/GPRMCGpsSentence.cs](https://github.com/amezcua/GPS-NMEA-Parser/blob/master/C%23/GPRMCGpsSentence.cs)
* Ruby: [https://github.com/ifreecarve/nmea\_plus](https://github.com/ifreecarve/nmea_plus)
*
GO: [https://github.com/buxtronix/golang/blob/master/nmea/src/nmea/gprmc.go](https://github.com/buxtronix/golang/blob/master/nmea/src/nmea/gprmc.go)
* C: [https://github.com/jacketizer/libnmea](https://github.com/jacketizer/libnmea)
  , [http://nmea.sourceforge.net/](http://nmea.sourceforge.net/)

### Vehicle Ids

To get the current list of trains that delivers data through the Trainpos API,
see [https://api.oxyfi.com/trainpos/trainIdentites.htm](https://api.oxyfi.com/trainpos/trainIdentites.htm)

On the 2020-06-01 the current list of trains is:

**Värmlandstrafk**

1414 1415 1416 1420 1421 9048 9049 9050 9066 9067 9081 9082 9083

**Norrtåg**

62001 62002 62003 62004 62005 62006 62007 62008 62009 62010 62011 62012 9034 9042 9062 3112 3167 3189 1429

**Tåg i Bergslagen**

9005 9006 9007 9008 9009 9011 9012 9013 9014 9015 9018 9019 9020 9021 9022 9023 9024 9025  
9037 9039 9068 9056 9057 3190 3223 3231 3234 3235

**Blekingetrafiken**

3108 3109 3111

**Kalmars länstrafik**

3106 3134 3135 3136 3167 3168 3169

### What is next

Oxyfi continuously works on adding more vehicles to this real-time position API. It may also be possible to add filters
in the WebSocket request so only positions for the specified trains are forwarded over the WebSocket.

We are very happy to receive feedback and feature requests, please drop an email
to [apisupport@oxyfi.com](mailto:apisupport@oxyfi.com).

### Known Issues

It is the train operator who plans the traffic that decides which vehicle will serve what train number. On occasion the
train operator has reported one vehicle to serve a specific train number but in reality it is served by another train.
At present the vehicle to train number mapping, as reported by the train operator, is not verified to conform to reality
in any way, it is just forwarded as is. Any such checks have to be carried out by the subscriber.
