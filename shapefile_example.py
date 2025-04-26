

import matplotlib.pyplot as plt

import cartopy.io.shapereader as shpreader



import cartopy.crs as ccrs

"""
Felix Muzny
March 31/April 1st, 2021
DS 2001 - CS Practicum #10

Example of using shape files from cartopy, then 
graphing on top of the shape file, using the same lat/long coordinates
as in the scatter_latlong example.


See further examples at:
https://scitools.org.uk/cartopy/docs/v0.15/examples/hurricane_katrina.html

https://scitools.org.uk/cartopy/docs/latest/gallery/

You can graph any geographic region if you have its shape file in this way.
"""


LATITUDES = [44.5,
39,
44,
31,
44.5,
41.700001,
44,
43,
44,
41.5,
38.5,
33,
40,
39,
41.599998,
34.799999,
40.273502,
38.573936,
27.994402,
39.876019,
45.367584,
44.182205,
33.247875,
19.741755,
66.160507,
35.860119,
37.926868,
39.833851,
37.839333,
47.650589,
46.39241,
36.084621,
46.96526,
47.751076,
39.41922,
39.113014,
40.367474,
32.31823,
42.032974,
34.307144,
33.836082,
41.203323,
34.048927,
39.045753,
42.407211,
36.778259,
44.068203,
43.07597,
35.782169,
30.39183]

LONGITUDES = [-89.5,
-80.5,
-72.699997,
-100,
-100,
-71.5,
-120.5,
-75,
-71.5,
-100,
-98,
-90,
-89,
-75.5,
-72.699997,
-92.199997,
-86.126976,
-92.60376,
-81.760254,
-117.224121,
-68.972168,
-84.506836,
-83.441162,
-155.844437,
-153.369141,
-86.660156,
-78.024902,
-74.871826,
-84.27002,
-100.437012,
-94.63623,
-96.921387,
-109.533691,
-120.740135,
-111.950684,
-105.358887,
-82.996216,
-86.902298,
-93.581543,
-106.018066,
-81.163727,
-77.194527,
-111.093735,
-76.641273,
-71.382439,
-119.417931,
-114.742043,
-107.290283,
-80.793457,
-92.329102]



def main():    
    ax = plt.axes([0, 0, 1, 1],
                  projection=ccrs.LambertConformal())

    ax.set_extent([-125, -66.5, 20, 50], ccrs.Geodetic())

    shapename = 'admin_1_states_provinces_lakes_shp'
    states_shp = shpreader.natural_earth(resolution='110m',
                                         category='cultural', name=shapename)

    plt.title('US States')


    for state in shpreader.Reader(states_shp).geometries():
        # pick a default color for the land with a black outline,
        facecolor = 'yellow'
        edgecolor = 'black'

        ax.add_geometries([state], ccrs.PlateCarree(),
                          facecolor=facecolor, edgecolor=edgecolor)

    # add latitude and longitude lines
    ax.gridlines(draw_labels=True)
    ax.plot(LONGITUDES, LATITUDES, 'o', transform=ccrs.PlateCarree())
    plt.show()


if __name__ == '__main__':
    main()