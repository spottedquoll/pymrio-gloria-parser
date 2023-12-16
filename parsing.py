import pandas as pd
import glob


def read_monetary_blocks(path=None, year=None, loop=None):
    """
        Reads GLORIA matrices
        date field in filename is fragile as it may not be common across all files
    """

    fname = '_120secMother_AllCountries_002_T-Results_' + str(year) + '_' + loop + '_Markup001(full).csv'
    files = glob.glob(path + '*' + fname)
    T = pd.read_csv(files[0], header=None)

    T_ar = T.to_numpy()
    del T

    fname = '_120secMother_AllCountries_002_Y-Results_' + str(year) + '_' + loop + '_Markup001(full).csv'
    files = glob.glob(path + '*' + fname)
    y = pd.read_csv(files[0], header=None)

    y_ar = y.to_numpy()
    del y

    fname = '_120secMother_AllCountries_002_V-Results_' + str(year) + '_' + loop + '_Markup001(full).csv'
    files = glob.glob(path + '*' + fname)
    v = pd.read_csv(files[0], header=None)

    v_ar = v.to_numpy()
    del v

    return T_ar, v_ar, y_ar


def read_gloria_meta(gloria_path):
    """
        Read the region and sector specifications
    """

    files = glob.glob(gloria_path + 'GLORIA_ReadMe*.xlsx')
    assert len(files) == 1

    regions = pd.read_excel(files[0], sheet_name='Regions')
    n_reg = regions.shape[0]

    sectors = pd.read_excel(files[0], sheet_name='Sectors')
    n_sec = sectors.shape[0]

    va_fd_sheet = pd.read_excel(files[0], sheet_name='Value added and final demand')

    fd_cats = va_fd_sheet['Final_demand_names'].to_list()
    n_fd = len(fd_cats)

    va_cats = va_fd_sheet['Value_added_names'].to_list()
    n_va = len(va_cats)

    return n_va, n_fd, n_reg, n_sec, regions, sectors, fd_cats, va_cats


def read_satellites(path=None, year=None, loop=None):
    """
        Reads GLORIA satellite files
    """

    fname = '_120secMother_AllCountries_002_TQ-Results_' + str(year) + '_' + loop + '_Markup001(full).csv'
    files = glob.glob(path + '*' + fname)
    Q_T = pd.read_csv(files[0], header=None)
    Q_T_ar = Q_T.to_numpy()

    fname = '_120secMother_AllCountries_002_YQ-Results_' + str(year) + '_' + loop + '_Markup001(full).csv'
    files = glob.glob(path + '*' + fname)
    Q_y = pd.read_csv(files[0], header=None)
    Q_y_ar = Q_y.to_numpy()

    return Q_T_ar, Q_y_ar


def read_satellite_meta(gloria_path):
    """
        Read the satellite specifications
    """

    satellite_meta = pd.read_excel(gloria_path + 'GLORIA_ReadMe.xlsx', sheet_name='Satellites')

    return satellite_meta
