---
title: Migration guide 
weight: 1 
date: 2022-02-07
---

This page collects the differences between version 2.0 and version 2.1 of the ResRobot APIs, so you can swiftly adapt
your application to the updated specification.

{{% success %}}
On March 24th, 2022, an additional improvement to this API was made. You can now use one API key to use all API 
endpoints, instead of needing two keys. This does not negatively affect any existing keys. 

If you before this change already created a *ResRobot Routeplanner v2.1* key, this key has been upgraded automatically. 
If you created a *ResRobot Stoptimes v2.1* API key, you can simply discard 
this key and use your upgraded route-planner key (if you have one) or create a new *ResRobot 2.1* key.
{{% /success %}}

## Changes for all endpoints

Users of all API endpoints for which an API key is needed have to do the following:

### Obtaining new API keys

Similar to the previous versions, there is only one API key required to access all features.
In order to aquire this new key, you need to add them to your existing projects or create a new project with them. In
order to add them to an existing project, you can follow these steps:

- Login to [the Trafiklab developer portal](https://developer.trafiklab.se)
- Add the new ResRobot API to your project (Redigera project > Add the new API > Spara). For a more detailed
  description, see [adding APIs to a project](/docs/using-trafiklab/adding-apis-to-a-project.md)
- Click "Hämta nyckel" to obtain the new API key
- If you previously had a key with an upgraded usage level, you can request for the same level. We will approve all
  these requests.

### AccessId instead of key

Across all endpoints, the `key` parameter has been replaced with `accessId`. All requests your application makes should
be updated with this new parameter.

### OperatorURL is no longer available

`OperatorUrl` has been removed from all API responses. Ensure you do not rely on this value in your application.

### Internal ids no longer match public ids

The `id` fields are no longer identical to the `extId` fields. Use `extId` if you were not using this already. Note that
this only affects responses. Names of request parameters are not affected.

### requestId for asynchronous API calls

You can now submit a `requestId` parameter to all API endpoints. The value of this parameter will be included in
the `requestId` field in the response. This makes it easier to handle asynchronous API calls, for example when using
NodeJS.

## Specific changes to the departureBoard and arrivalBoard endpoints

The following specific breaking changes have been made to the departureBoard/arrivalBoard request parameters, along with
the change from `key` to `accessId` described above:

- `maxJourneys` is ignored when making queries in the near past or future, when realtime data is available. We recommend
  using the new `duration` parameter to consistently limit the results list to a specific time window.
- `passlist` is now `0` by default. Set to `1` to keep the responses the same if you need this data.

The following specific changes have been made to the departureBoard/ArrivalBoard responses:

- The `Product` object has been renamed to `ProductAtStop`.
- `Product` is now the name of an array of products, containing one element. Use `ProductAtStop` for consistent results.
- `TransportNumber` is no longer included. Use `ProductAtStop.num` or `ProductAtStop.displayNumber` instead.
- `Type` has a different meaning and different possible values. This field used to indicate the type of the
  departing/arriving journey, but now indicates the type of location for this departure/arrival.

Non-breaking changes:

- JourneyStatus and JourneyDetailRef have been added

## Specific changes to the trips endpoint

The following specific breaking changes have been made to the trips request parameters, other than the change from `key`
to `accessId` described above:

- `passlist` is now `0` by default. Set to `1` to keep the responses the same if you need this data.

The following breaking changes have been made to the trips responses:

- `Product` is now an array of products, containing one element.

Non-breaking changes:

- JourneyStatus and JourneyDetailRef have been added to each `Leg`

## Specific changes to the nearby stops endpoint

No specific breaking changes have been made to the nearby stops request parameters, other than the change from `key`
to `accessId` described above.

The following breaking changes have been made to the nearby stops responses:

- The root object now contains an array of `stopLocationOrCoordLocation` instead of an array of `stopLocation`.
- `stopLocation` can now be found in the items present in the `stopLocationOrCoordLocation` array.
- The `products` field has been replaced with an array of Products. Instead of accessing the sum of all products
  through `products`, you can now obtain all the individual products through `ProductAtStop[].cls`
- `timezoneOffset` has been added to each `StopLocation`.

## Specific changes to the stop lookup endpoint

No specific breaking changes have been made to the nearby stop lookup parameters, other than the change from `key`
to `accessId` described above.

The following breaking changes have been made to the stop lookup responses:

- The root object now contains an array of `stopLocationOrCoordLocation` instead of an array of `stopLocation`.
- `stopLocation` can now be found in the items present in the `stopLocationOrCoordLocation` array.
- The `products` field has been replaced with an array of Products. Instead of accessing the sum of all products
  through `products`, you can now obtain all the individual products through `ProductAtStop[].cls`
- `timezoneOffset` has been added to each `StopLocation`.