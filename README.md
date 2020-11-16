# Random Boolean Network

[Inspired by](https://www.youtube.com/watch?v=mCML2B94rUg&feature=youtu.be) 

## Network
Connection between nodes ar modeled by node numbers, each node has 3 other nodes connections

the network is calculated at system start and is fixed. Each node is allocated 3 other nodes that are not itself

```
i E (0:N)
state[i] => {j,k,l} where (j,k,l) E (0:N & !i)
```
N > 0

i in range(N)

j in range(N) && j # i

k in range(N) && k ## i

l in range(N) && l # i

example:
```
state[0] = 0 // false
connections[0] = [4,7,11]
```

## Truth table
each node value is true or false, in binary that is 0 or 1
```
true = 1
false = 0
```

taking 3 nodes value together we get a 3 digits binary number:
```
0 [0,0,0]
1 [0,0,1]
2 [0,1,0]
3 [0,1,1]
4 [1,0,0]
5 [1,0,1]
6 [1,1,0]
7 [1,1,1]
```
the truth table has 8 values calculated at random when system starts and never changes over the life of the system

```
truth[i] => 0 OR 1
```

for each possible combination of node values wer generate a random new value:

```
node[i] => random(0,7)
```

Now we can calculate the next state of the system by matching the connection state to a number from the truth table.

```
state[i] => [j,k,l] => state[j], state[k], state[l] => truth[m]
```
where m is the value of converting the binary single digit of the connection state by placing each binary value in the 
different location.

for example:
```
state[j] = 0
state[k] = 1
state[l] = 0
```

then the binary value is
```
010
```
which is equal to 2
so the new state' (prime) value for node i is

```
state'[i] = truth[2]
```

