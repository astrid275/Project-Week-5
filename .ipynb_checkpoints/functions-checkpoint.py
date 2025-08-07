def clean_column_names(dataframe):
    dataframe.columns = dataframe.columns.str.lower().str.replace(" ","_")
    return dataframe