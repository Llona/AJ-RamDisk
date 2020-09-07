import gui_template
import ctypes
import win32api
import wx
from collections import OrderedDict
import settings
from settings import ControlCfgType
from settings import RamDIskCfg
import utils


class MainGuiFrame(gui_template.main_frame):
    def __init__(self, parent):
        gui_template.main_frame.__init__(self, parent)
        self.cfg_data = None
        self.init_gui()

    def init_gui(self):
        self.init_cfg_listctrl()

    def init_cfg_listctrl(self):
        self.ramdrive_listctrl.ClearAll()
        self.ramdrive_listctrl.InsertColumn(0, 'ID', format=wx.LIST_FORMAT_CENTRE)
        self.ramdrive_listctrl.InsertColumn(1, 'Drive', format=wx.LIST_FORMAT_CENTRE)
        self.ramdrive_listctrl.InsertColumn(2, 'Size', format=wx.LIST_FORMAT_CENTRE)
        self.ramdrive_listctrl.InsertColumn(3, 'Label', format=wx.LIST_FORMAT_CENTRE)
        self.ramdrive_listctrl.InsertColumn(4, 'Store Image?', format=wx.LIST_FORMAT_CENTRE)
        self.ramdrive_listctrl.InsertColumn(5, 'Store Full Image?', format=wx.LIST_FORMAT_CENTRE)
        self.ramdrive_listctrl.InsertColumn(6, 'Image path', format=wx.LIST_FORMAT_CENTRE)

        cfg_h = utils.JsonControl(settings.CONFIG_FILENAME)
        self.cfg_data = cfg_h.read_json()

        item_index = 0
        for ramdisk_cfg in self.cfg_data:
            index = self.ramdrive_listctrl.InsertItem(item_index, ramdisk_cfg[RamDIskCfg.ID.value])
            self.ramdrive_listctrl.SetItem(index, 1, ramdisk_cfg[RamDIskCfg.DRIVE.value] + ":")
            self.ramdrive_listctrl.SetItem(index, 2, str(ramdisk_cfg[RamDIskCfg.SIZE.value]))
            self.ramdrive_listctrl.SetItem(index, 3, ramdisk_cfg[RamDIskCfg.LABEL.value])

            self.ramdrive_listctrl.SetItem(index, 4, self.bool_to_str(ramdisk_cfg[RamDIskCfg.STORE_IMG.value]))
            self.ramdrive_listctrl.SetItem(index, 5, self.bool_to_str(ramdisk_cfg[RamDIskCfg.STORE_ALL.value]))
            self.ramdrive_listctrl.SetItem(index, 6, ramdisk_cfg[RamDIskCfg.IMG_PATH.value])
            # self.ramdrive_listctrl.SetItem(index, 7, ramdisk_cfg[RamDIskCfg.STORE_FOLDER_LIST.value])

            item_index += 1

        for i in range(0, 7):
            self.ramdrive_listctrl.SetColumnWidth(i, wx.LIST_AUTOSIZE_USEHEADER)

        self.ramdrive_listctrl.Select(0)

    @staticmethod
    def bool_to_str(bool_value):
        if bool_value:
            return "Y"
        else:
            return "N"

    def add_press(self, event=None):
        index = self.ramdrive_listctrl.GetFocusedItem()
        if index < 0:
            index = 0
        add_frame = AddEditRamDisk(self, ControlCfgType.add, self.cfg_data, index, settings.CONFIG_FILENAME)
        add_frame.Show(True)

    def edit_press(self, event=None):
        index = self.ramdrive_listctrl.GetFocusedItem()
        if index < 0:
            index = 0
        add_frame = AddEditRamDisk(self, ControlCfgType.edit, self.cfg_data, index, settings.CONFIG_FILENAME)
        add_frame.Show(True)


