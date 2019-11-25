import json

python_dict = {
    "이름":"홍길동",
    "나이": 25,
    "거주지": "서울",
    "신체 정보": {
        "키" : 175.4,
        "몸무게" : 71.2
    },
    "취미": [
        "등산",
        "자전거 타기",
        "독서"
    ]

}
print(type(python_dict), python_dict)

json_data = json.dumps(python_dict) # json 형태로변환
print(type(json_data), json_data)

json_data = json.dumps(python_dict, sort_keys = True, indent = 4, ensure_ascii=False)
print(type(json_data), json_data)

python_dict2 = json.loads(json_data)
print(type(python_dict2), python_dict2)

student = [
    {
        'no': 1,
        'name': '김승영',
        'score': {'국어': 90, '영어': 90, '수학': 90}
    },
    {
        'no': 2,
        'name': '지재삼',
        'score': {'국어': 80, '영어': 79, '수학': 69}
    }
]

print(type(student))

#write
json_student = json.dumps(student) # json 형태로 변환
print(type(json_student))

with open('json_test.txt', 'w', encoding ='utf-8') as f:
    json.dump(json_student, f)  # json 파일 작성 한굴은 unicode형태로 저장

with open('json_test.txt', 'r', encoding ='utf-8') as f:
    x = json.load(f)    #json 형태의 파일 load
    print(type(x), x)

students = json.loads(x)
type(students)
for std in students:
    print("{}{} # {}{}{}"
            .format(type(std['no']),
                    type(std['name']),
                    type(std['score']['국어']),
                    type(std['score']['영어']),
                    type(std['score']['수학'])))
    print(std['no'], std['name'], end = ' ')
    total = sum([x for x in std['score'].values()])
    #total = std['score']['국어'] + std['score']['영어'] + std['score']['수학']
    [print(score, end=' ') for score in std['score'].values()]
    print(total, total /float(3))