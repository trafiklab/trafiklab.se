---
title: Keeping API keys secret
---

Your API keys are personal, and you should try to keep them secret. You shouldn't try hard, but just, you know, don't
post them in plain text on the internet.

{{% warning %}} Others using your API key might lead to your API key hitting its quota. We cannot reset your
API usage for this, and will not upgrade your key for this. If your key is being abused, assigning a new API key will
not fix these issues either, unless you take measures to prevent abuse. {{% /warning %}}

While you should keep the above disclaimer in mind, you can relax a bit as we do not know of any cases in where keys got
abused. You can find some tips on handling your API keys below.

## I have an open-source project

**Don't hardcode your API key, but make sure it can be configured in a configuration file!**

Most projects have a separte properties file that isn't committed to the versioning system. In git, you can use the
.gitignore file to exclude files from being committed. Save your key in a file that isn't comitted and explain how to
obtain and configure the needed API keys in your readme or documentation. This way others can use your project with
their own API keys.

## I'm distributing binaries

Well, they likely need to have the API key on board, and there's nothing wrong with that. Just include them in your app
or program if needed.

## I'm running my own (proxy-)server

You might be running your own server, to transform API data, to add more data, or for any other reason. In this case,
you might want to limit your server so only your own app can use it. Again, you shouldn't be aiming to build something
similar to the Great Firewall of China around your server. You can simply validate the user-agent to check if it matches
your app, or use rate-limiting to block others from scraping your API. The easiest solution to prevent others from
trying to use your server is of course to open-source it, allowing anyone to run their own instances (but we understand
that this isn't always possible).
