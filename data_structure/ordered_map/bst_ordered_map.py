from collections import deque

# BST로 Ordered Map 짜기
# find, insert, delete, update, range query


class Node:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    @property
    def has_children(self):
        return self.left or self.right

    def __repr__(self):
        return f"<Node Pair = {self.key}:{self.value}>"


class BstOrderedMap:
    def __init__(self, node: Node):
        self.root = node
        self.count = 1

    def insert(self, new_node: Node):
        current = self.root
        while True:
            if current.key > new_node.key:
                if current.left is None:
                    new_node.parent = current
                    current.left = new_node
                    break
                else:
                    current = current.left
            else:
                if current.key == new_node.key:
                    raise TypeError("중복된 키를 넣을 수 없습니다.")
                if current.right is None:
                    new_node.parent = current
                    current.right = new_node
                    break
                else:
                    current = current.right

        self.count += 1
        print(f"삽입 성공! 부모: {new_node.parent.key},  삽입된 노드 : {new_node.key}")

    def delete(self, key):
        # 오른쪽 서브트리에서 제일 작은 값을 가진 노드를 지울 노드와 교체
        if self.count <= 1:
            raise ValueError("트리의 원소는 1개 이상이어야 합니다.")

        delete_node = self.find_node(key)

        def kill_node(node: Node):
            if node.parent.key > node.key:
                node.parent.left = None
            else:
                node.parent.right = None

        if delete_node.has_children:  # 지울 노드에 자식이 있다면 어떤 노드와 replace 할 것인지 찾기
            if delete_node.right:
                replace_node = delete_node.right
                while replace_node.left:
                    replace_node = replace_node.left
            else:
                replace_node = delete_node.left
                while replace_node.right:
                    replace_node = replace_node.right

            kill_node(replace_node)
            delete_node.key, delete_node.value = replace_node.key, replace_node.value

        else:  # 자식이 없다면 그냥 지우기
            kill_node(delete_node)

        self.count -= 1
        print(f"{key} 삭제 성공")

    def update(self, key, new_value):
        self.find_node(key).value = new_value
        print(f"값 변경 성공! 새로운 값 : {new_value}")

    def find_node(self, query):
        node = self.root

        while node.key != query:
            if node.key > query:
                node = node.left
            else:
                node = node.right

        if not node:
            raise KeyError(f"키 : {query} 가 존재하지 않습니다")

        return node

    def find(self, query):
        return self.find_node(query).value

    def range_query(self, lo, hi, current_node=False) -> list:
        node = current_node

        if node is False:
            node = self.root
        elif node is None:
            return []

        if node.key < lo:
            return self.range_query(lo, hi, node.right)
        elif node.key == lo:
            return [(node.key, node.value)] + self.range_query(lo, hi, node.right)
        elif lo < node.key < hi:
            return self.range_query(lo, hi, node.left) + [(node.key, node.value)] + self.range_query(lo, hi, node.right)
        elif node.key == hi:
            return self.range_query(lo, hi, node.left) + [(node.key, node.value)]
        else:  # hi < key
            return self.range_query(lo, hi, node.left)

    def bfs(self):
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            print(node.value, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

    def dfs_pre(self, node=None):
        if not node:
            node = self.root

        print(node.value, end=" ")

        if node.left:
            self.dfs_pre(node.left)
        if node.right:
            self.dfs_pre(node.right)

    def dfs_in(self, node=None):
        if not node:
            node = self.root

        if node.left:
            self.dfs_in(node.left)
        print(node.value, end=" ")
        if node.right:
            self.dfs_in(node.right)

    def dfs_post(self, node=None):
        if not node:
            node = self.root

        if node.left:
            self.dfs_post(node.left)
        if node.right:
            self.dfs_post(node.right)
        print(node.value, end=" ")

    def rotate_cw(self, node=None):
        if not node:
            node = self.root

        if not node.left:
            print("can't rotate cw")
            return

        new_root = node.left
        node.left = new_root.right
        new_root.right = node

    def rotate_ccw(self, node=None):
        if not node:
            node = self.root

        if not node.right:
            print("can't rotate ccw")
            return

        new_root = node.right
        node.right = new_root.left
        new_root.left = node


bst_map = BstOrderedMap(Node(10, '10'))
bst_map.insert(Node(5, '5'))
bst_map.update(5, 'new5')
#bst_map.bfs()
#print(bst_map.find_node(5))
bst_map.insert(Node(3, '3'))
bst_map.insert(Node(7, '7'))
bst_map.insert(Node(15, '15'))
bst_map.insert(Node(17, '17'))
bst_map.insert(Node(13, '13'))
bst_map.bfs()
bst_map.dfs_pre()
print()
print(bst_map.range_query(3, 7))
print()
print(bst_map.root)

