import random

def number_guess_game():
    answer = random.randint(1, 100)
    max_attempts = 7
    tries = 0  # 入力回数カウント

    print("【数当てゲーム】1〜100の整数を入力してください。")
    print(f"最大 {max_attempts} 回まで挑戦できます。")

    while tries < max_attempts:
        while True:
            guess = input(f"{tries+1} 回目の予想: ")

            # 非整数チェック
            if not guess.isdigit():
                print("1〜100の整数を入力してください。")
                continue  # 再入力

            guess = int(guess)

            # 範囲チェック
            if not (1 <= guess <= 100):
                print("1〜100の整数を入力してください。")
                continue  # 再入力

            break  # 正しい入力が得られたので while から抜ける

        tries += 1  # 正しい入力時のみ1回増える

        # 判定（完全一致メッセージ）
        if guess == answer:
            print("正解！")
            return  # 正解で即終了
        elif guess < answer:
            print("もっと大きいです。")
        else:
            print("もっと小さいです。")

    # 7回失敗
    print(f"残念。正解は {answer} です。")
if __name__ == "__main__":
    number_guess_game()

