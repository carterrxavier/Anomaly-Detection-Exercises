# get outliers
def get_outliers(df , col, lquan=.25, upquan=.75, case = 1.5, direction=None, graph=False, remove= True ):
    q1 = df[col].quantile(lquan)
    q3 = df[col].quantile(upquan)
    iqr = q3-q1 #Interquartile range
    lower_bound  = q1-case*iqr
    upper_bound = q3+case*iqr
    
    if graph == True:
        plt.axvline(lower_bound, c= 'b')
        plt.axvline(upper_bound, c='r')
        sns.boxplot(x=df[col])
        plt.show()
    if remove == False:
        if direction == 'lower':
            df = df.loc[(df[col] < lower_bound)]
        elif direction == 'upper':
            df = df.loc[(df[col] > upper_bound)]
        else:
            df = df.loc[(df[col] < lower_bound) | (df[col] > upper_bound)]
    if remove == True:
        if direction == 'lower':
            df = df.loc[(df[col] > lower_bound)]
        elif direction == 'upper':
            df = df.loc[(df[col] < upper_bound)]
        else:
            df = df.loc[(df[col] > lower_bound) & (df[col] < upper_bound)]
        

        
    return df


def get_sigma_percent(df, col, step = 1, outliers = False):
    print(np.round((len(df.loc[(df[col] < df[col].mean() + (df[col].std()) * step) & (df[col] > df[col].mean() - (df[col].std()) * step)]) / len(df)),4))
    if outliers:
        return df.loc[(df[col] > df[col].mean() + (df[col].std()) * step) | (df[col] < df[col].mean() - (df[col].std()) * step)]