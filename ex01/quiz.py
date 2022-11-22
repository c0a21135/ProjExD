from random import choice


def shutudai():
    que_dict = {}
    que_dict["サザエのダンナの名前は？"] = ["マスオ","ますお"]
    que_dict["カツオの妹の名前は？"] = ["ワカメ","わかめ"]
    que_dict["タラオはカツオから見てどんな関係？"] = ["甥","おい","甥っ子","おいっこ"]
    question, answer = choice(list(que_dict.items()))
    return question, answer
    

if __name__ == "__main__":
    question, f_ans = shutudai()
    print("問題：")
    print(question)
    ans = input("答えるんだ：")
    if ans in f_ans:
        print("正解！！！")
    else:
        print("出直してこい")
