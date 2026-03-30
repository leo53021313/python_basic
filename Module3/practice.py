# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」
import random

user_input = -1
random_int = random.randint(1, 100)
# print("Rand: " + str(random_int))

while True:
    try:
        user_input = int(input("請輸入 1 到 100 之間的整數: "))
    except Exception:
        print("請輸入數字")
        continue  # 跳過下面的程式執行，進入到下一個迴圈

    if user_input > 100 or user_input < 1:
        print("請填寫 1 到 100 的整數!")
        continue

    # print("你填入了: " + str(user_input))
    if user_input == random_int:
        print("你猜對了!")
        break
    elif user_input > random_int:
        print("數字太大了，繼續猜小一點!")
    elif user_input < random_int:
        print("數字太小了，繼續猜大一點!")
