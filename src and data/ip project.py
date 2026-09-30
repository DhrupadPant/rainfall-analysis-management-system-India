import pandas as pd
import matplotlib.pyplot as plt


# =========================================
# RAINFALL ANALYSIS AND MANAGEMENT SYSTEM
# =========================================

# Reading the CSV file
df = pd.read_csv("rainfall.csv")

# Removing extra spaces from column names
df.columns = df.columns.str.strip()


# =========================================
# FUNCTION 1: DISPLAY DATA
# =========================================

def display_data():

    print("\nFIRST 10 RECORDS")
    print("----------------")

    print(df.head(10))


# =========================================
# FUNCTION 2: ANALYSE A PARTICULAR YEAR
# =========================================

def year_analysis():

    year = int(input("Enter year (1901-2015): "))

    if year in df["YEAR"].values:

        record = df[df["YEAR"] == year].iloc[0]

        print("\n================================")
        print("       RAINFALL ANALYSIS")
        print("================================")

        print("Region:", record["REGION"])
        print("Year:", year)

        print("\nMONTHLY RAINFALL")
        print("----------------")

        print("January   :", record["JAN"], "mm")
        print("February  :", record["FEB"], "mm")
        print("March     :", record["MAR"], "mm")
        print("April     :", record["APR"], "mm")
        print("May       :", record["MAY"], "mm")
        print("June      :", record["JUN"], "mm")
        print("July      :", record["JUL"], "mm")
        print("August    :", record["AUG"], "mm")
        print("September :", record["SEP"], "mm")
        print("October   :", record["OCT"], "mm")
        print("November  :", record["NOV"], "mm")
        print("December  :", record["DEC"], "mm")

        print("\nSEASONAL RAINFALL")
        print("-----------------")

        print("Jan-Feb :", record["Jan-Feb"], "mm")
        print("Mar-May :", record["Mar-May"], "mm")
        print("Jun-Sep :", record["Jun-Sep"], "mm")
        print("Oct-Dec :", record["Oct-Dec"], "mm")

        print("\nAnnual Rainfall:",
              record["ANNUAL"], "mm")

        # Rainfall classification
        annual = record["ANNUAL"]

        if annual < 800:

            print("\nRainfall Status: LOW")
            print("Management Advice:")
            print("Water conservation should be prioritized.")

        elif annual < 1200:

            print("\nRainfall Status: NORMAL")
            print("Management Advice:")
            print("Maintain normal water storage.")

        else:

            print("\nRainfall Status: HIGH")
            print("Management Advice:")
            print("Monitor drainage and water storage.")


    else:

        print("Year not found in dataset.")


# =========================================
# FUNCTION 3: AVERAGE ANNUAL RAINFALL
# =========================================

def average_rainfall():

    average = df["ANNUAL"].mean()

    print("\nAVERAGE ANNUAL RAINFALL")
    print("-----------------------")

    print("Average:", round(average, 2), "mm")


# =========================================
# FUNCTION 4: HIGHEST RAINFALL YEAR
# =========================================

def highest_rainfall():

    index = df["ANNUAL"].idxmax()

    year = df.loc[index, "YEAR"]
    rainfall = df.loc[index, "ANNUAL"]

    print("\nHIGHEST ANNUAL RAINFALL")
    print("-----------------------")

    print("Year:", year)
    print("Rainfall:", rainfall, "mm")


# =========================================
# FUNCTION 5: LOWEST RAINFALL YEAR
# =========================================

def lowest_rainfall():

    index = df["ANNUAL"].idxmin()

    year = df.loc[index, "YEAR"]
    rainfall = df.loc[index, "ANNUAL"]

    print("\nLOWEST ANNUAL RAINFALL")
    print("----------------------")

    print("Year:", year)
    print("Rainfall:", rainfall, "mm")


# =========================================
# FUNCTION 6: AVERAGE MONTHLY RAINFALL
# =========================================

def monthly_average():

    months = [
        "JAN", "FEB", "MAR", "APR",
        "MAY", "JUN", "JUL", "AUG",
        "SEP", "OCT", "NOV", "DEC"
    ]

    print("\nAVERAGE MONTHLY RAINFALL")
    print("------------------------")

    for month in months:

        average = df[month].mean()

        print(month, ":", round(average, 2), "mm")


# =========================================
# FUNCTION 7: AVERAGE SEASONAL RAINFALL
# =========================================

def seasonal_average():

    seasons = [
        "Jan-Feb",
        "Mar-May",
        "Jun-Sep",
        "Oct-Dec"
    ]

    print("\nAVERAGE SEASONAL RAINFALL")
    print("-------------------------")

    for season in seasons:

        average = df[season].mean()

        print(season, ":", round(average, 2), "mm")


# =========================================
# FUNCTION 8: ANNUAL RAINFALL GRAPH
# =========================================

def rainfall_graph():

    plt.figure(figsize=(10, 5))

    plt.plot(df["YEAR"], df["ANNUAL"])

    plt.title("Annual Rainfall in India (1901-2015)")
    plt.xlabel("Year")
    plt.ylabel("Rainfall (mm)")

    plt.grid()

    plt.show()


# =========================================
# FUNCTION 9: MONTHLY RAINFALL GRAPH
# =========================================

def monthly_graph():

    months = [
        "JAN", "FEB", "MAR", "APR",
        "MAY", "JUN", "JUL", "AUG",
        "SEP", "OCT", "NOV", "DEC"
    ]

    rainfall = []

    for month in months:

        rainfall.append(df[month].mean())

    plt.figure(figsize=(10, 5))

    plt.bar(months, rainfall)

    plt.title("Average Monthly Rainfall in India")
    plt.xlabel("Month")
    plt.ylabel("Average Rainfall (mm)")

    plt.show()


# =========================================
# FUNCTION 10: SEASONAL RAINFALL GRAPH
# =========================================

def seasonal_graph():

    seasons = [
        "Jan-Feb",
        "Mar-May",
        "Jun-Sep",
        "Oct-Dec"
    ]

    rainfall = []

    for season in seasons:

        rainfall.append(df[season].mean())

    plt.figure(figsize=(8, 5))

    plt.bar(seasons, rainfall)

    plt.title("Average Seasonal Rainfall in India")
    plt.xlabel("Season")
    plt.ylabel("Average Rainfall (mm)")

    plt.show()


# =========================================
# MAIN MENU
# =========================================

while True:

    print("\n==========================================")
    print("     RAINFALL ANALYSIS AND MANAGEMENT")
    print("==========================================")

    print("1. Display rainfall data")
    print("2. Analyse a particular year")
    print("3. Calculate average annual rainfall")
    print("4. Find highest rainfall year")
    print("5. Find lowest rainfall year")
    print("6. Display average monthly rainfall")
    print("7. Display average seasonal rainfall")
    print("8. Display annual rainfall graph")
    print("9. Display monthly rainfall graph")
    print("10. Display seasonal rainfall graph")
    print("11. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:

        display_data()

    elif choice == 2:

        year_analysis()

    elif choice == 3:

        average_rainfall()

    elif choice == 4:

        highest_rainfall()

    elif choice == 5:

        lowest_rainfall()

    elif choice == 6:

        monthly_average()

    elif choice == 7:

        seasonal_average()

    elif choice == 8:

        rainfall_graph()

    elif choice == 9:

        monthly_graph()

    elif choice == 10:

        seasonal_graph()

    elif choice == 11:

        print("\nThank you for using the")
        print("Rainfall Analysis and Management System.")

        break

    else:

        print("Invalid choice. Please enter 1-11.")

