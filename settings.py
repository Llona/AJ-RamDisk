import enum

PREFIX_DRIVE_NAME = 'AJRamDisk'
CONFIG_FILENAME = 'config.cfg'
SIZE_UNIT = {"0": 'M', "1": "G"}

ALL_DISK_SET = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}


class ControlCfgType(enum.IntEnum):
    add = 0
    edit = 1


class RamDIskCfg(enum.Enum):
    ID = 'ID'
    SIZE = 'Size'
    DRIVE = 'Drive'
    LABEL = 'Label'
    STORE_IMG = 'Store_img'
    STORE_ALL = 'Store_all'
    IMG_PATH = 'img_path'
    STORE_FOLDER_LIST = 'Store_folder_list'
