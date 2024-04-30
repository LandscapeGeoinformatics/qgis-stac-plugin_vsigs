# qgis-stac-plugin (Custom with GCP access by vsigs)

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/stac-utils/qgis-stac-plugin/ci.yml?branch=main)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/stac-utils/qgis-stac-plugin?include_prereleases)
![GitHub](https://img.shields.io/github/license/stac-utils/qgis-stac-plugin)

QGIS plugin for reading STAC APIs 

Site https://stac-utils.github.io/qgis-stac-plugin

**The QGIS STAC API Browser currently lacks funding for maintenance,
bug fixes and new features; therefore development will be slow for now.
However we’re dedicated to maintaining the project. 
For assistance or if you have funding to contribute 
please reach out to Kartoza ([info@kartoza.com](mailto:info@kartoza.com))**
Customization Author : Landscap Geoinfomatics Lab (University of Tartu)


### Installation (From zip file)

1. Download the release 1.1.2b from ![here](https://github.com/LandscapeGeoinformatics/qgis-stac-plugin_vsigs/releases/download/first_release/qgis_stac.1.1.2b.zip)
2. Open the QGIS plugin manager, then select the **Install from ZIP**
3. Click on "..." and select the zip file download in step 1
4. Click install plugin

![Screenshot for install from zip option](docs/images/install_from_zip.png)



#### Mini Howto

## Add google cloud access credential to QGIS
1.  In QGIS,  **Settings -> options**
2.  Click **System** on the left panel
3.  From the right panel, look for *Environment* Section
4.  Add a new variables with :
    - Apply : Overwrite
    - Variable : GOOGLE_APPLICATION_CREDENTIALS
    - Value : The path to the Google credential JSON file (ex. C:\Users\John\glomodat-stac-testing-svc.json)
5. Click ok

![Screenshot for addding GCP credential](docs/images/gcp_qgis.png)


## Configuration of qgis-stac plugin
1. 

