# PotatoLang2

My programming language

## Quick Examples

Say "Hello world!":
```cs
printf("Hello world!")

>>> Hello world!
```
***
Ask a question and print the response:
```cs
declare name = inputf("What's ur name ?\nYou: ")

printf("Hi [name] !")

>>> What's ur name ?
>>> You: Artic
>>> Hi Artic !
```
***
Create a function and call it:
```cs
build SayHelloTo(name)
{
    printf("Hello [name] !")
}

SayHelloTo("Artic")

>>> Hello Artic !
```
***
Return a string:
```cs
build ReturnString()
{
    declare myString = "Hello world!"
    return myString
}

ReturnString()
printf(myString)

>>> Hello world!
```
***
The modules:

_module.potato_
```cs
build hi(name)
{
    printf("Hi [name] !")
}
```
_file.potato_
```cs
with module.potato

hi("Artic")

>>> Hi Artic !
```

***

## You want to help me ?
It's simple, [join the discord](https://discord.gg/H63XBBBkMC) and post your code in the channel "project-potatolang"

I will merge the code every day if your code adds features to the language ! 

## How to install it ?

1. [Download the language](https://github.com/ArticOff/PotatoLang/raw/main/PotatoLang2.exe)
2. [Download some examples](https://github.com/ArticOff/PotatoLang/tree/main/example)
3. Put them in a common folder
4. Open a terminal
5. Type "./PotatoLang2 helloWorld.potato"
6. You're done !

***

That's all

***

- [The official discord server](https://discord.com/invite/h7YFnP45jv)
- [The github issues page](https://github.com/ArticOff/potatoLang/issues)
- [Click here to download](https://github.com/ArticOff/potatoLang/archive/refs/heads/main.zip)
- [Wikipedia](https://en.wikipedia.org/wiki/Draft:Potato_Lang)

Made with ❤️ by [Artic](https://discord.com/users/855783629047988274) and [CodeSec Community](https://discord.gg/H63XBBBkMC) (SilentHealer's server)
