"""
Esse programa faz conversões.
"""


def converte_F_pra_C(f_temp):
    """Converte de F° para C°

    Args:
        f_temp (float): _description_

    Returns:
        float: _description_

    Testes:
        >>> converte_F_pra_C(32)
        0.0
        >>> converte_F_pra_C(-40)
        -40.0
    """
    return ((f_temp - 32) / 9) * 5


def converte_C_pra_F(c_temp):
    """Converte de C° para F°

    Args:
        c_temp (float): _description_

    Returns:
        float: _description_

    Testes:
        >>> converte_C_pra_F(0)
        32.00
        >>> converte_C_pra_F(-40)
        -40.0
    """
    return c_temp * (9 / 5) + 32

