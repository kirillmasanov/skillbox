import os, time, shutil, zipfile


class FileArrange:
    def __init__(self, zip_file, final_folder):
        self.zip_file = zip_file
        self.final_folder = final_folder
        self.file_dict = {}

    def make_dir(self):
        zfile = zipfile.ZipFile(self.zip_file, 'r')

        for info in zfile.infolist():
            if '.' in info.filename:
                self.file_dict[os.path.basename(info.filename)] = zfile.getinfo(info.filename).date_time

    def make_arrange(self):
        with zipfile.ZipFile(self.zip_file) as zip:
            for zip_info in zip.infolist():
                if zip_info.filename[-1] == '/':
                    continue
                zip_info.filename = os.path.basename(zip_info.filename)
                final_dist = os.path.join(
                    'icons_by_year',
                    str(self.file_dict[zip_info.filename][0]),
                    f'{self.file_dict[zip_info.filename][1]:02d}'
                )
                zip.extract(zip_info, final_dist)


zip_file = 'icons.zip'
path_out = 'icons_by_year'
my_folder = FileArrange(zip_file=os.path.normpath(zip_file), final_folder=os.path.normpath(path_out))
my_folder.make_dir()
my_folder.make_arrange()
