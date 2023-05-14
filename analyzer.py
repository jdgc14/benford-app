def analyzer_benford(values_list):
    benford_dic = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
    }
    for num in values_list:
        first_digit = str(num)[0]
        benford_dic[first_digit] += 1

    return benford_dic


values_list = [
    33, 147, 469, 15, 8, 902, 13, 95, 21, 176,
    413, 295, 67, 207, 12, 91, 3, 231, 38, 22,
    78, 50, 410, 132, 38, 273, 166, 401, 34, 60,
    25, 178, 71, 47, 329, 137, 58, 12, 19, 241,
    32, 6, 228, 118, 107, 147, 104, 291, 19, 28,
    85, 12, 60, 70, 89, 38, 201, 17, 72, 52,
    44, 15, 129, 54, 29, 27, 132, 67, 9, 28,
    113, 22, 59, 14, 2, 61, 191, 3, 57, 173,
    17, 87, 29, 67, 41, 6, 52, 1, 123, 146
]

dic = analyzer_benford(values_list)

for value in dic:
    print(value)
