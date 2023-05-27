def randlet():
    import random
    letters = "abcdefghijklmnopqrstuvwxyz"
    l=3
    mk=''
    for i in range(l):
        mk+=random.choice(letters)
    print(mk)

st = input("Enter message\n")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding = True if (coding=="1") else False
print(coding)
if(coding):
  nwords = []
  for word in words:
    if(len(word)>=3):
      vc='egs'
      vb='evs'
      stnew = vc+ word[1:] + word[0] + vb
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))

else:
  nwords = []
  for word in words:
    if(len(word)>=3): 
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
  

