import sys
import os
import json
import configparser
from collections import OrderedDict

sys.path.append(os.path.join(sys.path[0], ".."))
sys.path.append(os.path.join(sys.path[0], "..//.."))


class JsonControl(object):
    def __init__(self, json_full_path):
        self.json_full_path = json_full_path
        self.json_format = 'utf8'
        self.format_list = ['utf8', 'utf-8-sig', 'utf16', None, 'big5', 'gbk', 'gb2312']
        if os.path.exists(self.json_full_path):
            self.try_file_format()

    def try_file_format(self):
        for file_format in self.format_list:
            try:
                with open(self.json_full_path, 'r', encoding=file_format) as file:
                    json.load(file)
                self.json_format = file_format
                # print('find correct format {} in json file: {}'.format(file_format, self.json_full_path))
                return
            except Exception as e:
                # print('checking {} format: {}'.format(self.json_full_path, file_format))
                str(e)

    def read_json(self):
        try:
            with open(self.json_full_path, 'r', encoding=self.json_format) as file:
                return json.load(file)
        except Exception as e:
            print("Error! 讀取cfg設定檔發生錯誤!: {} {}".format(self.json_full_path, e))
            raise

    def write_json(self, json_content):
        try:
            with open(self.json_full_path, 'w', encoding=self.json_format) as file:
                json.dump(json_content, file, ensure_ascii=False, indent=4, separators=(',', ':'))
        except Exception as e:
            print("Error! 寫入cfg設定檔發生錯誤! {} {}".format(self.json_full_path, e))
            # str(e)
            raise


class IniControl(object):
    def __init__(self, ini_full_path):
        self.ini_full_path = ini_full_path
        self.ini_format = 'utf8'
        self.format_list = ['utf8', 'utf-8-sig', 'utf16', None, 'big5', 'gbk', 'gb2312']
        self.try_ini_format()

    def try_ini_format(self):
        for file_format in self.format_list:
            try:
                config_lh = configparser.ConfigParser()
                with open(self.ini_full_path, 'r', encoding=file_format) as file:
                    config_lh.read_file(file)
                self.ini_format = file_format
                print('find correct format {} in ini file: {}'.format(file_format, self.ini_full_path))
                return
            except Exception as e:
                print('checking {} format: {}'.format(self.ini_full_path, file_format))
                str(e)

    def read_config(self, section, key):
        try:
            config_lh = configparser.ConfigParser()
            file_ini_lh = open(self.ini_full_path, 'r', encoding=self.ini_format)
            config_lh.read_file(file_ini_lh)
            file_ini_lh.close()
            return config_lh.get(section, key)
        except Exception as e:
            print("Error! 讀取ini設定檔發生錯誤! " + self.ini_full_path)
            str(e)
            raise

    def read_section_config(self, section):
        try:
            config_lh = configparser.ConfigParser()
            file_ini_lh = open(self.ini_full_path, 'r', encoding=self.ini_format)
            config_lh.read_file(file_ini_lh)
            file_ini_lh.close()
            single_section = config_lh.items(section)

            section_dict = OrderedDict()
            for item in single_section:
                section_dict[item[0]] = item[1]
            return section_dict
        except Exception as e:
            print("Error! 讀取ini設定檔發生錯誤! " + self.ini_full_path)
            str(e)
            raise

    def write_config(self, sections, ini_dict):
        try:
            config_lh = configparser.ConfigParser()
            config_lh.optionxform = str
            file_ini_lh = open(self.ini_full_path, 'r', encoding=self.ini_format)
            config_lh.read_file(file_ini_lh)
            file_ini_lh.close()

            for key, value in ini_dict.items():
                config_lh.set(sections, key, value)
            file_ini_lh = open(self.ini_full_path, 'w', encoding=self.ini_format)
            config_lh.write(file_ini_lh)
            file_ini_lh.close()
        except Exception as e:
            print("Error! 寫入ini設定檔發生錯誤! " + self.ini_full_path)
            str(e)
            raise


class StringEncryption(object):
    def __init__(self):
        self.key = '$^&@$FacGh9!37|+#op,kq%=0-\\gxi4%hmod8]s;l/p[}htu{"'

    def enctry(self, s):
        encry_str = ""
        for i, j in zip(s, self.key):
            # i為字符，j為秘鑰字符
            # 加密字符 = 字符的Unicode碼 + 秘鑰的Unicode碼
            temp = str(ord(i)+ord(j))+'_'
            encry_str = encry_str + temp
        return encry_str

    def dectry(self, p):
        dec_str = ""
        for i, j in zip(p.split("_")[:-1], self.key):
            # i 為加密字符，j為秘鑰字符
            # 解密字符 = (加密Unicode碼字符 - 秘鑰字符的Unicode碼)的單字節字符
            temp = chr(int(i) - ord(j))
            dec_str = dec_str+temp
        return dec_str

    # data = "zmister.com"
    # print("原始數據為：", data)
    # enc_str = enctry(data)
    # print("加密數據為：", enc_str)
    # dec_str = dectry(enc_str)
    # print("解密數據為：", dec_str)


# class DateTimeControl(object):
#     def __init__(self):
#         super(DateTimeControl, self).__init__()
#
#     def change_string_to_utc_datetime(self, time_text, current_timezone):
#         datetime_h = self.str_to_datetime(time_text)
#         return self.datetime_current_timezone_to_utc(datetime_h, current_timezone)
#
#     @staticmethod
#     def str_to_datetime(s):
#         t = None
#         try:
#             if s.find('-') > -1:
#                 if s.find('T') > -1:
#                     t = datetime(*map(int, re.split('[-T:]', s)))
#                 else:
#                     t = datetime(*map(int, re.split('[- :]', s)))
#             elif s.find('/') > -1:
#                 t = datetime(*map(int, re.split('[/ :]', s)))
#         except Exception as e:
#             print('set string to datetime error: %s, error log: %s' % (s, e))
#
#         return t
#
#     @staticmethod
#     def datetime_current_timezone_to_utc(datetime_h, current_timezone):
#         time_h = datetime_h.replace(tzinfo=tz.gettz(current_timezone))
#         return time_h.astimezone(tz.tzutc())
#
#     @staticmethod
#     def datetime_naive_add_utc_timezone(datetime_h):
#         time_h = datetime_h.replace(tzinfo=tz.tzutc())
#         return time_h.astimezone(tz.tzutc())
#
#     @staticmethod
#     def datetime_cover_timezone(datetime_h, timezone):
#         return datetime_h.astimezone(tz.gettz(timezone))
