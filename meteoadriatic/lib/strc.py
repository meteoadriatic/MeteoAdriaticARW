from datetime import timedelta
import urllib.request
import os
import shutil


# Build list of LBC's time stamps
def lbc_hours(wrf_init_time, wrf_end_time, lbc_frequency):
    strc_time = wrf_init_time
    mylist = []
    while strc_time <= wrf_end_time:
        mylist.append(strc_time)
        strc_time = strc_time + timedelta(hours=int(lbc_frequency))
    return mylist


# Build strc request string for all ptiles
def ptiles_string(gfs_run, lbc_hours, strc_gfs_grid):
    strcfilestring = ''
    for lbc_time in lbc_hours:
        ftime = (lbc_time - gfs_run)
        ftime = (ftime.seconds // 3600)
        ftime = str(ftime).zfill(3)
        strcfilestring += 'file=' + \
                          gfs_run.strftime("%y%m%d%H") + \
                          '.gfs.t' + \
                          gfs_run.strftime("%H") + \
                          'z.' + \
                          str(strc_gfs_grid) + \
                          '.pgrb2f' + \
                          str(ftime) + \
                          '&'
    return strcfilestring


# Build strc cgi-bin command
def build_cgi(strc_server, strc_path, strc_ptiles_string, strc_leftlon,
             strc_rightlon, strc_toplat, strc_bottomlat, strc_dataset):
    command = strc_server + '/' + strc_path + '?' + \
              strc_ptiles_string + '&leftlon=' + strc_leftlon + \
              '&rightlon=' + strc_rightlon + '&toplat=' + strc_toplat + \
              '&bottomlat=' + strc_bottomlat + '&dset=' + strc_dataset
    return command


# Download ptiles from strc
def download_ptiles(strc_response, download_dir):
    response = iter(strc_response.splitlines())
    for line in response:
        if "http://" in line:
            path, file, status, size = line.split(' ')
            if status == 'Success':
                myfileurl = path + '/' + file
                myfiledest = download_dir + '/' + file
                print('Downloading ' + myfileurl + ' into ' + myfiledest)
                urllib.request.urlretrieve(myfileurl, myfiledest)

'''
TODO:
We must write MUCH more robust downloading system with required features:
1) Configurable network timeout
2) Checking downloaded file size
3) Checking number of downloaded files
4) Retrying request for missing files
5) Redownloading missing files
6) Repeating whole cycles configurable number of times
7) Configurable delays between cycles
8) Cycling through configurable list of servers
9) Fallback methods in case of STRC failure (NOMADS, HTTP)

Contributors are welcome.
'''

# Clean input directory
def clean_inputdir(download_dir):
    if os.path.isdir(download_dir):
        shutil.rmtree(download_dir)
    os.mkdir(download_dir)
