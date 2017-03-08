
items = { "coins": 7, "pens": 3, "cups": 2, 

    "bags": 1, "bottles": 4, "books": 5 }

    


for key in sorted(items.iterkeys()):
#for key in sorted(items):
    print "%s: %s" % (key, items[key])
    
#for key in items:
  
#  print sorted(items.iterkeys())
  





for key in sorted(items.iterkeys(), reverse=True):

    print "%s: %s" % (key, items[key])







