---
title: Oxyfi-Realtidspositionering
layout: "single"
summary: Push-API med information om realtidspositioner på fordon i kollektivtrafiken. För närvarande levererar API:et information för alla tåg som körs av Värmlandstrafik, Norrtåg och Tåg i Bergslagen. Informationen kommer från Oxyfis system för Internet ombord. Arbete pågår också för att ta med tåg från andra tågoperatörer.
weight: 95
aliases:
  - /api/oxyfi-realtidspositionering
  - /api/oxyfi-realtidspositionering/dokumentation
  - /api/oxyfi-realtidspositionering/nivaer
  - /api/oxyfi-realtidspositionering/konsol
  - /api/oxyfi-realtidspositionering/licens
  - /node/16601
  - /node/16601/dokumentation
  - /node/16601/nivaer
  - /node/16601/konsol
  - /node/16601/licens
---

## API Overview

Positions are represented by GPS data that is generated locally onboard each train-set. The current position is
transmitted as a message every second to Oxyfi’s real-time server on shore.

Beside storing the message for future use, the server customizes messages on the fly by tagging it with additional
information and passes them on to subscribers. One such subscriber is the websocket API service.

The Trainpos API is one such subscriber. It subscribes on messages that contains the NMEA version 2.2 specification of
the $GPRMC sentence tagged with vehicleId and train number (tågnummer), both public and internal train numbers.

