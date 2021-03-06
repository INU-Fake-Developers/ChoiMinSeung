def temperature():
    temp = int(input("오늘의 온도 : "))
    if temp >= 35:
        print("더워죽겠다")
    elif temp > 10:
        print("살만한 날씨구나")
    else:
        print("추운 날씨다")
temperature()