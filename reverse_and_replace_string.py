strval = "India defeated England and Spain defeated France"
splitval = strval.split()
reverseval = (' '.join(reversed(splitval))).replace('defeated','lost to')
print (reverseval)
