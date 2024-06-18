series=list(map(str,input().split()))
a=0
def string_manipulation(series):
    ascii=[[ord(char)for char in string]for string in series]
    print(ascii)
    def finding_series(ascii):
        differences = [[i[j] - i[j+1] for j in range(len(i) - 1)]for i in ascii]
        print(differences)
        new_diff = [diff[0] for diff in differences if diff]
        print(new_diff)
        for i in range(len(new_diff)):
            if new_diff[i] != new_diff[0]:
                new_diff[i] = new_diff[0]
        print(new_diff)
        neww=[[x]for x in new_diff]
        print(neww)
    finding_series(ascii)

string_manipulation(series)