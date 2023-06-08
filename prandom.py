from random import randint

def throw():
    dices = [randint(1, 6) for dice in range(3)]
    print(f"3 xúc xắc đã tung có kết quả lần lượt là {dices}.\nTổng: {sum(dices)} -", "Xỉu" if sum(dices) < 11 else "Tài")

def xthrow(loop, detail):
    result = [0] * 16
    gap = 0
    
    for i in range(loop):
        diceSum = sum([randint(1,6) for dice in range(3)])
        result[diceSum - 3] += 1
        if loop - i < 101:
            gap += 1 if diceSum > 10 else -1
    
    if detail == "1":
        print("\nBẢNG PHÂN TÍCH\n---------------")
        print("- Số lượt ra các mặt")
        for i in range(len(result)):
            print(f'\t+ {i + 3} điểm: {result[i]} lần ({round(result[i]/loop * 100, 2)}%)')
        print("- Kết quả")
        print(f"\t+ Tài: {sum(result[8:])} ({round(sum(result[8:])/loop*100, 2)})")
        print(f"\t+ Xỉu: {sum(result[:8])} ({round(sum(result[:8])/loop*100, 2)})")
        print("\nTrong 100 lượt tung cuối cùng, kết quả có xu hướng nghiêng về", "Tài" if gap > 0 else "Xỉu", f"(gap = {abs(gap)})") if gap != 0 else print("Kết quả cân bằng trong 100 lượt gần nhất")
    else:
        print("\nBẢNG SỐ LIỆU\n------------")
        for i in range(len(result)):
            print(f'+ {i + 3} điểm: {result[i]} lần')