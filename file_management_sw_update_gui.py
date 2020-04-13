import Tkinter as tk
import os
from tkFileDialog import askopenfilename
import ftplib
import sys
import shutil
import ttk
import zlib
import paramiko
import socket
import fnmatch
import time
import serial
import tftpy
import multiprocessing
import fnmatch
import subprocess
import re
import pylzma
import py7zlib
from Tkinter import StringVar
import threading
import wget
from Tkinter import *
import urllib2
import tarfile

command_root = '****\r\n'
command_reboot = '********* **'
command_reboot_serial = '********* **\r\n'
command_d = '*'
command_tftpload = '*** ********\r\n'
command_5_8 = '******* * *\r\n'
host_name = '***.***.***.*'
password = '****'
tel_port = 22
local_path = r'****************************************'
ftp_path = r'*************'
release_build_path = '**********************************************'
flash_path = r'*****************************************'
file_name_itb = '**************'
wide = 44
wide_combobox = 62
wide_medium_frame = 21
develop_build_path = '**********************************************'
lzma_catalog_path = r'******************************'
tar_catalog_path = r'****************************'
port_com = '*****'
tftp_ip = '***.***.***.*'
pdu_ip = '**.**.***.***'
wide_label = 44
font_all = 'Helvetica'
projekt = r"****"
job = r"**********************"
artefact = r"************************"
path_to_last_successfull_build = r"**************************************************"

