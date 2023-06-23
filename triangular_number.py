def triangle_number(number):
    """ Returns the triangular number of input.
    .. math::
        \sum_{i=1}^{\\infty} x_{i}
    """
    if number == 1:
        return 1
    return number + triangle_number(number - 1)