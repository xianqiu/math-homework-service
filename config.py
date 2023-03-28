from pathlib import Path


class Config(object):

    _front_path = 'web/'  # 前端页面地址(文件夹最后要加"斜杠"）
    _file_cache_name = 'd'  # 存放作业的文件夹名称

    def __int__(self):
        pass

    @property
    def front_path(self):
        return Path(self._front_path)

    @property
    def cache_path(self):
        return self.front_path / self._file_cache_name

    def get_file_path(self, series, level):
        path = self._front_path + self._file_cache_name + '/'
        file_name = 'math_homework_{}_{}.pdf'.format(series, level)
        return path + file_name
