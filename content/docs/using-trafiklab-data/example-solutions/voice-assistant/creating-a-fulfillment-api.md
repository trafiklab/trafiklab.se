---
title: Creating a fulfillment API
---

### Fulfillment

While we now have an agent that can understand what users want, it still doesn't know what to answer. This is where
fulfillment comes in.

> Fulfillment is code that's deployed as a webhook that lets your Dialogflow agent call business logic on an intent-by-intent basis. During a conversation, fulfillment allows you to use the information extracted by Dialogflow's natural language processing to generate dynamic responses or trigger actions on your back-end.

Whenever your intent is called, dialogflow will send an HTTP POST request to a URL of your choosing. Information about
the intent which was used and the parameters which were extracted is sent as JSON data in the request body. The server
application now needs to process this data and formulate a response, which will then be passed back to the digital
assistant. You can see the entire process in the image below.

![The complete data flow](/media/2020/05/voice-bot-architecture.png)

In order to enable fulfillment, head over to the fulfillment page on DialogFlow by clicking _fulfillment_ in the left
sidebar. Switch the slider to enabled, and enter the address of your server app here. You can also use the inline editor
to write your fulfillment code in NodeJS on Firebase cloud functions. If you don't have any URL just now, and you don't
want to use the built-in editor, you can come back to this step later on when your fulfillment server is ready.

In order to be able to code a fulfillment application, we need to know the request and response
format. [This format is explained fully on the dialogflow website](https://dialogflow.com/docs/fulfillment/how-it-works)
. You can find an example Dialogflow request and response in the V2 format below.

{{% tabs %}} {{% tab "Request" %}} Headers:

```xml
 POST https://my-service.com/action

 Headers:
 //user defined headers
 Content-type: application/json
```

Request Body:

```json
 {
   "responseId": "ea3d77e8-ae27-41a4-9e1d-174bd461b68c",
   "session": "projects/your-agents-project-id/agent/sessions/88d13aa8-2999-4f71-b233-39cbf3a824a0",
   "queryResult": {
     "queryText": "user's original query to your agent",
     "parameters": {
       "param": "param value"
     },
     "allRequiredParamsPresent": true,
     "fulfillmentText": "Text defined in Dialogflow's console for the intent that was matched",
     "fulfillmentMessages": [
       {
         "text": {
           "text": [
             "Text defined in Dialogflow's console for the intent that was matched"
           ]
         }
       }
     ],
     "outputContexts": [
       {
         "name": "projects/your-agents-project-id/agent/sessions/88d13aa8-2999-4f71-b233-39cbf3a824a0/contexts/generic",
         "lifespanCount": 5,
         "parameters": {
           "param": "param value"
         }
       }
     ],
     "intent": {
       "name": "projects/your-agents-project-id/agent/intents/29bcd7f8-f717-4261-a8fd-2d3e451b8af8",
       "displayName": "Matched Intent Name"
     },
     "intentDetectionConfidence": 1,
     "diagnosticInfo": {},
     "languageCode": "en"
   },
   "originalDetectIntentRequest": {}
 }
```

{{% /tab %}}

{{% tab "Response" %}} Response body:

```json
{
  "fulfillmentText": "This is a text response",
  "fulfillmentMessages": [
    {
      "card": {
        "title": "card title",
        "subtitle": "card text",
        "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
        "buttons": [
          {
            "text": "button text",
            "postback": "https://assistant.google.com/"
          }
        ]
      }
    }
  ],
  "source": "example.com",
  "payload": {
    "google": {
      "expectUserResponse": true,
      "richResponse": {
        "items": [
          {
            "simpleResponse": {
              "textToSpeech": "this is a simple response"
            }
          }
        ]
      }
    },
    "facebook": {
      "text": "Hello, Facebook!"
    },
    "slack": {
      "text": "This is a text response for Slack."
    }
  },
  "outputContexts": [
    {
      "name": "projects/${PROJECT_ID}/agent/sessions/${SESSION_ID}/contexts/context name",
      "lifespanCount": 5,
      "parameters": {
        "param": "param value"
      }
    }
  ],
  "followupEventInput": {
    "name": "event name",
    "languageCode": "en-US",
    "parameters": {
      "param": "param value"
    }
  }
}
```

These are samples containing a lot of fields. _FulfillmentMessages_, _outputContexts_ and _followupEventInput_ are
optional when you just want to have a voice response. A simple response could look like this:

```json
{
  "fulfillmentText": "This is a text response",
  "payload": {
    "google": {
      "expectUserResponse": false,
      "richResponse": {
        "items": [
          {
            "simpleResponse": {
              "textToSpeech": "this is a simple response"
            }
          }
        ]
      }
    }
  }
}
```

{{% /tab %}} {{% /tabs %}}

More details on setting up fulfillment using Firebase, Google cloud, or using NodeJS libraries can be found
in [the dialogflow docs](https://dialogflow.com/docs/fulfillment/configure). If you want more information on specific
Google Assistant replies, you can
use [the Google Assistant documentation](https://developers.google.com/actions/assistant/responses#json)

## Creating a custom fulfillment server application

We now know the request format, and how our response should look like. In order to be able to anwer, we will use
the Trafiklab APIs. Depending on which features we want to implement, there are two or three
types of API requests which we will use:

* **Station lookups**: The station name, passed as a parameter by DialogFlow, needs to be converted to an ID so we can
  specify which station we mean

  when talking to other APIs.

* **Departure boards**: A departures API gives information about the next departures from a given stop location.
* **Routeplanning**: If you want to create an extra intent that handles routeplanning, you will need an API like this to
  quickly provide you with a response.

The following table shows which API can be used for each purpose, depending on the region for which you want to get
information.

|  | Sweden | Stockholm |
| :--- | :--- | :--- |
| Station lookup | [ResRobot Reseplanerare](/api/trafiklab-apis/resrobot-v2/stop-lookup) | [SL Platsuppslag](/api/trafiklab-apis/sl/stop-lookup) |
| Departure boards | [ResRobot Stolptidstabeller 2](/api/trafiklab-apis/resrobot-v2/timetables) | [SL Realtidsinformation 4](/api/trafiklab-apis/sl/departures-4) |
| Routeplanning | [ResRobot Reseplanerare](/api/trafiklab-apis/resrobot-v2/route-planner) | [SL Reseplanerare 3.1](/api/trafiklab-apis/sl/route-planner-31) |

\* ResRobot also works in Stockholm, but the SL APIs might offer better accuracy and realtime data.  
\*\* API versions are the latest at time of writing. Future versions will be just as suited for this.

To use these APIs, you can either use [our SDKs](../../our-sdks-and-libraries/), or write your own client. You can also
make use of
the [GTFS Sverige 2](../../../public-transport-data/our-data-and-apis/gtfs/gtfs-sverige-2-static/) [stops.txt]() file to
find the stop id for a given name on your own server without any API,
or [SL's hallplatser-och-linjer-2](https://www.trafiklab.se/api/sl-hallplatser-och-linjer-2) dataset to do the same for
SL.
