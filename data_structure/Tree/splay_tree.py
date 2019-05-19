from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @property
    def has_children(self):
        return self.left or self.right

    def __repr__(self):
        return f"<Node value:{self.value}>"


class SplayTree:
    def __init__(self, node):
        if isinstance(node, Node):
            self.root = node
        else:
            self.root = Node(node)
        self.count = 1

    def get_node_and_parents(self, query):
        node = self.root
        parents = []

        while node.value != query:
            parents.append(node)
            if node.value > query:
                node = node.left
            else:
                node = node.right

        if not node:
            raise KeyError(f"키 : {query} 가 존재하지 않습니다")

        return node,     parents

    def splay(self, query):
        node_to_splay, parents = self.get_node_and_parents(query)
        print(f"\n====== splay start ======\n{node_to_splay} will be splayed and parents are {parents}")

        if node_to_splay is self.root:
            print(f"{query}은/는 이미 루트입니다!")
            return

        # while parent is not root
        while len(parents) > 1:
            old_root = parents.pop()
            grand_parent = parents[-1]

            if node_to_splay.value < old_root.value:
                old_root.left = node_to_splay.right
                node_to_splay.right = old_root
            else:  # new_root.value > old_root.value:
                old_root.right = node_to_splay.left
                node_to_splay.left = old_root

            if old_root.value < grand_parent.value:
                grand_parent.left = node_to_splay
            else:
                grand_parent.right = node_to_splay

        #  when parent is root
        if node_to_splay.value < self.root.value:
            self.root.left = node_to_splay.right
            node_to_splay.right = self.root
            self.root = node_to_splay
        else:
            self.root.right = node_to_splay.left
            node_to_splay.left = self.root
            self.root = node_to_splay

        print("====== splay result ======")
        self.bfs()
        self.dfs_in()

    def insert(self, new_node: Node):
        current = self.root

        while True:  # find right place to insert
            if current.value > new_node.value:
                if current.left is None:
                    new_node.parent = current
                    current.left = new_node
                    break
                else:
                    current = current.left
            else:
                if current.value == new_node.value:
                    raise TypeError("중복된 키를 넣을 수 없습니다.")

                if current.right is None:
                    new_node.parent = current
                    current.right = new_node
                    break
                else:
                    current = current.right

        self.count += 1
        print(f"삽입 성공! 부모: {new_node.parent.value},  삽입된 노드의 키 : {new_node.value}")

    def insert_nodes(self, list_of_values: list):
        for value in list_of_values:
            if isinstance(value, Node):
                self.insert(value)
            elif isinstance(value, int):
                self.insert(Node(value))

    def delete(self, query):
        # 오른쪽 서브트리에서 제일 작은 값을 가진 노드를 지울 노드와 교체
        if self.count <= 1:
            raise ValueError("트리의 원소는 1개 이상이어야 합니다.")

        delete_node = self.get_node_and_parents(query)[0]

        def _kill_node(node: Node, parent_node: Node):
            if parent_node.value > node.value:
                parent_node.left = None
            else:
                parent_node.right = None

        if delete_node.has_children:  # 지울 노드에 자식이 있다면 어떤 노드와 replace 할 것인지 찾기
            parent = delete_node
            if delete_node.right:
                replace_node = delete_node.right
                while replace_node.left:
                    parent = replace_node
                    replace_node = replace_node.left
            else:
                replace_node = delete_node.left
                while replace_node.right:
                    parent = replace_node
                    replace_node = replace_node.right

            _kill_node(replace_node, parent)
            delete_node.value = replace_node.value

        else:  # 자식이 없다면 그냥 지우기
            _kill_node(delete_node)

        self.count -= 1
        print(f"{query} 삭제 성공")

    def dfs_in(self, node=None):
        if not node:
            print("dfs_in : ", end="")
            node = self.root

        if node.left:
            self.dfs_in(node.left)
        print(node.value, end=" ")
        if node.right:
            self.dfs_in(node.right)

    def bfs(self):
        dq = deque([self.root])
        print("bfs : ", end="")
        while dq:
            node = dq.popleft()
            print(node.value, end=" ")

            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        print()


def main():
    tree = SplayTree(50)
    tree.insert_nodes([30, 60, 10, 40, 90, 20, 70, 100, 15])
    tree.delete(60)
    tree.insert(Node(80))
    tree.bfs()
    tree.dfs_in()
    print()
    tree.splay(30)


if __name__ == "__main__":
    main()
