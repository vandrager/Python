#4-2, 4번문제 리스트가 리스트로 인식이 안되는 문제
dis = {"pip": ["love", "you", "me"]}
print(type(dis["pip"]))
print(type(dis["pip"]) is list)

chr = {
    "name": "기사",
    "level": 12,
    "item": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
        },
        "skill": ["swing", "power swing", "full swing"],
    }

print(type(chr["skill"]) is list)
print(type(chr["item"]["sword"]))
print(type(chr["item"]))
print(type(chr["skill"]))
print(len(chr["item"]))

for k in chr:
    v = type(chr[k])
    if v is dict:
        for u in chr[k]:
            print(u, ":", chr[k][u])
    elif v is list:
        for j in (chr[k]):
            print(k, ":", j)
    else:
        print(k, ":", chr[k])


print()

