import re


class Node:
    def __init__(self, name, weight, children=None):
        self.name = name
        self.weight = int(weight)
        self.children = children

    def insert(self, node):
        self.children.remove(node.name)
        self.children.append(node)

    def find_parent(self, name):
        if not self.children:
            return False

        if name in self.children:
            return self
        else:
            for child in filter(lambda n: isinstance(n, Node), self.children):
                pos_parent = child.find_parent(name)
                if pos_parent:
                    return pos_parent

    def children_weight(self):
        return sum(map(lambda n: n.sum_weights(), self.children)) if self.children else 0

    def sum_weights(self):
        return self.weight + self.children_weight()


def parse_line(line: str) -> Node:
    raw_parsed = re.match(r'([a-z]+) \((\d+)\)(?: -> )?(.*)', line)

    name, weight = raw_parsed[1], raw_parsed[2]
    children = None if raw_parsed[3] == "" else [s.strip() for s in raw_parsed[3].split(',')]

    return Node(name, weight, children)


def build_tree(lines):
    nodes = list(map(parse_line, lines))

    def try_add(child):
        for n in nodes:
            parent = n.find_parent(child.name)
            if parent:
                parent.insert(child)
                return True

    while len(nodes) > 1:
        node = nodes.pop()
        success = try_add(node)

        if not success:
            nodes.insert(0, node)

    return nodes[0]


def build_tree_from_file(file_dir):
    with open(file_dir, 'r') as file:
        return build_tree(file.readlines())


def check_weights(node):
    weights = list(map(lambda n: n.sum_weights(), node.children))

    if sum(weights) == len(weights) * weights[0]:  # all the same elements.
        return None, None

    different_weight = next(weight for weight in weights if weights.count(weight) == 1)
    same_weight = weights[0] if weights[0] != different_weight else weights[1]

    return same_weight, different_weight


def find_wrong_weight(node):
    current_node = node

    previous_target = None

    while True:
        target, different = check_weights(current_node)

        problem_node = next((node for node in current_node.children if node.sum_weights() == different), None)

        if not (problem_node and problem_node.children):
            return previous_target - current_node.children_weight()
        else:
            previous_target = target
            current_node = problem_node


assert build_tree_from_file('./test.txt').name == "tknk"
assert find_wrong_weight(build_tree_from_file('./test.txt')) == 60

input_tree = build_tree_from_file('./input.txt')
print("Part 1:", build_tree_from_file('./input.txt').name)
print("Part 2:", find_wrong_weight(input_tree))
