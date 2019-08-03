import sys

S = sys.stdin.readline().rstrip()
last_char = S[len(S)-1]

for idx, char in enumerate(S[:-1]):
    if char == last_char:
        is_pal = True
        s = idx
        e = len(S)-1

        while s <= e:
            if S[s] != S[e]:
                is_pal = False
                break
            s += 1
            e -= 1

        if is_pal:
            print(len(S)+idx)
            exit(0)

print(len(S)*2-1)
