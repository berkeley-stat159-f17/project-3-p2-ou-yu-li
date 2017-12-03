def two_sample_t_test(group1, group2, group1_name, group2_name, alpha = 0.05):
    """Performs a two-sided two sample t-test to see if there is a difference in mean between
    the value of two groups. 
    
    Parameters
    ----------
    group1: Data for the first group. Can be list or array
    group2: Data for the second group. Can be list or array
    group1_name: Name of first group
    group2_name: Name of second group
    alpha: Significance level, default of 0.05 (Although this is very arbitrary as we saw in this class)
    
    
    Return
    ------
    (t, p, reject)
    t: the t-statistic
    p: the p-value
    reject: whether we reject the null hypothesis
    
    Example
    -------
    
    >>> group1 = [1, 2, 3]
    ... group2 = [1, 2, 3]
    ... two_sample_t_test(group1, group2, "group1", "group2")
    There is no statistically significant difference between Group group1 and Group group2
    (0.0, 1.0)    
    """    
        
    n1 = len(group1)
    n2 = len(group2)
    assert(n1 > 0)
    assert(n2 > 0)
    s12 = np.var(group1)
    s22 = np.var(group2)
    m1 = np.mean(group1)
    m2 = np.mean(group2)
    se = np.sqrt((s12/n1) + (s22/n2))
    df = (np.square(s12/n1 + s22/n2) / (( np.square(s12 / n1) / (n1 - 1) ) + (np.square(s22 / n2) / (n2 - 1)))).astype(int)
    t = ((m1 - m2)) / se
    p = stats.t.sf(np.abs(t), df)*2
    if (p < alpha):
        print("The mean difference is statistically significant for Group "  + group1_name +" and Group " + group2_name)
        print("p-value is " + str(p))
        print()
    else:
        print("There is no statistically significant difference between Group " + group1_name +" and Group " + group2_name)
        print()
    return (t, p, p < alpha)
    
    