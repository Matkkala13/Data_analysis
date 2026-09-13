import numpy as np 

def calculate(arrange):
    if len(arrange) > 9 or len(arrange) < 9:
        raise ValueError('List must contain nine numbers.')

    arr = np.array([arrange[:3], arrange[3:6], arrange[6:]])

    #mean
    mean_axis1, mean_axis2, flat_mean = arr.mean(axis=0), arr.mean(axis=1), arr.mean()
    mean = [mean_axis1.tolist(), mean_axis2.tolist(), flat_mean.tolist()]

    #variance
    variance_axis1, variance_axis2, flat_variance = arr.var(axis=0), arr.var(axis=1), arr.var()
    variance = [variance_axis1.tolist(), variance_axis2.tolist(), flat_variance.tolist()]

    #standart deviation
    std_axis1, std_axis2, flat_std = arr.std(axis=0), arr.std(axis=1), arr.std()
    standard_deviation = [std_axis1.tolist(), std_axis2.tolist(), flat_std.tolist()]

    #max
    max_axis1, max_axis2, flat_max = arr.max(axis=0), arr.max(axis=1), arr.max()
    max_ = [max_axis1.tolist(), max_axis2.tolist(), flat_max.tolist()]

    #min
    min_axis1, min_axis2, flat_min = arr.min(axis=0), arr.min(axis=1), arr.min()
    min_ = [min_axis1.tolist(), min_axis2.tolist(), flat_min.tolist()]

    #sum
    sum_axis1, sum_axis2, flat_sum = arr.sum(axis=0), arr.sum(axis=1), arr.sum()
    sum_ = [sum_axis1.tolist(), sum_axis2.tolist(), flat_sum.tolist()]

    output_dict = {}
    output_dict['mean'] = mean
    output_dict['variance'] = variance
    output_dict['standard deviation'] = standard_deviation
    output_dict['max']= max_
    output_dict['min']= min_
    output_dict['sum']= sum_
    return output_dict

