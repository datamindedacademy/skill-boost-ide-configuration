def dataframe_modifier(dataframe, fact):
    dataframe['a'] = dataframe['a'] * fact
    return dataframe