def var_numbers(number, precision = 2):
    med = (number + 1)/2
    var_n = 0
    for i in range(1, number+1):
        var_n += (i - med)**2
    var = var_n / number
    var = round(var, ndigits = precision)
    return(var)
