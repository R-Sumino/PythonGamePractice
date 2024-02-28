QUESTION = [
    "サザエさんの旦那さんの名前は？",
    "カツオの妹の名前は？",
    "タラちゃんはカツオから見てどんな関係？"
]
R_ANS = ["マスオ", "ワカメ", "甥"]

for i, question in enumerate(QUESTION):
    print(question)
    ans = input()
    if ans == R_ANS[i]:
        print("正解です")
    else:
        print("不正解です")
