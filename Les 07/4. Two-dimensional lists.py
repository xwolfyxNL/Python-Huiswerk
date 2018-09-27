studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
   studentsom = sum(student)
   studentgemiddeld = studentsom / 30
   #print(studentgemiddeld)
   return studentgemiddeld

def gemiddelde_van_alle_studenten(studentencijfers):
   totaal = 0
   for studenten in studentencijfers:
      studentensom = sum(studenten)
      totaal = totaal + studentensom

   return totaal / 120

for student in studentencijfers:

   print(gemiddelde_per_student(studentencijfers))


print(gemiddelde_van_alle_studenten(studentencijfers))