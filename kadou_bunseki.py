import time
import tkinter as tk
from tkinter import font
from threading import Thread
from copy import deepcopy

class MAIN_ROUCHINE:
    def __init__(self):
        self.file_name = ''
        self.super_zero = 0
        self.now_time = 0
        self.ft = 1
        self.timer0 = 0
        self.lap_no = 0
        self.living = 1
        self.key_from_tk = ''
        self.last_msg = ''
        self.measureing = 0

        self.locker = 0

        print('デシマルストップウォッチ for 稼働分析')
        #print('Enter押下でスタート＆ラップタイム記録')
        #print('"q"入力後Enter押下で停止')

    def killMe(self):
        self.living = 0

    def startMe(self):
        self.file_name = f'稼働分析{time.time():.0f}.csv'
        self.measureing = 1

    def stopMe(self):
        self.measureing = 0

    def lapMe(self):
        self.locker = 1
        if self.measureing:
            if self.ft:
                print(self.nowTime(), f'計測開始！ "{self.file_name}"に記録します。')
                self.super_zero = time.time()
                self.timer0 = time.time()
                self.ft = 0
            else:
                self.now_time = time.time()
                result = self.now_time - self.timer0
                result_total = self.now_time - self.super_zero
                result_decimal = result / 0.6
                result_total_decimal = result_total / 0.6
                self.last_msg = f'{self.nowTime()} Lap{self.lap_no:3}: {result_decimal:.1f} DM   Total:{result_total_decimal:.1f} DM'
                print(self.last_msg)
                self.f.write(f'{self.lap_no},{result_decimal:.1f},{result_total_decimal:.1f}\n')
                self.timer0 = time.time()
            self.lap_no += 1
        self.locker = 0

    # time of time
    def nowTime(self):
        from time import strftime, localtime
        return strftime('%H:%M:%S', localtime())

    def main(self):
        while self.living:
            self.super_zero = 0
            self.now_time = 0
            self.ft = 1
            self.timer0 = 0
            self.lap_no = 0
            self.key_from_tk = ''
            self.last_msg = ''

            #self.file_name = f'稼働分析{time.time():.0f}.txt'
            if self.measureing:
                with open(self.file_name, mode='w') as self.f:
                    while self.measureing:

                        '''
                        #inp = input()

                        if inp == 'q':
                            break
                        '''

                        '''
                        if self.key_from_tk in {'Return', 'space'}:

                            if self.ft:
                                print(self.nowTime(), f'計測開始！ "{self.file_name}"に記録します。')
                                self.super_zero = time.time()
                                self.timer0 = time.time()
                                self.ft = 0
                            else:
                                self.now_time = time.time()
                                result = self.now_time - self.timer0
                                result_total = self.now_time - self.super_zero
                                result_decimal = result / 0.6
                                result_total_decimal = result_total / 0.6
                                self.last_msg = f'{self.nowTime()} Lap{self.lap_no:3}: {result_decimal:.1f} DM   Total:{result_total_decimal:.1f} DM'
                                print(self.last_msg)
                                self.f.write(f'{self.lap_no},{result_decimal:.1f},{result_total_decimal:.1f}\n')
                                self.timer0 = time.time()
                            self.lap_no += 1
                            self.key_from_tk = ''
                        else:
                            self.key_from_tk = ''
                        '''
                        time.sleep(0.01)
                    print(self.nowTime(), f'計測終了！ "{self.file_name}"に記録しました。')
            else:
                time.sleep(0.01)

            '''
            print('Enter押下でスタート＆ラップタイム記録')
            #print('"q"入力後Enter押下で終了')

            inp = input()

            if inp == 'q':
                break
            '''

