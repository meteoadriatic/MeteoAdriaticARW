from time_calc import calculate_init_time, calculate_end_time
from datetime import datetime, timedelta



def lbc_hours(wrf_init_time, wrf_end_time, lbc_frequency):
    strc_time = wrf_init_time
    mylist = []

    while strc_time <= wrf_end_time:
        strc_time = strc_time + timedelta(hours=int(lbc_frequency))
        mylist.append(strc_time)

    return mylist





# strcdate=${ST_YYYY}${ST_MM}${ST_DD}${ST_HH}
# strcdate=`echo "$strcdate" | cut -c 3-`
# strcinit=${ST_HH}
# strcfilestring=""
# for ((i=$FIRSTFTIME;i<=$LASTFTIME;i+=$STEP)) ; do
#     FCST_TIME=`printf "%03d\n" "$i"`
#     strcfilestring+="file=${strcdate}.gfs.t${strcinit}z"
#     strcfilestring+=".${STRCRES}.pgrb2f${FCST_TIME}&"
# done