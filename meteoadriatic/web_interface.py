from flask import Flask, render_template
app = Flask(__name__)
from lib.time_calc import gfs_run, wrf_init_time, wrf_end_time

data = [
    {
        'gfs_run': gfs_run,
        'wrf_init_time': wrf_init_time,
        'wrf_end_time': wrf_end_time
    },
]

@app.route("/main")
def main():
    return render_template('main.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)