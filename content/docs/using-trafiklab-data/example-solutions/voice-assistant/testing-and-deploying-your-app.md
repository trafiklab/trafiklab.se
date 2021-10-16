---
title: Testing and deploying your app
description: "Understanding why things work, or why they don't."
---

## Putting it to the test

The right sidebar in your dialogflow project allows you to test your intents, and to see how parameters are extracted.
When using this sidebar for testing, no resposne will be generated, as it only tests the input.

![Testing DialogFlow intents](./media/2020/05/voice-bot-intents.png)

By following the "_See how it works on Google Assistant_" link, you will be redirected to a simulator for Google
Assistant. From this screen you can also configure how your agent will be invoked from Google Assistant, and publish it
to the Assistant store.

![The Actions on Google platform](/media/2020/05/voice-bot-actions-on-google.png)

When testing with the Google Assistant simulator, both the intents and the responses are tested (understanding what the
user says, and creating a response). After you have set up the name for your app under _Setup > invocation_, you can
test from the online console, but also from any devices that have Google Assistant and are linked to your Google
account. This way you can test it exactly the same as users would use it. Open the assistant by saying "_OK Google_"
(or opening it using a button on your phone), followed by "_Talk to_ " to talk with your agent.
