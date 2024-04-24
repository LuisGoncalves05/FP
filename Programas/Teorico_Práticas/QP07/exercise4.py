def isomorphic(astring1, astring2):
    for i in range(len(astring1)):
        if astring1.count(astring1[i]) == astring2.count(astring2[i]):
            pass
        else:
            return (f"'{astring1}' and '{astring2}' are not isomorphic")
    return (f"'{astring1}' and '{astring2}' are isomorphic")

