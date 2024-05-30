course = "python for beginners"
print(len(course)) #len is a general method use for all data types.. lets use some specific methods for strings
course2 = course.replace("python", "Java")
print(course2)

name = "Jeremiah"
name2 = name.upper()
print(name2)

subject = "physics for Advance"
print(subject.upper())
print(subject.find("p")) #gives you the index of p
print(subject.find("Advance"))
print(subject.replace("Advance", "Intermediate"))
print(subject.replace("d", "c"))
print("Java" in subject)