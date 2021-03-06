import numpy as np

# decison made not to include hospital-wide patient ID.
dataRAW_expected_col_dtypes = {
'PSEUDONYMISED_PATIENT_ID':str,
'AGE_AT_ARRIVAL':int,
'GENDER_NATIONAL_DESCRIPTION':str,      # exp: Male/Female
'SITE':str,
'ARRIVAL_DTTM':object,
'ARRIVAL_MODE_NATIONAL_CODE':str,       # exp: 1,2 ...
'TRIAGE_ASSESSMENT_DTTM':object,
'FIRSTDOC_FOR_TREATMENT_DTTM':object,
'ADM_REQUEST_DTTM':object,
'ADM_REQUEST_LOC_DESCRIPTION':str,
'ADMISSION_FLAG':int,
'DEPARTURE_DTTM':object,
'STREAM_LOCAL_CODE':str,
'BREACH_FLAG':int,                      # not required, NOTE: should autocalc if not available
}

dataRAW_essential_columns = [
    
]

dataRAW_expected_datetime_cols = [
    'ARRIVAL_DTTM',
    'TRIAGE_ASSESSMENT_DTTM',
    'FIRSTDOC_FOR_TREATMENT_DTTM',
   'ADM_REQUEST_DTTM',
    'DEPARTURE_DTTM',
]

dataRAW_first_datetime_col = 'ARRIVAL_DTTM' # used for making flags like attendance month, attendance_flag_weekend
dataRAW_second_datetime_col = 'DEPARTURE_DTTM' # used for making flags like departure month, departure_flag_weekend

# #defunct below?

# dataRAW_expected_dtypes2 = {
# 'dept_patid':[np.float,np.int,np.int64,np.str],
# 'hosp_patid':[np.float,np.int,np.int64,np.str],
# 'age':[np.int,np.int64],
# 'age_group':[np.str, 'pandas category type'],
# 'gender':[np.object],
# 'site':[np.object],
# 'arrive_date':[np.object],
# 'arrive_time':[np.object],
# 'arrive_datetime':[np.dtype('datetime64[ns]')],
# 'arrive_mode':[np.object],
# 'arrive_hour':[np.float,np.int,np.int64],
# 'arrive_dayofweek':[np.float,np.int,np.int64],
# 'arrive_week':[np.float,np.int,np.int64],
# 'arrive_month':[np.float,np.int,np.int64],
# 'arrive_year':[np.float,np.int,np.int64],
# 'arrive_dayofweek_name':[np.object],
# 'arrive_flag_wkend':[np.int],
# 'arrive_day':[np.int],
# 'first_triage_time':[np.object],
# 'first_triage_datetime':[np.dtype('datetime64[ns]')],
# 'first_dr_time':[np.object],
# 'first_dr_datetime':[np.dtype('datetime64[ns]')],
# 'first_adm_request_time':[np.object],
# 'first_adm_request_datetime':[np.dtype('datetime64[ns]')],
# 'adm_referral_loc':[np.object],
# 'depart_time':[np.object],
# 'depart_date':[np.object],
# 'depart_datetime':[np.dtype('datetime64[ns]')],
# 'depart_method':[np.object],
# 'depart_hour':[np.float,np.int,np.int64],
# 'depart_dayofweek':[np.float,np.int,np.int64],
# 'depart_week':[np.float,np.int,np.int64],
# 'depart_month':[np.float,np.int,np.int64],
# 'depart_year':[np.float,np.int,np.int64],
# 'depart_dayofweek_name':[np.str],
# 'depart_flag_wkend':[np.int],
# 'depart_day':[np.int],
# 'waiting_time':[np.float],
# 'BREACH_FLAG':[np.int],
# 'adm_flag':[np.int,np.int64,np.int64],
# 'stream':[np.float,np.int,np.int64,np.str],
# 'minutes_today':[np.int],
# 'minutes_tomo':[np.int],
# 'breach_datetime':[np.dtype('datetime64[ns]')],
# 'arr_triage_wait':[np.float,np.float64],
# 'first_adm_request_datetime':[np.dtype('datetime64[ns]')],
# 'arr_triage_wait':[np.float,np.float64],
# 'arr_dr_wait':[np.float,np.float64],
# 'arr_adm_req_wait':[np.float,np.float64],
# 'adm_req_dep_wait':[np.float,np.float64],
# 'dr_adm_req_wait':[np.float,np.float64],
# 'dr_dep_wait':[np.float,np.float64]
# }

# dataRAW_expected_cols = {
# 'hosp_patid':'',
# 'age':'check column name',
# 'age_group':'use make_age_group_column',
# 'gender':'',
# 'arrive_datetime':'use ',
# 'arrive_mode':'',
# 'arrive_hour':'make_callender_columns',
# 'arrive_dayofweek':'make_callender_columns',
# 'arrive_month':'make_callender_columns',
# 'arrive_dayofweek_name':'make_callender_columns',
# 'arrive_date':'make_callender_columns',
# 'arrive_week':'make_callender_columns',
# 'first_triage_datetime':'create_datetime_from_time',
# 'first_dr_datetime':'create_datetime_from_time',
# 'first_adm_request_datetime':'create_datetime_from_time',
# 'adm_referral_loc':'',
# 'depart_datetime':'',
# 'depart_method':'',
# 'depart_hour':'make_callender_columns',
# 'depart_dayofweek':'make_callender_columns',
# 'depart_week':'make_callender_columns',
# 'depart_month':'make_callender_columns',
# 'depart_dayofweek_name':'make_callender_columns',
# 'depart_date':'make_callender_columns',
# 'waiting_time':'',
# 'BREACH_FLAG':'',
# 'adm_flag':'',
# 'stream':'',
# 'minutes_today':'',
# 'minutes_tomo':'',
# 'breach_datetime':'',
# 'arr_triage_wait':'',
# 'arr_dr_wait':'',
# 'arr_adm_req_wait':'',
# 'adm_req_dep_wait':'',
# 'dr_adm_req_wait':'',
# 'dr_dep_wait':''

# }
