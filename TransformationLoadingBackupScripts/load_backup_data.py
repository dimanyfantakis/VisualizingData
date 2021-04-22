import mysql.connector


def main():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="mysqlpassword",
            database="gapminderdb"
            )

        cursor = connection.cursor()
        # load data to tables
        load_countries_table = """LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/countries_data.csv' 
        INTO TABLE countries
        FIELDS TERMINATED BY ','
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS
        (C_ID, C_Name);
        """

        load_years_table = """LOAD DATA  INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/years_data.csv' 
        INTO TABLE years
        FIELDS TERMINATED BY ','
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS
        (Y_ID, Year, Lustrum, Decade, Vicennial);
        """

        load_measurements_table = """LOAD DATA  INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/measurements_data.csv' 
        INTO TABLE measurements
        FIELDS TERMINATED BY ','
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS
        (Countries_C_ID, Years_Y_ID, Civil_Liberties, Democracy, Direct_Democracy, Electoral_Participation, Freedom_of_Expression,
         Freedom_Of_Movement, Freedom_Of_Religion, Free_Political_Parties, Fundamental_Rights, Gender_Equality, 
         Gini_Index, Hapiscore, Human_Development, Local_Democracy, Social_Group, Social_Rights_And_Equality,
         Urban_Population);
        """

        cursor.execute(load_countries_table)
        cursor.execute(load_years_table)
        cursor.execute(load_measurements_table)
        connection.commit()

        # create backup
        countries_backup = """SELECT *
        INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/countries_backup.csv'
        FIELDS TERMINATED BY ","
        OPTIONALLY ENCLOSED BY '"'
        ESCAPED BY '\'
        LINES TERMINATED BY '\n'
        FROM countries"""

        years_backup = """SELECT *
        INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/years_backup.csv'
        FIELDS TERMINATED BY ","
        OPTIONALLY ENCLOSED BY '"'
        ESCAPED BY '\'
        LINES TERMINATED BY '\n'
        FROM years"""

        measurements_backup = """SELECT *
        INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/measurements_backup.csv'
        FIELDS TERMINATED BY ","
        OPTIONALLY ENCLOSED BY '"'
        ESCAPED BY '\'
        LINES TERMINATED BY '\n'
        FROM measurements"""

        cursor.execute(countries_backup)
        cursor.execute(years_backup)
        cursor.execute(measurements_backup)
        connection.commit()

    except Exception as e:
        print(e)


main()
