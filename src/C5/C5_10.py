ph = int(input("ph: "))
if (ph >=0 and ph <=4):
    print("강산성")
elif (ph >=5 and ph <=6):
    print("약산성")
elif (ph ==7):
    print("중성")
elif (ph >=8 and ph <=9):
    print("약염기성")
else:
    print("강염기성")