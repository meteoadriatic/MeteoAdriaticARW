from datetime import timedelta
import urllib.request
import os


# Build list of LBC's time stamps
def lbc_hours(wrf_init_time, wrf_end_time, lbc_frequency):
    strc_time = wrf_init_time
    mylist = []
    while strc_time <= wrf_end_time:
        mylist.append(strc_time)
        strc_time = strc_time + timedelta(hours=int(lbc_frequency))
    return mylist

# Build strc request string for all ptiles
def strc_ptiles_string(gfs_run, lbc_hours, strc_gfs_grid):
    strcfilestring=''
    for lbc_time in lbc_hours:
        ftime = (lbc_time - gfs_run)
        ftime = (ftime.seconds//3600)
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
def strc_cgi(strc_server, strc_path, strc_ptiles_string, strc_leftlon,
                 strc_rightlon, strc_toplat, strc_bottomlat, strc_dataset):
    command = strc_server + '/' + strc_path + '?' + \
                   strc_ptiles_string + '&leftlon=' + strc_leftlon + \
                   '&rightlon=' + strc_rightlon + '&toplat=' + strc_toplat + \
                   '&bottomlat=' + strc_bottomlat + '&dset=' + strc_dataset
    return command

# Download ptiles from strc
def strc_download(strc_response, download_dir):
    response = iter(strc_response.splitlines())
    for line in response:
        if "http://" in line:
            path, file, status, size = line.split(' ')
            if status == 'Success':
                myfileurl = path + '/' + file
                myfiledest = download_dir + '/' + file
                print ('Downloading ' + myfileurl + ' into ' + myfiledest)
                urllib.request.urlretrieve(myfileurl, myfiledest)

# Clean input directory
def clean_inputdir(download_dir):
    folder = download_dir
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)