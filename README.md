# 🎓 Student CGPA Calculator

## Project Description
This project is a **Student CGPA Calculator** built using **Streamlit**.  
It allows students or teachers to enter marks for multiple subjects and automatically calculates:

- GPA for each subject
- Total marks
- Percentage
- Overall CGPA
- Pass/Fail status

The project features a **modern, responsive, animated UI** that adapts to any screen size and includes visual progress bars and result cards.

---

## Features

- Input student information (Name, Roll Number)
- Enter marks for any number of subjects
- Automatically calculate:
  - GPA per subject
  - Total marks
  - Percentage
  - Overall CGPA
  - Pass/Fail status
- Animated result card with progress bars
- Fully responsive UI that works on desktop and mobile
- Easy-to-use interface with input validation

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/student-cgpa-calculator.git
cd student-cgpa-calculator
2:Create a virtual environment
python -m venv venv
3.Activate the virtual environment
.on Window
venv\Scripts\activate
.On macOS/Linux:
source venv/bin/activate
4.Install dependencies
pip install -r requirements.txt
Usage:
1.Run the Streamlit app:
streamlit run app.py
Enter student details:

Name

Roll Number

Enter marks for each subject:

Maximum marks

Obtained marks

View results:

GPA per subject

Total marks

Percentage

CGPA

Pass/Fail

The result card displays animated progress bars and responsive layout for any screen.

GPA Calculation Logic
Percentage	GPA
85% - 100%	4.0
80% - 84.99%	3.7
75% - 79.99%	3.3
70% - 74.99%	3.0
65% - 69.99%	2.7
60% - 64.99%	2.3
50% - 59.99%	2.0
Below 50%	0

CGPA is calculated as the average of all subject GPAs.
Project Structure:
student-cgpa-calculator/
│
├─ app.py                  # Main Streamlit application
├─ README.md               # This file
├─ requirements.txt        # Required packages
├─ data/                   # Optional: Store student marks JSON/CSV
│   └─ students.json
└─ assets/                 # Optional: images, icons, animations
Dependencies:

Python 3.10 or higher

Streamlit >= 1.25.0
License:

This project is open-source and available under the MIT License.
✅ Summary of What Goes Where:
| File/Folder        | What to Include                                                               |
| ------------------ | ----------------------------------------------------------------------------- |
| `README.md`        | Project description, features, installation, usage, logic, structure, license |
| `requirements.txt` | Streamlit and pandas versions                                                 |
| `data/`            | Optional JSON/CSV data for storing marks                                      |
| `assets/`          | Optional images, animations, icons                                            |
| `app.py`           | Streamlit code of your project (UI + logic)                                   |
