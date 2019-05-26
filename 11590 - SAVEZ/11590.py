import sys

# i번째와 j번째 문자열을 xi, xj (단 i<j)이라고 할 때, xj의 접미/접두사가 xi이면 subsequence를 만들 수 있다.
# 가장 긴 subsequence의 길이를 구하는 문제.
# Trie + DP 문제였다.
# 포인트는 인풋을 받아 Trie에 집어넣는 동시에 현재 선택할 수 있는 최장의 루트를 취하는 것.
# A-ABA-A-A-ABABA인 경우, ABABA는 A-ABA-ABABA 루트보다 A-A-A-ABABA 루트를 취하는 게 낫다는 소리다.


class Trie:
    result = 0

    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_match = False
        self.chain = 1

    def add(self, query):
        current = self
        candidates = []

        for idx, char in enumerate(query):
            if char in current.children:
                # is_match라면 접미사이기 때문에 subsequence 후보로 저장해 둔다.
                if current.children[char].is_match:
                    candidates.append((idx+1, current.children[char].chain))
            else:
                # 없는 쿼리였다면 새로운 노드를 만들어서 넣는다.
                current.children[char] = Trie(char)
            current = current.children[char]

        if current.is_match:
            current.chain += 1
        else:
            current.is_match = True

        # subsequence 후보 중 접두사인 것을 찾고, 그 중 가장 긴 체인을 가진 노드와 연결한다.
        max_chain = 0
        for substring_length, chain in candidates:
            if query[:substring_length] == query[len(query) - substring_length:]:
                max_chain = max(max_chain, chain)

        current.chain = max_chain + 1
        Trie.result = max(Trie.result, current.chain)


def main():
    trie = Trie(None)
    for _ in range(int(sys.stdin.readline())):
        trie.add(sys.stdin.readline().rstrip('\n'))

    print(Trie.result)


if __name__ == '__main__':
    main()
