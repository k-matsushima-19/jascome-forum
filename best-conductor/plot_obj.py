#!/usr/bin/env python3
# coding:utf-8
import matplotlib
import matplotlib.pyplot as plt # v1.5.3
import matplotlib.ticker as ticker
import matplotlib.animation as animation
import matplotlib.patches as patches
import numpy as np
import os

def init_matplotlib():
    #
    # plotの設定
    #
    # figureのサイズ
    figsize = (6,4)
    # アスペクト比 ("equal": 等比，None: 自動)
    aspect = None
    # tickラベルのfontサイズ
    tick_labelsize = 22
    # tickとtickラベルの間のスペース
    pad = 10
    # x方向の範囲 (Noneにすると自動で決定)
    xlim = (0,200)
    # y方向の範囲 (Noneにすると自動で決定)
    ylim = (0,1.5)
    # x方向のmajor tickの間隔
    x_major_tick = None
    # x方向のminor tickの間隔
    x_minor_tick = None
    # y方向のmajor tickの間隔
    y_major_tick = None
    # y方向のminor tickの間隔
    y_minor_tick = None
    # x軸をlogスケールに
    xscale_log = False
    # y軸をlogスケールに
    yscale_log = False
    # x軸ラベル
    xlabel = r"Step"
    # y軸ラベル
    ylabel = r"$J$"
    # 軸ラベルのfontサイズ
    ax_labelsize = 25
    # Type 3のフォントが埋め込まれるのを防ぐ
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42
    matplotlib.rcParams["font.family"] = "Times New Roman"
    matplotlib.rcParams["mathtext.fontset"] = "cm"
    # 背景色
    bgcolor = "#ffffff"
    
    #
    # fig, axの生成
    #
    fig = plt.figure(1,figsize=figsize)
    ax = fig.add_subplot(111)
    if aspect: ax.set_aspect(aspect)
    ax.tick_params(labelsize=tick_labelsize)
    ax.tick_params(pad=pad)
    if xlim: ax.set_xlim(*xlim)
    if ylim: ax.set_ylim(*ylim)
    ax.set_xlabel(xlabel, fontsize=ax_labelsize)
    ax.set_ylabel(ylabel, fontsize=ax_labelsize)
    if x_major_tick is not None: ax.xaxis.set_major_locator(ticker.MultipleLocator(x_major_tick))
    if x_minor_tick is not None: ax.xaxis.set_minor_locator(ticker.MultipleLocator(x_minor_tick))
    if y_major_tick is not None: ax.yaxis.set_major_locator(ticker.MultipleLocator(y_major_tick))
    if y_minor_tick is not None: ax.yaxis.set_minor_locator(ticker.MultipleLocator(y_minor_tick))
    if xscale_log: ax.set_xscale('log')
    if yscale_log: ax.set_yscale('log')
    
    return fig, ax
    
def init_matplotlib_dual():
    #
    # plotの設定
    #
    # figureのサイズ
    figsize = (9,5)
    # アスペクト比 ("equal": 等比，None: 自動)
    aspect = None
    # tickラベルのfontサイズ
    tick_labelsize = 22
    # tickとtickラベルの間のスペース
    pad = 10
    # x方向の範囲 (Noneにすると自動で決定)
    xlim = None
    # y方向の範囲 (Noneにすると自動で決定)
    ylim_1 = None
    # y方向の範囲 (Noneにすると自動で決定)
    ylim_2 = None
    # x方向のmajor tickの間隔
    x_major_tick = None
    # x方向のminor tickの間隔
    x_minor_tick = None
    # y方向のmajor tickの間隔
    y_major_tick = None
    # y方向のminor tickの間隔
    y_minor_tick = None
    # x軸をlogスケールに
    xscale_log = False
    # y軸をlogスケールに
    yscale_log = False
    # x軸ラベル
    xlabel = r"$\omega$"
    # y軸ラベル (1)
    ylabel_1 = r"$|S_{00}|$"
    # y軸ラベル (2)
    ylabel_2 = r"$\mathrm{arg}\, S_{00} / \pi$"
    # 軸ラベルのfontサイズ
    ax_labelsize = 25
    # Type 3のフォントが埋め込まれるのを防ぐ
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42
    matplotlib.rcParams["font.family"] = "Times New Roman"
    matplotlib.rcParams["mathtext.fontset"] = "cm"
    # 背景色
    bgcolor = "#ffffff"
    
    #
    # fig, axの生成
    #
    fig = plt.figure(1,figsize=figsize)
    if bgcolor is None:
        ax1 = fig.add_subplot(111)
        ax2 = ax1.twinx() # 二つ目の軸を定義
    else:
        ax1 = fig.add_subplot(111)
        ax2 = ax1.twinx() # 二つ目の軸を定義

    for ax, ylabel, ylim in zip((ax1,ax2), (ylabel_1,ylabel_2), (ylim_1, ylim_2)):
        if aspect: ax.set_aspect(aspect)
        ax.tick_params(labelsize=tick_labelsize)
        ax.tick_params(pad=pad)
        if xlim: ax.set_xlim(*xlim)
        if ylim: ax.set_ylim(*ylim)
        ax.set_xlabel(xlabel, fontsize=ax_labelsize)
        ax.set_ylabel(ylabel, fontsize=ax_labelsize)
        if x_major_tick is not None: ax.xaxis.set_major_locator(ticker.MultipleLocator(x_major_tick))
        if x_minor_tick is not None: ax.xaxis.set_minor_locator(ticker.MultipleLocator(x_minor_tick))
        if y_major_tick is not None: ax.yaxis.set_major_locator(ticker.MultipleLocator(y_major_tick))
        if y_minor_tick is not None: ax.yaxis.set_minor_locator(ticker.MultipleLocator(y_minor_tick))
        if xscale_log: ax.set_xscale('log')
        if yscale_log: ax.set_yscale('log')
    
    return fig, ax1, ax2
    