class MAIN_GUI:
    def __init__(self):
        self.font_family = 0
        self.panel_font = 0
        self.panel_font_mid = 0
        self.panel_font_big = 0
        self.panel_font_button = 0

        self.keyb_tk = 0

        self.measureing_time = ''
        self.lap_time = ''
        self.console_texts = ''

        self.root = 0
        self.focus_thief = 0
        self.timer_main = 0
        self.lap_label = 0

        self.stw = MAIN_ROUCHINE()
        self.mainLoop()

    def loopEnd(self):
        self.stw.killMe()
        time.sleep(0.1)

    def getUsableFontFamily(self):
        font_families = font.families()
        '''
        for fc in font_families:
            if 'M+' in fc:
                print(fc)
        '''
        if 'M+ 1mn' in font_families:
            font_family = 'M+ 1mn'
        elif 'Consolas' in font_families:
            font_family = 'Consolas'
        elif 'DejaVu Sans Mono' in font_families:
            font_family = 'Dejavu Sans Mono'
        else:
            font_family = 'Courier'
        return font_family

    def resetKeyTk(self):
        self.keyb_tk = 0

    def keyBind(self, event):
        self.keyb_tk = event.keysym
        #self.stw.key_from_tk = deepcopy(self.keyb_tk)
        if self.keyb_tk in {'Return', 'space'}:
            if not self.stw.locker:
                self.stw.lapMe()
        self.resetKeyTk()

    def createStringVar(self):
        self.measureing_time = tk.StringVar()
        self.lap_time = tk.StringVar()
        self.console_texts = tk.StringVar()

    def createGUI(self):
        # create root-panel
        self.root = tk.Tk()
        try:
            self.root.attributes('-toolwindow', True)
            self.root.attributes('-topmost', True)
        except:
            pass

        font_family = self.getUsableFontFamily()
        font_size = {
            'normal': 10,
            'mid': 25,
            'big': 44,
            'button': 38,
        }

        self.panel_font = font.Font(root=self.root, family=font_family, size=font_size.get('normal'), weight='normal')
        self.panel_font_mid = font.Font(root=self.root, family=font_family, size=font_size.get('mid'), weight='normal')
        self.panel_font_big = font.Font(root=self.root, family=font_family, size=font_size.get('big'), weight='normal')
        self.panel_font_button = font.Font(root=self.root, family=font_family, size=font_size.get('button'), weight='normal')

        self.root.title(f'稼働分析用DMストップウォッチ by Keigo.M')
        # set the top right close button minimize (iconify) the main window
        self.root.protocol('WM_DELETE_WINDOW', self.loopEnd)
        # set Esc exit the program and keyBind
        self.root.bind('<Escape>', func=lambda events: self.loopEnd())
        self.root.bind('<Key>', self.keyBind)
        self.root.focus_set()
        self.createStringVar()

        # create main-label
        self.timer_main = tk.Label(master=self.root, textvariable=self.measureing_time, font=self.panel_font_big, bg='dodger blue')
        self.timer_main.grid(row=0, column=0, columnspan=2, sticky='W' + 'E' + 'N' + 'S')

        # create reset-buttons-label
        self.btn_start = tk.Button(master=self.root, text='計測開始', font=self.panel_font_button, bg='deep sky blue', command=self.stw.startMe)

        # create write-button-label
        self.btn_stop = tk.Button(master=self.root, text='計測停止', font=self.panel_font_button, bg='orange red', command=self.stw.stopMe)

        # grid for buttons
        self.btn_start.grid(row=1, column=0)
        self.btn_stop.grid(row=1, column=1)

        # create console-label
        self.lap_label = tk.Label(master=self.root, textvariable=self.lap_time, anchor='nw', justify='left', font=self.panel_font, bg='black', fg='alice blue', relief=tk.RIDGE, bd=2)
        self.lap_label.grid(row=2, column=0, columnspan=2, sticky='W' + 'E' + 'N' + 'S')

    def mainLoop(self):
        stw_main_th = Thread(target=self.stw.main)
        stw_main_th.setDaemon(True)
        stw_main_th.start()
        self.createGUI()
        time.sleep(0.1)
        while True:
            if self.stw.measureing:
                self.btn_start['state'] = 'disable'
                self.btn_stop['state'] = 'normal'
            else:
                self.btn_start['state'] = 'normal'
                self.btn_stop['state'] = 'disable'

            if self.stw.timer0 == 0:
                set_time = '0.0 DM'
            else:
                set_time = f'{(time.time() - self.stw.super_zero) / 0.6:.1f} DM'
            self.measureing_time.set(set_time)

            if self.stw.last_msg == '':
                if not self.stw.measureing:
                    last_msg = '「計測開始」押下でスタンバイ'
                elif self.stw.ft:
                    last_msg = 'EnterかSpace押下で記録開始(まだ時計は動いていない)'
                else:
                    last_msg = 'EnterかSpace押下で最初のLap記録(もう時計は動いている)'
                    if not self.root.focus_get():
                        self.root.lift()
                        self.root.focus_force()
            else:
                last_msg = self.stw.last_msg
                if not self.root.focus_get():
                    self.root.lift()
                    self.root.focus_force()

            self.lap_time.set(last_msg)

            self.root.update_idletasks()
            self.root.update()

            #if self.stw.key_from_tk == '':
            #    self.resetKeyTk()

            if not self.stw.living:
                break

            #time.sleep(0.01)

if __name__ == '__main__':
    main_gui = MAIN_GUI()
