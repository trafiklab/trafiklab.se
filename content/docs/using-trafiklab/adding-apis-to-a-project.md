---
title: Adding APIs to a project 
description: Adding more APIs to an existing project 
weight: 40
---
{{% warning %}}  Disable browser plugins like Google Translate when creating a project. They are known to
cause issues on the developer portal, when logging in, creating accounts and creating projects. {{% /warning %}}

When you want to add more APIs to an existing project, you need to head edit the project first. This can be done by
heading to your "profile and projects" page (found in the dropdown from your username in the top-right corner). From
the "profile and projects" page, choosethe project you want to edit and click on its name.

Now choose "Redigera" in the navigation bar. This will bring up the edit interface. Now you can select all apis you want
to add and press "save". The newly added APIs will now show up on the project page.

{{% warning %}}  You can see a warning when saving a project that contains deprecated APIs. Continue reading
to learn how to resolve this.  {{% /warning %}}

### Saving a project that contains deprecated APIs

When editing an existing project, you might be confronted with a warning when you save.

![The warning which is shown when your project contains deprecated APIs](/media/2020/05/remove-old-keys.png)

This means you still have an old API in your project, while the API has been shut down. In this case you will be forced
to remove the old API and its associated keys. Press the "Delete keys" button and save the project to make it "normal"
again, after which you can edit it as you like.

{{% note %}} Right now, the developer portal is not available in English yet. While these guides should help you to get
started, the following list of common Swedish words should help you to get around on the developer portal.

* **Spara**: Save/Submit
* **Tillbaka**: Back
* **Radera**: Delete
* **Hämta**: Fetch
* **Skapa**: Create
* **Nyckel**: (API) key
* **Nivå**: Level
* **Konto**: Account
{{% /note %}}

{{% page-ref "getting-api-keys" %}}