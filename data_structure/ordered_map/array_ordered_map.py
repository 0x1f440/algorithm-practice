from bisect import *

# 정렬된 배열만으로 Ordered Map 짜기
# (find, insert, delete, update, range query, 정해진 갯수만큼 가져오기, predecessor 찾기)


class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        x, y = self, other
        if isinstance(other, int):
            return x.key < other
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other

    def __repr__(self):
        return f"<Pair {self.key}:{self.value}>"


class ArrayOrderedMap:
    def __init__(self):
        self.table = [None] * 256
        self.count = 0

    def insert(self, pair: Pair):
        index = bisect_left(self.table[:self.count], pair)
        if index > 0 and self.table[index-1].key == pair.key:
            raise KeyError("키가 중복인데요")

        if index < self.count:
            for i in range(self.count, index, -1):
                self.table[i] = self.table[i-1]

        self.table[index] = pair
        self.count += 1
        print(f"{pair} 삽입 성공")

    def delete(self, key):
        index = self.get_index(key)
        for i in range(index, self.count):
            self.table[i] = self.table[i+1]

        self.count -= 1
        print(f"{key} 삭제 성공")

    def find(self, key):
        return self.table[self.get_index(key)].value

    def get_index(self, key):
        index = bisect_left(self.table[:self.count], key)
        if self.table[index].key == key:
            return index
        else:
            raise KeyError(f"키가 존재하지 않습니다 : {key}")

    def update(self, key, new_value):
        self.table[self.get_index(key)].value = new_value
        print(f"{key}의 값이 {new_value}로 변경되었습니다.")

    def range_query(self, lo, hi):
        for i in range(bisect_left(self.table[:self.count], lo), bisect_right(self.table[:self.count], hi)):
            print(f"{self.table[i].key}:{self.table[i].value}", end=" ")
        print()

    def print(self):
        for pair in self.table[:self.count]:
            print(f"{pair.key}:{pair.value}", end=" ")
        print()


a = ArrayOrderedMap()
a.insert(Pair(1, 111))
a.insert(Pair(5, 555))
a.insert(Pair(6, 666))
a.insert(Pair(3, 333))
a.insert(Pair(4, 444))
a.insert(Pair(2, 222))
a.print()
a.delete(2)
a.delete(4)
a.update(3, "바뀐3")
a.print()
a.insert(Pair(-1, 15))
a.print()
a.range_query(-1, 2)
print(a.find(3))
