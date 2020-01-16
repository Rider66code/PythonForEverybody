#3. Once again, sort the list nums based on the last digit of each number from highest to lowest. However, now you should do so by writing a lambda function. Save the new list as nums_sorted_lambda.
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']
nums_sorted_lambda=sorted(list(map(lambda x:x[-1],nums)),reverse=True)
print(nums_sorted_lambda)
