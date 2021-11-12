import os
from datetime import datetime


class Log:
    def __init__(self, path):
        self.logs_path = path
        self.abbr_list = []
        self.start_list = []
        self.end_list = []

    def read_data(self):
        try:
            with open(os.path.join(self.logs_path, 'start.log')) as f:
                self.start_list = [line.strip() for line in f.readlines()]
            with open(os.path.join(self.logs_path, 'end.log')) as f:
                self.end_list = [line.strip() for line in f.readlines()]
            with open(os.path.join(self.logs_path, 'abbreviations.txt')) as f:
                self.abbr_list = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            raise FileNotFoundError("directory not found or  incorrect names of files")

    def validate(self):
        length_start = len(self.start_list)
        length_end = len(self.end_list)
        if len(self.abbr_list)*2 != length_end+length_start:
            exit("data is not full")
        for abbr, s_abbr, e_abbr in zip(self.abbr_list, self.start_list, self.end_list):
            if abbr[:3] != s_abbr[:3]:
                exit("data is not correct")
            if abbr[:3] != e_abbr[:3]:
                exit("data is not correct")

    def get_logs(self):
        self.read_data()
        self.start_list.sort()
        self.end_list.sort()
        self.abbr_list.sort()
        self.validate()
        return self.abbr_list, self.start_list, self.end_list


class Web_report:
    def __init__(self, abbr_list, start_list, end_list):
        self.diff_list = []
        self.abbreviations = abbr_list
        self.start_log_list = start_list
        self.end_log_list = end_list

    def get_diff(self):
        for start_time, end_time in zip(self.start_log_list, self.end_log_list):
            start = start_time[3:]
            end = end_time[3:]
            _s = datetime.strptime(start, "%Y-%m-%d_%I:%M:%S.%f")
            _e = datetime.strptime(end, "%Y-%m-%d_%I:%M:%S.%f")
            diff = _e - _s
            self.diff_list.append(diff)

    def get_info(self):
        names = []
        codes = []
        cars = []
        for driver in self.abbreviations:
            split_list = driver.split("_")
            _code, _name, _car = split_list[0], split_list[1], split_list[-1]
            names.append(_name)
            codes.append(_code)
            cars.append(_car)
        #name,car,time,code,place
        tpl_data = zip(names, cars, self.diff_list, codes)
        tpl_data = sorted(tpl_data, key=lambda x: x[2])
        tpl_data = [element + (index,) for index, element in enumerate(tpl_data, start=1)]
        list_of_lists_data = []
        for el in tpl_data:
            list_el = list(el)
            fmt_string = str(list_el[2]).replace("000", "")
            list_el[2] = fmt_string
            list_of_lists_data.append(list_el)
        return list_of_lists_data


def driver_result(data, order_asc=True, filter=None):
    drv = None
    if filter:
        for element in data:
            if filter == element[3]:
                drv = element
        if not drv:
            return None
        return drv
    if order_asc is True:
        return data
    if order_asc is False:
        return data[::-1]


def read_logs_driver_info():
    log = Log(path="/data")
    abbreviations, time_start, time_end = log.get_logs()
    report = Web_report(abbr_list=abbreviations, start_list=time_start, end_list=time_end)
    report.get_diff()
    info = report.get_info()
    return info