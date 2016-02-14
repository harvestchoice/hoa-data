#select ' data = mysite.action.bulk_update_private(datasets = [''' || id || '''], org_id = ''' ||  owner_org || ''')' from package where name in ('s9q1','s9q2');

import pandas as pd;
f1 = pd.read_csv('/Users/maria/Projects/hoa/Outputs/aux_files/diseases_Tharaka_2006_by region.csv')
f2 = pd.read_csv('/Users/maria/Projects/hoa/Outputs/aux_files/diseases_Tharaka_2007_by region.csv')
f3 = pd.read_csv('/Users/maria/Projects/hoa/Outputs/aux_files/diseases_Tharaka_2008_by region.csv')

print f3.columns
del f2['SUB-TOTAL.1'],f2['SUB-TOTAL.2'], f2['SUB-TOTAL'], f2['GRAND TOTAL'], f2['Unnamed: 23']
f1['year'] = 2006
f2['year'] = 2007
f3['year'] = 2008

result = f1.append([f2, f3])
print result.head
print list(result.columns.values)
result = result[['year', 'Month', 'DISEASES', 'CHIAKARIGA HC GOK', 'GACIONGO DISP GOK', 'GATUNGA DISP MISSION', 'JOSAN DISP PRIVATE', 'KAGENI DISP PRIVATE', 'KAMANYAKI DISP GOK', 'KAMWATHU', 'KANYURU DISP GOK', 'KATHANGACINI DISP', 'KIBUNGA H/C', 'MATERI GIRLS DISP MISSION', 'MUGAS CLINIC', 'MUKOTHIMA HC MISSION', 'NKONDI DISP GOK', 'RUUNGU DISP MISSION', 'ST ORSOLA HOSP MISSION', 'SUNSHINE CLINIC', 'THANANTU DISP NGO', 'THARAKA DIST HOSP', 'TUNYAI DISP GOK']]
print len(res)
res = result[result.DISEASES.notnull()]
res.to_csv('/Users/maria/Projects/hoa/Outputs/aux_files/diseases_by_region_06_to_08.csv', index = False)

l = [u'Samburu', u'Kitui']
print l
print ', '.join(l)

s = pd.read_csv('/Users/maria/Projects/hoa/Outputs/Human Capital/Health/Samburu/diseases_by_health_facility_2007.csv')
l = pd.read_csv('/Users/maria/Projects/hoa/Outputs/aux_files/Location.csv')
sl = pd.read_csv('/Users/maria/Projects/hoa/Outputs/aux_files/SubLocation.csv')
d = pd.read_csv('/Users/maria/Projects/hoa/Outputs/aux_files/Division.csv')
print l.columns
print len(s)
ml = pd.merge(s, l, how='left', left_on = 'LocationId', right_on = 'LocationId')
msl = pd.merge(s, sl, how='left', left_on = 'SubLocationId', right_on = 'SubLocationId')

# construct by division
md = pd.merge(s, d, how='left', left_on = 'DivisionId', right_on = 'DivisionId')
print len(md)
print list(md.columns.values)
md = md[['DivisionId', 'DivisionName', 'DiseasesQtyMalaria', 'DiseasesRankMalaria', 'DiseasesQtyGastroEnteritis', 'DiseasesRankGastroEnteritis', 'DiseasesQtyHIVAids', 'DiseasesRankHIVAids', 'DiseasesQtyTB', 'DiseasesRankTB', 'DiseasesQtyWorms', 'DiseasesRankWorms', 'DiseasesQtyURTILRTI', 'DiseasesRankURTILRTI', 'DiseasesQtyUTI', 'DiseasesRankUTI', 'DiseasesQtyGonorrhoea', 'DiseasesRankGonorrhoea', 'DiseasesQtySTD', 'DiseasesRankSTD', 'DiseasesQtySkinInfection', 'DiseasesRankSkinInfection', 'DiseasesQtyEyeInfection', 'DiseasesRankEyeInfection', 'DiseasesQtyAnaemia', 'DiseasesRankAnaemia', 'DiseasesQtyMalnutrition', 'DiseasesRankMalnutrition']]
mdg = md.groupby(['DivisionId', 'DivisionName']).sum().reset_index()
print mdg
mdg.to_csv('/Users/maria/Projects/hoa/Outputs/Human Capital/Health/Samburu/diseases_by_division_2007.csv', index = False)


