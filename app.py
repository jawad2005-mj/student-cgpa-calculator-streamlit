import streamlit as st

# -------------------
# Page Config
# -------------------
st.set_page_config(page_title="Student CGPA Calculator", layout="wide")
st.title("🎓 Student CGPA Calculator")

# -------------------
# Student Info Inputs
# -------------------
with st.expander("Student Information", expanded=True):
    name = st.text_input("Enter Student Name")
    roll_no = st.text_input("Enter Roll Number")
    num_subjects = st.number_input("Enter number of subjects", min_value=1, max_value=20, value=5, step=1)

# -------------------
# Subject Marks Inputs
# -------------------
st.subheader("Enter marks for each subject")
obtained_marks = []
max_marks = []
gpa_list = []

for i in range(1, int(num_subjects)+1):
    st.markdown(f"**Subject {i}**")
    cols = st.columns([1,1])
    max_m = cols[0].number_input(f"Maximum marks for Subject {i}", min_value=1.0, max_value=1000.0, value=100.0, step=1.0, key=f"max{i}")
    obt_m = cols[1].number_input(f"Obtained marks for Subject {i}", min_value=0.0, max_value=max_m, value=0.0, step=1.0, key=f"obt{i}")
    
    obtained_marks.append(obt_m)
    max_marks.append(max_m)
    
    # GPA Calculation
    percentage = (obt_m / max_m) * 100
    if percentage >= 85:
        gpa = 4.0
    elif percentage >= 80:
        gpa = 3.7
    elif percentage >= 75:
        gpa = 3.3
    elif percentage >= 70:
        gpa = 3.0
    elif percentage >= 65:
        gpa = 2.7
    elif percentage >= 60:
        gpa = 2.3
    elif percentage >= 50:
        gpa = 2.0
    else:
        gpa = 0
    gpa_list.append(gpa)

# -------------------
# Calculate Button
# -------------------
if st.button("Calculate CGPA"):
    total_obtained = sum(obtained_marks)
    total_max = sum(max_marks)
    cgpa = sum(gpa_list) / len(gpa_list)
    percentage = (total_obtained / total_max) * 100
    passed = all(g > 0 for g in gpa_list)
    
    # -------------------
    # Result Card
    # -------------------
    st.markdown("### 📋 Student Result Card")
    st.markdown(f"""
    <div style="background-color:#f0f8ff;padding:20px;border-radius:10px;">
        <h4>Name: {name}</h4>
        <h4>Roll No: {roll_no}</h4>
        <h4>Total Marks: {total_obtained}/{total_max}</h4>
        <h4>Percentage: {round(percentage,2)}%</h4>
        <h4>CGPA: {round(cgpa,2)}</h4>
        <h4>Passed: {"✅ Yes" if passed else "❌ No"}</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Subject-wise Performance")
    
    # Animated progress bars for each subject
    for i in range(int(num_subjects)):
        percent = int((obtained_marks[i] / max_marks[i]) * 100)
        st.markdown(f"**Subject {i+1}**: Obtained {obtained_marks[i]} / {max_marks[i]} | GPA: {gpa_list[i]}")
        st.progress(percent)
    
    # Celebration animation if all passed
    if passed:
        st.balloons()
    else:
        st.warning("Some subjects are failed. Work harder! 💪")
