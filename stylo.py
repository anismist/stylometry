from collections import defaultdict
from math import sqrt

T = filter(None,open("thunt").read().split())
E = filter(None,open("erinys").read().split())
M = filter(None,open("mum").read().split())

print 'T avg word length:', sum(map(len,T))/float(len(T))
print 'E avg word length:', sum(map(len,E))/float(len(E))
print 'M avg word length:', sum(map(len,M))/float(len(M))
print

te = []
tm = []
em = []

for k in range(2,10):
  Grams = []
  for D in T,E,M:
      grams = defaultdict(float)
      text = ' '.join(D)
      norm = 1./len(text)
      for i in range(len(text)-k):
          grams[text[i:i+k]] += norm
      Grams.append(grams)

  gT, gE, gM = Grams

  allgrams = set(gT.keys()+gE.keys()+gM.keys())

  te.append(sqrt(sum((gT[x]-gE[x])**2 for x in allgrams)))
  tm.append(sqrt(sum((gT[x]-gM[x])**2 for x in allgrams)))
  em.append(sqrt(sum((gE[x]-gM[x])**2 for x in allgrams)))

print "Letter k-gram distances"
print "k:    ", "     ".join(`k` for k in range(2,10))
print "TE:", " ".join("%.03f"%x for x in te)
print "TM:", " ".join("%.03f"%x for x in tm)
print "EM:", " ".join("%.03f"%x for x in em)



te = []
tm = []
em = []

for k in range(2,10):
  Grams = []
  for D in T,E,M:
      grams = defaultdict(float)
      norm = 1./len(D)
      text = ' '.join(D)
      for i in range(len(D)-1):
          grams[' '.join(D[i:i+k])] += norm

      Grams.append(grams)

  gT, gE, gM = Grams

  allgrams = set(gT.keys()+gE.keys()+gM.keys())

  te.append(sqrt(sum((gT[x]-gE[x])**2 for x in allgrams)))
  tm.append(sqrt(sum((gT[x]-gM[x])**2 for x in allgrams)))
  em.append(sqrt(sum((gE[x]-gM[x])**2 for x in allgrams)))

print "Word k-gram distances"
print "k:    ", "     ".join(`k` for k in range(2,10))
print "TE:", " ".join("%.03f"%x for x in te)
print "TM:", " ".join("%.03f"%x for x in tm)
print "EM:", " ".join("%.03f"%x for x in em)
