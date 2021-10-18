---
title: New SL API ”Public transport information Region Stockholm” replacing today’s 7 SL APIs at Trafiklab 
date: 2020-06-26 
aliases:
- /node/29122
- /api/sl-reseplanerare/new-sl-api-public-transport-information-region
---

**The new SL API has been delayed to Q1 2021. We will update you when we know more.**

SL launched its first open APIs in 2014 and today there are 7 APIs with a functionality that has gradually been
extended. These services have been used extensively, and SL has received valuable feedback that has been used as part of
the basis for the design of the new open SL API.

The keywords when designing the new API have been simplicity, consistency, standardized and more extensive. The new SL
API will replace the current 7 APIs and offer a consistent data model throughout the whole API.

You are no longer required to know that Slussen has the id 9192 in order to find the next departure. Just search for
Slussen and you’ll get next departure, deviations and the actual lines. Searching could be done for the whole station or
for a single stop point.

The API is RESTful and supports [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS) implying simpler error handling and
navigation of information.

The structure of the API is future-proof and facilitates the addition of traffic information such as entrance points,
vehicle positions etc. Documentation and version handling will also be improved – you won’t need to retrieve a new key
for each new version of the API.

Summary:

- API capabilities
    - Trip search
    - Stop areas and Lines
    - Deviations
    - Next departure
    - Auto completion
- RESTful (supporting HATEOAS)
- Consistent data model
- Improved documentation
- More precise and standardized error messages
- One single API key no matter the endpoint or the API version
- Enables faster change of consuming applications

The migration of applications currently using the SL APIs will be possible during a transition period of 4 months when
these APIs will coexist with the new SL API. Thereafter, only the new SL API will be available.

We’ll keep you updated with additional information about the time schedule for the new SL API with its parameters and
corresponding response data. For any questions, please contact Trafiklab via Kundo
at [support.trafiklab.se](https://support.trafiklab.se).