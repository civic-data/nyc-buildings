#!/usr/bin/env python
# boro,block,lot,bin,lhnd,lhns,lcontpar,lsos,hhnd,hhns,hcontpar,hsos,scboro,sc5,sclgc,stname,addrtype,realb7sc,validlgcs,parity,b10sc,segid,zipcode
import sys
import csv
import re
from datetime import datetime

csvwriter = csv.writer(sys.stdout, delimiter=',', quotechar='"')
datesearch = re.compile('\d\d/\d\d/\d\d\d\d')
numbersearch = re.compile('^\d')
numbersearch2 = re.compile('.*\d$')
reader = csv.DictReader( sys.stdin )
headersave=[]

# bq --project personal-real-estate load nyc.dob_permit_issuance bigquery.out.csv  Owners_House_State:string,Owners_First_Name:string,Permit_Status:string,Residential:string,Street_Name:string,Permittees_License_Type:string,Superintendent_Business_Name:string,Owners_Business_Type:string,Lot:string,Owners_Last_Name:string,Owners_House_number:string,Act_as_Superintendent:string,Self_Cert:string,Bin_number:string,Filing_Status:string,Owners_House_Street_Name:string,Bldg_Type:string,Permittees_Last_Name:string,Permit_Subtype:string,Owners_Business_Name:string,Special_District_1:string,Filing_Date:timestamp,Permittees_Other_Title:string,Special_District_2:string,Site_Fill:string,Site_Safety_Mgrs_First_Name:string,Permittees_Business_Name:string,Non-Profit:string,HIC_License:string,Job_number:string,Permit_Sequence_number:string,Site_Safety_Mgrs_Last_Name:string,House_number:string,Issuance_Date:timestamp,Work_Type:string,Job_Type:string,Community_Board:string,Site_Safety_Mgr_Business_Name:string,Job_doc_number:string,Superintendent_First_n_Last_Name:string,Permittees_Phone_number:string,Oil_Gas:string,Block:string,Owners_House_Zip_Code:string,DOBRunDate:timestamp,Expiration_Date:timestamp,Permittees_First_Name:string,Permit_Type:string,Owners_Phone_number:string,Permittees_License_number:string,Owners_House_City:string,BOROUGH:string,Job_Start_Date:timestamp,Zip_Code:string

# bq --project personal-real-estate load nyc.311 ~/download2/311_Service_Requests_from_2010_to_Present.csv  Unique_Key:string,Created_Date:timestamp,Closed_Date:timestamp,Agency:string,Agency_Name:string,Complaint_Type:string,Descriptor:string,Location_Type:string,Incident_Zip:string,Incident_Address:string,Street_Name:string,Cross_Street_1:string,Cross_Street_2:string,Intersection_Street_1:string,Intersection_Street_2:string,Address_Type:string,City:string,Landmark:string,Facility_Type:string,Status:string,Due_Date:timestamp,Resolution_Action_Updated_Date:timestamp,Community_Board:string,Borough:string,X_Coordinate_State_Plane:string,Y_Coordinate_State_Plane:string,Park_Facility_Name:string,Park_Borough:string,School_Name:string,School_Number:string,School_Region:string,School_Code:string,School_Phone_Number:string,School_Address:string,School_City:string,School_State:string,School_Zip:string,School_Not_Found:string,School_or_Citywide_Complaint:string,Vehicle_Type:string,Taxi_Company_Borough:string,Taxi_Pick_Up_Location:string,Bridge_Highway_Name:string,Bridge_Highway_Direction:string,Road_Ramp:string,Bridge_Highway_Segment:string,Garage_Lot_Name:string,Ferry_Direction:string,Ferry_Terminal_Name:string,Latitude:string,Longitude:string,Location:string

#print '1'

# Job_#:string,Owners_House_State:string,Owners_First_Name:string,Permit_Status:string,Residential:string,Street_Name:string,Owners_House_#:string,Permit_Sequence_#:string,Owners_Business_Type:string,Lot:string,Owners_Last_Name:string,Act_as_Superintendent:string,Owner's_Phone_#:string,Self_Cert:string,HIC_License:string,Filing_Status:string,Owners_House_Street_Name:string,Bldg_Type:string,Permittees_Last_Name:string,Permit_Subtype:string,Owners_Business_Name:string,Special_District_1:string,Filing_Date:timestamp,Permittees_Other_Title:string,Special_District_2:string,House_#:string,Site_Safety_Mgrs_First_Name:string,Permittees_Business_Name:string,Non-Profit:string,Superintendent_Business_Name:string,Bin_#:string,Site_Safety_Mgrs_Last_Name:string,Issuance_Date:timestamp,Work_Type:string,Job_Type:string,Community_Board:string,Site_Safety_Mgr_Business_Name:string,Permittees_Phone_#:string,Permittees_License_#:string,Permittees_License_Type:string,Oil_Gas:string,Site_Fill:string,Block:string,Owners_House_Zip_Code:string,DOBRunDate:timestamp,Expiration_Date:timestamp,Permittees_First_Name:string,Permit_Type:string,Job_doc_#:string,Superintendent_First_&_Last_Name:string,Owners_House_City:string,BOROUGH:string,Job_Start_Date:timestamp,Zip_Code:string

