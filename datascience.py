import streamlit as st

def greet():
    st.write("Good morning Everyone!")

greet()
st.write("-" * 40)

password = st.text_input("Enter password: ", type="password")

if password == "Enoch123":
    st.write("Login Successfully!")
    st.write("-" * 40)

    class StudentIntroduction:
        def __init__(self, name, age, roll_no, department, placefrom, clubmember, college_name):
            self.name = name
            self.age = age
            self.roll_no = roll_no
            self.department = department
            self.placefrom = placefrom
            self.clubmember = clubmember
            self.college_name = college_name

        def display(self):
            st.write("Name:", self.name)
            st.write("Age:", self.age)
            st.write("Roll No:", self.roll_no)
            st.write("Place from:", self.placefrom)
            st.write("Department:", self.department)
            st.write("Club member:", self.clubmember)
            st.write("College Name:", self.college_name)

    S1 = StudentIntroduction(
        "Enoch Andrew Jaisingh", 19, 14, "BCA 1st year",
        "Mengadu", "Data Science", "St Joseph University"
    )
    S1.display()
    st.write("-" * 40)

    class StudentMarks:
        def __init__(self, tamil, english, maths,
                     c_programming, computer_fundamental, vac):
            self.tamil = tamil
            self.english = english
            self.maths = maths
            self.c_programming = c_programming
            self.computer_fundamental = computer_fundamental
            self.vac = vac

        def display(self):
            st.write("Tamil:", self.tamil)
            st.write("English:", self.english)
            st.write("Maths:", self.maths)
            st.write("C programming:", self.c_programming)
            st.write("Computer Fundamental:", self.computer_fundamental)
            st.write("VAC:", self.vac)

        def get_total(self):
            return self.tamil + self.english + self.maths + \
                   self.c_programming + self.computer_fundamental + self.vac

        def get_average(self):
            return self.get_total() / 6

        def check_status(self):
            return "Pass" if min(
                self.tamil, self.english, self.maths,
                self.c_programming, self.computer_fundamental,
                self.vac) >= 40 else "Fail"

    S2 = StudentMarks(100, 100, 100, 100, 100, 100)
    S2.display()
    st.write("-" * 40)
    st.write("Total Marks Obtained:", S2.get_total())
    st.write("Average Marks:", round(S2.get_average(), 2))
    st.write("Academic Status:", S2.check_status())
    st.write("-" * 40)

elif password != "":
    st.write("Wrong password!try again.")
