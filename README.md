# MeteoAdriatic ARW

**Python interface to run WRF-ARW model**

Developmental version *"Copernicus"*

## Authors

* **Ivan Toman** - *Initial work* - [meteoadriatic](https://github.com/meteoadriatic)


### Prerequisites

Prerequisites that most often should be compiled by user and installed into system in order to run *"Copernicus"* features are numerous. The main ones are as follows:

[WRF](https://github.com/wrf-model/WRF/releases),
[WPS](https://github.com/wrf-model/WPS/releases),
[UPP](https://dtcenter.org/wrf-nmm/users/overview/upp_overview.php),
[mpich](http://www.mpich.org/),
[wgrib](http://www.cpc.ncep.noaa.gov/products/wesley/wgrib.html),
[wgrib2](http://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/),
[cnvgrib](http://www.nco.ncep.noaa.gov/pmb/codes/GRIB2/),
[OpenGrADS](http://opengrads.org/),
[NCL](https://www.ncl.ucar.edu/)

Details will be given within project documentation.

File *requirements.txt* lists all required python modules. Installation of python modules with pip:

```
(sudo) pip(3) install -r /path/to/requirements.txt
```