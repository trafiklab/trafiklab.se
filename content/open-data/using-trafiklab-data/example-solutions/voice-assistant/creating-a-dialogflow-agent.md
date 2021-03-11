# Creating a DialogFlow agent

## I'm sorry, could you repeat that?

Language is hard. The first challenge when creating a \(voice\) assistant is understanding users, by both recognizing _
what they say_, and figuring out _what they mean_. Luckily we don't need to solve this problem entirely by ourselves.
There are already platforms available which take care of the speech recognition and the natural language processing
\(NLP\). Examples are Dialogflow \(Google\), Lex \(Amazon\), Bot Framework \(Microsoft Azure\), Snips, ...

Today we will explore Dialogflow, a service through which anyone can create apps on the Google Home platform, and with
little extra effort on other platforms as well. Other frameworks might have small differences in naming, but generally
have the same structure.

Head over to [the dialogflow website](https://dialogflow.com/) and sign in through a Google account. This Google account
can be used later on to test on your device \(you can add additional testing accounts as well\). Create a new _agent_
\(this is what an 'app' is called\) by filling in the name, and possibly changing the language. You can add other
languages to your _agent_ later on.

There are 3 core concepts needed to build our app.

### Intents

With intents, you configure which actions your user can undertake, and what they will say to take a certain action. Take
for example the following sentence: `When does the next train leave from Stockholm City ?`

When a user asks this, we want to show the next departures, for stop "Stockholm City", where the vehicle is a train. In
order to realise this, we configure various training phrases. In our example, we used 10 different ways of asking for
the next departure, with different stations and vehicles.

Now we create a new parameter for our intent. We will store the stop name here, and call our parameter location. We use
the Entity type `@sys.any`, meaning this can be anything. Setting this to, for example, @geo.city, would mean . Check
the box to make it required, and enter some questions which your assistant can ask when this parameter is missing. An
example is `From where do you want to leave?`.

Now we can mark the station names in our training phrases, and indicate that they will fill the location parameter. Now
our agent will accept any station name, and extract it as a variable.

When it comes to the train type, we do the same by creating a transportation-method variable. This case is a little
special though, as we only want a limited list: only bus, ferry, metro, tram or train is valid. To make things more
complex, not everyone will say metro. Some may use the word undergound instead. And is it ferry or boat? For this, we
can use entities with synonyms.

### Entities

Entities let you define `types` of variables. This influences how the speech recognition will autocorrect the input.
Built-in entities are for example

* `sys.geo-city`, which will autocorrect with city names
* `sys.geo-capital`, which will autocorrect with capital names
* `sys.airport`, which will autocorrect with airport names
* `sys.number`, `sys.flight-number`, `sys.weight-unit`, ...

Using `@sys.any` will accept any input, without trying to correct it to a certain set of names or a specific format.

While there is a wide range of built-in entities, we can also create our own. We will do this to recognize types of
transport. The advantage in doing this is that there will be less errors in the user input, and our application will
receive one of our given possibilities as transport mode. We create our own transport-method entity, and accept bus,
tram, train, metro and ferry. We enter some synonyms for each method, to ensure we understand our user well, but
dialogflow will internally replace the synonym with the reference value \( bus, tram, train, metro or ferry\) when
storing it in a variable. This means our own little server application which will deliver the data doesn't need to think
about synonyms.

**Important:** When adding a new language for your _agent_, you will need to create the entity again. In this case, use
the same reference values but use translated synonyms.

![Our own DialogFlow entity](../../../.gitbook/assets/image%20%286%29.png)

We now change our transportation method in our intent from `@sys.any` to `@transportation-method` to make use of our
newly created entity. Previously, when the user said "When does the next train in Stockholm leave", the voice assistant
might understand "train in" as "training", and store "training" in the variable. Now that we use our own entity, the
voice assistant knows what can go in the transportation-method variable. If it recognizes "training" where a
transportation method should go, it will automatically correct it to "train in", and store "train" in the variable.

At this point our users can ask "When does the next subway leave from Stockholm", and

* The intent will be detected
* The parameters will be extracted
* Subway will be replaced with metro in the variable

If either the location or transportation method aren't present, the user will receive one of the questions configured
for that parameter.