def init_matplotlib_3d():
    #
    # plotの設定
    #
    # figureのサイズ
    figsize = (8,8)
    # アスペクト比 ("equal": 等比，None: 自動)
    aspect = "equal"
    # tickラベルのfontサイズ
    tick_labelsize = 22
    # tickとtickラベルの間のスペース
    pad = 10
    # x方向の範囲 (Noneにすると自動で決定)
    xlim = None
    # y方向の範囲 (Noneにすると自動で決定)
    ylim = None
    # z方向の範囲 (Noneにすると自動で決定)
    zlim = (-1,1)
    # x方向のmajor tickの間隔
    x_major_tick = None
    # x方向のminor tickの間隔
    x_minor_tick = None
    # y方向のmajor tickの間隔
    y_major_tick = None
    # y方向のminor tickの間隔
    y_minor_tick = None
    # x軸をlogスケールに
    xscale_log = False
    # y軸をlogスケールに
    yscale_log = False
    # x軸ラベル
    xlabel = r"$\mathrm{Re}[\beta/\pi]$"
    # y軸ラベル
    ylabel = r"$\mathrm{Im}[\beta/\pi]$"
    # z軸ラベル
    zlabel = r"$\mathrm{Re}[G_\beta(x,y;I)]$"
    # 軸ラベルのfontサイズ
    ax_labelsize = 25
    # Type 3のフォントが埋め込まれるのを防ぐ
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42
    matplotlib.rcParams["font.family"] = "Times New Roman"
    matplotlib.rcParams["mathtext.fontset"] = "cm"
    # 背景色
    bgcolor = "#ffffff"
    
    #
    # fig, axの生成
    #
    fig = plt.figure(1,figsize=figsize)
    ax = fig.add_subplot(111, projection="3d")
    if aspect: ax.set_aspect(aspect)
    ax.tick_params(labelsize=tick_labelsize)
    ax.tick_params(pad=pad)
    if xlim: ax.set_xlim(*xlim)
    if ylim: ax.set_ylim(*ylim)
    if zlim: ax.set_zlim(*zlim)
    ax.set_xlabel(xlabel, fontsize=ax_labelsize, labelpad=25)
    ax.set_ylabel(ylabel, fontsize=ax_labelsize, labelpad=25)
    ax.set_zlabel(zlabel, fontsize=ax_labelsize, labelpad=25)
    if x_major_tick is not None: ax.xaxis.set_major_locator(ticker.MultipleLocator(x_major_tick))
    if x_minor_tick is not None: ax.xaxis.set_minor_locator(ticker.MultipleLocator(x_minor_tick))
    if y_major_tick is not None: ax.yaxis.set_major_locator(ticker.MultipleLocator(y_major_tick))
    if y_minor_tick is not None: ax.yaxis.set_minor_locator(ticker.MultipleLocator(y_minor_tick))
    if xscale_log: ax.set_xscale('log')
    if yscale_log: ax.set_yscale('log')
    
    return fig, ax

  
if __name__ == "__main__":
    fig, ax = init_matplotlib()

    data = np.genfromtxt("output/history.dat")
    
    #
    # plot
    #
    ax.plot(data[:,0], data[:,1], ls="-", c="black", lw=2)
    
    #
    # 保存
    #
    plt.tight_layout()
    filename = "obj"
    fig.savefig(filename+".eps",bbox_inches='tight', pad_inches=0.05)
    fig.savefig(filename+".png",bbox_inches='tight', pad_inches=0.05)
    
    #
    # 表示
    #
    plt.show()
    
    # figを閉じる
    fig.clf()
    plt.close(fig) # これがないと完全にfig,axがresetされない