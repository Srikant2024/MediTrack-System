from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
def readPatientsFromFile(fileName):
    try:          
        patient_Data = {}   #  empty dictionary which stores patient IDs, where each patient has a list of visits including all data
        with open("patients.txt", 'r') as file:    # r is used to open the file in read mode
        #with open("error_patients.txt",'r') as file:    
            for line_num, line in enumerate(file, start=1):   
                line = line.strip()        # strip is used remove whitespaces and characters 
                fields = line.split(',')   # split is used to convert the string into a list
                
                if len(fields) != 8:       # check the field length  
                    print(f"Invalid number of fields {len(fields)} in line: {line_num}")
                    continue                # continue is used to skip/ pass control to next iteration
                
                try:                         # nested try block
                    patient_id = int(fields[0])    # for patient id visit  field 0
                    date = fields[1]                # for date visit  field 1
                    temperature = float(fields[2])   # for temperature visit   field 2
                    heart_rate = int(fields[3])       # for  heartrate  visit field 3
                    respiratory_rate = int(fields[4])   # for  respiratory_rate  visit field 4
                    systolic_bp = int(fields[5])          # for    systolic_bp  visit field 5
                    diastolic_bp = int(fields[6])         # for      diastolic_bp  visit field 6
                    oxygen_saturation = int(fields[7])    # for        oxygen_saturation   visit field 7
                except ValueError:         #exception  block (value error)
                    print(f"Invalid data type in line: {line_num}")
                    continue    #continue is used to pass control to next iteration / to skip
                
                if not (35 <= temperature <=42):
                    print(f"Invalid temperature value ({temperature}) in line: {line_num}")
                    continue     #continue is used to pass control to next iteration / to skip
                
                if not (30 <= heart_rate <= 180):
                    print(f"Invalid heart rate value ({heart_rate}) in line: {line_num}")
                    continue      #continue is used to pass control to next iteration / to skip
                
                if not (5 <= respiratory_rate <= 40):
                    print(f"Invalid respiratory rate value ({respiratory_rate}) in line: {line_num}")
                    continue      #continue is used to pass control to next iteration / to skip
                
                if not (70 <= systolic_bp <= 200):
                    print(f"Invalid systolic blood pressure value ({systolic_bp}) in line: {line_num}")
                    continue    #continue is used to pass control to next iteration / to skip
                
                if not (40 <= diastolic_bp <= 120):
                    print(f"Invalid diastolic blood pressure value ({diastolic_bp}) in line: {line_num}")
                    continue      #continue is used to pass control to next iteration / to skip
                
                if not (70 <= oxygen_saturation <= 100):
                    print(f"Invalid oxygen saturation value ({oxygen_saturation}) in line: {line_num}")
                    continue      #continue is used to pass control to next iteration / to skip
                
                if patient_id not in patient_Data:
                    patient_Data[patient_id] = []    # empty list to store the values
                
                patient_Data[patient_id].append([date, temperature, heart_rate, respiratory_rate, systolic_bp, diastolic_bp, oxygen_saturation])
             # append function is used to add the data at the end of the file
        return patient_Data      # return all patients data
    
    except FileNotFoundError:      # exception block file not foound error
        print(f"The file '{fileName}' could not be found.")
        return {}       
    except Exception as e:
        print("An unexpected error occurred while reading the file.")
        return {}
def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    #print(type(patientId))
    if (patientId not in  patients and patientId!=0 ):   # check the condition for find patient is present or not
        print(f"patientId {patientId} is not found")
    else:    
        if patientId == 0:                               # 0 is used to print the data of all the patients
          for patient_id, visits in patients.items():   
            print(f"Patient ID: {patient_id}")
            for visit in visits:        
                print(f"  Visit Date: {visit[0]}")                      # print visit date of all patients        
                print(f" Temperature: {visit[1]:.2f} c")                # .2f used to print the temperature upto 2 decimal places
                print(f"   Heart Rate: {visit[2]} bpm")                 # print heart rate of all patients
                print(f"   Respiratory Rate: {visit[3]} bpm")           # print  Respiratory Rate  of all patients
                print(f"   Systolic Blood Pressure: {visit[4]} mmHg")   # print    Systolic Blood Pressure of all patients
                print(f"   Diastolic Blood Pressure: {visit[5]} mmHg")  # print   Diastolic Blood Pressure  of all patients
                print(f"   Oxygen Saturation: {visit[6]} %")            # print oxygen saturation of  all patients
        elif patientId in patients:                   # print the data of individual patient  
         print(f"Patient ID: {patientId}")  
         for visit in patients[patientId]:
            print(f" Visit Date: {visit[0]}")                   # print visit date of  individual patients 
            print(f"  Temperature: {visit[1]:.2f} c")           #.2f used to print the temperature upto 2 decimal places
            print(f"  Heart Rate: {visit[2]} bpm")               # print heart rate of  individual patients
            print(f"  Respiratory Rate: {visit[3]} bpm")         # print  Respiratory Rate  of individual patients
            print(f"  Systolic Blood Pressure: {visit[4]} mmHg")   # print    Systolic Blood Pressure of individual patients
            print(f"  Diastolic Blood Pressure: {visit[5]} mmHg")    # print   Diastolic Blood Pressure  of individual  patients
            print(f"  Oxygen Saturation: {visit[6]} %")               # print oxygen saturation of  individual  patients
        else:
            print(f"patient id{patientId} not found")    
    return patients         


