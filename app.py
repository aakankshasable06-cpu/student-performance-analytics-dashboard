import streamlit as st
import pandas as pd
import  analysisc as a

st.set_page_config(
    page_title="Student Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)
st.title("📊 Student Performance Analytics Dashboard")
st.markdown("""
<style>
.stApp {
    background-color: #1E1E2F;
}
</style>
""", unsafe_allow_html=True)


file =st.file_uploader("Upload Student dataset")
if file is not None:
    df=pd.read_csv(file)
    df=a.clean_data(df)
    df=a.average(df)
    df=a.result(df)
    df=a.grade(df)
    df= a.strong_subject(df)
    df= a.weak_subject(df)
    df =a.rank(df)
    df =a.risk_category(df)
    df =a.predict_final(df)


    
    filtered_df = df.copy()
    
    st.sidebar.header("🔎 Dashboard Filters")
    grade_filter = st.sidebar.selectbox(
        "Select Grade",
        ["All","A","B","C","D"]
    )
    risk_filter =st.sidebar.selectbox(
        "Select Risk",
        ["All","Safe","At Risk","High Risk"]
    ) 
    
   

    if grade_filter!="All":
        filtered_df =filtered_df [filtered_df ["Grade"]==grade_filter] 

    if risk_filter!= "All":
        filtered_df =filtered_df [filtered_df ["Risk"]==risk_filter] 
    st.sidebar.write(
      f"Students Found: {len(filtered_df)}"
     )
    
    tab1,tab2,tab3,tab4=st.tabs(["Raw Data",'Analysis Data',"Prediction","Summary"])  
   
    with tab1:
        st.subheader("📂 Uploaded Student Dataset")
        row_df =filtered_df[['Name' ,'Maths','Science','English','Computer',"Attendance"]]
        st.dataframe(row_df)
    with tab2:
        st.subheader("📈 Student Performance Analysis")
        analysis_df=filtered_df[["Name","Percentage","Grade","Rank","Strong_Subject","Weak_Subject"]]
        st.dataframe(analysis_df)
    with tab3:
        st.subheader("⚠ Risk and Prediction Analysis")
        prediction_df=filtered_df[["Name","Percentage","Attendance","Risk","Prediction"]]
        st.dataframe(prediction_df)    
    with tab4 :
        
        st.subheader("📌 Class Performance Summary")
        if filtered_df.empty:
             st.warning("No students match selected filters.")
             st.stop()
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric("👨‍🎓 Total Students", a.total_student(filtered_df))

        with col2:
            st.metric("Passed",a.pass_count(filtered_df))

        with col3:
            st.metric("Failed",a.fail_count(filtered_df))

        with col4:
            st.metric("High Risk",a.high_risk_count(filtered_df))

        with col5:
            st.metric("Class Average",round(a.class_average(filtered_df),2)) 
        st.divider()
        topper = a.top_student(filtered_df)  
        st.subheader("🏆 Top Performer")  
        st.write(
            f'{topper["Name"]} - {round(topper["Percentage"],2)}%'
            )
        csv = filtered_df.to_csv(index=False).encode("utf-8")
        st.download_button(
        label="⬇ Download Full Report",
        data=csv,
        file_name="student_analysis_report.csv",
        mime="text/csv"
        )
        st.divider()
        chart1,chart2 = st.columns(2)
        with chart1:
            st.subheader("📈 Grade Distribution")
            grade_counts = a.grade_count(filtered_df)
            st.bar_chart(grade_counts)


        with chart2:

            st.subheader("⚠ Risk Distribution")
            risk_counts=a.risk_count(filtered_df)
            st.bar_chart(risk_counts)
        
else:
   st.info("Upload a CSV file to start analysis 📁")     




