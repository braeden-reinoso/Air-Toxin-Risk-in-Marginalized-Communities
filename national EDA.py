import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

# loading census and epa csvs

us_epa = pd.read_csv("data/epa_data/epa_tracts_continental_us.csv")

us_census = pd.read_csv("data/census_data/acs_all_tracts_cleaned.csv")

# merging csvs and computing values

us_full = pd.merge(us_epa,us_census,on='ID')
us_full['density'] = us_full['pop_tot'] / (us_full['AREALAND'])
us_full['sec_ind_share'] = (us_full['industry_ag_for']+ us_full['industry_const'] + us_full['industry_manu']) / us_full['industry_tot']
us_full['health_ins_pct'] = us_full['health_ins_yes'] / us_full['health_ins_tot']

us_full['white_only_pct'] = us_full['pop_white_only'] / us_full['pop_tot']
us_full['white_pct'] = us_full['pop_white'] / us_full['pop_tot']
us_full['black_pct'] = us_full['pop_black'] / us_full['pop_tot']
us_full['asian_pct'] = us_full['pop_asian'] / us_full['pop_tot']
us_full['hispanic_pct'] = us_full['pop_hispanic_latino_any'] / us_full['pop_tot']

us_full['PN_density'] = us_full['density'].rank(pct=True)*100
us_full['PN_sec_ind_share'] = us_full['sec_ind_share'].rank(pct=True)*100
us_full['PN_health_ins_pct'] = us_full['health_ins_pct'].rank(pct=True)*100
us_full['PN_income_median'] = us_full['income_median'].rank(pct=True)*100

us_full['PN_white_only_pct'] = us_full['white_only_pct'].rank(pct=True)*100
us_full['PN_white_pct'] = us_full['white_pct'].rank(pct=True)*100
us_full['PN_black_pct'] = us_full['black_pct'].rank(pct=True)*100
us_full['PN_asian_pct'] = us_full['asian_pct'].rank(pct=True)*100
us_full['PN_hispanic_pct'] = us_full['hispanic_pct'].rank(pct=True)*100

urban_full = us_full[us_full['pop_tot'] > 5000]

# continental us dataframes

us_env_raw = us_full[['PN_CANCER', 'PM25', 'OZONE', 'DSLPM', 'RESP', 'RSEI_AIR', 'PNPL', 'PRMP', 'PTSDF', 'UST', 'PWDIS']]
us_env_national = us_full[['PN_CANCER', 'PN_RESP', 'PN_PM25', 'PN_OZONE', 'PN_DSLPM', 'PN_RSEI_AIR', 'PN_PNPL', 'PN_PRMP', 'PN_PTSDF', 'PN_UST', 'PN_PWDIS']]
us_env_state = us_full[['PN_CANCER', 'PS_PM25', 'PS_OZONE', 'PS_DSLPM', 'PS_RESP', 'PS_RSEI_AIR', 'PS_PNPL', 'PS_PRMP', 'PS_PTSDF', 'PS_UST', 'PS_PWDIS']]

us_race = us_full[['PN_CANCER', 'white_only_pct', 'white_pct', 'black_pct', 'asian_pct', 'hispanic_pct']]
us_race_national = us_full[['PN_CANCER', 'PN_white_only_pct', 'PN_black_pct', 'PN_asian_pct', 'PN_hispanic_pct']]

us_econ = us_full[['PN_CANCER', 'density', 'PN_PTRAF', 'PN_LDPNT', 'sec_ind_share', 'income_median', 'health_ins_pct']]
us_econ_national = us_full[['PN_CANCER', 'PN_density', 'PN_PTRAF', 'PN_LDPNT', 'PN_sec_ind_share', 'PN_income_median', 'PN_health_ins_pct']]

# urban dataframes

urban_env_raw = urban_full[['PN_CANCER', 'PM25', 'OZONE', 'DSLPM', 'RESP', 'RSEI_AIR', 'PNPL', 'PRMP', 'PTSDF', 'UST', 'PWDIS']]
urban_env_national = urban_full[['PN_CANCER', 'PN_RESP', 'PN_PM25', 'PN_OZONE', 'PN_DSLPM', 'PN_RSEI_AIR', 'PN_PNPL', 'PN_PRMP', 'PN_PTSDF', 'PN_UST', 'PN_PWDIS']]
urban_env_state = urban_full[['PN_CANCER', 'PS_PM25', 'PS_OZONE', 'PS_DSLPM', 'PS_RESP', 'PS_RSEI_AIR', 'PS_PNPL', 'PS_PRMP', 'PS_PTSDF', 'PS_UST', 'PS_PWDIS']]

urban_race = urban_full[['PN_CANCER', 'white_only_pct', 'white_pct', 'black_pct', 'asian_pct', 'hispanic_pct']]
urban_race_national = urban_full[['PN_CANCER', 'PN_white_only_pct', 'PN_black_pct', 'PN_asian_pct', 'PN_hispanic_pct']]

urban_econ = urban_full[['PN_CANCER', 'density', 'PN_PTRAF', 'PN_LDPNT', 'sec_ind_share', 'income_median', 'health_ins_pct']]
urban_econ_national = urban_full[['PN_CANCER', 'PN_density', 'PN_PTRAF', 'PN_LDPNT', 'PN_sec_ind_share', 'PN_income_median', 'PN_health_ins_pct']]


# correlation table

fig, axes = plt.subplots(3, figsize=(100, 300))

sns.heatmap(us_env_national.corr(), annot = True, cmap = 'BrBG', ax = axes[0])
sns.heatmap(us_race_national.corr(), annot = True, cmap = 'BrBG', ax = axes[1])
sns.heatmap(us_econ_national.corr(), annot = True, cmap = 'BrBG', ax = axes[2])

plt.show()
