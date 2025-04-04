# Maze Solver in Python

This project is a maze generator and solver implemented in Python for the [Maze Solver course on Boot.dev](https://www.boot.dev/courses/build-maze-solver-python). It generates a maze in a different way than [I did here (randomized DFS)](https://github.com/jakemckenzie/ShortestTradeRoute) or it [might be this one](https://github.com/jakemckenzie/traversing-on-the-cheap) which is apparently [still on twitter](https://x.com/granderojo/status/1001069704486703104). This is a shorter refresher for graphs as I haven't done them in a while and was mostly just fiddling with fiddling with the gui. Coming from web I've read a lot about mvc at this point, thanks DHH. It ensures when you're writing in a sloppy (<3) language like python you can keep the the application logic concerns separated. If I were to approach this problem again [I think I'd use maximum flow](https://youtu.be/dorq_YA6plQ?si=wh9nXvrhr8zGOoxj&t=858), since I've never actually solve this problem that way.

[Roughgarden has a series of books](https://timroughgarden.org/books.html) on algorithms that's a good primer to [TCRC](https://archive.org/details/introduction-to-algorithms-third-edition-2009). 

## Features

- **Maze Generation**: no loops, just pure recursion, had to increase the recursion limit because lol python
- **Maze Solving**: uses dfs
- **Animation**: animate() in model.py doesn't need to be in view because it complies with ["immediate mode M/V/C"](https://johno.se/book/immvc.html), I included init to comply with java classes rules and OO
- **MVC Architecture**: Casey Muratori explains this fairly good job of [explaining immediate mode M/V/C here](https://youtu.be/Z1qyvQsjK5Y?si=BCjF3VZ_dotFz9LB).
