---
title: ResRobot error codes
weight: 500
date: 2022-09-06
---


When a request to the Resrobot APIs cannot be answered, an error response is thrown. This error response has an
identical format between all Resrobot API endpoints, and looks like the example code below.

{{% tabs %}} {{% tab "Json" %}}

```json
{
  "errorCode": "API_AUTH",
  "errorText": "access denied for 'key' on 'service' "
}
```

{{% /tab %}}

{{% tab "Xml" %}}

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Error errorCode="API_AUTH" errorText="access denied for 'key' on 'service'">
</Error>
```

{{% /tab %}} {{% /tabs %}}

## Complete list of error codes

The following error codes can be thrown by Resrobot. For each Resrobot error code, the according HTTP code and
description are provided. Note that not all error messages are actively used by the current

| Error code            | HTTP Code | Description                                     |
|-----------------------|-----------|-------------------------------------------------|
| API_AUTH              | 403       | access denied for 'key' on 'service'            |
| API_QUOTA             | 400       | quota exceeded for 'key' on 'service'           |
| API_TOO_MANY_REQUESTS | 429       | too many requests                               |
| API_PARAM             | 400       | required parameter <<name>> is missing          |
| API_PARAM             | 400       | numB wrong, only number in range [0,6] allowed  |
| API_PARAM             | 400       | numF wrong, only number in range [0,6] allowed  |
| API_PARAM             | 400       | numF + numB not greater than [6] allowed        |
| API_FORMAT            | 400       | response format not supported                   |
| SVC_PARAM             | 400       | request parameter missing or invalid            |
| SVC_LOC               | 400       | location missing or invalid                     |
| SVC_LOC_ARR           | 400       | arrival location missing or invalid             |
| SVC_LOC_DEP           | 400       | departure location missing or invalid           |
| SVC_LOC_VIA           | 400       | unknown change stop                             |
| SVC_LOC_EQUAL         | 400       | start/destination or vias are equal             |
| SVC_LOC_NEAR          | 400       | start and destination too close                 |
| SVC_DATATIME          | 400       | date/time missing or invalid                    |
| SVC_DATATIME_PERIOD   | 400       | date/time not in timetable or allowed period    |
| SVC_PROD              | 400       | product field missing or invalid                |
| SVC_CTX               | 400       | context invalid                                 |
| SVC_NO_RESULT         | 400       | no result found                                 |
| SVC_FAILED_SEARCH     | 500       | unsuccessful search                             |
| SVC_NO_MATCH          | 422       | no match found                                  |
| INT_ERR               | 500       | internal error                                  |
| INT_GATEWAY           | 503       | communication error with backend systems        |
| INT_TIMEOUT           | 503       | timeout during service processing               |