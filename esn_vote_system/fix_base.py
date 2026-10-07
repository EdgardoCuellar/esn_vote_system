import re
import sys
n = chr(10)
q = chr(34)
path = q + chr(101) + chr(115) + chr(110) + chr(95) + chr(118) + chr(111) + chr(116) + chr(101) + chr(95) + chr(115) + chr(121) + chr(115) + chr(116) + chr(101) + chr(109) + chr(47) + chr(116) + chr(101) + chr(109) + chr(112) + chr(108) + chr(97) + chr(116) + chr(101) + chr(115) + chr(47) + chr(98) + chr(97) + chr(115) + chr(101) + chr(46) + chr(104) + chr(116) + chr(109) + chr(108) + q

with open(path, q+chr(114)+q, encoding=q+chr(117)+chr(116)+chr(102)+chr(56)+q) as f: c = f.read()

c = re.sub(chr(60)+chr(100)+chr(105)+chr(118)+chr(32)+chr(105)+chr(100)+chr(61)+chr(97)+chr(110)+chr(105)+chr(109)+chr(97)+chr(116)+chr(101)+chr(100)+chr(45)+chr(103)+chr(114)+chr(97)+chr(100)+chr(105)+chr(101)+chr(110)+chr(116)+chr(91)+chr(94)+chr(62)+chr(42)+chr(62)+chr(60)+chr(47)+chr(100)+chr(105)+chr(118)+chr(62), chr(39)+chr(39), c, flags=re.DOTALL)

with open(path, q+chr(119)+q, encoding=q+chr(117)+chr(116)+chr(102)+chr(56)+q) as f: f.write(c)
print(chr(68)+chr(111)+chr(110)+chr(101))