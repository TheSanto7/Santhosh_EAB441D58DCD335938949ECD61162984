import time
def animate_text(text):
    for char in text:
        print('\033[1m' + char, end='', flush=True)
        time.sleep(0.01)
    print('\033[95m')
animate_text("-------------------------------------------------------------------------------------------------------------")
print()
print()
animate_text("H    H   AAAA   PPPP   PPPP   Y    Y     BBBBBB   IIIII   RRRRR   TTTTTTT   H    H   DDDDD      AAAA   Y    Y")
animate_text("H    H  A    A  P   P  P   P   Y  Y       B    B    I     R    R     T      H    H   D    D    A    A   Y  Y ")
animate_text("HHHHHH  AAAAAA  PPPP   PPPP     YY        BBBBB     I     RRRRR      T      HHHHHH   D    D    AAAAAA    YY  ")
animate_text("H    H  A    A  P      P        YY        B    B    I     R    R     T      H    H   D    D    A    A    YY  ")
animate_text("H    H  A    A  P      P        YY       BBBBBB   IIIII   R     R    T      H    H   DDDDD     A    A    YY  ")
print()
print()
def animate_text(text):
    for char in text:
        print('\033[96m' + char, end='', flush=True)
        time.sleep(0.01)
    print('\033[1m')
animate_text("            RRRRRR         OOOOO        HH    HH       IIIIIIII       TTTTTTTTTT     HH    HH ")
animate_text("            RR   RR       O     O       HH    HH          II              TT         HH    HH ")
animate_text("            RRRRRR        O     O       HHHHHHHH          II              TT         HHHHHHHH ")
animate_text("            RR   RR       O     O       HH    HH          II              TT         HH    HH ")
animate_text("            RR    RR       OOOOO        HH    HH       IIIIIIII           TT         HH    HH ")
print()
print()
print()
def animate_text(text):
    for char in text:
        print('\033[91m' + char, end='', flush=True)
        time.sleep(0.01)
    print('\033[0m')
animate_text("                                             ****   ****")
animate_text("                                            ****** ******")
animate_text("                                            *************")
animate_text("                                             *********** ")
animate_text("                                               *******   ")
animate_text("                                                 ***     ")
animate_text("                                                  *      ")
print()
print()
animate_text("---------------------------------------------------------------------------------------------------------------")