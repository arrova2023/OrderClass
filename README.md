# Automatic Generator of School Timetables

This program is an automatic school timetable generator based on machine learning. It uses data from teachers, subjects, and settings to create detailed schedules in the form of CSV files.

##Requirements

Before running the program, make sure you have the following files in the same directory:

- `profesores_asignaturas.txt`: This file must contain the list of professors and their subjects, each line in the format `teacher,subject`.

- `preCons.txt`: This file must contain the duration of each class in minutes, as well as the start and end times in HH:MM format.

## Machine Learning and Using Python 3.10

This program uses machine learning school concepts to generate efficient schedules. Through data reading and automatic processing, the program creates schedules that fit the class schedules and subjects provided.

##Functioning

1. The program uses Python 3.10 to take advantage of the latest language features.

2. Read the file `profesores_asignaturas.txt` to obtain the information of professors and subjects.

3. Read the duration of each class, start time and end time from `preCons.txt`.

4. Create a folder called "preExpanded" where the generated CSV files will be saved.

5. Generate a CSV file for each teacher in the schedule. Each file contains information about start and end times, subject, and sections for each day of the week (Monday, Tuesday, Wednesday, Thursday, and Friday) with initial values ​​of 0.

## Execution

1. Make sure you have the required files in the same directory.

2. Open a terminal and navigate to the directory where the file is located.

3. Run the program using the following command:

python3.10 program_name.py


4. The generated schedules will be saved in the "preExpanded" folder.

## Grades

This school schedule is a simple solution to generate schedules based on the data provided. You can adjust and extend this code according to your specific needs and requirements. If you want to explore more advanced approaches, such as the use of neural networks, we recommend doing more research on machine learning and data processing.

**Note:** This program does not handle the resolution of schedule conflicts, specific restrictions, or complex considerations. It is important to understand its limitations and customize it according to your requirements.# OrderClass
