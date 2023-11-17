def look_for_nan(df):
    print('------------------------------------')
    print(f"File containd NaN-values: {df.isnull().values.any()}")
    print('------------------------------------')

def info(df, column_name: str) -> None:
    print(f'Column names: {df.columns}')
    print('---------------------------')
    print('\tDescription')
    print('---------------------------')
    print(df[column_name].describe())