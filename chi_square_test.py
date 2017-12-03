def chi_square_test(data, var1, var2, pairwise = False, alpha = 0.05):
    """Performs a chi-square test on two categorical variables, with one being group 
    If doing pairwise comparisions for groups, perform chi-square test on each pair. 
    Displays contigency tables (in percents) that are statistically significant. 
    If there are rows in the contigency with 0s, we delete these rows. 
    
    Parameters
    ----------
    data: Pandas Dataframe
    var1: one categorical column of the data Dataframe
    var2: one categorical column of the data Dataframe. In our case this will be the group column.
    pairwise: if true, do pairwise comparisions.
    alpha: significance level
    
    Return
    ------
    if pairwise: 
        None
    else:
        rtn 
           A tuple where 
           the first value is the chi-square value
           the second value is the p-value
           the third value is the degrees of freedom
           the fourth value is the expected counts 
        
    """    
    cont_table = pd.crosstab(data[var1], data[var2])
    if not pairwise:
        missing_indices = find_indices_with_value(cont_table, 0)
        cont_table = cont_table.drop(missing_indices)
        chi2, p, df, exp = stats.chi2_contingency(cont_table)
        if (p < alpha): 
            print("statistically significant: %s" % (tuple([var1, var2]), ))
            print("p-value is " + str(p))
            display(cont_table.apply(lambda r: 100 * r/r.sum(), axis=0))

        return chi2, p, df, exp
    else:
        pairs = [",".join(map(str, comb)).split(",") for comb in combinations(cont_table.columns, 2)]
        for pair in pairs:
            cont_table2 = cont_table[pair]
            missing_indices = find_indices_with_value(cont_table2, 0)
            cont_table2 = cont_table2.drop(missing_indices)
        
            chi2, p, df, exp = stats.chi2_contingency(cont_table2)
            if (p < alpha): 
                print("statistically significant: %s" % (tuple(pair), ))
                print("p-value is " + str(p))
                display(cont_table2.apply(lambda r: 100 * r/r.sum(), axis=0))            
           
