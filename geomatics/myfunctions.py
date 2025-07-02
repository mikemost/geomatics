# Function to convert decimal degrees to degree minutes and seconds
def degtodms(decimal, decimals=0):
    dd = int(decimal)
    decimal = abs(decimal - dd) * 60
    mm = int(decimal)
    ss = (decimal - mm) * 60
    if mm == 59 and round(ss) == 60:
        dd += 1; mm = 0; ss = 0
    if round(ss) == 60:
        mm += 1; ss = 0
    return f'{dd}° {mm}\' {ss:.{decimals}f}"'

import sympy as sp

def round_matrix(matrix, digits, method='sig'):
    """
    Round each element of a Sympy Matrix, either by significant figures or decimal places.
    :param matrix: Sympy Matrix
    :param digits: Number of digits (sig figs if method is significant, or decimal places if decimal)
    :param method: 'sig' or 'significant' for significant figures; 'dec' or 'decimal' for decimal places
    :return: Rounded Sympy Matrix
    """
    # normalize method keyword
    m = method.lower()
    if m in ('sig', 'significant'):
        use_sig = True
    elif m in ('dec', 'decimal'):
        use_sig = False
    else:
        raise ValueError(f"Invalid method '{method}'. Use 'sig'/'significant' or 'dec'/'decimal'.")
    rounded_matrix = matrix.copy()
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            val = matrix[i, j]
            if use_sig:
                out = sp.N(val, digits)
            else:
                try:
                    out = round(float(val), digits)
                except Exception:
                    out = val
            rounded_matrix[i, j] = out
    return rounded_matrix

from math import floor, log10
def roundsf(value, n):
    if value == 0:
        return 0
    # Calculate the order of magnitude
    magnitude = int(floor(log10(abs(value)))) + 1
    # Calculate the rounding factor based on the desired significant figures
    rounding_factor = n - magnitude
    # Round the value using the rounding factor
    rounded_value = round(value, rounding_factor)
    return rounded_value
