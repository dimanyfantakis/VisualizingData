import pandas as pd
import numpy as np
import glob


def main():

    # list of all files
    data_files = [file for file in glob.glob('C:\\Users\\user\\GapMinderOriginalData\\*.csv')]
    # list of all countries in all datasets
    countries_avail = []
    # list of all years in all datasets
    years_avail = []
    # fill lists with all available countries and years from all dataset files
    for i in range(len(data_files)):
        df = pd.read_csv(data_files[i])
        for c in df.country:
            countries_avail.append(c)
        for x in df.columns.values:
            if x.isdigit():
                years_avail.append(int(x))
    # list with all unique countries sorted
    countries_final = sorted(set(countries_avail))
    # list with all unique years sorted
    years_final = sorted(set(years_avail))

    # np array with unique id's for all countries
    c_id = np.arange(len(countries_final))
    countries_arr = np.array(countries_final)
    # create dataframe to hold the countries ids and countries names
    countries_df = pd.DataFrame({'Countries_Id': c_id, 'Countries': countries_arr})

    # np array with unique id's for all years
    y_id = np.arange(len(years_final))
    # lists for organizing years by 5, 10, 20 years periods
    lstrm = [x // 5 + 1 for x in y_id]
    dcd = [x // 10 + 1 for x in y_id]
    vcnnl = [x // 20 + 1 for x in y_id]

    years_arr = np.array(years_final)
    lstr_arr = np.array(lstrm)
    dcd_arr = np.array(dcd)
    vcnnl_arr = np.array(vcnnl)
    # create dataframe to hold the years ids, years values and years categories
    years_df = pd.DataFrame(
        {'Years_Id': y_id, 'Years': years_arr, 'Lustrum': lstr_arr, 'Decade': dcd_arr, 'Vicennial': vcnnl_arr})

    transformed_data_files = []
    for i in range(len(data_files)):
        test = pd.read_csv(data_files[i])
        for c in countries_final:
            if c not in test.country.values:
                test = test.append({'country': c}, ignore_index=True)
        test.sort_values(by='country', inplace=True)
        for y in years_final:
            if y not in [int(x) for x in test.columns.values[1:]]:
                y2 = str(y)
                test[y2] = np.nan
        cols = [x for x in sorted(test.columns.values[1:])]
        test = test[cols]
        new_test = pd.DataFrame({data_files[i][:-4]: test.values.reshape(-1)})
        transformed_data_files.append(new_test)

    final_df = pd.concat(transformed_data_files, axis=1)

    # transform countries id to match final dataframe
    y = []
    for i in range(len(countries_final)):
        y.extend([i] * len(years_final))
    # transform years id to match final dataframe
    z = []
    for i in range(len(countries_final)):
        z.extend(y_id)
    c_id_final = np.array(y)
    y_id_final = np.array(z)
    # insert countries and years id to final dataframe
    final_df.insert(loc=0, column='y_id', value=y_id_final)
    final_df.insert(loc=0, column='c_id', value=c_id_final)
    # replace empty values
    final_df.replace('', np.nan, inplace=True)
    final_df.fillna(0, inplace=True)
    final_df.replace(',', '.', inplace=True)

    # remove punctuations
    countries_df['Countries'] = countries_df['Countries'].str.replace(r'[^\w\s]+', '')

    # write dataframes to csv files
    # final_df.to_csv('C:\\Users\\user\\GapMinderTransformedData\\measurements_data.csv', index=False)
    # countries_df.to_csv('C:\\Users\\user\\GapMinderTransformedData\\countries_data.csv', index=False)
    # years_df.to_csv('C:\\Users\\user\\GapMinderTransformedData\\years_data.csv', index=False)
    final_df.to_csv('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\measurements_data.csv', index=False)
    countries_df.to_csv('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\countries_data.csv', index=False)
    years_df.to_csv('C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\years_data.csv', index=False)


main()
