---
title: Putting it all online
---

As DialogFlow needs to send an HTTP request to your server application, your server application needs to be accessible
from the internet, either with a static IP address or a domain name.

* You can deploy through Heroku, which offers a free-tier with unlimited duration.
  See [our tutorial on Heroku](https://github.com/trafiklab/trafiklab-docs/tree/85417ce9d0f16da3542693f3543876deea25161c/using-trafiklab-data-1/related-tools/heroku.md)
  to learn how to set it up.
* You can host the application on a server or VPS, for example on DigitalOcean
* You can host the application on a Raspberry Pi in combination with port forwarding on your router.

After you have deployed your server application, don't forget to update your DialogFlow fulfillment settings!
