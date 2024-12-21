import os


class CreateFolder(object):
    def __init__(self, r_path) -> None:
        self._base_dir = r_path+'/result'
        self._storage_path = ""

    def initialize(self) -> None:
        self.__create_base_dir()
        self.__create_storage_dir()

    def get_current_storage_path(self) -> str:
        return self._storage_path

    def __create_storage_dir(self) -> None:
        storage_dir_num = self.__calc_storage_dir_name() + 1
        self._storage_path = self._base_dir + "/" + str(storage_dir_num)
        os.mkdir(self._storage_path)

    def __calc_storage_dir_name(self) -> int:
        dirs = os.listdir(self._base_dir)
        dir_max_num = 0
        current_num = 0
        for dir in dirs:
            try:
                current_num = int(dir)
            except ValueError:
                current_num = 0
            if current_num > dir_max_num:
                dir_max_num = current_num

        return dir_max_num

    def __create_base_dir(self) -> None:
        if not os.path.exists(self._base_dir):
            os.makedirs(self._base_dir)
