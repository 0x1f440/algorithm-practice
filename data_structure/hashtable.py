from hasher import pearson_hash

# Open Addressing
# Tombstone (lazy deletion)
# Improvement : after searching an element, relocate the element to the first location marked for deletion


class HashTable:
    TOMBSTONE = [object(), None]

    def __init__(self):
        self.clear()

    def __setitem__(self, key, value):
        try:
            self.insert(key, value)
        except KeyError:
            self.update(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __delitem__(self, key):
        self.delete(key)

    def get_key(self, idx):
        return self.table[idx][0]

    def find_slot(self, key):
        idx = pearson_hash(key)

        while self.table[idx]:
            if self.get_key(idx) == key:
                return idx
            idx += 1

        raise KeyError(f"{key}를 찾으려고 했지만 유감! 존재하지 않습니다")

    def insert(self, key, val):
        idx = pearson_hash(key)

        while self.table[idx]:
            if self.get_key(idx) == key:
                raise KeyError(f"당신은 똑가튼 키를 입력해서 고먐미의 저주를 받아따!!! 중복된 키는 {key}이다!!!")
            idx += 1

        self.table[idx] = (key, val)
        print(f"{idx}번 인덱스에 {key}: {val} 을 성공적으로 삽입했습니다")

    def delete(self, key):
        self.table[self.find_slot(key)] = self.TOMBSTONE

    def update(self, key, val):
        print(f"{key}키의 값이 {val}로 바뀌었습니다")
        self.table[self.find_slot(key)] = (key, val)

    def get(self, key):
        return self.table[self.find_slot(key)][1]

    def clear(self):
        # noinspection PyAttributeOutsideInit
        self.table = [None] * 256


a = HashTable()
a["key1"] = "val1"  # a.insert("key1", "val1")
print(a["key1"])  # a.get("key1")
a["key1"] = "new_val1"  # a.update("key1", "new_val1")
print(a["key1"])  # a.get("key1")

del a["key1"]  # a.delete("key1")
print(a.table[100] == HashTable.TOMBSTONE)

a.insert("key2", "val2")
print(a.get("key2"))
