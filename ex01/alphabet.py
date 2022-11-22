import random
import time
word_num = random.randint(8,15)
del_word_num = random.randint(2, 5)



def shutudai(word_list):
    taisyou = []
    kesson = []
    hyouji = []
    for i in range(word_num):
        key = word_list.pop(random.randint(0,len(word_list)-1))
        taisyou.append(key)
    hyouji = taisyou.copy()
    for j in range(del_word_num):
        key = hyouji.pop(random.randint(0, len(hyouji)-1))
        kesson.append(key)

    print("対象文字：")
    for moji in taisyou:
        print(moji, end=" ")
    # print()
    # print("欠損文字：")
    # for moji in kesson:
    #     print(moji, end=" ")
    print()
    print("表示文字：")
    for moji in hyouji:
        print(moji, end=" ")
    print()

    kesson_num = (input("欠損文字はいくつあるでしょうか？"))
    if kesson_num == str(del_word_num):
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
        for k in range(del_word_num):
            ch_moji = input(f"{k+1}つ目の文字を入力してください")
            if ch_moji in kesson:
                kesson.remove(ch_moji)
            else:
                print("不正解です。またチャレンジしてください")
                break
            if k+1 == del_word_num:
                print("完答おめでとう！！！")
    else:
        print("不正解です。またチャレンジしてください")
    print("-------------------")

if __name__ == "__main__":
    word_list = []
    for i in range(26):
        word_list.append(chr(65+i))

    start_time = time.time()
    shutudai(word_list)
    end_time = time.time()
    print(f"所要時間：{(end_time-start_time)}")