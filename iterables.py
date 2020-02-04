from collections.abc import Iterable


def get_lowest_level_objects(nested, *excluded_types):

    r"""get_lowest_level_objects(nested, (type1, type2, ...))

    Count recursively all lowest level elements of iterable nested structure.

    Parameters
    ----------
    nested : iterable object
    type1, type2, ... : sequence of iterable types, optional
        By default, lowest level elements are not iterable objects,
        but their list can be expanded here.

    Returns
    -------
    int
        Number of elements found.

    Examples
    --------
    >>> import numpy as np
    >>> nested_dict = {
    ...     'a': {
    ...         'aa': 1,
    ...         'bb': 2.0,
    ...     },
    ...     'b': np.array([3, 4, 5]),
    ...     'c': [
    ...           (6.0, 7.0, 8.0),
    ...           ('9.0', '10.0')
    ...     ]
    ... }
    >>> get_lowest_level_objects(nested)
    [1, 2.0, 3, 4, 5, 6.0, 7.0, 8.0, '9', '.', '0', '1', '0', '.', '0']

    Do not iterate over str:

    >>> get_lowest_level_objects(nested, str)
    [1, 2.0, 3, 4, 5, 6.0, 7.0, 8.0, '9.0', '10.0']

    Do not iterate over str and numpy.ndarray:

    >>> get_lowest_level_objects(nested, str, np.ndarray)
    [1, 2.0, array([3, 4, 5]), 6.0, 7.0, 8.0, '9.0', '10.0']
    """

    obj_list = []

    for obj in nested:

        if type(nested) is dict:

            value = nested[obj]

        else:

            value = obj

        if isinstance(value, Iterable) and type(value) not in excluded_types:

            if type(value) is str and len(value) == 1:
                obj_list.append(value)

            else:
                obj_list.extend(get_lowest_level_objects(value,
                                                         *excluded_types))

        else:
            obj_list.append(value)

    return obj_list

