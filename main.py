import random

if __name__ == '__main__':

    N = 20

    truth = [0, 1, 1, 1, 0, 1, 1, 0]

    state = []

    for i in range(N):
        r = random.randint(0, 1)
        state.append(r)

    print("Truth", truth)
    print("State", state)

    connections = []

    for i in range(N):
        connections.append([random.randint(0, N - 1), random.randint(0, N - 1), random.randint(0, N - 1)])

    print("Connections", connections)

    state2 = []

    for j in range(N):
        a = state[connections[j][0]]
        b = state[connections[j][1]]
        c = state[connections[j][2]]
        num = a * 4 + b * 2 + c
        print("Nodes", a, b, c, num)
        state2.append(truth[num])
        print("State'", truth[num])

    state = state2
    print("State", state)