VehicleId is a unique number assigned to every train-set or carriage in Sweden, this number is typically written on the
vehicle and is never changed. The train number on the other hand identifies a specific route, the train number is
typically found on tickets, billboards and timetables. A train can serve 0 or more train identities at any one time, see
further information under ![](https://docs.google.com/drawings/d/syxOJ1JeO4zisbX6X1rSkSw/image?w=708&h=417&rev=397&ac=1)

The Trainpos API will redistribute the real-time positions to all Trainpos subscribers. A Trainpos API subscriber is
typically some form of server that in turn is responsible to distribute positions to all of its clients. In other words,
the clients should not try to subscribe directly from the Trainspos API. In fact, the API key is only valid for one
subscriber, if a new subscribe request arrives at the API, it will close any open websocket with the same API key.

The total delay from position generation onboard until it is sent out from the real-time server is typically less than
100 ms. The vast majority of this delay is occurring in the mobile network that connects the vehicle to the internet.

Each train-set or carriage reports its position every second, so you should get a message per second for each vehicle
that currently has both power and radio coverage.

## Message Details

– API version 1.0

A message sent from the real-time server to a subscriber is encoded as an ASCII-string and sent over the subscribers
websocket.

The message format is based on the NMEA specification version 2.2 and contains the GPRMC sentence followed by a number
of additional fields as explained in Table 1\. Each message begins with $GP and fields are separated by comma. Time zone
will always be UTC.

This is a sample message:

$GPRMC,142937,A,5948.7028,N,01307.9771,E,49.53,349.7,101212,1.8,E*
3A,,1421.trains.se,,8955.public.trains.se@2012-12-10;8957.public.trains.se@2012-12-10,oxyfi

### Table 1 message Specification

|No|Field example|Explanation|
|--- |--- |--- |
|1|RMC|Recommended Minimum sentence C|
|2|142937|Fix taken at 14:29:37 UTC|
|3|A|Status A=active or V=Void|
|4|5948.7028|Latitude 59 deg 48.7028'|
|5|N|Latitude hemisphere N for northern and S for southern|
|6|01307.9771|Longitude 13 deg 07.9771'|
|7|E|Longitude direction, E for east of the meridian 0° and W for west|
|8|49.53|Speed over ground in knots|
|9|349.7|Track angle in degrees True|
|10|101212|Date – 10th of December 2012|
|11|1.8|Magnetic Variation|
|12|E|Magnetic deviation direction, E for east of the meridian 0° and W for west|
|13|*3A|The checksum data, always begins with *|
|14|n/a|Not used|
|15|1421.trains.se|Identifies the vehicle, 1421 in this case (Värmlandstrafik)|
|16|n/a|Not used|
|17|8955.public.trains.se@2012-12-10;
8957.public.trains.se@2012-12-10|Train numbers concatenated with semicolon if more than one is present. See more details about how this string is built
up in section "A Note on Train Numbers".|
|18|oxyfi|Data origin|

### A Note on Train Numbers

A train-set or carriage may carry more than one train number at a time, each being either announced (public) or
technical (internal). The string in the message field that carries train number is therefore built up like domain-names
concatenated together with semicolon. For instance, train number 8955 is the announced train number and thus “tagged”
with public resulting in 8955.public.trains.se. If there had been a corresponding technical only train number too, say
8845, that would have resulted in the following string 8955.public.trains.se;8845.internal.trains.se.

In addition to the above, if a train-set or carriage is running late so that the current train number becomes
overlapping with the next planned number, both those numbers will be presented in the field. As the message sample
shows, at the time when the message was intercepted that particular train served both 8955 and 8957, thus the train
number field is 8955.public.trains.se@2012-12-10;8957.public.trains.se@2012-12-10.

To give subscribers a head start, the train number is applied 5 minutes before the actual train starts to serve it.

## How to Subscribe

### Subscribe to stream

wss://api.oxyfi.com/trainpos/listen?v=1&key=YOUR-KEY-HERE

## Code example

{{% tabs %}} {{% tab "Python" %}}
**Python:**
```python
# Uses https://github.com/websocket-client/websocket-client
import websocket
def on_message(ws, message):
print(message)
ws = websocket.WebSocketApp("wss://api.oxyfi.com/trainpos/listen?v=1&key=YOUR-KEY-HERE",on_message = on_message)
ws.run_forever()
```
{{% /tab %}} {{% tab "Node.js" %}}
**Node.js:**
```nodejs
// Uses https://github.com/websockets/ws
const WebSocket = require('ws');
const ws = new WebSocket('wss://api.oxyfi.com/trainpos/listen?v=1&key=YOUR-KEY-HERE');
ws.on('message', function incoming(data) {console.log(data); })
```
{{% /tab %}} 
{{% /tabs %}}

## Usage

A Trainpos API subscriber is typically some form of server that in turn is responsible to distribute positions to all of
its clients. In other words, the clients should not try to subscribe directly from the Trainspos API. In fact, the API
key is only valid for one subscriber at the time, if a new websocket request is made, the Trainpos API will close any
open websocket with the same API key.

Here are some suggestion of libraries that can be used to parse NMEA formatted data to objects or data structures:

* JS: [nmea-0183](https://www.npmjs.com/package/nmea-0183)
* Python: [Knio/pynmea2](https://github.com/Knio/pynmea2)
* Java: [nmealib on Sourceforge](http://nmealib.sourceforge.net/)
* C#: [amezcua/GPS-NMEA-Parse](https://github.com/amezcua/GPS-NMEA-Parser/blob/master/C%23/GPRMCGpsSentence.cs)
* Ruby: [ifreecarve/nmea_plus](https://github.com/ifreecarve/nmea_plus)
* GO: [buxtronix/golang/blob/master/nmea/src/nmea/gprmc.go](https://github.com/buxtronix/golang/blob/master/nmea/src/nmea/gprmc.go)
* C: [jacketizer/libnmea](https://github.com/jacketizer/libnmea), [nmea on Sourceforge](http://nmea.sourceforge.net/)

## VehicleIds

To get the current list of trains that delivers data through the Trainpos API, see

{{% warning %}} The current list of trains is not available over HTTPS. {{% /warning %}}

[http://api.oxyfi.com/trainpos/trainIdentites.htm](http://api.oxyfi.com/trainpos/trainIdentites.htm) push-API

On the 2021-09-24 the current list of trains is:

### Värmlandstrafik

<table>
    <tbody>
    <tr>
        <td>1414</td>
        <td>1415</td>
        <td>1416</td>
        <td>1420</td>
        <td>1421</td>
    </tr>
    <tr>
        <td>9048</td>
        <td>9049</td>
        <td>9050</td>
        <td>9066</td>
        <td>9067</td>    
    </tr>
    <tr>
        <td>9081</td>
        <td>9082</td>
        <td>9083</td>
        <td></td>
        <td></td>
    </tr>
    </tbody>
</table>

### Norrtåg

<table>
    <tbody>
<tr>
<td>1429</td>
<td>3112</td>
<td>3167</td>
<td>3189</td>
<td>9032</td>
    </tr>
    <tr>
<td>9033</td>
<td>9034</td>
<td>9042</td>
<td>9051</td>
<td>9062</td>
    </tr>
    <tr>
<td>62001</td>
<td>62002</td>
<td>62003</td>
<td>62004</td>
<td>62005</td>
    </tr>
    <tr>
<td>62006</td>
<td>62007</td>
<td>62008</td>
<td>62009</td>
<td>62010</td>
    </tr>
    <tr>
<td>62011</td>
<td>62012</td>
</tr>
    </tbody>
</table> 

### Tåg i Bergslagen

<table>
    <tbody>
    <tr>
<td>3190</td>
<td>3223</td>
<td>3231</td>
<td>3234</td>
<td>3235</td>
    </tr>
    <tr>
<td>9005</td>
<td>9006</td>
<td>9007</td>
<td>9008</td>
<td>9009</td>
    </tr>
    <tr>
<td>9011</td>
<td>9012</td>
<td>9013</td>
<td>9014</td>
<td>9015</td>
    </tr>
    <tr>
<td>9018</td>
<td>9019</td>
<td>9020</td>
<td>9021</td>
<td>9022</td>
    </tr>
    <tr>
<td>9023</td>
<td>9024</td>
<td>9025</td>
<td>9037</td>
<td>9039</td>
    </tr>
    <tr>
<td>9056</td>
<td>9057</td>
<td>9068</td>
    </tr>
    </tbody>
</table>

### Blekingetrafiken

<table>
    <tbody>
    <tr>
        <td>3108</td>
        <td>3109</td>
        <td>3111</td>
        <td></td>
        <td></td>
    </tr>
    </tbody>
</table>

### Kalmars länstrafik
<table>
    <tbody>
    <tr>
        <td>3106</td>
        <td>3134</td>
        <td>3135</td>
        <td>3136</td>
        <td>3137</td>
    </tr>
    <tr>
        <td>3168</td>
        <td>3169</td>
    </tr>
    </tbody>
</table>

## What is next

Oxyfi continuously works on adding more vehicles to this real-time position API. It may also be possible to add filters
in the websocket request so only positions for the specified trains are forwarded over the websocket.

We are very happy to receive feedback and feature requests, please drop an email
to [apisupport@oxyfi.com](mailto:apisupport@oxyfi.com).

## Known Issues

It is the train operator who plans the traffic that decides which vehicle will serve what train number. On occasion the
train operator has reported one vehicle to serve a specific train number but in reality it is served by another train.
At present the vehicle to train number mapping, as reported by the train operator, is not verified to conform to reality
in any way, it is just forwarded as is. Any such checks have to be carried out by the subscriber.