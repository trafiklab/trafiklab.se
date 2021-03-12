# Limiting requests

Our departures/arrivals APIs are commonly used for digital signage, both in public spaces \(digital signage in stores,
malls, appartment blocks, ...\) and private spaces \(magic mirror, hobby projects, ...\). Since every API call incurrs
costs for the provider \(Trafiklab, SL, ...\), we encourage people to use them in an efficient way.

{% hint style="info" %} We want you to use data, we like it when you use our data, but we do not want to needlessly "
waste" computing resources. {% endhint %}

Generally, our policy is to limit private projects \(which affect 5 or less persons\) to the bronze, 10,000 requests per
month level. We believe this is enough for the usual hobby projects such as a smart mirror, a computer widget, ... . Of
course, if you have a private project that requires more requests, feel free to reach out to us, but please read the
hints below first.

### Adjusting the update frequency during the day

In many cases, you'll have some sort of display showing when the next bus leaves. However, if you never travel between
midnight and 06:00, you don't need to fetch this data. If you're very unlikely to travel between 22:00 and 23:00, a time
when busses are unlikely to be delayed as well, it might be enough to fetch their data once every 5 minutes. During rush
hour, when you usually leave for school or work, you want to most accurate data and could update every minute or two. By
varying the update frequency throughout the day, you can have high update frequencies when needed while saving requests
when you don't need them. The table below shows an example on how you can vary the number of requests per hour to fit
inside the bronze level.

| Interval | Number of hours | Requests per hour for one stop | Number of requests |
| :--- | :--- | :--- | :--- |
| Every 10 minutes in 6:00-6:59 | 1 | 6 | 6 |
| Every 2 minutes in 7:00-9:59 | 3 | 30 | 90 |
| Every 5 minutes in 10:00-21:59 | 12 | 12 | 144 |
| Every 10 minutes in 22:00-22:59 | 1 | 6 | 6 |
| **Total** | 17 |  | **246 requests per day** |

This solution will use about 7600 requests per month, which is well under the maximum of 10.000 monthly requests / 31
days per month = 322 requests per day, and will thus work perfectly. There is even a margin of 70 requests per day,
which can be used to update the data even more during certain intervals.

{% hint style="info" %} Updating data every 2 or 5 minutes doesnt mean your "bus leaves in 5 minutes" data will be wrong
after one minute. We strongly recommend that you generate these  "in ... minutes" texts on the client side, based on the
timestamp included in the API responses. This way you can update the user interface every 10 seconds while only updating
the data every 2 minutes. {% endhint %}

