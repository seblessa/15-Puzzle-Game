# Summary
**Authors**:
- [Sebastião Santos Lessa](https://github.com/seblessa/)
- [Margarida Vila Chã](https://github.com/margaridavc/)

<br />

Python aplication of the 15 puzzle game. The game is playble, you can input the initial state or one generate randomly. It's also possivel to use search algorithms to find the shortest path between the an initial and final configuration.

# Versions
The versions of our systens used to develop and test the app are:
- Ubuntu 22.04.2
- macOS Ventura 13.1

The python versions testes in are:
- 3.10.6
- 3.11.2

# Execution
To run the app you need to enter the directory where `start.py` is located and run:


```
python3 start.py
```
<br />

To execute a search with a given algorithm you need to run:

```
python3 start.py algorithm < config.txt
```

It's possible to print the path between the initial and final state by activateing the flag:

```
python3 start.py algorithm -p < config.txt
```
ou
```
python3 start.py algorithm --print < config.txt
```
<br />

The available algorithms are:

```
DFS
BFS
IDFS
Greedy-misplaced
Greedy-manhattan
Astar-misplaced
Astar-manhattan
```

The file config.txt can have any name(just change it when you run it too) and needs to be in this format:
```
1 2 3 4 5 6 8 12 13 9 0 7 14 11 10 15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0
```
