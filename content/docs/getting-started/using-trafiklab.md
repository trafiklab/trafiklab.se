---
title: "Using Trafiklab.se"
weight: 10
layout: "single"
sidebar: true
aliases:
  - "/hur-gor-jag"
  - "/docs/using-trafiklab/creating-a-project"
  - /docs/using-trafiklab/getting-api-keys/
  - /docs/using-trafiklab/upgrading-api-keys/
  - /docs/using-trafiklab/getting-started/
  - /docs/using-trafiklab/creating-an-account/
  - /docs/using-trafiklab/projects/
  - /docs/using-trafiklab/api-keys/
  - /docs/using-trafiklab/frequently-asked-questions/
---

## Getting started

{{% info %}}
New to trafiklab? Start reading here and continue to the next pages using the buttons at the
bottom.
{{% /info %}}

All the data on Trafiklab is provided free of charge to anyone who is interested. However, most of the APIs which we
provide cost us money, and therefore we need to keep control over the number of requests to each service.

In order to obtain API keys, you create one or more projects on our website. To do this, you will need an account. The
following pages will guide you through the account creation process and will help you to set up your first project and
obtain API keys.

## Creating an account

Creating an account on Trafiklab is required in order to create projects and API keys.

To start, go [the account creation page](https://developer.trafiklab.se/register).

{{% info %}} If you have a GitHub account, you can register and login through GitHub. In order to do so, just click
the "Register with github" button. {{% /info %}}

You need to fill in a valid email address, a username and a password. This email address will be used to contact you if we make changes
to an API you are using. Your email address will not be made public unless you share a project together with other users,
in which case your email adress will be visible for the other members of this project.

![Screenshot of the e-mail address and username fields](/media/2023/create-account.png)

After filling in your information, you need to accept the terms and conditions.

Hit the register button at the bottom of the page, and you will receive an email with a link to verify your email address.
After verifying you are ready to create your first project.

## Projects

{{% info %}}  You need an account in order to create projects. Haven't created an account
yet? [Get started here](#creating-an-account). {{% /info %}}

## Creating a project

After logging in, you will be re-directed to [your projects page](https://developer.trafiklab.se/project/list) where you
can create your very first project. In order to do this, hit the purple "New project" button in the top right corner and fill
in a cool name, project type and a short description of your next project. You can also add optional information like website and
open-source repository. Press the save button.

If you need to edit any of the details at a later stage you simply click the edit button in the top right corner.

After creating your project, you can start adding API keys. Select which APIs you want to use in the dropdown list and
click the "Add API key to project" button. Don't worry if you're still unsure about which ones you need - you can come
back and add or delete keys and other setting anytime you need.

![Screenshot of the API picking screen](/media/2023/add-api-key.png)

## Projects with multiple users

You can add or remove users to a project by contacting the Trafiklab team at info@trafiklab.se

At the bottom of the page you will see all users connected to the project. A user can have one out of three different Access Rights:
* **Read Only**: User has permission to access project content but cannot make any changes
* **Read/Write**: User has same allowance as Read Only user with added permission to modify and change content, e.g. API keys
* **Project Owner**: User has same allowance as Read/Write user with added permission to delete a project and handle project members

## API keys
In order to access the APIs at Trafiklab you need an API key. If you want to read more about the different APIs and 
datasets that are provided, check out the [**APIs**](/api/) page.

### Creating API keys

In order to create an API key, navigate to the project and select the API to add. Every API can only be added once to a
project.

![The new key option](/media/2023/create-API-key.png "The 'add key' dropdown")

Keys are created with a default profile, allowing you to test the API and build applications for home use. If you need
more API requests than allowed in the standard profile, you can create a request to upgrade the key for free.

### Upgrading API keys

When your application needs more API calls than your API key quota allow, you can upgrade your keys to a higher level.
Upgrading API keys is completely free of charge, and only needed to ensure all Trafiklab users can keep using the
service for
free.
![Screenshot of an api key with an upgrade link](/media/2023/upgrade-quota.png "Upgrade buttons can be seen for keys which can be upgrade")

In order to upgrade your API key, go to your project and click on the "Upgrade quota" button next to the API key that
you want
to upgrade.

![Screenshot of the key upgrade dialog](/media/2023/request-key-upgrade.png "The key upgrade request form")

Fill out the request form by choosing which level you would like to have from the dropdown and write a motivation.
Your motivation should include:

* A short description of the project
* An estimate of the number of requests your will need
* How many users/travelers will use your application

Your request will be approved within one or two workdays. If your request is declined, or if more information is needed,
you will receive email on your registered email address. You can see all your pending and closed requests on the page "My
key upgrades" under Projects & Keys.

### Requests which will not be approved

We aim to offer transport data to as many users as possible. However, in some cases your upgrade request may be denied.
The following requests will always be denied:

* **Silver or higher for departure boards used in Magic Mirror and other non-public projects.** The reason for this is
  that the bronze level offers enough API calls to show the next departures all day long. Better coding is more
  effecient than polling an API every 30 seconds or
  minute. [See Adjusting the update frequency during the day ](./../using-trafiklab-data/best-practices/limiting-requests.md#adjusting-the-update-frequency-during-the-day)
  in our best practices to learn how you can do this.
* **Upgrades on journey planning APIs in order to get analytics like isochrone maps and travel times between all cities,
  all current delays.** We want you to use the right tool for the job. We will deny all requests where the goal is to
  scrape API results in order to build analytics. As a rule of thumb, if you need to make more than 10 requests in order
  to get the data you need, you should
  be [using GTFS and GTFS-RT instead](../../public-transport-data/our-data-and-apis/gtfs/). As a result, you will be
  able to build better analytics, and they will take less time to generate, so this is a win-win.
* **Stress tests etc** Are not allowed and will never be approved. Ask us if you have special needs for your application.

{{% page-ref page="/api/" %}}

## Frequently asked questions

### Trafiklab

#### Why do I need API keys? Wouldn't it be easier without?

While we agree, we need the API keys in order to be able to offer this data. Every API call and GTFS download costs us
money. Through API keys we can prevent people from downloading the same GTFS file every 15 or 30 minutes, while we are
clear about the fact that it only updates once a day.

Don't worry if you need an upgrade - you'll most likely get it.

#### What happens when an API is discontinued?

We rarely discontinue APIs. When a change is coming up, users are notified in good time (often multiple months
before).

### Data

#### Vehicles are appearing in the realtime data, even though they aren't present in the static data. Why is this?

There might be a high load on a certain bus line, in which case the operator may decide to send out one or more extra
buses. These buses are not associated with a planned trip, but will still show up in the realtime data.

Vehicle position data can also include parked vehicles, vehicles on their way to their starting point, or on the way
back after their last stop.

#### Can I stress test the APIs?

No. If you're wondering if our APIs can handle a certain load, please ask instead.

#### Why doesn´t the usage tracker increase when I make requests using my API key?

Statistics are only updated once a day. Some API´s need up to 48 hours for statistics to become visible for Trafiklab users.

#### Why did my request for an API key upgrade get denied?

You will get a message describing the reason when an API key upgrade gets denied. Typically, this is due to magic mirror
solutions wanting to use more than 10.000 API calls per month, or due to using the wrong data type, in which case we
will point out how other data can make your life easier (for example, when using an API for analytics/mass queries
instead of our GTFS/GTFS-RT data)

### I still have questions

Don't hesitate and reach out to us! You can do so by posting to our support
forum: [https://support.trafiklab.se](https://support.trafiklab.se)