class AddEditRamDisk(gui_template.AddEditDiskFrame):
    def __init__(self, parent, control_type, cfg_data, ramdisk_setting_index, cfg_filename):
        gui_template.AddEditDiskFrame.__init__(self, parent)
        self.parent = parent
        self.control_type = control_type
        self.cfg_filename = cfg_filename
        self.cfg_data = cfg_data
        self.ramdisk_setting_index = ramdisk_setting_index

        self.parent.Bind(wx.EVT_ACTIVATE, self.set_focus)

        self.init_gui()

    def init_gui(self):
        ramdisk_setting = self.cfg_data[self.ramdisk_setting_index]

        self.init_size(ramdisk_setting)
        self.init_driver_choice(ramdisk_setting)
        self.store_img_checkbox.SetValue(ramdisk_setting[RamDIskCfg.STORE_IMG.value])
        self.store_all_checkbox.SetValue(ramdisk_setting[RamDIskCfg.STORE_ALL.value])
        self.img_path_text.SetValue(ramdisk_setting[RamDIskCfg.IMG_PATH.value])

        self.arrange_gui()

    def init_size(self, ramdisk_setting):
        if self.control_type == ControlCfgType.edit:
            size = ramdisk_setting[RamDIskCfg.SIZE.value]
            if size[-1:] == 'M':
                self.size_unit_choice.SetSelection(0)
            else:
                self.size_unit_choice.SetSelection(1)
            self.size_text.SetValue(size[0:-1])

        self.label_text.SetValue(settings.PREFIX_DRIVE_NAME + str(self.ramdisk_setting_index))
        self.label_text.Disable()

    def init_driver_choice(self, ramdisk_setting):
        driver_list_str = win32api.GetLogicalDriveStrings()
        available_driver = settings.ALL_DISK_SET.copy()
        for driver in driver_list_str.split(':\\\x00'):
            if driver and driver != ramdisk_setting[RamDIskCfg.DRIVE.value]:
                available_driver.remove(driver)
        available_driver = tuple(sorted(available_driver))
        self.driver_choice.SetItems(available_driver)

        if self.control_type == ControlCfgType.add:
            self.driver_choice.SetSelection(len(available_driver)-1)
        else:
            count = 0
            for i in available_driver:
                if i == ramdisk_setting[RamDIskCfg.DRIVE.value]:
                    self.driver_choice.SetSelection(count)
                count += 1

    def arrange_gui(self):
        if not self.store_img_checkbox.GetValue():
            self.store_all_checkbox.Disable()
            self.choice_path_button.Disable()
            self.img_path_text.Disable()
            self.choice_folder_button.Disable()
        else:
            self.img_path_text.Enable()
            self.choice_path_button.Enable()
            self.store_all_checkbox.Enable()
            if self.store_all_checkbox.GetValue():
                self.choice_folder_button.Disable()
            else:
                self.choice_folder_button.Enable()

    @staticmethod
    def input_error_dialog():
        dlg = wx.MessageDialog(None,
                               'Error, please check your input is correct!\n\n',
                               'Please check input', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def show_error_dialog(self):
        self.input_error_dialog()
        self.SetFocus()

    def get_ramdisk_setting_from_input(self):
        new_ramdisk_setting = OrderedDict()
        try:
            int(self.size_text.GetValue())
        except Exception as e:
            str(e)
            self.show_error_dialog()
            return
        size_unit = settings.SIZE_UNIT[str(self.size_unit_choice.GetSelection())]
        new_ramdisk_setting[RamDIskCfg.ID.value] = "#" + str(self.ramdisk_setting_index)
        new_ramdisk_setting[RamDIskCfg.SIZE.value] = self.size_text.GetValue() + size_unit
        new_ramdisk_setting[RamDIskCfg.DRIVE.value] = self.driver_choice.GetItems()[self.driver_choice.GetSelection()]
        new_ramdisk_setting[RamDIskCfg.LABEL.value] = self.label_text.GetValue()
        new_ramdisk_setting[RamDIskCfg.STORE_IMG.value] = self.store_img_checkbox.GetValue()
        new_ramdisk_setting[RamDIskCfg.STORE_ALL.value] = self.store_all_checkbox.GetValue()
        new_ramdisk_setting[RamDIskCfg.IMG_PATH.value] = self.img_path_text.GetValue()
        # new_ramdisk_setting[RamDIskCfg.STORE_FOLDER_LIST.value] =

        return new_ramdisk_setting

    def renew_config_file(self):
        new_ramdisk_setting = self.get_ramdisk_setting_from_input()
        if self.control_type == ControlCfgType.add:
            self.cfg_data.append(new_ramdisk_setting)
        else:
            self.cfg_data[self.ramdisk_setting_index] = new_ramdisk_setting

        cfg_h = utils.JsonControl(self.cfg_filename)
        cfg_h.write_json(self.cfg_data)

    def press_ok(self, event):
        self.renew_config_file()
        self.parent.init_gui()
        self.close_frame()

    def press_cancel(self, event):
        self.close_frame()

    def check_store_all(self, event):
        self.arrange_gui()

    def check_store_img(self, event):
        self.arrange_gui()

    def set_focus(self, event=None):
        if event.GetActive():
            self.SetFocus()
            self.size_text.SetFocus()

    def close_frame(self):
        self.parent.Unbind(wx.EVT_ACTIVATE)
        self.parent.init_gui()
        self.Destroy()


def start_gui():
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    except Exception as e:
        print('set DPI awareness fail, only need in windows, skip it: {}'.format(e))

    app = wx.App(False)
    frame = MainGuiFrame(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    start_gui()
