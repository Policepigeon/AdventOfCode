from numpy import sort, loadtxt

A, B = sort(loadtxt('/home/policepigeon/Documents/code/AdventOfCode/2024/2024⁄01.txt').T)
print(sum(abs(A - B)),
      sum(a * sum(a==B) for a in A))