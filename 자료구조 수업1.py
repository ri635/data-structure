def contains(bag, e) :
    return e in bag

def insert(bag, e) :
    bag.append

def remove(bag, e) :
    bag.remove(e)

def count(bag) :
    return len(bag)


myBag = []
insert(myBag, '휴대폰')
insert(myBag, '1')
print('내 가방속의 물건:', myBag)
