---
title: "ResRobot update 2.1 with breaking changes"
date: "2022-02-07"
image: /media/2021/10/ResRobot-header.png 
image_credit: Samtrafiken
---

Our Resrobot API has got a well deserved update! After more than 6 years with Resrobot 2.0, Resrobot 2.1 is now
available. This maintenance update is focussed on updates to the platform back-end and fixes multiple bugs. For example
the long-standing bug with the HTTP content-encoding response header has been fixed, which should make the API easier to
use with standard tools and libraries.

The downside of all this is that we could not avoid certain breaking changes, such as a change in the base URL and API
keys, some default parameters which have been changed and slightly changed response structures. We have created a
migration guide, describing all changes in the request and response formats, along with a short refresher on how you can
add these new API keys to your existing projects.

Due to technical issues the nearby stops and stop lookup endpoints will unfortunately only be available from March 24,
2022. The migration guide and updated documentation is already available, so those who want can dive into the new
specifications before these endpoints right away.

## Timeline 

The two versions will work in parallel until June 30, 2022 when the current Resrobot APIs are shut down. Make sure you
update your project before this date.

## Using our SDK?

If you are using [our ResRobot PHP SDK](https://github.com/trafiklab/resrobot-php-sdk), you only need to update this SDK
version in your application in order to start using the new version. Our goal is to make these SDKs available in more
programming languages in the future.

If you have any more questions, do not hesitate to contact us at [info@trafiklab.se](mailto:info@trafiklab.se), or to
open a support issue at [support.trafiklab.se](https://support.trafiklab.se).

Regards, Team Trafiklab
