
#Float foramtting follows "{value:width.precision f}

result = 100/777
print(result)#0.1287001287001287

#we can specify how many digit after decimal we want to see
#we will see 3 digit after decimal(with or without f it works)
print('The result was {r:1.3f}'.format(r=result))#The result was 0.129