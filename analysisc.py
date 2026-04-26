import pandas as pd

# loading data from csv file
def load_data():
    df=pd.read_csv("dataset.csv")
    return df

# cleaning data handle missing data
def clean_data(df):
    subjacts=df.columns.drop(["Name","Attendance"])
    for s in subjects:
        df[s]=df[s].fillna(df[s].mean())
      
    df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())  
        
    return df
    

# calculate percentage of student mid sem marks
def average(df):  
    subjacts=df.columns.drop(["Name","Attendance"])
    df["Percentage"] = round(df[subjects].mean(axis =1),2)
    return df 

# result marked
def result(df):
    df["Result"] = df["Percentage"] .apply(lambda x: "Pass" if x>30 else "Fail")
    return df

# giving grades
def grade(df):
    def get_grade(p):
        if p >= 75:
            return "A"
        elif p >= 50:
            return "B"
        elif p >= 30:
            return "C"
        else:
            return "D"
    
    df["Grade"] = df["Percentage"].apply(get_grade)
    return df 

# subject averrage
def subject_average(df):
     subjacts=df.columns.drop(["Name","Attendance"])
    return df[subjects].mean()

#topper 
def top_student(df):
    return df.loc[df['Percentage'].idxmax()]


# weak subject 
def  weak_subject(df):
     subjacts=df.columns.drop(["Name","Attendance"])
    df["Weak_Subject"]=df[subjects].idxmin(axis=1)
    return df

# strong subject
def strong_subject(df):
     subjacts=df.columns.drop(["Name","Attendance"])
    df["Strong_Subject"]=df[subjects].idxmax(axis=1)
    return df 

#rank giving
def rank(df):
    df["Rank"]=df["Percentage"].rank(ascending=False,method ="dense").astype(int)

    return df
 # risk analyisis
def risk_category(df):
    def get_risk(row):

        if( row["Percentage"]<30 or row["Attendance"]<40):
            return "High Risk"
        elif ((30 <= row["Percentage"]<50) or (40<=row["Attendance"] <60)):
            return "At Risk"
        else :
            return "Safe"
    df['Risk'] =df.apply(get_risk,axis=1)    
    return df

# predication for finals
def predict_final(df):
    def predict_row(row):

        if (row["Risk"]=="High Risk"):
            return "Fail"
        elif(row["Risk"]== "At Risk") and (row["Percentage"]<45):
            return "Fail"
        else:
            return "Pass"
    df["Prediction"]  = df.apply(predict_row,axis =1)
    return df  
def total_student(df):
        return len(df)
def pass_count(df):
        
    return len(df [df["Result"]=="Pass"])

def fail_count(df):
        
    return len(df [df["Result"]=="Fail"])
    

def high_risk_count(df):
    return len(df[df["Risk"]=="High Risk"])
    
def class_average(df):
    return df["Percentage"].mean()

def grade_count(df):
    return df["Grade"].value_counts()

def risk_count(df):
    return df["Risk"].value_counts()
 #function calling
if __name__== "__main__" :
    df=load_data()
    df=clean_data(df)
    df=average(df)
    df=result(df)
    df=grade(df)
    df= strong_subject(df)
    df= weak_subject(df)
    df =rank(df)
    df = risk_category(df)
    df = predict_final(df)


# output
    print (df.head())
    print("\n\nsubject average",subject_average(df))
    print('\n\ntop Student',top_student(df))


  
