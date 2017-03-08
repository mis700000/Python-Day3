'''Description
The method get() returns a value for the given key. If key is not available then returns default value None.


Syntax
Following is the syntax for get() method −

dict.get(key, default=None)'''




dict = {'Name': 'Zara', 'Age': 27}

print dict.get('Name','never')

print "Value :%d"% dict.get('Age','Never')



'''print "Value : %s" %  dict.get('Age',"Never")

print "Value : %s" %  dict.get('Sex','irfan')
 
print "Value: %s" % dict.get('company name')'''