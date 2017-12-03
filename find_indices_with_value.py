

def find_indices_with_value(df, value):
    """Return the row indices of a Pandas Dataframe where the row contains the given value.
    
    Parameters
    ----------
    
    df: Pandas Dataframe
    value: value we want to see if row contains
    
    Return
    ------
    array
        An integer array where each value is the row index of a row that contains the value
        
    Example
    -------
    
    >>> row0 = [">", "?", "!"]
    ... df = pd.DataFrame([row0])
    ... find_indices_with_value(df, "?")
    array([0])
    """    
    
    
    rows = []
    for index, row in df.iterrows():
        if value in row.unique():
            rows.append(index)
    return np.array(rows) 
