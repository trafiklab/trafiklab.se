---
description: Just want to play around and experiment? Run our demo app in minutes on your own phone.
---

# Importing our demo project

## Importing an existing agent

We created [a demo project](https://github.com/trafiklab/google-assistant-demo/) consisting of a DialogFlow agent and a
fulfillment server application. The DialogFlow project has been exported
to [a zip file](https://raw.githubusercontent.com/trafiklab/google-assistant-demo/master/docs/dialogflow-stockholm-public-transport.zip)
, and can be downloaded and imported to your own DialogFlow project.

In order to do this, head over to [the dialogflow console](https://console.dialogflow.com) and create a new agent first.
After creating a new agent, you click the gear wheal in the top left, next to your agent name.

![Locating the DialogFlow project settings](../../../.gitbook/assets/image-5.png)

After going to the settings, choose the Export and Import tab. Choose Restore from zip to clone the project from the zip
file. Once your project has been restored, you will still need to update the fulfillment settings to point to your own
server. You can read [the dialogflow docs](https://dialogflow.com/docs/agents/export-import-restore) for more
information.

### Deploying the demo application

If you want to experiment with our demo application first, you can simply head over
to [our Google Assistant demo project](https://github.com/trafiklab/google-assistant-demo/)' and press the "deploy on
Heroku" button to deploy an instance for free. You can read more detail in the readme of our demo project.

