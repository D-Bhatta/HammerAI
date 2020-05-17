def hammer(object):
    """ 
    Print a line about hammering an object
    args:
        object (str): name of the object
    returns:
        None
    """
    if type(object) != str:
        raise TypeError

    print("I'll hammer an {} someday.".format(object))
