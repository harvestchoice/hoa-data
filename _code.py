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