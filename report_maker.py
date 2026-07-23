def format_report(func):
    def wrapper(self):
        print("*" * 10)
        func(self)
        print("*" * 10)
        print("\nEnd of Report")
    return wrapper

class Report:
    def __init__(self, author, date, marks, grade):
        self.author = author
        self.date = date
        self.marks = marks
        self.grade = grade

    @classmethod
    def stud_report(cls):
        return cls("AB", "23/07/2026", 99, "O")
    
    @classmethod
    def stud_report2(cls):
        return cls("Rahul", "24/07/2026", 85, "A")

    def __str__(self):
        return (
            "STUDENT REPORT\n\n"
            f"Author : {self.author}\n\n"
            f"Date : {self.date}\n\n"
            f"Marks : {self.marks}\n\n"
            f"Grade : {self.grade}"
        )

    @format_report
    def display(self):
        print(self)

report1 = Report.stud_report()
report2 = Report.stud_report2()
report1.display()
report2.display()





