from .curry import curry


@curry
def pick(keys: list[str], obj: dict[str, any]):
    """
    ------
    Picks specified keys from a given dictionary, returning a new dictionary that includes
    only the key-value pairs whose keys are included in the provided list.
    
    Parameters:
    ----------
    keys : list[str]
        A list of keys (as strings) that should be retained in the input dictionary.
    obj : dict[str, any]
        The source dictionary from which key-value pairs will be picked. The dictionary maps
        string keys to values of any type.
    
    Returns:
    -------
    dict[str, any]
        A new dictionary with only the key-value pairs from the input dictionary whose keys
        are present in the `keys` list.
    
    Examples:
    ---------
    >>> pick(['a', 'c'], {'a': 1, 'b': 2, 'c': 3})
    {'a': 1, 'c': 3}
    
    Filepath:
    ---------
    
    Note:
    -----
    This function is decorated with @curry, which allows it to be partially applied. This means 
    that you can call the function with fewer arguments than it expects, returning a new function 
    that takes the remaining arguments.
    """
    return {k: v for k, v in obj.items() if k in keys}