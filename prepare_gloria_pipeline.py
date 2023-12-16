import os
from parsing import read_monetary_blocks, read_gloria_meta, read_satellites, read_satellite_meta
from tests import test_mrio_dimensions, test_satellite_dimensions

# GLORIA config
mrio_year = 2020
mrio_version = '055'

# Environment
mrio_path = os.environ['MRIO_PATH'] + mrio_version + '/'
assert os.path.isdir(mrio_path)

# Read IO blocks
T, v, y = read_monetary_blocks(path=mrio_path,
                               year=mrio_year,
                               loop=mrio_version
                               )

# Read MRIO meta
n_va, n_fd, n_reg, n_sec, region_labels, sector_labels, fd_cats, va_cats = read_gloria_meta(mrio_path)

# Read satellite
Q_T, Q_y = read_satellites(path=mrio_path,
                           year=mrio_year,
                           loop=mrio_version
                           )

# Read satellite meta
satellite_meta = read_satellite_meta(mrio_path)

# Tests
test_mrio_dimensions(T, v, y, n_va, n_fd, n_reg, n_sec)
test_satellite_dimensions(Q_T, Q_y, n_sec, n_reg, satellite_meta)