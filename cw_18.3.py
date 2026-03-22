class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def highest_score(self):
        return max(self.math_score, self.english_score, self.science_score)

    def check_highest_score(self):
        print("**** Checking Highest Score for", self.name, "****")
        math_score = int(input("Enter Math score: "))
        english_score = int(input("Enter English score: "))
        science_score = int(input("Enter Science score: "))
        score_dict = {
            math_score: 'Math',
            english_score: 'English',
            science_score: 'Science'
        }
        highest_score = max(score_dict)
        subject = score_dict[highest_score]
        print(self.name, "of", self.grade, "has the highest score of", highest_score, "in", subject)

s1 = Student("Nick", "Freshaman")
s1.check_highest_score()

s2 = Student("Mark", "Sophomore")
s2.check_highest_score()