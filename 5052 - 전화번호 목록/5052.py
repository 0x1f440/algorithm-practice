class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_match = False

    def add_node(self, number: str):
        current = self

        for val in number:
            if val in current.children:
                if current.children[val].is_match:
                    return False
            else:
                current.children[val] = Node(val)
            current = current.children[val]

        if current.children:
            return False

        current.is_match = True
        return True


def main():
    for case in range(int(input())):
        trie = Node("")
        integrity = True
        numbers = []

        for _ in range(int(input())):
            numbers.append(input())

        for number in numbers:
            if not trie.add_node(number):
                integrity = False
                break

        print("YES" if integrity else "NO")


if __name__ == '__main__':
    main()
