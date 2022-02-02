def sum(c):
	res = 0
	for x in c.objects.all():
		res += x.amount
	return res
