if __name__ == '__main__':

    truth = [0, 1, 1, 1, 0, 1, 1, 0]

    state = []

    for i in range(20):
        state.append(1)

    print("Truth", truth)
    print("State", state)

    connections = []

    for i in range(20):
        connections.append([1, 2, 12])

    state2 = []

    for j in len(state):
        a = connections[j][0]
        b = connections[j][1]
        c = connections[j][2]
        print("Nodes", a, b, c)

    print("Connections", connections)