#construct by sublocation
md = pd.merge(s, sl, how='left', left_on = 'SubLocationId', right_on = 'SubLocationId')
print len(md)
print list(md.columns.values)
md = md[['SubLocationId', 'SubLocationName', 'DiseasesQtyMalaria', 'DiseasesRankMalaria', 'DiseasesQtyGastroEnteritis', 'DiseasesRankGastroEnteritis', 'DiseasesQtyHIVAids', 'DiseasesRankHIVAids', 'DiseasesQtyTB', 'DiseasesRankTB', 'DiseasesQtyWorms', 'DiseasesRankWorms', 'DiseasesQtyURTILRTI', 'DiseasesRankURTILRTI', 'DiseasesQtyUTI', 'DiseasesRankUTI', 'DiseasesQtyGonorrhoea', 'DiseasesRankGonorrhoea', 'DiseasesQtySTD', 'DiseasesRankSTD', 'DiseasesQtySkinInfection', 'DiseasesRankSkinInfection', 'DiseasesQtyEyeInfection', 'DiseasesRankEyeInfection', 'DiseasesQtyAnaemia', 'DiseasesRankAnaemia', 'DiseasesQtyMalnutrition', 'DiseasesRankMalnutrition']]
mdg = md.groupby(['SubLocationId', 'SubLocationName']).sum().reset_index()
print mdg
mdg.to_csv('/Users/maria/Projects/hoa/Outputs/Human Capital/Health/Samburu/diseases_by_sublocation_2007.csv', index = False)


# construct by location
md = pd.merge(s, l, how='left', left_on = 'LocationId', right_on = 'LocationId')
print len(md)
print list(md.columns.values)
md = md[['LocationId', 'LocationName', 'DiseasesQtyMalaria', 'DiseasesRankMalaria', 'DiseasesQtyGastroEnteritis', 'DiseasesRankGastroEnteritis', 'DiseasesQtyHIVAids', 'DiseasesRankHIVAids', 'DiseasesQtyTB', 'DiseasesRankTB', 'DiseasesQtyWorms', 'DiseasesRankWorms', 'DiseasesQtyURTILRTI', 'DiseasesRankURTILRTI', 'DiseasesQtyUTI', 'DiseasesRankUTI', 'DiseasesQtyGonorrhoea', 'DiseasesRankGonorrhoea', 'DiseasesQtySTD', 'DiseasesRankSTD', 'DiseasesQtySkinInfection', 'DiseasesRankSkinInfection', 'DiseasesQtyEyeInfection', 'DiseasesRankEyeInfection', 'DiseasesQtyAnaemia', 'DiseasesRankAnaemia', 'DiseasesQtyMalnutrition', 'DiseasesRankMalnutrition']]
mdg = md.groupby(['LocationId', 'LocationName']).sum().reset_index()
print mdg
mdg.to_csv('/Users/maria/Projects/hoa/Outputs/Human Capital/Health/Samburu/diseases_by_location_2007.csv', index = False)


