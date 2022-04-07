
Andersen = {"The Emperor's New Clothes", "The Little Mermaid", "The Little Match Girl",
            "The Snow Queen"}
Shakespeare = {"Romeo and Juliet","Hamlet","King Lear","Macbeth",
                "A Midsummer Night's Dream", "A Comedy of Errors"}
Tragedy = {"Medea","Octavia","Oedipus","Ur-Hamlet"}
Comedy = {"The Three Musketeer", "The Clouds"}
Uncategory = {"Don Quixote", "Rapunzel", "Cinderella"}
# cau 4
Shakespeare_Tragedy = Shakespeare.difference(Tragedy)
print("Cau 4: ", Shakespeare_Tragedy)
# cau 5
Andersen_Comedy = Andersen.intersection(Comedy)
print("Cau 5: ", Andersen_Comedy)
# cau 6
lis1 = [Andersen_Comedy, Shakespeare_Tragedy]
lis2 = [Shakespeare, Andersen, Tragedy, Comedy, Uncategory]
issubset = [[y.issubset(x) for x in lis2] for y in lis1]
issuperset = [[y.issuperset(x) for x in lis2] for y in lis1]
isdisjoint = [[y.isdisjoint(x) for x in lis2] for y in lis1]
print("Cau 6: ")
print(issubset)
print(issuperset)
print(isdisjoint)
# cau 7
Work = set()
Work.update(Andersen_Comedy)
Work.update(Shakespeare_Tragedy)
Work.update(Shakespeare)
Work.update(Andersen)
Work.update(Tragedy)
Work.update(Comedy)
Work.update(Uncategory)
print("Cau 7: ", Work)
# Cau 8
Author = {"Andersen", "Shakespeare", "Unknown"}
print("Cau 8: ", Author)
# Cau 9
Author_Of = dict()
for work in Work:
    authorName = ""
    if work in Andersen: authorName = "Andersen"
    elif work in Shakespeare: authorName = "Shakespeare"
    else: authorName = "Unknown"
    Author_Of.update({work:authorName})
print("Cau 9: ", Author_Of["Hamlet"])

# Cau 10
Writen_By = {value : key for key, value in Author_Of.items()}
print("Cau 10: ",Writen_By)

#Cau 11
Work_Count = dict()
for x in Work:
    y = 0
    if x in Andersen: y +=1
    if x in Shakespeare: y += 1
    if x in Andersen_Comedy: y += 1
    if x in Shakespeare_Tragedy: y += 1
    if x in Tragedy: y += 1
    if x in Comedy: y += 1
    if x in Uncategory: y += 1
    Work_Count.update({x: y})
print("Cau 11: ", Work_Count)