class App(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("File Management")
        self.master.configure(background = 'light blue')
        self.master.resizable(width = False, height = False)
        self.grid(sticky = W + N + S + E)
        top_frame = Frame(self)
        medium_frame = Frame(self)
        top_frame.pack(side = "top", fill="x")
        medium_frame.pack(side = "bottom", fill="x")
        self.appbutton_putty = tk.Button(medium_frame, text = 'Close_Putty', command = self.close_putty_thread, height = 1, width = wide, font=font_all, foreground = 'black', background='orange', borderwidth=3)
        self.appbutton_putty.grid( )
        self.appbutton = Button(medium_frame,  text = 'Browse file from catalog', command = self.browse_file, height = 1, width = wide, font = font_all, foreground = 'black', background = 'yellow',borderwidth=3)
        self.appbutton.grid()
        self.appbutton = Button(medium_frame,  text = 'Open ****** directory', command = self.browse_file_ftp_catalog, height = 1, width = wide, font = font_all, foreground = 'black', background ='yellow',borderwidth=3)
        self.appbutton.grid()
        self.appbutton_copy_file_to_ftproot = tk.Button(medium_frame, text = 'Send file to ******* catalog', command = self.copy_file_to_ftpcatalog_from_local_file2, height = 1, width = wide, font = font_all, foreground = 'black', background = 'lightgreen',borderwidth = 3)
        self.appbutton_copy_file_to_ftproot.grid()
        self.appbutton_ftp = tk.Button(medium_frame, text = 'Send file to **', command = self.choose_file_ftp, height = 1, width = wide, font = font_all, foreground = 'black', background = 'light green',borderwidth = 3)
        self.appbutton_ftp.grid()
        self.appbutton_software_u = tk.Button(medium_frame, text = 'Software update', command = self.software_update_thread, height = 1, width = wide, font = font_all, foreground = 'black', background = 'grey', borderwidth = 3)
        self.appbutton_software_u.grid()
        self.appbutton_software_s = tk.Button(medium_frame, text = 'Software save', command = self.software_s_thread, height = 1, width = wide, font = font_all, foreground = 'black', background='grey', borderwidth=3)
        self.appbutton_software_s.grid()
        self.appbutton_software_a = tk.Button(medium_frame, text = 'Software activate', command = self.software_activate_thread, height = 1, width = wide, font = font_all, foreground = 'black', background='grey', borderwidth=3)
        self.appbutton_software_a.grid()
        self.appbutton_software_i = tk.Button(medium_frame, text = 'Software inventory', command = self.software_i_thread, height = 1, width = wide, font = font_all, foreground = 'black', background='grey', borderwidth=3)
        self.appbutton_software_i.grid()
        self.appbutton_slot_access = tk.Button(medium_frame, text = 'Brinfo_slot_access_slot_content', command = self.br_i_slot_a_thread, height = 1, width = wide, font = font_all, foreground = 'black', background='grey', borderwidth=3)
        self.appbutton_slot_access.grid()
        self.appbutton_ubi = tk.Button(medium_frame, text = 'ubi_a', command = self.ubi_a_thread, height = 1, width = wide, font = font_all, foreground = 'black', background='grey', borderwidth=3)
        self.appbutton_ubi.grid()
        self.appbutton_ubirm_0 = tk.Button(medium_frame, text = 'Ubirmvol_SW0', command = self.ubirm_0_thread, height = 1, width = wide, font = font_all, foreground = 'black', background='grey', borderwidth=3)
        self.appbutton_ubirm_0.grid()
        self.appbutton_i2c = tk.Button(medium_frame, text = 'i2c', command = self.i2c_thread, height = 1, width = wide, font = font_all, foreground = 'black', background='grey', borderwidth=3)
        self.appbutton_i2c.grid()
        self.label = Label(medium_frame, width = wide_label, text = "Set lzma file in combobox", font= font_all, foreground = 'black', background='light yellow', borderwidth=3)
        self.label.grid()
        self.Combobox = ttk.Combobox(medium_frame, width = wide_combobox)
        self.Combobox['values'] = [''] + self.combobox_values()  
        self.Combobox.bind("<<ComboboxSelected>>", self.combobox_updated_values)
        self.Combobox.bind("<Button>", self.combobox_updated_values)
        self.Combobox.grid()
        self.label = Label(medium_frame, width = wide_label, text = "Set itb file in combobox", font= font_all, foreground = 'black', background='light yellow', borderwidth=3)
        self.label.grid()
        self.appbutton_itb_update= tk.Button(medium_frame, text = 'Itb update', command = self.itb_update_thread, height = 1, width = wide, font= font_all, foreground = 'black', background='light grey',borderwidth=3)
        self.appbutton_itb_update.grid()
        self.Combobox_ITB = ttk.Combobox(medium_frame, values=[''] + self.combobox_values_for_itb(), width = wide_combobox, height = 1)
        self.Combobox_ITB.bind("<<ComboboxSelected>>", self.combobox_values_for_itb_updated)
        self.Combobox_ITB.bind("<Button>", self.combobox_values_for_itb_updated)
        self.Combobox_ITB.grid()
        self.appbutton_tftp_update = tk.Button(medium_frame, text = 'Tftp update', command = self.tftp_update, height = 1, width = wide, font = font_all, foreground = 'black', background='light grey',borderwidth=3)
        self.appbutton_tftp_update.grid()
        self.label = Label(medium_frame, width = wide_label, text = "Set itb and bin file in comboboxes", font= font_all, foreground = 'black', background='light yellow', borderwidth=3)
        self.label.grid()
        self.Combobox_TFTP = ttk.Combobox(medium_frame, values = [''] + self.combobox_values_for_tftp(),width = wide_combobox)
        self.Combobox_TFTP.grid()
        self.Combobox_TFTP.bind("<<ComboboxSelected>>", self.combobox_values_for_tftp_updated)
        self.Combobox_TFTP.bind("<Button>", self.combobox_values_for_tftp_updated)
        self.Combobox_TFTP_ITB = ttk.Combobox(medium_frame, values=[''] + self.combobox_values_for_itb(), width = wide_combobox)
        self.Combobox_TFTP_ITB.bind("<<ComboboxSelected>>", self.combobox_values_for_itb_tftp_updated)
        self.Combobox_TFTP_ITB.bind("<Button>", self.combobox_values_for_itb_tftp_updated)
        self.Combobox_TFTP_ITB.grid()
        self.appbutton_download = tk.Button(medium_frame, text='Download release build from catalog', command = self.download_and_unzip_release_file_from_catalog_parametrized_thread, height = 1, width = wide, font = font_all, foreground = 'black', background='light grey',borderwidth=3)
        self.appbutton_download.grid()
        self.label = Label(medium_frame, width = wide_label, text = "Set release and bin file in comboboxes", font = font_all, foreground = 'black', background='light yellow', borderwidth=3)
        self.label.grid()
        self.Combobox_Release = ttk.Combobox(medium_frame, values = [''] + self.combobox_values_releases(),width = wide_combobox)
        self.Combobox_Release.grid()
        self.Combobox_Release.bind("<<ComboboxSelected>>", self.combobox_values_releases_updated)
        self.Combobox_Release.bind("<Button>", self.combobox_values_releases_updated)
        self.Combobox_uboot = ttk.Combobox(medium_frame, values = [''] + self.uboot_version(), width = wide_combobox)        
        self.Combobox_uboot.grid()
        self.Combobox_uboot.bind("<<ComboboxSelected>>", self.uboot_version_update)
        self.Combobox_uboot.bind("<Button>", self.uboot_version_update)
        self.appbutton_download_develop = tk.Button(medium_frame, text='Download develop build from catalog', command = self.download_and_unzip_develop_file_from_catalog_parametrized_thread, height = 1, width = wide, font = font_all, foreground = 'black', background='light grey',borderwidth=3)
        self.appbutton_download_develop.grid()
        self.label = Label(medium_frame, width = wide_label, text = "Set develop build and bin file", font = font_all, foreground = 'black', background='light yellow', borderwidth=3)
        self.label.grid()
        self.Combobox_Develop = ttk.Combobox(medium_frame, values = [''] + self.combobox_values_develop(),width = wide_combobox)
        self.Combobox_Develop.grid()
        self.Combobox_Develop.bind("<<ComboboxSelected>>", self.combobox_values_develop_updated)
        self.Combobox_Develop.bind("<Button>", self.combobox_values_develop_updated)
        self.Combobox_uboot_develop = ttk.Combobox(medium_frame, values = [''] + self.uboot_version(), width = wide_combobox)        
        self.Combobox_uboot_develop.grid()
        self.Combobox_uboot_develop.bind("<<ComboboxSelected>>", self.uboot_version_update)
        self.Combobox_uboot_develop.bind("<Button>", self.uboot_version_update)
        self.appbutton_download_develop = tk.Button(medium_frame, text='Download last successfull build', command = self.download_artifacts_from_jenkins_thread, height = 1, width = wide, font = font_all, foreground = 'black', background='light grey',borderwidth=3)
        self.appbutton_download_develop.grid() 
        self.appbutton_putty_ssh = tk.Button(top_frame, text = 'Putty_SSH', command = self.putty_ssh_thread, height = 1, width = wide_medium_frame, font = font_all, foreground = 'black', background='light blue', borderwidth=3)
        self.appbutton_putty_ssh.grid(row =0, column=0)
        self.appbutton_putty_com = tk.Button(top_frame, text = 'Putty_COM', command = self.putty_com_thread, height = 1, width = wide_medium_frame, font= font_all, foreground = 'black', background='light blue', borderwidth=3)
        self.appbutton_putty_com.grid(row=0, column=1)
        self.appbutton_putty = tk.Button(top_frame, text = 'Putty', command = self.putty_thread, height = 1, width = wide_medium_frame, font = font_all, foreground = 'black', background='light blue', borderwidth=3)
        self.appbutton_putty.grid(row=1, column = 0)
        self.appbutton_putty = tk.Button(top_frame, text = '3CDeamon', command = self.cdeamon_thread, height = 1, width = wide_medium_frame, font = font_all, foreground = 'black', background='light blue', borderwidth=3)
        self.appbutton_putty.grid(row = 1, column =1)
        self.appbutton_pdu_on = tk.Button(top_frame, text = 'PDU_ON', command = self.pdu_on_thread, height = 1, width = wide_medium_frame, font = font_all, foreground = 'black', background='light blue', borderwidth=3)
        self.appbutton_pdu_on.grid(row = 2, column = 1)
        self.appbutton_pdu_off = tk.Button(top_frame, text = 'PDU_OFF', command = self.pdu_off_thread, height = 1, width = wide_medium_frame, font = font_all, foreground = 'black', background='light blue', borderwidth=3)
        self.appbutton_pdu_off.grid(row = 2, column =0)
        self.appbutton_hw_reset = Button(top_frame, text = 'SW_RESET', command = self.sw_reset_thread, height = 1, width = wide_medium_frame, font = font_all, foreground = 'black', background='light blue', borderwidth=3)
        self.appbutton_hw_reset.grid(row = 3, column =1)
        self.label = Label(top_frame, width = wide_medium_frame, text = "Set PDU port (1-12)", font = font_all, foreground = 'black', background='light yellow', borderwidth=3)
        self.label.grid(row = 4, column = 0)
        self.entry = tk.Entry(top_frame, width =21,font = font_all, foreground = 'black', background='white', borderwidth=3)
        self.entry.grid(row = 4, column = 1)
        self.appbutton_pdu_reset = Button(top_frame, text = 'PDU_RESET', command = self.pdu_reset_thread, height = 1, width = wide_medium_frame, font = font_all, foreground = 'black', background='light blue', borderwidth=3)
        self.appbutton_pdu_reset.grid(row = 3, column =0)
        
    def choose_file_ftp(self):
        try:
            combobox_lzma = self.Combobox.get()
            combobox_tftp = self.Combobox_TFTP.get()
            combobox_itb = self.Combobox_ITB.get()
            if combobox_lzma:
                self.place_file_thread(combobox_lzma)
            if combobox_tftp:
                self.place_file_thread(combobox_tftp)
            if combobox_itb:
                self.place_file_thread(combobox_itb)
            elif combobox_itb and combobox_tftp and combobox_lzma:
                self.place_file_thread(combobox_itb)
                self.place_file_thread(combobox_tftp)
                self.place_file_thread(combobox_lzma)                
        except Exception, e:
            print str(e)

    def copy_file_to_ftpcatalog_from_local_file(self):
        try:      
            combobox_lzma = self.Combobox.get()
            combobox_tftp = self.Combobox_TFTP.get()
            combobox_itb = self.Combobox_ITB.get()
            if combobox_lzma:
                self.copy_file_to_ftpcatalog_thread(combobox_lzma)
            if combobox_tftp:
                self.copy_file_to_ftpcatalog_thread(combobox_tftp)
            if combobox_itb:
                self.copy_file_to_ftpcatalog_thread(combobox_itb)
            elif combobox_itb and combobox_tftp and combobox_lzma:
                self.copy_file_to_ftpcatalog_thread(combobox_itb)
                self.copy_file_to_ftpcatalog_thread(combobox_tftp)
                self.copy_file_to_ftpcatalog_thread(combobox_lzma)
        except Exception, e:
            print str(e)
            
    def copy_file_to_ftpcatalog_from_local_file2(self):
        try:
            combobox_lzma = self.Combobox.get()
            combobox_tftp = self.Combobox_TFTP.get()
            combobox_itb = self.Combobox_ITB.get()
            if combobox_lzma:
                self.copy_lzma_file_to_ftpcatalog_from_local_file_thread()
            if combobox_tftp:
                self.copy_tftp_file_to_ftpcatalog_from_local_file_thread()
            if combobox_itb:
                self.copy_tftp_file_to_ftpcatalog_from_local_file_thread()
            elif combobox_itb and combobox_tftp and combobox_lzma:
                self.copy_lzma_file_to_ftpcatalog_from_local_file_thread()
                time.sleep(0.1)
                self.copy_tftp_file_to_ftpcatalog_from_local_file_thread()
                time.sleep(0.1)
                self.copy_tftp_file_to_ftpcatalog_from_local_file_thread()
        except Exception, e:
            print str(e)

    def copy_lzma_file_to_ftpcatalog_from_local_file_thread(self):
        try:
            t = threading.Thread(target = self.copy_file_to_ftpcatalog, args = (self.Combobox.get(),))
            t.start()
        except Exception, e:
            print str(e)

    def copy_tftp_file_to_ftpcatalog_from_local_file_thread(self):
        try:
            t = threading.Thread(target = self.copy_file_to_ftpcatalog, args = (self.Combobox_TFTP.get(),))
            t.start()
        except Exception, e:
            print str(e)

    def copy_tftp_file_to_ftpcatalog_from_local_file_thread(self):
        try:
            t = threading.Thread(target = self.copy_file_to_ftpcatalog, args = (self.Combobox_ITB.get(),))
            t.start()           
        except Exception ,e:
            print str(e)

    def copy_file_to_ftpcatalog(self, combobox):
        try:
            if not combobox:
                pass
            else:
                for each_file in os.listdir(local_path):
                    source = local_path + each_file
                    dastination = ftp_path + each_file
                    if each_file == combobox:
                        shutil.copy2(source, dastination)
                        print each_file + ' sent to catalog'
        except Exception, e:
            print str(e)

    def copy_file_to_ftpcatalog_thread(self, combobox):
        try:
            t = threading.Thread(target = self.copy_file_to_ftpcatalog, args = (combobox,))
            t.start()            
        except Exception, e:
            print str(e)
            
    def browse_file(self):
        try:
            browse_filename = askopenfilename(initialdir = local_path)
        except Exception, e:
            print str(e)
            
    def browse_file_thread(self):
        try:
            t = threading.Thread(target = self.browse_file)
            t.start()
        except Exception, e:
            print str(e)
            
    def browse_file_ftp_catalog(self):
        try:
            browse_filename = askopenfilename(initialdir = ftp_path)
        except Exception, e:
            print str(e)

    def combobox_values(self):
        try:
            lista_combobox = []
            for file_lzma in os.listdir(local_path):
                    if fnmatch.fnmatch(file_lzma,'*.lzma') or  fnmatch.fnmatch(file_lzma,'*.tar'):                    
                        lista_combobox.append(file_lzma)                       
            return (lista_combobox)
        except Exception, e:
            print str(e)
        
    def combobox_updated_values(self, event):
        try:
            self.Combobox['values'] = [''] + self.combobox_values()
            return self.Combobox.get()
        except Exception, e:
            print str(e)
        
    def combobox_values_releases(self):
        try:
            lista = []
            for file_name in os.listdir(release_build_path):
                lista.append(file_name)
            return lista
        except Exception, e:
            print str(e)
    
    def combobox_values_releases_updated(self, event):
        try:
            self.Combobox_Release['values'] = [''] + self.combobox_values_releases()
            self.Combobox_Release.get()     
        except Exception, e:
            print str(e)

    def combobox_values_develop(self):
        try:
            lista = []
            for file_name in os.listdir(develop_build_path):
                    lista.append(file_name)        
            return lista
        except Exception, e:
            print str(e)

    def combobox_values_develop_updated(self, event):
        try:
            self.Combobox_Release['values'] = [''] + self.combobox_values_develop()
            self.Combobox_Release.get()
        except Exception, e:
            print str(e)

    def combobox_values_for_flash(self):
        try:
            lista = []
            for file_for_flash in os.listdir(local_path + flash_path):
                    lista.append(file_for_flash)   
            return lista
        except Exception, e:
            print str(e)

    def combobox_values_for_flash_update(self, event):
        try:
            self.Combobox_FLash['values'] = [''] + self.combobox_values_for_flash()
            self.Combobox_FLash.get()
        except Exception, e:
            print str(e)

    def combobox_values_for_itb(self):
        try:
            lista = []               
            for file_for_itb in os.listdir(local_path):
                if fnmatch.fnmatch(file_for_itb,'*.itb'):
                    lista.append(file_for_itb)                    
            return lista        
        except Exception, e:
            print str(e)
    
    def combobox_values_for_itb_updated(self, event):
        try:
            self.Combobox_ITB['values'] = [''] + self.combobox_values_for_itb()
            self.Combobox_ITB.get()            
        except Exception, e:
            print str(e)

    def combobox_values_for_itb_tftp_updated(self, event):
        try:
            self.Combobox_TFTP_ITB['values'] = [''] + self.combobox_values_for_itb()
            self.Combobox_TFTP_ITB.get()            
        except Exception, e:
            print str(e)

    def combobox_values_for_tftp(self):
        try:
            listaa = []
            for file_for_tftp in os.listdir(local_path):
                if fnmatch.fnmatch(file_for_tftp,'*.bin'):
                    listaa.append(file_for_tftp)                    
            return sorted(listaa)        
        except Exception, e:
            print str(e)
    
    def combobox_values_for_tftp_updated(self, event):
        try:
            self.Combobox_TFTP['values'] = [''] + self.combobox_values_for_tftp()
            self.Combobox_TFTP.get()
        except Exception, e:
            print str(e)

    def justamethod (self, event):
        s = self.Combobox.get()
        return s

    def combo(self):
        return self.Combobox.get()
        
    def place_file(self, which_combobox):
        try:        
            file_name = local_path + which_combobox
            print file_name
            ftp = ftplib.FTP(host_name,password,'')
            files = open(file_name, 'rb')
            ftp.storbinary('STOR ' + os.path.basename(file_name), files)
            ftp.quit()
            files.close()
            print 'File downloading to RF wait.'
            time.sleep(5)
            print 'File ' + os.path.basename(file_name) + ' downloaded to Device'            
        except Exception, e:
            print str(e)
            
    def place_file_thread(self, which_combobox):
        try:
            t = threading.Thread(target = self.place_file, args = (which_combobox,))
            t.start()            
        except Exception, e:
            print str(e)

    def choose_file_ftp2(self):
        try:
            combobox_lzma = self.Combobox.get()
            combobox_tftp = self.Combobox_TFTP.get()
            combobox_itb = self.Combobox_ITB.get()            
            if combobox_lzma:
                self.place_file_lzma_thread()
            if combobox_tftp:
                self.place_file_tftp_thread()
            if combobox_itb:
                self.place_file_itb_thread()
            elif combobox_itb and combobox_tftp and combobox_lzma:
                self.place_file_itb_thread()
                self.place_file_tftp_thread()
                self.place_file_lzma_thread()                
        except Exception, e:
            print str(e)

    def place_file_tftp_thread(self):
        try:
            t = threading.Thread(target = self.place_file, args = (self.Combobox_TFTP.get(),))
            t.start()            
        except Exception, e:
            print str(e)

    def place_file_itb_thread(self):
        try:
            t = threading.Thread(target = self.place_file, args = (self.Combobox_ITB.get(),))
            t.start()            
        except Exception, e:
            print str(e)

    def place_file_lzma_thread(self):
        try:
            t = threading.Thread(target = self.place_file, args = (self.Combobox.get(),))
            t.start()            
        except Exception, e:
            print str(e)
            
    def place_file2_flash(self, combobox, extension, regex,path):
        file_name2 = combobox
        for file_ubi in os.listdir(path):
            if re.match(regex, file_name2) and fnmatch.fnmatch(file_name2, extension):
                ftp = ftplib.FTP(host_name,password,'')
                file_name2 = os.path.basename(file_name2)
                files = open(os.path.basename(file_name2), 'rb')
                ftp.storbinary('STOR ' + file_name2, files)
                ftp.quit()
                files.close()
        print 'File ' + os.path.basename(file_name2) + ' sent to  Device'

    def calculate_checksum(self):
        try:
            combobox_lzma = self.combo()
            if not combobox_lzma:
                pass
            else:                
                combobox_lzma = self.combo()
                with open(local_path + combobox_lzma, 'rb') as files:
                    data = files.read()
                    checksum = hex((zlib.adler32(data) & 0xffffffff))
                    checksum = checksum.rstrip('L')
                    time.sleep(1)
                    return checksum
        except Exception, e:
            print str(e)

    def software_update(self):
        try:
            print '*****SW update from Combobox ongoing***'
            command_to_a_combobox = str('**********************' + 
            self.Combobox.get().strip('**************************')+ 
            '************' + ' ' + self.Combobox.get().strip('***********************************************')+ 
            '***************' + ' ' +  self.Combobox.get() + ' ' + 
            self.Combobox.get().strip('***************************') + '**********')
            command_to_i_combobox = str('************************')
            command_to_s_combobox = str('****************************' + self.combo()
            + ' ' + self.calculate_checksum()+ ' '  + 
            self.Combobox.get().strip('****************************************************')+ 
            '*****************'+ ' '+ 
            self.Combobox.get().strip('*************************************************')+ '***********')                
            client = paramiko.SSHClient() 
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sock = socket.socket()
            sock.connect((host_name, tel_port))
            t = paramiko.Transport(sock)
            t.connect()
            t.auth_none('root')
            client._transport = t    
            stdin, stdout, stderr=client.exec_command(command_to_s_combobox)
            print command_to_s_combobox
            output1= ''.join(stdout.readlines())
            print output1
            output_err1=''.join(stderr.readlines())
            print output_err1
            stdin, stdout, stderr=client.exec_command(command_to_a_combobox)
            print command_to_a_combobox
            output2=''.join(stdout.readlines())
            print (output2)
            output_err2=''.join(stderr.readlines())
            print output_err2        
            stdin, stdout, stderr=client.exec_command(command_to_i_combobox)
            print command_to_i_combobox
            output3=''.join(stdout.readlines())
            print (output3)
            output_err3=''.join(stderr.readlines())
            print output_err3        
            client.close()
            print 'Please perform restart to complete SW update'                
        except Exception, e:
            print str(e)
            
    def software_update_thread(self):
        try:
            if not self.Combobox.get():
                print "Please select file"
            else:
                t = threading.Thread(target = self.software_update)
                t.start()
                t.join()
        except Exception, e:
            print str(e)
            
    def software_s(self):
        try:                              
            command_to_s_combobox = str('*************************' + self.combo() + ' '+ self.calculate_checksum()+ ' '  +  self.combo().strip('***********************') + '***********' + ' '+ self.combo().strip('******************')+ '*****************')                
            client = paramiko.SSHClient() 
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sock = socket.socket()
            sock.connect((host_name, tel_port))
            t = paramiko.Transport(sock)
            t.connect()
            t.auth_none('root')
            client._transport = t    
            stdin, stdout, stderr=client.exec_command(command_to_s_combobox)
            print command_to_s_combobox
            output1= ''.join(stdout.readlines())
            print output1
            output_err1=''.join(stderr.readlines())
            print output_err1        
            client.close()
            print 'save done'
        except Exception, e:
            print str(e)
            
    def software_s_thread(self):     
        try:
            combobox_lzma = self.combo()
            if not combobox_lzma:
                print "Please select file"
            else:
                t = threading.Thread(target = self.software_s)
                t.start()
                t.join()  
        except Exception, e:
            print str(e)                      
            
    def software_a(self):
        try:
            combobox_lzma = self.combo()
            if not  combobox_lzma:
                pass
            else:                
                print '********************'               
                file_from_combobox = str(combobox_lzma)
                command_to_a_combobox = str('**********************' + (file_from_combobox).strip('*******************************')+ '*********' + ' ' + (file_from_combobox).strip('**************************')+ '********' + ' ' +  file_from_combobox + ' ' + file_from_combobox.strip('*************************')+ '********************')
                client = paramiko.SSHClient() 
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                sock = socket.socket()
                sock.connect((host_name, tel_port))
                t = paramiko.Transport(sock)
                t.connect()
                t.auth_none('root')
                client._transport = t    
                stdin, stdout, stderr=client.exec_command(command_to_a_combobox)
                print command_to_a_combobox
                output2=''.join(stdout.readlines())
                print (output2)
                output_err2=''.join(stderr.readlines())
                print output_err2               
                client.close()
                print 'activation done'                
        except Exception, e:
            print str(e)
            
    def software_a(self):
        try:
            combobox_lzma = self.combo()
            if not combobox_lzma:
                print "Please select file"
            else:
                t = threading.Thread(target = self.software_a)
                t.start()
                t.join()
        except Exception, e:
            print str(e)
            
    def software_i(self):
        try:
            command_to_i_combobox = str('***********************')
            client = paramiko.SSHClient() 
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sock = socket.socket()
            sock.connect((host_name, tel_port))
            t = paramiko.Transport(sock)
            t.connect()
            t.auth_none('root')
            client._transport = t          
            stdin, stdout, stderr=client.exec_command(command_to_i_combobox)
            print command_to_i_combobox
            output3=''.join(stdout.readlines())
            print (output3)
            output_err3=''.join(stderr.readlines())
            print output_err3        
            client.close()
            print 'sw inventory done'                
        except Exception, e:
            print str(e)
            
    def software_i_thread(self):
        try:
            t = threading.Thread(target = self.software_i)
            t.start()    
        except Exception, e:
            print str(e)
            
    def br_i_slot_a(self):
        try:        
            bri = '*******'
            slot_a = '******'
            slot_sw = '**********************'                               
            client = paramiko.SSHClient() 
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sock = socket.socket()
            sock.connect((host_name, tel_port))
            t = paramiko.Transport(sock)
            t.connect()
            t.auth_none('root')
            client._transport = t    
            stdin, stdout, stderr=client.exec_command(bri)
            output1= ''.join(stdout.readlines())
            print output1
            output_err1=''.join(stderr.readlines())
            print output_err1
            stdin, stdout, stderr=client.exec_command(slot_a)
            output2=''.join(stdout.readlines())
            print output2 
            output_err2=''.join(stderr.readlines())
            print output_err2       
            stdin, stdout, stderr=client.exec_command(slot_sw)
            output3=''.join(stdout.readlines())
            print output3
            output_err3=''.join(stderr.readlines())
            print output_err3        
            client.close()                
        except Exception, e:
            print str(e)
            
    def br_i_slot_a_thread(self):
        try:
            t = threading.Thread(target = self.br_i_slot_a)
            t.start()                
        except Exception, e:
            print str(e)
            
    def ubi_a(self):
        try:
            ubi = '******'
            client = paramiko.SSHClient() 
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sock = socket.socket()
            sock.connect((host_name, tel_port))
            t = paramiko.Transport(sock)
            t.connect()
            t.auth_none('root')
            client._transport = t    
            stdin, stdout, stderr=client.exec_command(ubi)
            output1= ''.join(stdout.readlines())
            print output1
            output_err1=''.join(stderr.readlines())
            print output_err1        
            client.close()
        except Exception, e:
            print str(e)
    
    def ubi_a_thread(self):
        try:
            t = threading.Thread(target = self.ubi_a_thread)
            t.start()                
        except Exception, e:
            print str(e)
    
    def i2c(self):
        try:
            print "i2c checks counter"
            ubi = '*************************************'
            client = paramiko.SSHClient() 
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sock = socket.socket()
            sock.connect((host_name, tel_port))
            t = paramiko.Transport(sock)
            t.connect()
            t.auth_none('root')
            client._transport = t    
            stdin, stdout, stderr=client.exec_command(ubi)
            output1= ''.join(stdout.readlines())
            print output1
            output_err1=''.join(stderr.readlines())
            print output_err1        
            client.close()
        except Exception, e:
            print str(e)
            
    def i2c_thread(self):
        try:
            t = threading.Thread(target = self.i2c)
            t.start()                
        except Exception, e:
            print str(e)

    def ubirm_vol_n(self, ubirm):
        try:
            print(ubirm)
            client = paramiko.SSHClient() 
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sock = socket.socket()
            sock.connect((host_name, tel_port))
            t = paramiko.Transport(sock)
            t.connect()
            t.auth_none('root')
            client._transport = t    
            stdin, stdout, stderr=client.exec_command(ubirm)
            output1= ''.join(stdout.readlines())
            print output1
            output_err1=''.join(stderr.readlines())
            print output_err1        
            client.close()
        except Exception, e:
            print str(e)
            
    def ubirm_0_thread(self):
        try:
            t = threading.Thread(target = self.ubirm_vol_n, args = ('*****************************',) )
            t.start()                
        except Exception, e:
            print str(e)
            
    def ubirm_1_thread(self):
        try:
            t = threading.Thread(target = self.ubirm_vol_n, args = ('*************************************',) )
            t.start()                
        except Exception, e:
            print str(e)
            
    def ubirm_2_thread(self):
        try:
            t = threading.Thread(target = self.ubirm_vol_n, args = ('****************************************',) )
            t.start()                
        except Exception, e:
            print str(e)
            
    def rm_slo(self):
        try:
            rm_slo_all = '*********************'             
            client = paramiko.SSHClient() 
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sock = socket.socket()
            sock.connect((host_name, tel_port))
            t = paramiko.Transport(sock)
            t.connect()
            t.auth_none('root')
            client._transport = t    
            stdin, stdout, stderr=client.exec_command(rm_slo_all)
            output1= ''.join(stdout.readlines())
            print output1
            output_err1=''.join(stderr.readlines())
            print output_err1        
            client.close()               
        except Exception, e:
            print str(e)
            
    def rm_slo_thread(self):
        try:
            t = threading.Thread(target = self.rm_slo)
            t.start()                
        except Exception, e:
            print str(e)
 
    def itb_update(self):  
        print "Itb update ongoing"     
        combobox_itb = self.Combobox_ITB.get()
        try:
            for file_itb in os.listdir(ftp_path):
                if fnmatch.fnmatch(file_itb,'*.itb'):
                    os.remove(ftp_path + file_itb)
            time.sleep(1)                        
            for file_itb in os.listdir(local_path):
                source = local_path + file_itb
                dastination_itb1 = ftp_path + file_name_itb
                dastination_itb2 = ftp_path + combobox_itb
                if file_itb in combobox_itb:
                    shutil.copy2(source, dastination_itb2)
                    time.sleep(0.2)
                    os.rename(dastination_itb2, dastination_itb1)  
                    if os.path.exists(dastination_itb1):
                        pass
                    else: 
                        shutil.copy2(source, dastination_itb2)
                        time.sleep(0.2)
                        os.rename(dastination_itb2, dastination_itb1)         
                time.sleep(1) 
            if os.path.exists(dastination_itb1):           
                ser = serial.Serial(port = port_com, baudrate = 115200)
                while 1:
                    ser.write(command_root)
                    a = ser.readline()
                    if r"=>" in a:
                        ser.write(command_tftpload)
                        time.sleep(5)
                        ser.close()
                        break
                    elif r"-sh: root: not found" in a:
                        ser.write(command_reboot_serial)  
                        time.sleep(2)
                        ser.write(command_d)
                        ser.write(command_tftpload) 
                        ser.close()
                        break                             
        except serial.SerialException, e:
            print str(e)
            self.close_putty()
            time.sleep(1)
            ser = serial.Serial(port = port_com, baudrate = 115200)
            while 1:
                ser.write(command_root)
                a = ser.readline()
                if r"=>" in a:
                    ser.write(command_tftpload)
                    time.sleep(5)
                    ser.close()
                    break
                elif r"-sh: root: not found" in a:
                    ser.write(command_reboot_serial)  
                    time.sleep(2)
                    ser.write(command_d)
                    ser.write(command_tftpload) 
                    ser.close()
                    break                
            print 'Itb_update done' 

    def itb_update_thread(self):
        combobox_itb = self.Combobox_ITB.get()
        if not combobox_itb:            
            print 'Please select file'            
        else:            
            t = threading.Thread(target = self.itb_update)
            t.start()
            
    def tftp_update(self):
        combobox_tftp = self.Combobox_TFTP.get()
        combobox_itb = self.Combobox_TFTP_ITB.get()
        if not combobox_tftp:
                print 'Please select files'
        elif not combobox_itb:
            print 'Please select files'
        else:
            try:                                             
                for file_bin in os.listdir(ftp_path):
                    if fnmatch.fnmatch(file_bin,'*.bin') or fnmatch.fnmatch(file_bin,'*.itb'):
                        os.remove(ftp_path + file_bin)
                print 'All bin file removed from FTPCATALOG'            
                time.sleep(3)        
                for file_bin in os.listdir(local_path):
                    source = local_path + file_bin
                    dastination = ftp_path + combobox_tftp
                    dastination_itb = ftp_path + file_name_itb
                    if file_bin in combobox_tftp:
                        shutil.copy2(source, dastination)
                        if os.path.exists(ftp_path + file_bin):
                            pass
                        else: shutil.copy2(source, dastination)         
                time.sleep(1)              
                for file_itb in os.listdir(local_path):
                    source = local_path + file_itb
                    dastination_itb1 = ftp_path + file_name_itb
                    dastination_itb2 = ftp_path + combobox_itb
                    if file_itb in combobox_itb:
                        shutil.copy2(source, dastination_itb2)
                        time.sleep(0.2)
                        os.rename(dastination_itb2, dastination_itb1)  
                        if os.path.exists(dastination_itb1):
                            pass
                        else: 
                            shutil.copy2(source, dastination_itb2)
                            time.sleep(0.2)
                            os.rename(dastination_itb2, dastination_itb1)         
                    time.sleep(1)
                if os.path.exists(dastination_itb) and os.path.exists(combobox_tftp):              
                    for file_bin in os.listdir(ftp_path):
                        dastination = ftp_path + file_bin
                        if fnmatch.fnmatch(file_bin,'*.bin'):
                            ser = serial.Serial(port = port_com, baudrate = 115200)                         
                            while 1:
                                ser.write(command_root)
                                a = ser.readline()
                                print a
                                if r"=>" in a:
                                    ser.write(command_5_8)
                                    time.sleep(1)
                                    ser.close()
                                    break
                                elif r"-sh: root: not found" in a:
                                    ser.write(command_reboot_serial)  
                                    time.sleep(2)
                                    ser.write(command_d)
                                    ser.write(command_5_8) 
                                    ser.close()
                                    break                       
                            client = tftpy.TftpClient(tftp_ip, 69)
                            client.upload(file_bin, dastination)
                            print 'Tftp_update done'  
            except serial.SerialException, e:
                print str(e)
                self.close_putty()
                time.sleep(1)
                for file_bin in os.listdir(ftp_path):
                    dastination = ftp_path + file_bin
                    if fnmatch.fnmatch(file_bin,'*.bin'):
                        ser = serial.Serial(port = port_com, baudrate = 115200)                         
                        while 1:
                            ser.write(command_root)
                            a = ser.readline()
                            print a
                            if r"=>" in a:
                                ser.write(command_5_8)
                                time.sleep(1)
                                ser.close()
                                break
                            elif r"-sh: root: not found" in a:
                                ser.write(command_reboot_serial)  
                                time.sleep(2)
                                ser.write(command_d)
                                ser.write(command_5_8) 
                                ser.close()
                                break                       
                        client = tftpy.TftpClient(tftp_ip, 69)
                        client.upload(file_bin, dastination)
                        print 'Tftp_update done' 

    def tftp_update_thread(self):
        combobox_tftp = self.Combobox_TFTP.get()
        combobox_itb = self.Combobox_TFTP_ITB.get()
        if not combobox_tftp:
                print 'Please select files'
        elif not combobox_itb:
            print 'Please select files'
        else:
            t = threading.Thread(target = self.tftp_update)
            t.start()
            
    def flash_backupy(self, script_name):
        ser = serial.Serial(port = 'COM3', baudrate = 115200)
        time.sleep(5)
        ser.write('chmod +x /run/' + script_name)
        print 'chmod +x /run/' + script_name
        print 'chmod changed'
        ser.write('/run/' + script_name)
        print '/run/' + script_name + '\r\n'
        print script_name + ' done'
        ser.close()

    def tftp_update_in_unit_flash(self):      
        for file_bin in os.listdir(ftp_path):
            if fnmatch.fnmatch(file_bin,'*.bin'):
                ser = serial.Serial(port = 'COM3', baudrate = 115200)
                ser.write(command_reboot)
                ser.write(pss )
                time.sleep(2)
                ser.write(command_d)
                time.sleep(2)
                ser.write(command_5_8)
                print file_bin
                print dastination
                client = tftpy.TftpClient('***.***.***.*', 69)
                print 'connected to tftp client'
                client.upload(file_bin, dastination)
                print 'ubooted'
                
    def flash_radio_unit_first_part(self): 
        self.place_file2_flash(self.Combobox_FLash.get(),'*.sh', r'*****************', flash_path)        
        time.sleep(3)
        ser = serial.Serial(port = 'COM3', baudrate = 115200)
        time.sleep(5)
        ser.write('chmod +x ******************\r\n')
        print 'chmod changed'
        ser.write('********************\r\n')
        ser.close()
        ftp = ftplib.FTP(host_name,password,'')
        for factory_bck in ftp.nlst():
            if re.match(r'*****************',factory_bck):
                    files = open(flash_path + factory_bck, 'wb')
                    ftp.retrbinary('RETR ' + factory_bck, files.write)
                    files.close()
                    ftp.quit()
                    ftp.close()
        print 'Factory bck_copied to flash my dastination'        
        ##USUWANIE PLIKOW ITB I BIN Z FTPCATALOG
        for file_bin in os.listdir(ftp_path):
            if fnmatch.fnmatch(file_bin,'*.bin') or fnmatch.fnmatch(file_bin,'*.itb'):
                os.remove(ftp_path + file_bin)
        print 'all bin file removed from FTPCATALOG'
        time.sleep(1)
        ##KOPIOWANIE PLIKOW DO FTPCATALOG
        for file_bin in os.listdir(flash_path):
            source = flash_path + file_bin
            dastination_bin = ftp_path + file_bin
            dastination_itb = ftp_path + file_name_itb 
            if fnmatch.fnmatch(file_bin,'*.bin'):
                shutil.copy2(source, dastination_bin)
            if fnmatch.fnmatch(file_bin,'*.itb'):
                shutil.copy2(source, dastination_itb)
                print source               
        print 'bin file copied from my location to catalog'      
        time.sleep(1)
        self.tftp_update_in_unit_flash()
        time.sleep(30)                
        self.place_file2_flash('*************.sh','*.sh', r'****************', flash_path)                
        time.sleep(1)        
        ser = serial.Serial(port = 'COM3', baudrate = 115200)
        time.sleep(5)
        ser.write('root\r\n')
        ser.write('chmod +x /run/************.sh\r\n')
        print 'chmod changed'
        ser.write('/run/************.sh\r\n')
        print 'running ubi'
        ser.close()       
        time.sleep(300)
        self.tftp_update_in_unit_flash()        
        ser.close()
        print 'flash done'
        
    def flash_radio_unit_first_part_thread(self):
        t = threading.Thread(target = self.flash_radio_unit_first_part)
        t.start()       

#proba podlinkowania developerSkich buildow  
    def download_and_unzip_file_from_catalog(self, build_path, combobox, combobox_uboot, regex_bin):
        try:
            print 'downloading wait'            
            downloaded_lzma = combobox + '.tar'
            dastination_lzma = local_path + downloaded_lzma
            if  combobox:
                path_to_itb_lzma_files = combobox + '/' + lzma_catalog_path                
                for build_name in os.listdir(build_path):
                    source = build_path + build_name
                    dastination = local_path + build_name
                    if build_name == combobox:
                        if os.path.exists(local_path + build_name):
                            print build_name + ' already exist in local direction'                            
                        else:
                             shutil.copytree(source, dastination)
                             print build_name + ' folder coppied'
                time.sleep(3)                
                if os.path.exists(local_path + path_to_itb_lzma_files):
                        for filelzma in os.listdir(local_path + path_to_itb_lzma_files):                            
                           if  fnmatch.fnmatch(filelzma,'*.tar'):
                            #JESLI NIE MA FILELZMA TO GO KOPIUJE
                               if not os.path.exists(dastination_lzma):
                                   source2 = local_path + path_to_itb_lzma_files + filelzma
                                   shutil.copy2(source2, dastination_lzma)
                                   print filelzma + ' coppied as ' + downloaded_lzma
                                   time.sleep(2)
                               else:                            
                                   print downloaded_lzma + ' already in local direction'
                else:
                    for filetar in os.listdir((local_path + combobox + '/')):
                            if  fnmatch.fnmatch(filetar,'*.tar'):
                                if os.path.exists(dastination_lzma):
                                    print os.path.basename(dastination_lzma) + ' already in local directory'
                                else:
                                    shutil.copy2((local_path + combobox + '/' + filetar),dastination_lzma)
                                    print  os.path.basename(dastination_lzma) + ' coppied'                              
                if  combobox_uboot and os.path.exists(local_path + path_to_itb_lzma_files):
                    for filebin in os.listdir(local_path + path_to_itb_lzma_files):
                       source =  local_path + path_to_itb_lzma_files + filebin
                       dastination_bin = local_path + combobox.lstrip(regex_bin) + combobox_uboot                       
                       if  filebin == combobox_uboot:                           
                           if not os.path.exists(dastination_bin):
                              shutil.copy2(source, dastination_bin)
                              print filebin + ' coppied as ' + combobox.lstrip(regex_bin) + combobox_uboot
                           else: print combobox.lstrip(regex_bin) + combobox_uboot   + ' already in local directory'
                elif not combobox_uboot:
                    pass
                elif not os.path.exists(local_path + path_to_itb_lzma_files):
                    print 'There is no ' + combobox_uboot
                    pass
            else:
                    print 'There is no ********'                    
        except Exception, e:
            print str(e)
            
    def download_and_unzip_release_file_from_catalog_parametrized_thread(self):
        try:
            t = threading.Thread(target = self.download_and_unzip_file_from_catalog, args=(release_build_path, self.Combobox_Release.get(), self.Combobox_uboot.get(), '*****************************',))
            t.start()
        except Exception, e:            
            print str(e)
            
    def download_and_unzip_develop_file_from_catalog_parametrized_thread(self):
        try:
            t = threading.Thread(target = self.download_and_unzip_file_from_catalog, args=(develop_build_path, self.Combobox_Develop.get(), self.Combobox_uboot_develop.get(), 'common_build#',))
            t.start()            
        except Exception, e:
            print str(e)
    
    def download_artifacts_from_jenkins(self, projekt, job, artefact, local_path):
        url = r'********************************************' + projekt + '/job/' + job + '/lastSuccessfulBuild/artifact/' + artefact  
        wget.download(url, local_path)
        tar = tarfile.open(local_path + '*******************', "r:bz2")         
        tar.extractall(path_to_last_successfull_build)
        tar.close()        
        tar_download = [shutil.copyfile(path_to_last_successfull_build + '/' + tar_catalog_path + file_tar, local_path\
                 + self.last_successfully_build_file_version() + ".tar") for file_tar in os.listdir(path_to_last_successfull_build + tar_catalog_path)\
                  if fnmatch.fnmatch(file_tar, "*.tar")]
        bin_download = [shutil.copyfile(path_to_last_successfull_build + '/' + lzma_catalog_path + file_bin, local_path\
                 + self.last_successfully_build_file_version() + ".bin") for file_bin in os.listdir(path_to_last_successfull_build + lzma_catalog_path)\
                  if file_bin == r'**************************.bin'] 
        print 'Files downloaded'                       
        clean_folder = [shutil.rmtree(path_to_last_successfull_build + files) if os.path.isdir(path_to_last_successfull_build + files)\
        else os.remove(path_to_last_successfull_build + files)\
        for files in os.listdir(path_to_last_successfull_build)]
            
    def last_successfully_build_file_version(self):
        regex = r"*********************************"
        lista = [re.search(regex, open(path_to_last_successfull_build + file_txt, 'r').read()).group(0) for \
        file_txt in os.listdir(path_to_last_successfull_build) if file_txt.endswith('.txt')]
        return ''.join(lista)

    def download_artifacts_from_jenkins_thread(self):
        try:
            t = threading.Thread(target = self.download_artifacts_from_jenkins, args = (projekt, job , artefact, local_path))
            t.start()            
        except Exception, e:
            print str(e)
            
    def uboot_version(self):
        try:            
            with open(r'******************************************************', 'r') as files:
                my_list = [line.rstrip('\n') for line in files]                
                return my_list            
        except Exception, e:
            print str(e)
        
    def uboot_version_update(self, event):
        try:
            self.Combobox_uboot['values']=self.uboot_version()
            self.Combobox_uboot.get()
        except Exception,e:
            print str(e)
            
    def putty_ssh(self):
        pid = subprocess.Popen("putty.exe root@***.***.***.* -pw password").pid

    def putty_ssh_thread(self):
        t = threading.Thread(target = self.putty_ssh)
        t.start()

    def putty_com(self):
        pid = subprocess.Popen("putty.exe -serial " + port_com + " -sercfg 115200").pid

    def putty_com_thread(self):
        t = threading.Thread(target = self.putty_com)
        t.start()

    def putty(self):
        pid = subprocess.Popen("putty.exe").pid

    def putty_thread(self):
        t = threading.Thread(target = self.putty)
        t.start()

    def cdeamon(self):
        pid = subprocess.Popen("C:/Program Files (x86)/3Com/3CDaemon/3CDaemon").pid

    def cdeamon_thread(self):
        t = threading.Thread(target = self.cdeamon)
        t.start()

    def close_putty(self):
        try:
            os.system('TASKKILL /F /IM putty.exe')
            print 'Putty closed'            
        except Exception, e:
            print str(e)
            
    def close_putty_thread(self):
        try:
            t = threading.Thread(target = self.close_putty)
            t.start()
        except Exception, e:
            print str(e)
            
    def pdu_on(self):
        try:
            port = self.entry.get()
            lista = ['1','2','3','4','5','6','7','8','9', '10', '11', '12', '13', '14', '15']
            empty = ['']            
            if not port:
                print 'Port should be from 1-15'                
            if port in lista:
                os.chdir("C:\\Program Files (x86)\\GnuWin32\\bin")
                pid=subprocess.Popen('wget --delete-after' + " http://" + pdu_ip + "/ov.html?cmd=1&"+ "p=" + port + "&s=1").pid
                print 'Device is on'
        except Exception, e:
            print str(e)

    def pdu_on_thread(self):
        try:
            t = threading.Thread(target = self.pdu_on)
            t.start()
        except Exception, e:
            print str(e)

    def pdu_off(self):
        try:
            port = self.entry.get()
            lista = ('1','2','3','4','5','6','7','8','9', '10', '11', '12', '13', '14', '15')
            empty =''
            if not port:
                print 'Port should be from 1-15'                
            if port in lista :
                os.chdir("C:\\Program Files (x86)\\GnuWin32\\bin")
                pid=subprocess.Popen('wget --delete-after' + " http://" + pdu_ip + "/ov.html?cmd=1&"+ "p=" + port + "&s=0").pid
                print 'Device is off'
        except Exception, e:
            print str(e)
            
    def pdu_off_thread(self):
        try:
            t = threading.Thread(target = self.pdu_off)
            t.start()            
        except Exception, e:
            print str(e)

    def pdu_reset(self):
        try:
            self.pdu_off()
            print 'Power reset ongoing wait 5 second'
            time.sleep(5)
            self.pdu_on()
        except Exception ,e:
            print str(e)
            
    def pdu_reset_thread(self):
        try:        
            t = threading.Thread(target = self.pdu_reset)
            t.start()
        except Exception, e:
            print str(e)
            
    def sw_reset(self):
        try:  
            client = paramiko.SSHClient() 
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sock = socket.socket()
            sock.connect((host_name, tel_port))
            t = paramiko.Transport(sock)
            t.connect()
            t.auth_none('root')
            client._transport = t    
            stdin, stdout, stderr=client.exec_command(command_reboot)
            output1= ''.join(stdout.readlines())
            print output1
            output_err1=''.join(stderr.readlines())
            print output_err1        
            client.close()
        except Exception, e:
            print str(e)
            
    def sw_reset_thread(self):
        try:
            t = threading.Thread(target = self.sw_reset)
            t.start()
        except Exception, e:
            print str(e)

app= App()
app.mainloop()


