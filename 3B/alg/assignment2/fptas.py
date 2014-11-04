def fptas(n, M, W, C):
	e = 0.18
	maxC = max(C)
	K = (e*maxC)/n
	for i in xrange(0, n):
		C[i] = C[i]/K
	print C
	m = [[0 for x in xrange(M+1)] for x in xrange(n+1)]
	for i in xrange(1,int((n+1)/K)):
		for j in xrange(0,M+1):
			if W[i-1] <= j:
				m[i][j] = max(m[i-1][j], m[i-1][j-W[i-1]] + C[i-1])
			else:
				m[i][j] = m[i-1][j]
	# print int(m[int(n/K)][M] * K)

	# print m[int(n/K)]

for line in open('inst/knap_40.inst.dat', 'r'):
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
