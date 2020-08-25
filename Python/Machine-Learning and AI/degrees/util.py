class Node:
    def __init__(self, state, parent, action):
        self.state = state # persion_id
        self.parent = parent # persion_id of node that generated this one
        self.action = action # movie_id


class StackFrontier:
    def __init__(self):
        self.frontier = []
        self.explored = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def isExplored(self, state):
        return any(node_state == state for node_state in self.explored)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            self.explored.append(node.state)
            return node


class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            self.explored.append(node.state)
            return node