def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    try:
        patientId=int(patientId)    
    except: 
        if not isinstance(patientId, int):     # Check if 'patientId' is an integer
            print("Error: 'patientId' should be an integer.")
            return 
    print(type(patientId))      
    if  isinstance(patients, dict):    # Check if 'patients' is a dictionary
            pass                       # pass is a placeholder
    else:     
            print("Error: {patients} should be a dictionary.")
            return
    if (patientId not in patients and patientId!=0):    # check the condition for patientid
        print(f"patient id{patientId} not found")
    else:    
        # Initialize variables to calculate averages
        temp_sum = hr_sum = rr_sum = sbp_sum = dbp_sum = spo2_sum = num_visits = 0

        if patientId == 0:
            # Calculate averages for all patients
            for visits in patients.values():
                for visit in visits:
                    num_visits += 1
                    temp_sum += visit[1]   
                    hr_sum += visit[2]
                    rr_sum += visit[3]
                    sbp_sum += visit[4]
                    dbp_sum += visit[5]
                    spo2_sum += visit[6]
            if num_visits > 0:                          # print vital signs for all patients
                print("Vital Signs for All Patients:")   # print vital signs for all patients
                print("  Average temperature:","%.2f" %  (temp_sum / num_visits ), "C")    #print average temperature of all patients  
                print("  Average heart rate:","%.2f" % (hr_sum / num_visits), "bpm")                # print average heartrate  of all patients 
                print("  Average respiratory rate:","%.2f" % (rr_sum / num_visits), "bpm")            # print average respiratoryrate  of all patients 
                print("  Average systolic blood pressure:", "%.2f" %(sbp_sum / num_visits), "mmHg")    # print average systolicbloodpressure  of all patients 
                print("  Average diastolic blood pressure:","%.2f" %(dbp_sum / num_visits), "mmHg")   # print average  diastolicbloodpressure  of all patients 
                print("  Average oxygen saturation:", "%.2f" %(spo2_sum / num_visits), "%")            # print average oxygen saturation of all patients 
            else:
                print("No data found for all patients.")
        elif patientId in patients:
            # Calculate averages for a specific patient
            for visit in patients[patientId]:
                num_visits += 1
                temp_sum += visit[1]
                hr_sum += visit[2]
                rr_sum += visit[3]
                sbp_sum += visit[4]
                dbp_sum += visit[5]
                spo2_sum += visit[6]
            if num_visits > 0:          # print the vital sign for individual patient
                print(f"Vital Signs for Patient {patientId}:")
                print("  Average temperature:","%.2f" % (temp_sum / num_visits), "C")   #print average temperature of  individual patient
                print("  Average heart rate:", "%.2f" %(hr_sum / num_visits), "bpm")            # print average heartrate  of individual patient
                print("  Average respiratory rate:", "%.2f" %(rr_sum / num_visits), "bpm")      # print average respiratoryrate  of all patients
                print("  Average systolic blood pressure:","%.2f" % (sbp_sum / num_visits), "mmHg")    # print average systolicbloodpressure  of all patients 
                print("  Average diastolic blood pressure:","%.2f" % (dbp_sum / num_visits), "mmHg")   # print average  diastolicbloodpressure  of all patients 
                print("  Average oxygen saturation:", "%.2f" %(spo2_sum / num_visits), "%")     # print average oxygen saturation of all patients
            else:
                print(f"No data found for patient with ID {patientId}.")
        else:
            print(f"No data found for patient with ID {patientId}.")
                

