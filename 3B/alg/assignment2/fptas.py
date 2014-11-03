def fptas(n, M, W, C):
	e = 0.9999
	maxC = max(C)
	K = (e*maxC)/n
	for i in xrange(0, n):
		C[i] = C[i]/K
	m = [[0 for x in xrange(M+1)] for x in xrange(n+1)]
	for i in xrange(1,n+1):
		for j in xrange(0,M+1):
			if W[i-1] <= j:
				m[i][j] = max(m[i-1][j], m[i-1][j-W[i-1]] + C[i-1])
			else:
				m[i][j] = m[i-1][j]
	print int(m[n][M] * K)

for line in open('inst/knap_4.inst.dat', 'r'):
	lineArr = line.rstrip().split(' ')
	n = int(lineArr[1])
	M = int(lineArr[2])
	W = []
	C = []
	i = 0
	while i < n:
		W.append(int(lineArr[2*i+3]))
		C.append(int(lineArr[2*i+3+1]))
		i += 1

	fptas(n, M, W, C)
