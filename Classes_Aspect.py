# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Classes_Aspect.py
# Created on: 2019-01-15 09:50:58.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: Classes_Aspect <Output_Folder> <Input_raster> <RTP_DEM> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
Output_Folder = arcpy.GetParameterAsText(0)
if Output_Folder == '#' or not Output_Folder:
    Output_Folder = "C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f" # provide a default value if unspecified

Input_raster = arcpy.GetParameterAsText(1)

RTP_DEM = arcpy.GetParameterAsText(2)
if RTP_DEM == '#' or not RTP_DEM:
    RTP_DEM = "C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp" # provide a default value if unspecified

# Local variables:
Simplify_polygons = "false"
v1f = RTP_DEM
v2f_premerge = RTP_DEM
v3f = RTP_DEM
v4f = RTP_DEM
v5f = RTP_DEM
v6f = RTP_DEM
v7f = RTP_DEM
v8f = RTP_DEM
v9f = RTP_DEM
v10f_premerge = RTP_DEM
v1f_poly = "wcw_s14x_1f.shp"
v3f_poly = "wcw_s14x_3k.shp"
v4f_poly = "wcw_s14x_4k.shp"
v5f_poly = "wcw_s14x_5k.shp"
v6f_poly = "wcw_s14x_6k.shp"
v7f_poly = "wcw_s14x_7k.shp"
v8f_poly = "wcw_s14x_8k.shp"
v9f_poly = "wcw_s14x_9k.shp"
v2f_poly = "wcw_s14x_2f_premerge.shp"
v10f_poly = "wcw_s14x_10k.shp"
merged_2f = "C:\\Users\\kelsey.cartwright\\Documents\\ArcGIS\\Default.gdb\\wcw_s14x_2f_Merge"

# Process: Raster to Polygon
arcpy.RasterToPolygon_conversion(Input_raster, RTP_DEM, Simplify_polygons, "")

# Process: 1f_unclipped
arcpy.FeatureClassToFeatureClass_conversion(RTP_DEM, Output_Folder, v1f_poly, "\"GRIDCODE\" =  1", "ID \"ID\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,ID,-1,-1;GRIDCODE \"GRIDCODE\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,GRIDCODE,-1,-1", "")

# Process: 3f_unclipped
arcpy.FeatureClassToFeatureClass_conversion(RTP_DEM, Output_Folder, v3f_poly, "\"GRIDCODE\" =    3", "ID \"ID\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,ID,-1,-1;GRIDCODE \"GRIDCODE\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,GRIDCODE,-1,-1", "")

# Process: 4f_unclipped
arcpy.FeatureClassToFeatureClass_conversion(RTP_DEM, Output_Folder, v4f_poly, "\"GRIDCODE\" =  4", "ID \"ID\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,ID,-1,-1;GRIDCODE \"GRIDCODE\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,GRIDCODE,-1,-1", "")

# Process: 5f_unclipped
arcpy.FeatureClassToFeatureClass_conversion(RTP_DEM, Output_Folder, v5f_poly, "\"GRIDCODE\" =  5", "ID \"ID\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,ID,-1,-1;GRIDCODE \"GRIDCODE\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,GRIDCODE,-1,-1", "")

# Process: 6f_unclipped
arcpy.FeatureClassToFeatureClass_conversion(RTP_DEM, Output_Folder, v6f_poly, "\"GRIDCODE\" =   6", "ID \"ID\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,ID,-1,-1;GRIDCODE \"GRIDCODE\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,GRIDCODE,-1,-1", "")

# Process: 7f_unclipped
arcpy.FeatureClassToFeatureClass_conversion(RTP_DEM, Output_Folder, v7f_poly, "\"GRIDCODE\" =    7", "ID \"ID\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,ID,-1,-1;GRIDCODE \"GRIDCODE\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,GRIDCODE,-1,-1", "")

# Process: 8f_unclipped
arcpy.FeatureClassToFeatureClass_conversion(RTP_DEM, Output_Folder, v8f_poly, "\"GRIDCODE\" =  8", "ID \"ID\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,ID,-1,-1;GRIDCODE \"GRIDCODE\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,GRIDCODE,-1,-1", "")

# Process: 9f_unclipped
arcpy.FeatureClassToFeatureClass_conversion(RTP_DEM, Output_Folder, v9f_poly, "\"GRIDCODE\" =  9", "ID \"ID\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,ID,-1,-1;GRIDCODE \"GRIDCODE\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,GRIDCODE,-1,-1", "")

# Process: 2f_unclipped
arcpy.FeatureClassToFeatureClass_conversion(RTP_DEM, Output_Folder, v2f_poly, "\"GRIDCODE\" =   2", "ID \"ID\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,ID,-1,-1;GRIDCODE \"GRIDCODE\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,GRIDCODE,-1,-1", "")

# Process: 10f_unclipped
arcpy.FeatureClassToFeatureClass_conversion(RTP_DEM, Output_Folder, v10f_poly, "\"GRIDCODE\" =  10", "ID \"ID\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,ID,-1,-1;GRIDCODE \"GRIDCODE\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_f_rtp.shp,GRIDCODE,-1,-1", "")

# Process: 2&10 merge
arcpy.Merge_management("C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_2f_premerge.shp;C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_10k.shp", merged_2f, "ID \"ID\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_10k.shp,ID,-1,-1,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_2f_premerge.shp,ID,-1,-1;GRIDCODE \"GRIDCODE\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_10k.shp,GRIDCODE,-1,-1,C:\\Kelsey\\Fall_Sem\\WCW_3m\\aspect_f\\wcw_s14x_2f_premerge.shp,GRIDCODE,-1,-1")