def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    patient_data=[]        #creating an empty list to store patient data after checking conditions
    patient_data.append(patientId)
    try:
        #checking the date conditions
        if date[4]=='-' and date[7]=='-' and 1<=int(date[8:])<=31 and 1<=int(date[5:7])<=12 and int(date[:4])>=1900:
            patient_data.append(date)
        else:
            print("Invalid date.Please enter a valid date")
            return
        #checking the temperature conditions
        if 35.0<=temp<=42.0:
            patient_data.append(temp)
        else:
            print("Invalid temperature.Please enter a temperature between 35.0 and 42.0 degrees Celsius")
            return
        #checking the heart rate conditions
        if 30<=hr<=180:
            patient_data.append(hr)
        else:
            print("Invalid heart rate.Please enter a heart rate between 30 and 180 bpm") 
            return   
        #checking the respiratory rate conditions
        if 5<=rr<=40:
            patient_data.append(rr)
        else:
            print("Invalid respiratory rate.Please enter a respiratory rate between 5 and 40 bpm") 
            return   
        #checking the systolic blood pressure conditions
        if 70<=sbp<=200:
            patient_data.append(sbp)
        else:
            print("Invalid systolic blood pressure.Please enter a systolic blood pressure between 70 and 200 mmHg") 
            return   
        #checking the diastolic blood pressure conditions
        if 40<=dbp<=120:
            patient_data.append(dbp)
        else:
            print("Invalid diastolic blood pressure.Please enter a diastolic blood pressure between 40 and 120 mmHg") 
            return   
        #checking the oxygen saturation conditions
        if 70<=spo2<=100:
            patient_data.append(spo2)
        else:
            print("Invalid oxygen saturation.Please enter a oxygen saturation between 70 and 100 %") 
            return
        
        #appending the data in the patients file
        with open(fileName, 'a') as file:
            formatted_data = '\n'+','.join(map(str, patient_data)) # map is used to join the data
            file.write(formatted_data)
    
        #inserting the new data of patient into dictionary
        if patientId in patients:
            patients[patientId].append(patient_data)  # append is used to add the data  at the end of the file
        else:
            patients[patientId]=[patient_data]   
    except Exception:                             
        print("An unexpected error occurred while adding new data")
        return 
    print(f"Visit is saved successfully for patient #{patientId}")
    
def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    filtered_visits = []             #creating an empty list to store patient data after checking conditions

    for patient_id, visits in patients.items():
        for visit in visits:
            date_parts = visit[0].split('-')  # split is used converting string into a list and seperated by(-)
            
            # Check if the date format is valid (YYYY-MM-DD)
            if len(date_parts) != 3:
                continue                     #continue is used to pass control to next iteration / to skip

            try:
                visit_year = int(date_parts[0])
                visit_month = int(date_parts[1])
            except ValueError:
                continue                     #continue is used to pass control to next iteration / to skip

            # Check if the year matches (if provided)
            if year is not None and visit_year != year:
                continue                       #continue is used to pass control to next iteration / to skip

            # Check if the month matches (if provided)
            if month is not None and visit_month != month:
                continue                       #continue is used to pass control to next iteration / to skip
 
            # If both year and month match or if no filters are provided, include the visit
            filtered_visits.append((patient_id, visit))

    return filtered_visits     # return    the list


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []            # list of patient IDs that need follow-up visits to to abnormal health stats
    # loop to check the patient data from list of visits
    for patient_id, visits in patients.items():
        for visit in visits:
            # assigning value to variable as per requirment
            hr, _, sbp, dbp, spo2 = visit[2::] # '_' shows the unused variable which we don't require further
            # checking the data range of patients data
            if hr > 100 or hr < 60 or sbp > 140 or dbp > 90 or spo2 < 90:
                followup_patients.append(patient_id) # adding patient id to list who requires follow-up
                break # terminate the current loop
    return followup_patients # returning list of patient IDs that need follow-up visits to to abnormal health stats

def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
# Check if the patientId exists in the patients dictionary
    if patientId not in patients:
        print(f"No data found for patient with ID {patientId}.")
        return

    # Delete the patient visits from the dictionary
    del patients[patientId]

    # Write the updated patient data back to the file after deleting the particular patient data
    with open(filename, 'w') as file:
        for patient_id, visits in patients.items():
            for visit in visits:
                visit_data = ','.join(map(str, visit)) # joining the particular patient data using ','
                file.write(f"{patient_id},{visit_data}\n") # writing into the file

    # printing the success message
    print(f"Data for patient {patientId} has been deleted.")




###########################################################################
###########################################################################
#                                                                         #
#   The following code is being provided to you. Please don't modify it.  #
#                                                                         #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
               displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientId = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientId)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
if __name__ == '__main__':
    main()
