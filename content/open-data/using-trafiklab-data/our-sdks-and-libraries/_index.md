# Our SDKs and libraries

If you're using PHP, you're lucky! We developed open-source SDKs which offer those 3 features, both for the ResRobot and
SL APIs. They are interchangeable, meaning your code doesn't need any modification to change the data source. They are
also updated when APIs are updated, meaning you don't get breaking changes in your code.

The SDKs can be found at Github:

* ResRobot: [https://github.com/trafiklab/resrobot-php-sdk](https://github.com/trafiklab/resrobot-php-sdk)
* SL: [https://github.com/trafiklab/sl-php-sdk](https://github.com/trafiklab/sl-php-sdk)

Installation is as easy as `composer require trafiklab/resrobot-php-sdk` or `composer require trafiklab/sl-php-sdk`.

For an example on how these are used, you can look at the readme docs, or
in [our Google Assistant demo project](https://github.com/trafiklab/google-assistant-demo/blob/master/app/Http/Controllers/NextDepartureController.php#L62)
.

## Consuming the APIs in other programming language

Unfortunately our SDKs are only available in PHP right now, but let us know if you want to see them in an other
language! Luckily, using the APIs isn't too hard. All the documentation can be found
on [trafiklab](https://trafiklab.se). The table above contains direct links to the specific API documentation. You can
still use the source code of our SDKs to see which parameters we send to the APIs and which fields we parse. If you get
stuck, you can always reach out to Trafiklab [using the Kundo forum](https://kundo.se/org/trafiklabse/).

