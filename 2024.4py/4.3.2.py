a="if you wish to sueed,you should use persistence as your good friend,experience as your reference，prudence as your brother and hope as your sentry."
for ch in '!",.;':
    a=a.replace(ch," ")
a=a.lower()
b=a.split()
w={}
for word in b:
    w[word]=w.get(word,0)+1
for item  in w.items():
    print(item)




a=input(" ")
