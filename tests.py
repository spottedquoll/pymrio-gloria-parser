def test_mrio_dimensions(T, v, y, n_v, n_y, n_reg, n_sec):
    """
        MRIO dimension tests
    """

    assert T.shape[0] == n_reg*n_sec*2
    assert T.shape[0] == T.shape[1]
    assert n_y*n_reg == y.shape[1]
    assert n_v*n_reg == v.shape[0]
    assert y.shape[0] == v.shape[1]


def test_satellite_dimensions(Q_T, Q_y, n_sec, n_reg, satellite_meta):
    """
        MRIO dimension tests
    """

    assert Q_T.shape[0] == satellite_meta.shape[0]
    assert Q_y.shape[0] == satellite_meta.shape[0]
    assert Q_T.shape[1] == n_reg * n_sec * 2
    assert Q_y.shape[1] == n_reg
