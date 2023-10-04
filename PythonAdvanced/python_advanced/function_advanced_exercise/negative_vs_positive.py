numbers = [int(x) for x in input().split()]
negative_list = []
positive_list = []

for num in numbers:
    if num < 0:
        negative_list.append(num)
    else:
        positive_list.append(num)

negative_sum = sum(negative_list)
positive_sum = sum(positive_list)
print(negative_sum)
print(positive_sum)
if abs(negative_sum) > abs(positive_sum):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
