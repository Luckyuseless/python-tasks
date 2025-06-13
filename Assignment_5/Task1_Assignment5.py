dictionary= {
    "Alice" : 85 ,
    "Lucky" : 90 ,
    "Lakshya" : 100
}
name= input("Enter the student's name: ")

if name in dictionary:
    print (f"{name}'s marks: {dictionary[name]}")

else:
    print("Student not found.")