def persistence(num):
    output = 0
    while num//10 != 0:
    	p =1
    	for i in str(num):
    		p *=int(i)
    	num = p
    	output += 1
    print(output)
    return output

input = [39, 999, 4, 25]
result = list(map(persistence, input))
