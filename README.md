# MeteoAdriatic ARW

**Python interface to run WRF-ARW model**

Developmental version *"Copernicus"*

## Authors

* **Ivan Toman** - *Initial work* - [meteoadriatic](https://github.com/meteoadriatic)


## Mission

*"Copernicus"* is interface to run WRF-ARW model. Similar projects exist out there. Most notable one is UEMS by Robert
Rozumalski (SOO STRC, http://strc.comet.ucar.edu/software/uems). Although shares main ideology, Copernicus is different
in several key aspects. While UEMS tries to automate and control everything that can be automated, leaving to end user
pretty much preconfigured system that just needs to be run and enjoy, Copernicus is built on different idea.
  
The key aspects of Copernicus system are:
1) Copernicus should automate only those tasks that should be automated; everything else is left to the user.
2) It should not try to steal any control over the user. If user wants to break anything, it certanly always can.
3) Although it should not have any clutter code in it's core that tries to do tasks that user should do, it should still
be fully configurable and extensible through modules so that every user can tailor it to suite his particular needs.
4) Copernicus is geared toward professionals; it is assumed that individual who use it know all aspects of WRF modelling.
5) It does not provide any binaries that user can compile themself. Consenquently, user can customize and build their
WRF and other binaries in any way he wants and still be able to use such custom builds within Copernicus without it
standing in his way.


## Contributors
Copernicus needs contributors to the project for:
1) Coding
2) Testing
3) Documentation

Anyone who wants to join our efforts, can any time contact project leader Ivan Toman at toman@meteoadriatic.net


### Prerequisites

Prerequisites that most often should be compiled by user and installed into system in order to run *"Copernicus"*
features are numerous. The main ones are as follows:

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