import LogRegress

test_num = 10
error_sum = 0.0
for i in range(test_num):
    error_sum += LogRegress.colic_test()
print('after %d iterations the average error rate is: %f' % (test_num, error_sum / test_num))