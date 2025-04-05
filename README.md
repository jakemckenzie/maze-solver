# Maze Solver in Python

This project is a maze generator and solver implemented in Python for the [Maze Solver course on Boot.dev](https://www.boot.dev/courses/build-maze-solver-python). It generates a maze in a different way than [I did here (randomized DFS)](https://github.com/jakemckenzie/ShortestTradeRoute) or it [might be this one](https://github.com/jakemckenzie/traversing-on-the-cheap) which is apparently [still on twitter](https://x.com/granderojo/status/1001069704486703104). This is a shorter refresher for graphs as I haven't done them in a while and was mostly just fiddling with fiddling with the gui. Coming from web I've read a lot about mvc at this point, thanks DHH. It ensures when you're writing in a sloppy (<3) language like python you can keep the the application logic concerns separated. If I were to approach this problem again [I think I'd use maximum flow](https://youtu.be/dorq_YA6plQ?si=wh9nXvrhr8zGOoxj&t=858), since I've never actually solve this problem that way.

[Roughgarden has a series of books](https://timroughgarden.org/books.html) on algorithms that's a good primer to [TCRC](https://archive.org/details/introduction-to-algorithms-third-edition-2009). 

## Features

- **Maze Generation**: no loops, just pure recursion, had to increase the recursion limit because lol python
- **Maze Solving**: uses dfs
- **Animation**: animate() in model.py doesn't need to be in view because it complies with ["immediate mode M/V/C"](https://johno.se/book/immvc.html), I included init to comply with java classes rules and OO
- **MVC Architecture**: Casey Muratori explains this fairly good job of [explaining immediate mode M/V/C here](https://youtu.be/Z1qyvQsjK5Y?si=BCjF3VZ_dotFz9LB).

## Update 1

- **Max Flow aka Min Cut**: I'm still reading about about I would accomplish this given my current data structure. NetworkX min_cost_flow() requires a capacity and weight, I don't know if it's worth translating the data structure but we'll see.
- **Thorup's**: hierachical bucketing + tree components? it appears to exploit properties of undirected graphs with (varying?) integer weights so it doesn't make sense to use here. it also requires a lot of preprocessing to get the data structure right. here is a [good presentation on thorup](https://github.com/npruehs/thorup), I was unaware of the sorting bottle neck for dijkstra's algorithm. the most efficient algorithms tend to require data structures that are a pain in the ass to implement, probably best to stick to calling a library
- **Dijkstra's with Min-Heap Queue**: I ended up going with Dijkstra's algorithm, it required no modifications to gui and once the algorithm was written it just worked. this implementation, and I think the algorithm in general, reduces down to bfs + priority queue. It's interesting when I was taking algorithms over the summer with (years ago at this point) [professor nascimento](https://www.anderson-nascimento.org/), he gave us [an assignment](https://github.com/jakemckenzie/traversing-on-the-cheap/blob/master/main.java) that was meant to be solved with dynamic programming. I the over eager student exclaimed "I bet I can solve with Dijkstra's algorithm in better than O(n^2)!". He was skeptical but it turned [most dynamic programming problems](https://youtu.be/NzgFUwOaoIw?t=15m20s), and [many problems in software](https://courses.csail.mit.edu/6.854/20/sample-projects/A/connection%20_between_SSSP.pdf), reduce to similar sorts of problems. The entire difficulty of that project and this one is representing the data structure somehow, the algorithms are quite elegant.
- **Thoughts**: I've been doing a lot of functional programming lately (F#, might post a repo, Ocaml and Elixir before that) and years ago I tried to learn Haskell after being excited about streams in Java 8. related to the prior paragraph one of the major pitfalls of functional programming is having to manage I/O and maintain the software you write with it. Abstracting out your data completely can write really elegant code for a time but I think functional programming will have a hard time to take off over object-oriented or imperative programming because it's data agnostic and the world is not data agnostic. Thorup's and Min-Cut(Max Flow) require a lot of wrangling of data structures to get to work properly and the [maintainability of that software is questionable](https://www.youtube.com/watch?v=SPwnfSmyAGI). We'd like to just write it once and forget it. I don't think that will ever be a reality so while you can reduce most dynamic programming problems to graph problems, unless we get some way to do it reliably, it's probably not worth bothering.
- **Future Work**: If I get some extra time or get bored I'll try to think of an elevent way to represent the data structures for min-cut of the existing code to solve the maze I'll write that algorithm but I like where this project is for now