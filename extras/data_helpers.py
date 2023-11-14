def look_nan(df):
    print(f"File containd NaN-values: {df.isnull().values.any()}")
    print(df.head())