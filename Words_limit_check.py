course = input("Write your emotions: ")
word = course.split()
new_course = " "
if len(word) < 10:
    print("word is in limit")
else:
    print("word limit is exceeded")
    course = word[0:10]
    for items in course:
        new_course += items + " "
    print("Entered words are limited till: {}".format(new_course))
