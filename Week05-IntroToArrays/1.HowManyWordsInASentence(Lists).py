def longShort():
    howMany = input("Type in a sentence! : ")
    words = (howMany.split())
    sortedwords = sorted(words, key=len)
    print ("\nThe number of words in the list is: %s." % (len(words),))
    print ("\nThe shortest word in the list is: %s." % (sortedwords[0],))
    print ("\nThe longest word in the list is: %s." % (sortedwords[-1],))
longShort()