a = pd.merge(s, d, how='left', left_on = 'DivisionId', right_on = 'DivisionId')
a = pd.merge(a, sl, how='left', left_on = 'SubLocationId', right_on = 'SubLocationId')
a = pd.merge(a, l, how='left', left_on = 'LocationId_x', right_on = 'LocationId')
print len(a)
print list(a.columns.values)
a['DivisionId'] = a['DivisionId_x']
a['LocationId'] = s['LocationId']
a = a[['HealthFacilityId', 'QDate', 'SheetNo', 'InstitutionName', 'InstitutionType', 'InfraStructure', 'x','y','XCoordinateGPS', 'YCoordinateGPS', 'ElevationM', 'SubLocationId', 'SubLocationName','LocationId','LocationName','DivisionId', 'DivisionName', 'Ownership', 'OwnershipReligious', 'DiseasesQtyMalaria', 'DiseasesRankMalaria', 'DiseasesQtyGastroEnteritis', 'DiseasesRankGastroEnteritis', 'DiseasesQtyHIVAids', 'DiseasesRankHIVAids', 'DiseasesQtyTB', 'DiseasesRankTB', 'DiseasesQtyWorms', 'DiseasesRankWorms', 'DiseasesQtyURTILRTI', 'DiseasesRankURTILRTI', 'DiseasesQtyUTI', 'DiseasesRankUTI', 'DiseasesQtyGonorrhoea', 'DiseasesRankGonorrhoea', 'DiseasesQtySTD', 'DiseasesRankSTD', 'DiseasesQtySkinInfection', 'DiseasesRankSkinInfection', 'DiseasesQtyEyeInfection', 'DiseasesRankEyeInfection', 'DiseasesQtyAnaemia', 'DiseasesRankAnaemia', 'DiseasesQtyMalnutrition', 'DiseasesRankMalnutrition']]
print len(a)
print a.head()

import utm
get_x = lambda row: utm.to_latlon(row['XCoordinateGPS'], row['YCoordinateGPS'], 37, 'northern')[0]
a['x'] = a.apply(get_x, axis = 1)
get_y = lambda row: utm.to_latlon(row['XCoordinateGPS'], row['YCoordinateGPS'], 37, 'northern')[1]
a['y'] = a.apply(get_y, axis = 1)

#print utm.to_latlon(238305, 118203, 37, 'northern')[0]

a.to_csv('/Users/maria/Projects/hoa/Outputs/Human Capital/Health/Samburu/diseases_by_health_facility_2007.csv', index = False)


###########
a = pd.read_csv('/Users/maria/Projects/hoa/Outputs/Human Capital/Health/Tharaka/diseases_by_health_facilities_2006-2008.csv')
a.replace('\'', 0, inplace = True)
a.replace('#DIV/0!', 0, inplace = True)
a.fillna(0, inplace=True)

th = a.convert_objects(convert_numeric=True)

print th.dtypes
print float(th['THARAKA DIST HOSP'])
print th['CHIAKARIGA HC GOK'].unique()
print th['MATERI GIRLS DISP MISSION'].unique()
th['CENTRAL'] = th['THARAKA DIST HOSP']+th['RUUNGU DISP MISSION']+th['NKONDI DISP GOK']+th['JOSAN DISP PRIVATE']+th['GATUNGA DISP MISSION']+th['KIBUNGA H/C']+th['KANYURU DISP GOK']
th['NORTH'] = th['KATHANGACINI DISP']+th['MUKOTHIMA HC MISSION']+th['KAGENI DISP PRIVATE']+th['GACIONGO DISP GOK']+th['THANANTU DISP NGO']
th['SOUTH'] = th['CHIAKARIGA HC GOK']+th['ST ORSOLA HOSP MISSION']+th['TUNYAI DISP GOK']+th['MATERI GIRLS DISP MISSION']+th['KAMANYAKI DISP GOK']
th = th[['year', 'Month', 'DISEASES', 'CENTRAL', 'NORTH', 'SOUTH']]
print th.head()
th['Month_Year'] = th['year'].map(str) + th['Month'] + th['DISEASES']
d = th.pivot(index=['Month_Year'], columns='DISEASES', values=['CENTRAL','NORTH', 'SOUTH'])
d = th.pivot(['Month', 'year'], 'CENTRAL')
print d.head()
th.to_csv('/Users/maria/Projects/hoa/Outputs/Human Capital/Health/Tharaka/diseases_by_divisions_2006-2008.csv', index = False)
print list(th.columns.values)
th.to_csv('')
import numpy


'''
sub ce sub-component pun dhs si ibli

Pseudo panel data

sub -comp - 
Ecology - NDVI, 
climate - rainfall, drought, temp (Agroecology)
one entry for dhs regression results
one pseudo pane dhs data, 
map cu variation in time

22 1-5, 

upload https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/G4TBLF
'''
