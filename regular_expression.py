#yha par dekhenge ki hm kisi text m searching kaise karte h
import re
pattern=r"[a-z]ood" # r is just like f string bs ye jo in build keyword ko like \n in sabko run nhi krega 
text='''Mukul is very sood good programer and 
he has very good command in python . 
After some months he is master in python and getting admission in college and exploring data science field. bood'''
search=re.search(pattern, text)# ye sirf search karega or pehli bar milit hi search rok dega 
print(search)#print sood
#we Have best method than search is find 
matches= re.finditer(pattern, text)
for match in matches:
    print(match)#bro isne sare list kar diye 
    