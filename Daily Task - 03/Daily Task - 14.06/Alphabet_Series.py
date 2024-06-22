n=int(input())
series=list(map(str,input().split()))
def string_manipulation(series):
    ascii=[[ord(char)for char in string]for string in series]
    def finding_series(ascii):
        differences = [[i[j] - i[j+1] for j in range(len(i) - 1)]for i in ascii]
        new_diff = [diff[0] for diff in differences if diff]
        for i in range(len(new_diff)):
            if new_diff[i] != new_diff[0]:
                print(series[i])
    finding_series(ascii)
string_manipulation(series)