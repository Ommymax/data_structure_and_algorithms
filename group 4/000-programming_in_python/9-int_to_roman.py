def int_to_roman(n):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_number = ""
    for i in range(len(val)):
        count = n // val[i]
        roman_number += syms[i] * count
        n -= val[i] * count
    return roman_number
if __name__=="__main__":
   print(int_to_roman(n=27))  