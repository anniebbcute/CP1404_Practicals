
def main():
    score = float(input("Enter score: "))
    print (give_grade(score))

def give_grade(score):
    if score < 0 or score > 100:
        return("Invalid score")
    elif score >= 90:
        return("Excellent")
    elif score >= 50:
        return("Passable")
    else:
        return("Bad")

main()