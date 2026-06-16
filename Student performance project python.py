import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"F:\Data analysis\Student performance project\Student_Performance_Dataset.csv")

df = df.drop_duplicates()   #no effect on data as this dataset has no duplicate values
df = df.drop(columns = "Final_Percentage")

subjects = ["Math_Score", "Science_Score", "English_Score"]
df["Total_Marks"] = df[subjects].sum(axis = 1)   #axis = 1 -> operation is performed row wise
df["Percentage"] = ((df["Total_Marks"]/(len(subjects))*100)/100).round(2)    #round(2) -> percentage comes in 2 decimal places
# df["Percentage"] = df[subjects].mean(axis = 1).round(2)      #another syntax for finding percentage
def grade(p):
    if p>= 90:
        return "A"
    elif p>=75:
        return "B"
    elif p>=60:
        return "C"
    else:
        return "D"
df["Grade"] = df["Percentage"].apply(grade)
count = df["Grade"].value_counts().sort_index()
# print(count)

average = [df["Math_Score"].mean(), df["Science_Score"].mean(), df["English_Score"].mean()]   #average score for each subject
# print(average)


sort_percentage = df.sort_values(by = "Percentage", ascending = False)
# print((sort_percentage).head())


# print(df[["Attendance_Percentage","Percentage"]].corr())
# print(df.corr(numeric_only = True))    #gives correlation for all numeric columns 
# plt.figure(figsize = (10,8))
# sns.heatmap(df.corr(numeric_only = True), annot = True)   #shows correlation for all numeric columns
# plt.xticks(rotation = 45, ha = "right")     #ha -> horizontal alignment
# plt.tight_layout()         #automatically adjusts the spacing between the plot elements so that nothing gets cut off or overlaps.
# plt.show() 


#pie chart
# plt.pie(average, labels = subjects, autopct = "%1.2f")
# plt.title("Average for each subject")
# plt.show()


#bar plot
# count.plot(kind = "bar")
# plt.xticks(rotation = 0)
# plt.ylabel("No. of students")
# plt.title("Grade vs no.of students")
# plt.show()


#scatter plot
# plt.scatter(df["Attendance_Percentage"], df["Percentage"], s = 10)
# plt.xlabel("Attendance")
# plt.ylabel("Percentage")
# plt.show()

# plt.plot(df["Percentage"], df["Attendance_Percentage"], color = "red", marker = "o")
# sns.regplot(data = df, x = "Percentage", y = "Attendance_Percentage",  scatter_kws={"s":10, "alpha":0.3})


#lineplot
sns.set_style("whitegrid")
sns.lineplot(data = df, x = "Percentage", y = "Attendance_Percentage", errorbar = None)     #errorbar = None -> removes shadow in the lineplot and keeps only line
plt.ylabel("Attendance")
# plt.show()

# plt.savefig(r"F:\Data analysis\Student performance project.jpg")

#finding no. of students who got grade A
# number = 0
# for c in df["Grade"]:
#     if c == "A":
#         number+=1

# print(number)

#print(df.head())

#print(df.loc[df["Grade"] == "A", ["Gender", "Student_ID"]])    #gives gender and student_id column wherever the condition satisfies
                                                                #to get all columns syntax -> print(df[df["Grade"] == "A"])

#print(df.isnull().sum())


# df.to_excel(r"F:\Data analysis\Student performance project\Final Project.xlsx", index = False)