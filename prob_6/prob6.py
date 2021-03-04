'''
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
def main():
    sum_sqs = 0
    max = 101
    for x in range(1, max):
        sum_sqs = sum_sqs + (x * x)
    print("sum of numbers squared: ", sum_sqs)

    sum_sqd = 0
    for x in range(1, max):
        sum_sqd = sum_sqd + x
    sum_sqd = sum_sqd * sum_sqd
    print("square of numbers sum: ", sum_sqd)

    ans = sum_sqd - sum_sqs
    print(ans)


if __name__ == '__main__':
    main()