typedict = {'Job_number':'string','Owners_House_State':'string','Owners_First_Name':'string','Permit_Status':'string','Residential':'string','Street_Name':'string','Owners_House_number':'string','Permit_Sequence_number':'string','Owners_Business_Type':'string','Lot':'string','Owners_Last_Name':'string','Act_as_Superintendent':'string','Owners_Phone_number':'string','Self_Cert':'string','HIC_License':'string','Filing_Status':'string','Owners_House_Street_Name':'string','Bldg_Type':'string','Permittees_Last_Name':'string','Permit_Subtype':'string','Owners_Business_Name':'string','Special_District_1':'string','Filing_Date':'timestamp','Permittees_Other_Title':'string','Special_District_2':'string','House_number':'string','Site_Safety_Mgrs_First_Name':'string','Permittees_Business_Name':'string','Non_Profit':'string','Superintendent_Business_Name':'string','Bin_number':'string','Site_Safety_Mgrs_Last_Name':'string','Issuance_Date':'timestamp','Work_Type':'string','Job_Type':'string','Community_Board':'string','Site_Safety_Mgr_Business_Name':'string','Permittees_Phone_number':'string','Permittees_License_number':'string','Permittees_License_Type':'string','Oil_Gas':'string','Site_Fill':'string','Block':'string','Owners_House_Zip_Code':'string','DOBRunDate':'timestamp','Expiration_Date':'timestamp','Permittees_First_Name':'string','Permit_Type':'string','Job_doc_number':'string','Superintendent_First_n_Last_Name':'string','Owners_House_City':'string','BOROUGH':'string','Job_Start_Date':'timestamp','Zip_Code':'string'}

# typedict = { 'agency':'string','fiscal_year':'string','calendar_year':'string','document_id':'string','payee_name':'string','department':'string','check_amount':'float','expense_category':'string','contract_ID':'string','contract_purpose':'string','capital_project':'string','issue_date':'timestamp','spending_category':'string' }
# typedict = { 'Unique_Key':'string','Created_Date':'timestamp','Closed_Date':'timestamp','Agency':'string','Agency_Name':'string','Complaint_Type':'string','Descriptor':'string','Location_Type':'string','Incident_Zip':'string','Incident_Address':'string','Street_Name':'string','Cross_Street_1':'string','Cross_Street_2':'string','Intersection_Street_1':'string','Intersection_Street_2':'string','Address_Type':'string','City':'string','Landmark':'string','Facility_Type':'string','Status':'string','Due_Date':'timestamp','Resolution_Action_Updated_Date':'timestamp','Community_Board':'string','Borough':'string','X_Coordinate_State_Plane':'string','Y_Coordinate_State_Plane':'string','Park_Facility_Name':'string','Park_Borough':'string','School_Name':'string','School_Number':'string','School_Region':'string','School_Code':'string','School_Phone_Number':'string','School_Address':'string','School_City':'string','School_State':'string','School_Zip':'string','School_Not_Found':'string','School_or_Citywide_Complaint':'string','Vehicle_Type':'string','Taxi_Company_Borough':'string','Taxi_Pick_Up_Location':'string','Bridge_Highway_Name':'string','Bridge_Highway_Direction':'string','Road_Ramp':'string','Bridge_Highway_Segment':'string','Garage_Lot_Name':'string','Ferry_Direction':'string','Ferry_Terminal_Name':'string','Latitude':'string','Longitude':'string','Location':'string' }

lineno =0
first=True
for line in reader:
    lineno = lineno + 1
    row = []
    header=[]
    #print '2'
    for key in line:
        try:
                  
# 05/06/2014 03:05:28 AM
            #print '3', typedict[key]
            #print '3', key, typedict[key]
            if first:
                if 'Date' in key:
                    sys.stderr.write( '%s:timestamp,'% key)
                else:
                    sys.stderr.write( '%s:string,'% key)

            if typedict[key]=='timestamp':
                if line[key]=='' or line[key]=='Unspecified':
                    row.append('')
                else:
                    try:
                      # 06/05/2013 12:00:00 AM
                      #date = datetime.strptime(line[key],'%m/%d/%Y ')
                      date = datetime.strptime(line[key],'%m/%d/%Y %I:%M:%S %p')
                      row.append(datetime.strftime(date,'%Y-%m-%dT%H:%M:%S-05:00'))
                    except Exception,e:
                      #date = datetime.strptime(line[key],'%m/%d/%Y %I:%M:%S %p')
                      #date = datetime.strptime(line[key],'%Y-%m-%d')
                      try: 
                          date = datetime.strptime(line[key],'%m/%d/%Y')
                          row.append(datetime.strftime(date,'%Y-%m-%dT%H:%M:%S-05:00'))
                      except Exception,e:
                          print 'issue1:',e, key, line[key]
                          row.append('')
            elif typedict[key]=='integer':
                    row.append(int(float(line[key])))
                    pass
            elif typedict[key]=='float':
                    row.append(float(line[key]))
                    pass
            elif typedict[key]=='string':
                    row.append(str(line[key]))
                    pass


        except Exception,e:
            try:
                #sys.stderr.write( 'BIG ISSUE:%s\n'% e)
                sys.stderr.write( 'BIG ISSUE:%s:%s>>>%s<<< %s\n'% (typedict[key],key,line[key], line))
            except Exception,e:
                #sys.stderr.write( 'REALLY BIG ISSUE:%s:%s\n'% (key,line))
                pass



    #row = [line['BBLE']]
    #print "QQQ",len(row)
    first=False
    if len(row) == 54:
    #if True:
        csvwriter.writerow(row)
    else:
        #row=['ISSUE']+row
        #csvwriter.writerow(row)
        sys.stderr.write("row count issue %s %s\n" % ( len(row), lineno))
    #print len(row)
    if header!=headersave:
        #print 'HEADER ISSUE',header
        #print 'HEADER ISSUE',headersave
        pass
    headersave=header
