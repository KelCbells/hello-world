# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# LSDM_QC.py
# Created on: 2019-01-15 09:52:56.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: LSDM_QC <v99__Quartile> <Output_Folder> <Quality_Controlled__Reduced_Resolution_Raster> <Polygon_Name> <Coarse_LSDM> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
v99__Quartile = arcpy.GetParameterAsText(0)
if v99__Quartile == '#' or not v99__Quartile:
    v99__Quartile = "0 5.370117 1;5.370117 81.518555 2" # provide a default value if unspecified

Output_Folder = arcpy.GetParameterAsText(1)
if Output_Folder == '#' or not Output_Folder:
    Output_Folder = "C:\\Kelsey\\Fall_Sem\\WCW_3m" # provide a default value if unspecified

Quality_Controlled__Reduced_Resolution_Raster = arcpy.GetParameterAsText(2)
if Quality_Controlled__Reduced_Resolution_Raster == '#' or not Quality_Controlled__Reduced_Resolution_Raster:
    Quality_Controlled__Reduced_Resolution_Raster = "C:\\Kelsey\\Fall_Sem\\WCW_3m\\wcw_f14x.tif" # provide a default value if unspecified

Polygon_Name = arcpy.GetParameterAsText(3)
if Polygon_Name == '#' or not Polygon_Name:
    Polygon_Name = "wcw_f14x_1qc.shp" # provide a default value if unspecified

Coarse_LSDM = arcpy.GetParameterAsText(4)
if Coarse_LSDM == '#' or not Coarse_LSDM:
    Coarse_LSDM = "C:\\Kelsey\\Fall_Sem\\DEMs\\LSDM_f14_15m.tif" # provide a default value if unspecified

# Local variables:
Reclassified_Coarse_LSDM = "C:\\Kelsey\\Fall_Sem\\WCW_3m\\wcw_f14x_rec.tif"
Quality_Control_Shapefile = "C:\\Kelsey\\Fall_Sem\\WCW_3m\\wcw_f14x_QC_rtp.shp"
v99__Polygon = Quality_Control_Shapefile
SQL_Expression = "GRIDCODE = 1"
Watershed_Boundary = "C:\\Kelsey\\Fall_Sem\\WatershedExtents\\wcw_CSRS.shp"
Clipped_99__Polygon = "C:\\Kelsey\\Fall_Sem\\wcw_f14x_1qc_Clip.shp"
Final_Raster = Quality_Controlled__Reduced_Resolution_Raster

# Process: Reclassify
arcpy.gp.Reclassify_sa(Coarse_LSDM, "Value", v99__Quartile, Reclassified_Coarse_LSDM, "DATA")

# Process: Raster to Polygon
arcpy.RasterToPolygon_conversion(Reclassified_Coarse_LSDM, Quality_Control_Shapefile, "NO_SIMPLIFY", "VALUE")

# Process: Feature Class to Feature Class
arcpy.FeatureClassToFeatureClass_conversion(Quality_Control_Shapefile, Output_Folder, Polygon_Name, SQL_Expression, "ID \"ID\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\wcw_f14x_QC_rtp.shp,ID,-1,-1;GRIDCODE \"GRIDCODE\" true true false 0 Long 0 0 ,First,#,C:\\Kelsey\\Fall_Sem\\WCW_3m\\wcw_f14x_QC_rtp.shp,GRIDCODE,-1,-1", "")

# Process: Clip
arcpy.Clip_analysis(v99__Polygon, Watershed_Boundary, Clipped_99__Polygon, "")

# Process: Extract by Mask
arcpy.gp.ExtractByMask_sa(Coarse_LSDM, Clipped_99__Polygon, Quality_Controlled__Reduced_Resolution_Raster)

# Process: Build Pyramids And Statistics
arcpy.BuildPyramidsandStatistics_management(Quality_Controlled__Reduced_Resolution_Raster, "INCLUDE_SUBDIRECTORIES", "BUILD_PYRAMIDS", "CALCULATE_STATISTICS", "NONE", "", "NONE", "1", "1", "", "-1", "NONE", "NEAREST", "DEFAULT", "75", "SKIP_EXISTING")

