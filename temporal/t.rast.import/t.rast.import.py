#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################################################################
#
# MODULE:        t.rast.import
# AUTHOR(S):     Soeren Gebbert
#
# PURPOSE:        Import a space time raster dataset
# COPYRIGHT:        (C) 2011-2014 by the GRASS Development Team
#
#                This program is free software under the GNU General Public
#                License (version 2). Read the file COPYING that comes with GRASS
#                for details.
#
#############################################################################

#%module
#% description: Imports space time raster dataset.
#% keyword: temporal
#% keyword: import
#% keyword: raster
#% keyword: time
#%end

#%option G_OPT_F_INPUT
#%end

#%option G_OPT_STRDS_OUTPUT
#%end

#%option
#% key: basename
#% type: string
#% label: Basename of the new generated output maps
#% description: A numerical suffix separated by an underscore will be attached to create a unique identifier
#% required: no
#% multiple: no
#% gisprompt:
#%end

#%option G_OPT_M_DIR
#% key: directory
#% description: Path to the extraction directory
#% answer: /tmp
#%end

#%option
#% key: title
#% type: string
#% description: Title of the new space time dataset
#% required: no
#% multiple: no
#%end

#%option
#% key: description
#% type: string
#% description: Description of the new space time dataset
#% required: no
#% multiple: no
#%end

#%option
#% key: location
#% type: string
#% description: Create a new location and import the data into it. Do not run this module in parallel or interrupt it when a new location should be created
#% required: no
#% multiple: no
#%end

#%option
#% key: memory
#% type: integer
#% description: Cache size for raster rows
#% label: Maximum memory to be used (in MB)
#% options: 0-2047
#% answer: 300
#% multiple: no
#%end

#%flag
#% key: r
#% description: Set the current region from the last map that was imported
#%end

#%flag
#% key: l
#% description: Link the raster files using r.external
#%end

#%flag
#% key: e
#% description: Extend location extents based on new dataset
#%end

#%flag
#% key: o
#% label: Override projection check (use current location's projection)
#% description: Assume that the dataset has same projection as the current location
#%end

#%flag
#% key: c
#% description: Create the location specified by the "location" parameter and exit. Do not import the space time raster datasets.
#%end

import grass.script as grass


def main():
    # lazy imports
    import grass.temporal as tgis

    # Get the options
    input = options["input"]
    output = options["output"]
    directory = options["directory"]
    title = options["title"]
    descr = options["description"]
    location = options["location"]
    base = options["basename"]
    memory = options["memory"]
    set_current_region = flags["r"]
    link = flags["l"]
    exp = flags["e"]
    overr = flags["o"]
    create = flags["c"]

    tgis.init()

    tgis.import_stds(input, output, directory, title, descr, location,
                     link, exp, overr, create, "strds", base, 
                     set_current_region, memory)

if __name__ == "__main__":
    options, flags = grass.parser()
    main()
