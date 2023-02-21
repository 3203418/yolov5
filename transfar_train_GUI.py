from cProfile import label
from curses.textpad import Textbox
from os import popen
from socket import TIPC_SUBSCR_TIMEOUT
from struct import pack
import tkinter as tk
from tkinter import messagebox
from tkinter.tix import Tree
from turtle import width
from click import command

from matplotlib.pyplot import text
import subprocess

from numpy import place, size
from time import sleep
import os
import signal

global proc

root = tk.Tk()

def detect_output_to_train(w):
    global proc
    button_1["state"] = tk.DISABLED
    button_2["state"] = tk.DISABLED
    button_3["state"] = tk.DISABLED
    button_6["state"] = tk.DISABLED

    w_place = w - 380
    geo_set = '40x28+' + str(w_place) + '+20'
    shell_add = "exec " + run_path + '/detect_output_to_train.sh'
    proc = subprocess.Popen('gnome-terminal --geometry=' + geo_set + ' -- ' + shell_add, shell=True)
    print("[detect_output_to_train.sh]を開始しました")
    proc.kill()

def output_to_transfer_learning(w):
    global proc
    button_1["state"] = tk.DISABLED
    button_2["state"] = tk.DISABLED
    button_3["state"] = tk.DISABLED
    button_6["state"] = tk.DISABLED

    w_place = w - 380
    geo_set = '40x28+' + str(w_place) + '+20'
    shell_add = "exec " + run_path +'/output_to_transfer_learning.sh'
    proc = subprocess.Popen(['gnome-terminal --geometry=' + geo_set + ' -- ' + shell_add], shell=True)
    print("[output_to_transfer_learning.sh]を開始しました")
    sleep(5)
    proc.kill()
    # proc.terminate()
    # exit



def train(w):
    global proc
    button_1["state"] = tk.DISABLED
    button_2["state"] = tk.DISABLED
    button_3["state"] = tk.DISABLED

    w_place = w - 50
    geo_set = '50x30+' + str(w_place) + '+0'
    shell_add = "exec " + run_path + '/transfer_learning_start_comand.sh'
    shell_arg = 2
    proc = subprocess.Popen(['exec gnome-terminal --geometry=' + geo_set + ' -- ' + shell_add + ' ' + str(shell_arg)], shell=True)
    print("[train]を開始しました")
    print(proc.pid)
    proc.kill()


def update(w):
    global proc
    button_1["state"] = tk.DISABLED
    button_2["state"] = tk.DISABLED
    button_3["state"] = tk.DISABLED

    w_place = w - 50
    geo_set = '50x30+' + str(w_place) + '+0'
    shell_add = "exec " + run_path + '/train-to-detect_comand.sh'
    shell_arg = 2
    proc = subprocess.Popen(['exec gnome-terminal --geometry=' + geo_set + ' -- ' + shell_add + ' ' + str(shell_arg)], shell=True)
    print("[train-to-detect_comand]を開始しました")
    print(proc.pid)
    proc.kill()



def kill_process():
    global proc
    subprocess.run(shell=True)
    proc.terminate()
    print("[process]を強制終了しました")
    if (button_1["state"] == tk.DISABLED) or (button_2["state"] == tk.DISABLED) or (button_3["state"] == tk.DISABLED):
        button_1["state"] = tk.NORMAL
        button_2["state"] = tk.NORMAL
        button_6["state"] = tk.NORMAL
        # button_3["state"] = tk.NORMAL

# def end_forced():
#     # global proc
#     # proc.kill()
#     # os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
#     subprocess.run('pkill --parent ' + str(proc.pid), shell = True)
#     print("プロセスを強制終了しました")

#def ShutDown():
#    ret = messagebox.askokcancel("確認","シャットダウンを実行します")
#    if ret:
#        subprocess.run(['shutdown','-h','now'], shell = True)
#        messagebox.showinfo("実行中","約60秒後にシャットダウンします")

# def pro_test2():
#     button_1["state"] = tk.DISABLED
#     button_2["state"] = tk.DISABLED
#     button_3["state"] = tk.DISABLED
#     print("プログラム_No2が実行されます")

# def pro_test3():
#     button_1["state"] = tk.DISABLED
#     button_2["state"] = tk.DISABLED
#     button_3["state"] = tk.DISABLED
#     print("プログラム_No3が実行されます")


run_path = os.getcwd()
print(run_path)



root.title("Self-Growth_GUI")
root.attributes("-topmost", True)
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

print("DisplaySize=" + str(w) + "x" + str(h))
h_place = h - 120
but_x = w / 6

root.geometry(str(w) + "x120+"+ "20" + "+" + str(h_place))

# label = tk.Label(root, text = "テスト")
# label.place(x=100, y=200)

# txtBox = tk.Entry()
# txtBox.configure(state='normal', width=50)
# txtBox.pack()

button_1 = tk.Button(
    text='Detect_start',
    width=int(but_x/20),
    height=4,
    command=lambda:detect_output_to_train(w)
)
button_1.place(x=but_x*0 + 10, y=10)

button_2 = tk.Button(
    text='DATA_set',
    width=int(but_x/20),
    height=4,
    command=lambda:output_to_transfer_learning(w)
)
button_2.place(x=but_x*1 + 10, y=10)

button_3 = tk.Button(
    text='Transfar_Train',
    width=int(but_x/20),
    height=4,
    command=lambda:train(w)
)
button_3.place(x=but_x*2 + 10, y=10)

button_4 = tk.Button(
    text='Weight\nupdate',
    width=int(but_x/20),
    height=4,
    command=lambda:update()
)
button_4.place(x=but_x*3 + 10, y=10)

button_5 = tk.Button(
    text='kill\nProcess',
    fg="red",
    width=int(but_x/20),
    height=4,
    command=lambda:kill_process()
)
button_5.place(x=but_x*4 + 10, y=10)

button_6 = tk.Button(
    text='Auto_Run',
    fg="white",
    width=int(but_x/20),
    height=4,
    bg = "green",
    command=lambda:ShutDown()
)
button_6.place(x=but_x*5 + 10, y=10)


root.mainloop()
