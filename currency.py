Amount=int(input("enter the amount:"))
print("the amount is:",Amount)
print("-'-----------------------")
print("Number of notes required in indian currency dimensions:")
print("--------------")
print("no of 2000 note:",Amount//2000)
Amount=Amount%2000
print("no of 500 notes:",Amount//500)
Amount=Amount%500
print("no of 200 notes:",Amount//200)
Amount=Amount%200
print("no of 100 notes:",Amount//100)
Amount=Amount%100
print("no of 50 notes:",Amount//50)
Amount=Amount%50
print("no of 20 notes:",Amount//20)
Amount=Amount%20
print("no of 10 notes:",Amount//10)
Amount=Amount%10
print("no of 5 notes:",Amount//5)
Amount=Amount%5
print("no of 2 notes:",Amount//2)
Amount=Amount%2
print("no of 1 notes:",Amount//1)
Amount=Amount%1
