---
title: "ResRobot update with breaking changes"
date: "2021-12-15"
image: /media/2021/10/ResRobot-header.png 
image_credit: Samtrafiken
---

We are now releasing a new version of ResRobot. This version is an incremental update, keeping most things the same, but
it addresses a couple of bugs and adds some new features. While we always try to keep avoid changes to a minimum, we
could not avoid them this time.

## What changes?

The most important changes for you are the following:

- You now only need one API key for all endpoints. The route planner and departure boards no longer need separate keys.
- The key parameter has been renamed from `key` to `accessId`.
- You can now filter for X2000 trains, Movingo ticket validity, and more using the `attributes` filter.
- Multiple bugs have been fixed. This includes some bugs where HTTP headers were invalid. As a result, the API should be
  easier to use with all standard tools and libraries.
- Some parameters have updated default values, and some response structures have been slightly modified. We put together
  [a migration guide](/api/trafiklab-apis/resrobot-v21/migration-guide.md), and list all differences in the new API documentation.
- Along with the update, the documentation has been reviewed. We hope this makes the API easier to use.

## When will this data be available?

It is available right now as a new API, and both versions will be running until the end of april. The old version will
be shut down at april 30th, so make sure to update your existing applications as soon as possible!

## Using our SDK?

If you are using [our ResRobot PHP SDK](https://github.com/trafiklab/resrobot-php-sdk), you only need to update this SDK
version in your application in order to start using the new version. Our goal is to make these SDKs available in more
programming languages in the future.

If you have any more questions, do not hesitate to contact us at [info@trafiklab.se](mailto:info@trafiklab.se), or to
open a support issue at [support.trafiklab.se](https://support.trafiklab.se).

Regards, Team Trafiklab
