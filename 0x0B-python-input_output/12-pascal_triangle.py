#!/usr/bin/python3
"""
Function pascal triangle
"""


def pascal_triangle(n):
    """
    return list og integers
    Args:
        n (int): number of line
    """

    b_list = []
    # return empty if n <= 0
    if n <= 0:
        return b_list
    else:
        for idx_b_list in range(n):
            b_list.append([])
            if idx_b_list == 0:
                b_list[idx_b_list].append(1)
            else:
                prv_idx_list = b_lsit[idx_b_list - 1]
                c_list = b_list[idx_b_list]
                for i, value in enumerate(prv_idx_list):
                    if i == 0:
                        c_list.append(1)
                    else:
                        c_int = prv_idx_list[i]
                        p_int = prv_idx_list[i - 1]
                        n_int = c_int + p_int
                        c_list.append(n_int)
                c_list.append(1)
        return b_list
