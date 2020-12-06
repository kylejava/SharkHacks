# SharkHacks
PokeFind project using Twitter API
by Kyle and Neala

## Inspiration
We wanted to build a fun project, and we thought a project related to Pokemon was a great idea. Sharkhacks is a great hackathon to showcase such a project.

## What it does
PokeFind is a Twitter bot that finds out which pokemon the user is based on their birthday. The user would tweet at our bot like so, @PokeFind_ #whatpokemonami 01/01/2000". Then the bot will parse through the tweet obtaining the birthday, the birthday is then sent to our pokedex entry finding function, and will return the index number of the pokedex based on the birthday. We retrieve info of that pokemon using the PokeApi and tweet out information of that pokemon.


## How we built it
We built this bot using Python. We were able to filter, send, and retrieve tweets using the Twitter API. We were also able to get info about each pokemon through the PokeAPI.

## Challenges we ran into
We couldn't find a solution to keep the bot running, the only way we were able to keep the bot going is putting the function in a while loop and keep the program running on our computer.

## Accomplishments that we're proud of
Being able to download the image from the Pokemon API and tweeting it back to the user.  Being able to obtain the birthday from the user's tweet.


## What we learned
We learned more about Python and how to use API's. We also learned how to use the Twitter API more.

## What's next for PokeFind
Finding a way to keep the bot running, by using cloud solutions.
