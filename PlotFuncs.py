#================================PlotFuncs.py==================================#
# Based by Ciaran O'Hare 2020, created by Miguel Gonzalez

# Description:
# This file has many functions which are used throughout the project, but are
# all focused around making the plots

#==============================================================================#

from numpy import *
from numpy.random import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.gridspec as gridspec
from matplotlib.colors import ListedColormap
from matplotlib import colors
import matplotlib.ticker as mticker
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.cm as cm
from scipy.stats import norm
import matplotlib.patheffects as pe

pltdir = 'plots/'
pltdir_png = pltdir+'plots_png/'

#==============================================================================#
def col_alpha(col,alpha=0.1):
    rgb = colors.colorConverter.to_rgb(col)
    bg_rgb = [1,1,1]
    return [alpha * c1 + (1 - alpha) * c2
            for (c1, c2) in zip(rgb, bg_rgb)]
#==============================================================================#


def PlotBound(ax,filename,edgecolor='k',facecolor='crimson',alpha=1,lw=1.5,y2=1e10,zorder=0.1,
              linestyle='-',skip=1,FillBetween=True,edgealpha=1,rescale_m=False,
              scale_x=1,scale_y=1,start_x=0,end_x=nan,MinorEdgeScale=1.5,AddMinorEdges=False):
    dat = loadtxt(filename)
    if end_x/end_x==1:
        dat = dat[start_x:end_x,:]
    else:
        dat = dat[start_x:,:]
    dat[:,0] *= scale_x
    dat[:,1] *= scale_y
    if rescale_m:
        dat[:,1] = dat[:,1]/dat[:,0]
    if FillBetween:
        ax.fill_between(dat[0::skip,0],dat[0::skip,1],y2=y2,color=facecolor,alpha=alpha,zorder=zorder,lw=0)
    else:        
        ax.fill(dat[0::skip,0],dat[0::skip,1],color=facecolor,alpha=alpha,zorder=zorder,lw=0)
    ax.plot(dat[0::skip,0],dat[0::skip,1],color=edgecolor,zorder=zorder,lw=lw,linestyle=linestyle,alpha=edgealpha)
    if skip>1:
        ax.plot([dat[-2,0],dat[-1,0]],[dat[-2,1],dat[-1,1]],color=edgecolor,zorder=zorder,lw=lw,linestyle=linestyle,alpha=edgealpha)
    if AddMinorEdges:
        ax.plot([dat[-1,0],dat[-1,0]],[dat[-1,1],MinorEdgeScale*dat[-1,1]],color=edgecolor,zorder=zorder,lw=lw,linestyle=linestyle,alpha=edgealpha)
        ax.plot([dat[0,0],dat[0,0]],[dat[0,1],MinorEdgeScale*dat[0,1]],color=edgecolor,zorder=zorder,lw=lw,linestyle=linestyle,alpha=edgealpha)
    return

def line_background(lw,col):
    return [pe.Stroke(linewidth=lw, foreground=col), pe.Normal()]



def FilledLimit(ax,dat,text_label='',col='ForestGreen',edgecolor='k',zorder=1,linestyle='-',\
                    lw=2,y2=1e0,edgealpha=0.6,text_on=False,text_pos=[0,0],\
                    ha='left',va='top',clip_on=True,fs=15,text_col='k',rotation=0,facealpha=1,path_effects=None,textalpha=1):
    plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,alpha=facealpha,zorder=zorder)
    plt.plot(dat[:,0],dat[:,1],linestyle=linestyle,color=edgecolor,alpha=edgealpha,zorder=zorder,lw=lw)
    if text_on:
        plt.text(text_pos[0],text_pos[1],text_label,fontsize=fs,color=text_col,\
            ha=ha,va=va,clip_on=clip_on,rotation=rotation,rotation_mode='anchor',path_effects=path_effects,alpha=textalpha)
    return

def UnfilledLimit(ax,dat,text_label='',col='ForestGreen',edgecolor='k',zorder=1,\
                    lw=2,y2=1e0,edgealpha=0.6,text_on=False,text_pos=[0,0],\
                    ha='left',va='top',clip_on=True,fs=15,text_col='k',rotation=0,facealpha=1,\
                     linestyle='--'):
    plt.plot(dat[:,0],dat[:,1],linestyle=linestyle,color=edgecolor,alpha=edgealpha,zorder=zorder,lw=lw)
    if text_on:
        plt.text(text_pos[0],text_pos[1],text_label,fontsize=fs,color=text_col,\
            ha=ha,va=va,clip_on=clip_on,rotation=rotation,rotation_mode='anchor')
    return

def UpperFrequencyAxis(ax,N_Hz=1,tickdir='out',xtick_rotation=0,labelsize=25,xlabel=r"$\nu_a$ [Hz]",lfs=40,tick_pad=8,tfs=25,xlabel_pad=10):
    m_min,m_max = ax.get_xlim()
    ax2 = ax.twiny()
    ax2.set_xlabel(xlabel,fontsize=lfs,labelpad=xlabel_pad)
    ax2.set_xscale('log')
    plt.xticks(rotation=xtick_rotation)
    ax2.tick_params(labelsize=tfs)
    ax2.tick_params(which='major',direction=tickdir,width=2.5,length=13,pad=tick_pad)
    ax2.tick_params(which='minor',direction=tickdir,width=1,length=10)
    locmaj = mpl.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=50)
    locmin = mpl.ticker.LogLocator(base=10.0, subs=arange(2, 10)*.1,numticks=100)
    ax2.xaxis.set_major_locator(locmaj)
    ax2.xaxis.set_minor_locator(locmin)
    ax2.xaxis.set_minor_formatter(mpl.ticker.NullFormatter())
    ax2.set_xlim([m_min*241.8*1e12/N_Hz,m_max*241.8*1e12/N_Hz])
    plt.sca(ax)

def UpperFrequencyAxis_Simple(ax,tickdir='out',xtick_rotation=0,labelsize=25,xlabel=None,lfs=40,tick_pad=8,tfs=25,xlabel_pad=10):
    m_min,m_max = ax.get_xlim()
    ax2 = ax.twiny()
    ax2.set_xscale('log')
    ax2.set_xlabel(xlabel,fontsize=lfs,labelpad=xlabel_pad)
    ax2.tick_params(labelsize=tfs)
    ax2.tick_params(which='major',direction=tickdir,width=2.5,length=13,pad=tick_pad)
    ax2.tick_params(which='minor',direction=tickdir,width=1,length=10)
    locmaj = mpl.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=50)
    locmin = mpl.ticker.LogLocator(base=10.0, subs=arange(2, 10)*.1,numticks=100)
    ax2.xaxis.set_major_locator(locmaj)
    ax2.xaxis.set_minor_locator(locmin)
    ax2.xaxis.set_minor_formatter(mpl.ticker.NullFormatter())
    ax2.set_xticks(10.0**arange(-9,18))
    ax2.set_xticklabels(['nHz','','',r'\textmu Hz','','','mHz','','','Hz','','','kHz','','','MHz','','','GHz','','','THz','','','PHz','','']);
    ax2.set_xlim([m_min*241.8*1e12,m_max*241.8*1e12])
    plt.sca(ax)
    return

def AlternativeCouplingAxis(ax,scale=1,tickdir='out',labelsize=25,ylabel=r"$g_\gamma$ [GeV$^{-1}$]",lfs=40,tick_pad=8,tfs=25,ylabel_pad=60):
    g_min,g_max = ax.get_ylim()
    ax3 = ax.twinx()
    ax3.set_ylim([g_min*scale,g_max*scale])
    ax3.set_ylabel(ylabel,fontsize=lfs,labelpad=ylabel_pad,rotation=-90)
    ax3.set_yscale('log')
    ax3.tick_params(labelsize=tfs)
    ax3.tick_params(which='major',direction=tickdir,width=2.5,length=13,pad=tick_pad)
    ax3.tick_params(which='minor',direction=tickdir,width=1,length=10)
    locmaj = mpl.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=50)
    locmin = mpl.ticker.LogLocator(base=10.0, subs=arange(2, 10)*.1,numticks=100)
    ax3.yaxis.set_major_locator(locmaj)
    ax3.yaxis.set_minor_locator(locmin)
    ax3.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())
    plt.sca(ax)

def FigSetup(xlab='',ylab='',\
                 g_min = 1.0e-22,g_max = 1.0e-6,\
                 m_min = 1.0e-12,m_max = 1.0e7,\
                 lw=2.5,lfs=45,tfs=25,tickdir='out',figsize=(16.5,11),\
                 Grid=False,Shape='Rectangular',\
                 mathpazo=False,TopAndRightTicks=False,majorticklength=13,minorticklength=10,\
                xtick_rotation=20.0,tick_pad=8,x_labelpad=10,y_labelpad=10,\
             FrequencyAxis=False,N_Hz=1,upper_xlabel=r"$\nu_a$ [Hz]",**freq_kwargs):

    plt.rcParams['axes.linewidth'] = lw
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=tfs)

    if mathpazo:
            plt.rcParams.update({
        "text.usetex": True,
        "font.family": "serif",
        "font.serif": ["Palatino"],
            })

    if Shape=='Wide':
        fig = plt.figure(figsize=(16.5,5))
    elif Shape=='Rectangular':
        fig = plt.figure(figsize=(16.5,11))
    elif Shape=='Square':
        fig = plt.figure(figsize=(14.2,14))
    elif Shape=='Custom':
        fig = plt.figure(figsize=figsize)

    ax = fig.add_subplot(111)

    ax.set_xlabel(xlab,fontsize=lfs,labelpad=x_labelpad)
    ax.set_ylabel(ylab,fontsize=lfs,labelpad=y_labelpad)

    ax.tick_params(which='major',direction=tickdir,width=2.5,length=majorticklength,right=TopAndRightTicks,top=TopAndRightTicks,pad=tick_pad)
    ax.tick_params(which='minor',direction=tickdir,width=1,length=minorticklength,right=TopAndRightTicks,top=TopAndRightTicks)

    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_xlim([m_min,m_max])
    ax.set_ylim([g_min,g_max])

    locmaj = mpl.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=50)
    locmin = mpl.ticker.LogLocator(base=10.0, subs=arange(2, 10)*.1,numticks=100)
    ax.xaxis.set_major_locator(locmaj)
    ax.xaxis.set_minor_locator(locmin)
    ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter())

    locmaj = mpl.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=100)
    locmin = mpl.ticker.LogLocator(base=10.0, subs=arange(2, 10)*.1,numticks=100)
    ax.yaxis.set_major_locator(locmaj)
    ax.yaxis.set_minor_locator(locmin)
    ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())

    plt.xticks(rotation=xtick_rotation)

    if Grid:
        ax.grid(zorder=0)

    if FrequencyAxis:
        UpperFrequencyAxis(ax,N_Hz=N_Hz,tickdir='out',\
                           xtick_rotation=xtick_rotation,\
                           xlabel=upper_xlabel,\
                           lfs=lfs/1.3,tfs=tfs,tick_pad=tick_pad-2,**freq_kwargs)

    return fig,ax


#==============================================================================#
class AxionPhoton():
    def QCDAxion(ax,C_logwidth=10,KSVZ_on=True,DFSZ_on=True,cmap=cm.YlOrBr,fs=18,RescaleByMass=False,text_on=True,
                thick_lines=False,C_center=1,C_width=0.8,
                C_upper = 44/3-1.92,C_lower = abs(5/3-1.92),level_max = 4,nlevels=20,alpha=0.2,line_color='#a35c2f',
                KSVZ_label_mass=1e-8,DFSZ_label_mass=5e-8,vmax=0.9):
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0

        ## QCD Axion band:
        g_min,g_max = ax.get_ylim()
        m_min,m_max = ax.get_xlim()

        # Mass-coupling relation
        def g_x(C_ag,m_a):
            return 2e-10*C_ag*m_a
        KSVZ = 1.92
        DFSZ = 0.75

        if rs1==0:
            # # Plot Band
            # n = 200
            # g = logspace(log10(g_min),log10(g_max),n)
            # m = logspace(log10(m_min),log10(m_max),n)
            # QCD = zeros(shape=(n,n))
            # for i in range(0,n):
            #     QCD[:,i] = norm.pdf(log10(g)-log10(g_x(C_center,m[i])),0.0,C_width)
            # cols = cm.get_cmap(cmap)

            # cols.set_under('w') # Set lowest color to white
            # vmin = amax(QCD)/(C_logwidth/4.6)
            # plt.contourf(m, g, QCD, 50,cmap=cols,vmin=vmin,vmax=vmax,zorder=0)
            # plt.contourf(m, g, QCD, 50,cmap=cols,vmin=vmin,vmax=vmax,zorder=0)
            # plt.contourf(m, g, QCD, 50,cmap=cols,vmin=vmin,vmax=vmax,zorder=0)

            # QCD axion hadronic band
            m = array([1e-30,1e20])
            ga = 2e-10*m
            cols = cmap(linspace(0.1,0.45,nlevels))
            levels = (linspace(1,sqrt(level_max),nlevels))**2
            for i in range(nlevels-1):
                ax.fill_between(m,C_upper*ga/levels[i],C_lower*ga*levels[i],alpha=alpha,color=cols[i,:],zorder=-1000,lw=0)

            # QCD Axion models
            rot = 45.0
            trans_angle = plt.gca().transData.transform_angles(array((rot,)),array([[0, 0]]))[0]
            m2 = array([1e-9,5e-8])
            if KSVZ_on:
                if thick_lines:
                    plt.plot(m,g_x(KSVZ,m),'-',linewidth=5,color='k',zorder=0)
                    plt.plot(m,g_x(KSVZ,m),'-',linewidth=3,color=line_color,zorder=0)
                else:
                    plt.plot(m,g_x(KSVZ,m),'-',linewidth=2,color=line_color,zorder=0)
                if text_on:
                    plt.text(KSVZ_label_mass,g_x(KSVZ,KSVZ_label_mass)*1.05,r'{\bf KSVZ}',fontsize=fs,rotation=trans_angle,color=line_color,ha='left',va='bottom',rotation_mode='anchor',clip_on=True)
            if DFSZ_on:
                if thick_lines:
                    plt.plot(m,g_x(DFSZ,m),'-',linewidth=5,color='k',zorder=0)
                    plt.plot(m,g_x(DFSZ,m),'-',linewidth=3,color=line_color,zorder=0)
                else:
                    plt.plot(m,g_x(DFSZ,m),'-',linewidth=2,color=line_color,zorder=0)
                if text_on:
                    plt.text(DFSZ_label_mass,g_x(DFSZ,DFSZ_label_mass)/1.5,r'{\bf DFSZ}',fontsize=fs,rotation=trans_angle,color=line_color,ha='left',va='top',rotation_mode='anchor',clip_on=True)
        else:
            # QCD axion hadronic band
            m = array([1e-30,1e20])
            ga = 2e-10*m
            cols = cmap(linspace(0.1,0.45,nlevels))
            levels = (linspace(1,sqrt(level_max),nlevels))**2
            for i in range(nlevels-1):
                ax.fill_between(m,C_upper/levels[i],C_lower*levels[i],alpha=alpha,color=cols[i,:],zorder=-1000,lw=0)

            if DFSZ_on:
                if thick_lines:
                    plt.plot([m_min,m_max],[0.75,0.75],'-',lw=5,color=line_color)
                    plt.plot([m_min,m_max],[0.75,0.75],'-',lw=3,color=line_color)
                else:
                    plt.plot([m_min,m_max],[0.75,0.75],'-',lw=2,color=line_color)
                if text_on:
                    plt.text(DFSZ_label_mass,0.75/3,r'{\bf DFSZ II}',fontsize=fs,color=line_color,clip_on=True)

            if KSVZ_on:
                if thick_lines:
                    plt.plot([m_min,m_max],[1.92,1.92],'-',lw=5,color=line_color)
                    plt.plot([m_min,m_max],[1.92,1.92],'-',lw=3,color=line_color)
                else:
                    plt.plot([m_min,m_max],[1.92,1.92],'-',lw=2,color=line_color)
                if text_on:
                    plt.text(KSVZ_label_mass,0.75/3,r'{\bf KSVZ}',fontsize=fs,color=line_color,clip_on=True)
        return

    def ADMX(ax,col=[0.8, 0.0, 0.0],projection=False,fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1],zorder=0.1):
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        # 2018: arXiv[1804.05750]
        # 2019: arXiv[1910.08638]
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/ADMX.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        dat = loadtxt("limit_data/AxionPhoton/ADMX2018.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        dat = loadtxt("limit_data/AxionPhoton/ADMX2019_1.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        dat = loadtxt("limit_data/AxionPhoton/ADMX2019_2.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        dat = loadtxt("limit_data/AxionPhoton/ADMX2021.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        dat = loadtxt("limit_data/AxionPhoton/ADMX2024.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        dat = loadtxt("limit_data/AxionPhoton/ADMX2025.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        dat = loadtxt("limit_data/AxionPhoton/ADMX_Sidecar.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)


        if projection:
            # ADMX arXiv[1804.05750]
            dat = loadtxt("limit_data/AxionPhoton/Projections/ADMX_Projected.txt")
            plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
            plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.1)
            if text_on:
                if rs1==0:
                    plt.text(1e-5*text_shift[0],2.3e-16*text_shift[1],r'{\bf ADMX}',fontsize=20,color=col,rotation=0,ha='left',va='top',clip_on=True)
                    plt.plot([3e-5,2e-5],[3e-16,0.6e-15],'k-',lw=1.5)
                else:
                    plt.text(0.9e-6*text_shift[0],0.15*text_shift[1],r'{\bf ADMX}',fontsize=fs,color=col,rotation=0,ha='left',va='top',clip_on=True)
        else:
            if text_on:
                if rs1==0:
                    plt.text(0.85e-6*text_shift[0],1e-13*text_shift[1],r'{\bf ADMX}',fontsize=fs,color=col,rotation=90,ha='left',va='top',clip_on=True)
                else:
                    plt.gcf().text(0.39*text_shift[0],0.5*text_shift[1],r'{\bf ADMX}',rotation=90,color=col)
        return

    def RBF_UF(ax,col ='darkred',fs=13,RescaleByMass=False,text_on=True,text_shift=[1,1],zorder=0.1):
        # UF: Phys. Rev. D42, 1297 (1990).
        # RBF: Phys. Rev. Lett. 59, 839 (1987).
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/RBF.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        dat = loadtxt("limit_data/AxionPhoton/UF.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)


        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*0.37e-5,text_shift[1]*0.8e-11,r'{\bf RBF+UF}',fontsize=fs,color='w',rotation=-90,ha='left',va='top',clip_on=True)
            else:
                plt.text(text_shift[0]*0.7e-5,text_shift[1]*4e3,r'{\bf RBF}',fontsize=fs,color='w',rotation=0,ha='center',va='top',clip_on=True)
                plt.text(text_shift[0]*0.7e-5,text_shift[1]*1e3,r'{\bf UF}',fontsize=fs,color='w',rotation=0,ha='center',va='top',clip_on=True)

        return

    def HAYSTAC(ax,col=[0.88, 0.07, 0.37],fs=13,RescaleByMass=False,projection=True,text_on=True,text_shift=[1,1]):
        # HAYSTAC arXiv:[1803.03690] and [2008.01853]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 3
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = 0
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/HAYSTAC_PhaseI.txt")
        dat2 = loadtxt("limit_data/AxionPhoton/HAYSTAC_PhaseII_ab.txt")
        dat3 = loadtxt("limit_data/AxionPhoton/HAYSTAC_PhaseII_cd.txt")

        if rs1==0:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,zorder=zo,lw=2)
            plt.plot([dat2[0,0],dat2[0,0]],[dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),y2/(rs1*2e-10*dat2[0,0]+rs2)],color=col,zorder=zo,lw=2)
            plt.fill_between(dat3[:,0],dat3[:,1]/(rs1*2e-10*dat3[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zo)
            if text_on:
                if projection==False:
                    plt.text(text_shift[0]*2.1e-5,text_shift[0]*5e-13,r'{\bf HAYSTAC}',fontsize=fs,color=col,rotation=-90,ha='left',va='top',clip_on=True)
        else:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color='k',zorder=zo,lw=4)
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,zorder=zo,lw=3)
            plt.plot(dat[0,0],dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)

            plt.plot([dat2[0,0],dat2[0,0]],[dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),y2/(rs1*2e-10*dat2[0,0]+rs2)],color='k',zorder=zo,lw=4)
            plt.plot([dat2[0,0],dat2[0,0]],[dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),y2/(rs1*2e-10*dat2[0,0]+rs2)],color=col,zorder=zo,lw=3)
            plt.text(text_shift[0]*dat2[0,0]*1.1,text_shift[1]*y2*1.2,r'{\bf HAYSTAC}',fontsize=fs,color=col,rotation=40,ha='left',rotation_mode='anchor')
            plt.plot(dat2[0,0],dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)
        return

    def TASEH(ax,col=[0.88, 0.07, 0.24],fs=13,RescaleByMass=False,projection=True,text_on=True,text_shift=[1,1]):
        # TASEH https://arxiv.org/pdf/2205.05574.pdf
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 3
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = 0
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/TASEH.txt")

        if rs1==0:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,zorder=zo,lw=2)
        return

    def CASTCAPP(ax,col=[0.88, 0.07, 0.24],fs=13,RescaleByMass=False,projection=True,text_on=True,text_shift=[1,1]):
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 3
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = 0
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/CAST-CAPP.txt")

        if rs1==0:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,zorder=zo,lw=2)
        return

    def CAPP(ax,col=[1, 0.1, 0.37],fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 3
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = 0
        dat = loadtxt("limit_data/AxionPhoton/CAPP-1.txt")
        dat2 = loadtxt("limit_data/AxionPhoton/CAPP-2.txt")
        dat3 = loadtxt("limit_data/AxionPhoton/CAPP-3.txt")
        dat4 = loadtxt("limit_data/AxionPhoton/CAPP-4.txt")
        dat5 = loadtxt("limit_data/AxionPhoton/CAPP-5.txt")
        dat6 = loadtxt("limit_data/AxionPhoton/CAPP-6.txt")
        dat7 = loadtxt("limit_data/AxionPhoton/CAPP-7.txt")
        dat8 = loadtxt("limit_data/AxionPhoton/CAPP-8.txt")
        dat9 = loadtxt("limit_data/AxionPhoton/CAPP-9.txt")
        dat10 = loadtxt("limit_data/AxionPhoton/CAPP-MAX.txt")

        if rs1==0:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,zorder=zo,lw=3)
            plt.fill_between(dat2[:,0],dat2[:,1]/(rs1*2e-10*dat2[0,0]+rs2),y2=y2,color=col,zorder=zo)
            plt.fill_between(dat3[:,0],dat3[:,1]/(rs1*2e-10*dat3[0,0]+rs2),y2=y2,color=col,zorder=zo)
            plt.fill_between(dat4[:,0],dat4[:,1]/(rs1*2e-10*dat4[0,0]+rs2),y2=y2,color=col,zorder=zo)
            plt.fill_between(dat5[:,0],dat5[:,1]/(rs1*2e-10*dat5[0,0]+rs2),y2=y2,color=col,zorder=zo)
            plt.fill_between(dat6[:,0],dat6[:,1]/(rs1*2e-10*dat6[0,0]+rs2),y2=y2,color=col,zorder=zo)
            plt.fill_between(dat7[:,0],dat7[:,1]/(rs1*2e-10*dat7[0,0]+rs2),y2=y2,color=col,zorder=zo)
            plt.fill_between(dat8[:,0],dat8[:,1]/(rs1*2e-10*dat8[0,0]+rs2),y2=y2,color=col,zorder=zo)
            plt.fill_between(dat9[:,0],dat9[:,1]/(rs1*2e-10*dat9[0,0]+rs2),y2=y2,color=col,zorder=zo)
            plt.fill_between(dat10[:,0],dat10[:,1]/(rs1*2e-10*dat10[0,0]+rs2),y2=y2,color=col,zorder=zo)

            if text_on:
                plt.text(text_shift[0]*0.8e-5,text_shift[1]*0.1e-13,r'{\bf CAPP}',fontsize=fs,color=col,rotation=90,ha='center',va='top',clip_on=True)
        else:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color='k',zorder=zo,lw=4)
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,zorder=zo,lw=3)
            if text_on:
                plt.text(text_shift[0]*dat[0,0]*1.1,text_shift[1]*y2*1.8,r'{\bf CAPP}',fontsize=fs,color=col,rotation=40,ha='left',va='top',rotation_mode='anchor')
            plt.plot(dat[0,0],dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)
            imin = argmin(dat2[:,1])
            plt.plot(dat2[imin,0],dat2[imin,1]/(rs1*2e-10*dat2[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)
            imin = argmin(dat3[:,1])
            plt.plot(dat3[imin,0],dat3[imin,1]/(rs1*2e-10*dat3[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)
            plt.fill_between(dat2[:,0],dat2[:,1]/(rs1*2e-10*dat2[0,0]+rs2),y2=y2,color=col)
            plt.fill_between(dat3[:,0],dat3[:,1]/(rs1*2e-10*dat3[0,0]+rs2),y2=y2,color=col)
            plt.fill_between(dat4[:,0],dat4[:,1]/(rs1*2e-10*dat4[0,0]+rs2),y2=y2,color=col)
            plt.fill_between(dat5[:,0],dat5[:,1]/(rs1*2e-10*dat5[0,0]+rs2),y2=y2,color=col)
            plt.fill_between(dat6[:,0],dat6[:,1]/(rs1*2e-10*dat6[0,0]+rs2),y2=y2,color=col)
            plt.fill_between(dat7[:,0],dat7[:,1]/(rs1*2e-10*dat7[0,0]+rs2),y2=y2,color=col)
            plt.fill_between(dat8[:,0],dat8[:,1]/(rs1*2e-10*dat8[0,0]+rs2),y2=y2,color=col)
            plt.fill_between(dat9[:,0],dat9[:,1]/(rs1*2e-10*dat9[0,0]+rs2),y2=y2,color=col)
            plt.fill_between(dat10[:,0],dat10[:,1]/(rs1*2e-10*dat10[0,0]+rs2),y2=y2,color=col)

        return

    def QUAX(ax,col='crimson',fs=13,RescaleByMass=False,text_on=True,text_shift=[1,1],projection=False):
        # QUAX1 arXiv:[1903.06547]
        # QUAX2 arXiv:[2012.09498]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 3
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = -2
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/QUAX.txt")
        dat2 = loadtxt("limit_data/AxionPhoton/QUAX2.txt")
        dat3 = loadtxt("limit_data/AxionPhoton/QUAX4.txt")
        dat4 = loadtxt("limit_data/AxionPhoton/QUAX5.txt")

        if rs1==0:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=2,zorder=zo)
            plt.plot([dat2[0,0],dat2[0,0]],[dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),y2/(rs1*2e-10*dat2[0,0]+rs2)],color=col,lw=2,zorder=zo)
            plt.fill_between(dat3[:,0],dat3[:,1]/(rs1*2e-10*dat3[:,0]+rs2),y2=y2,color=col,lw=2,zorder=zo)
            plt.fill_between(dat4[:,0],dat4[:,1]/(rs1*2e-10*dat4[:,0]+rs2),y2=y2,color=col,lw=2,zorder=zo)

            if text_on:
                plt.text(text_shift[0]*6.3e-5,text_shift[1]*0.05e-11,r'{\bf QUAX}',fontsize=fs,color=col,rotation=-90,ha='center',va='top',clip_on=True)
        else:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color='k',lw=4,zorder=zo)
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=3,zorder=zo)
            plt.plot([dat2[0,0],dat2[0,0]],[dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),y2/(rs1*2e-10*dat2[0,0]+rs2)],color='k',lw=4,zorder=zo)
            plt.plot([dat2[0,0],dat2[0,0]],[dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),y2/(rs1*2e-10*dat2[0,0]+rs2)],color=col,lw=3,zorder=zo)
            plt.plot([dat3[0,0],dat3[0,0]],[dat3[0,1]/(rs1*2e-10*dat3[0,0]+rs2),y2/(rs1*2e-10*dat3[0,0]+rs2)],color='k',lw=4,zorder=zo)
            plt.plot([dat3[0,0],dat3[0,0]],[dat3[0,1]/(rs1*2e-10*dat3[0,0]+rs2),y2/(rs1*2e-10*dat3[0,0]+rs2)],color=col,lw=3,zorder=zo)
            if text_on:
                plt.text(text_shift[0]*dat2[0,0]*1.2,text_shift[1]*y2*1.2,r'{\bf QUAX}',fontsize=fs,color=col,rotation=40,ha='left',rotation_mode='anchor')
            plt.plot(dat[0,0],dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)
            plt.plot(dat2[0,0],dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)

        if projection==True:
            dat = loadtxt("limit_data/AxionPhoton/Projections/QUAX2005.txt")
            plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
            plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.2)
            if rs1==1.0:
                plt.text(2.5e-5,0.8e-1,r'{\bf QUAX}',color=col,fontsize=18)
                plt.plot([4.0e-5,4.0e-5],[2.2e-1,2.1e0],'k-',lw=1.5)
        return


    def LIDA(ax,text_on=True,text_label=r'{\bf LIDA}',col=[0.83, 0.07, 0.37],text_pos=[1e-9,0.5e-9],rotation=90,zorder=3.01,fs=13,lw=2,path_effects=line_background(1,'k'),text_col='w'):
        dat = loadtxt('limit_data/AxionPhoton/LIDA.txt')
        plt.plot(dat[:,0],dat[:,1],'-',zorder=zorder,color=col,lw=lw,path_effects=line_background(lw+1.5,'k'))
        if text_on:
            plt.text(text_pos[0],text_pos[1],text_label,fontsize=fs,rotation=rotation,color=text_col,path_effects=path_effects)
        return


    def ABRACADABRA(ax,col=[0.83, 0.07, 0.37],fs=15,projection=False,RescaleByMass=False,text_on=True,lw=1,text_shift=[1,1],edgealpha=1):
        # ABRACADABRA arXiv:[1810.12257]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/ABRACADABRA.txt")
        n = shape(dat)[0]
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=2)
        x = dat[arange(0,n,20),0]
        y = dat[arange(0,n,20),1]
        y[-1] = y2
        plt.plot(x,y/(rs1*2e-10*x+rs2),'k-',lw=lw,zorder=2.01,alpha=edgealpha)


        dat = loadtxt("limit_data/AxionPhoton/ABRACADABRA_run2.txt")
        n = shape(dat)[0]
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=2.02)
        x = dat[arange(0,n,1),0]
        y = dat[arange(0,n,1),1]
        y[-1] = y2
        plt.plot(x,y/(rs1*2e-10*x+rs2),'k-',lw=lw,zorder=2.02,alpha=edgealpha)


        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*1.5e-9,text_shift[1]*3e-8,r'{\bf ABRA}',fontsize=fs,color='w',rotation=0,ha='center',va='top',zorder=10,clip_on=True,path_effects=line_background(1.5,'k'))
                #plt.text(text_shift[0]*1.5e-9,text_shift[1]*1e-8,r'10 cm',fontsize=fs,color='w',rotation=0,ha='center',va='top',zorder=10,clip_on=True,path_effects=line_background(1.5,'k'))

        if projection:
            dat = loadtxt("limit_data/AxionPhoton/Projections/ABRACADABRA.txt")
            plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
            plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.1)
            if text_on:
                if rs1==0:
                    plt.text(text_shift[0]*5e-12,text_shift[1]*4e-18,r'{\bf ABRACADABRA}',fontsize=fs-1,color=col,rotation=13,ha='left',va='top',clip_on=True)
                else:
                    plt.text(text_shift[0]*1.3e-9,text_shift[1]*1.0e2,r'{\bf ABRACADABRA}',fontsize=fs-1,color=col,rotation=0,ha='left',va='top',clip_on=True)
                    plt.plot([dat[-1,0],dat[-1,0]],[dat[-1,1]/(rs1*2e-10*dat[-1,0]+rs2),1e6],lw=1.5,color=col,zorder=0)
        return

    def DMRadio(ax,col=[0.83, 0.07, 0.37],fs=23,text_on=True,RescaleByMass=False,lw=2,text_shift=[1,1],linestyle='-',rotation=90):
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt('limit_data/AxionPhoton/Projections/DMRadio.txt')
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),linestyle=linestyle,linewidth=2,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*2e-10,text_shift[1]*0.05e-16,r'{\bf DM-Radio}',color='crimson',fontsize=20,rotation=rotation,clip_on=True)
            else:
                plt.text(text_shift[0]*5e-9,text_shift[1]*4.0e-1,r'{\bf DM-Radio}',fontsize=fs-1,color=col,rotation=0,ha='left',va='top',clip_on=True)
        return


    def SRF(ax,col=[0.83, 0.07, 0.37],fs=20,text_on=True,RescaleByMass=False,lw=2,text_shift=[1,1],linestyle='-',rotation=-40):
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt('limit_data/AxionPhoton/Projections/SRF.txt')
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),linestyle=linestyle,linewidth=2,color=col,zorder=0.0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0.0,alpha=0.1)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*1.5e-11,text_shift[1]*0.7e-18,r'{\bf SRF-m$^3$}',color='crimson',fontsize=20,rotation=rotation,clip_on=True)
            else:
                plt.text(text_shift[0]*5e-9,text_shift[1]*4.0e-1,r'{\bf SRF-m$^3$}',fontsize=fs-1,color=col,rotation=0,ha='left',va='top',clip_on=True)
        return

    def WISPLC(ax,col=[0.8, 0.07, 0.37],fs=15,text_on=True,RescaleByMass=False,lw=2,text_shift=[1,1],linestyle='-',rotation=14):
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt('limit_data/AxionPhoton/Projections/WISPLC.txt')
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),linestyle=linestyle,linewidth=2,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*2e-11,text_shift[1]*8e-16,r'{\bf WISPLC}',color='crimson',fontsize=fs,rotation=rotation,clip_on=True)
            else:
                plt.text(text_shift[0]*1.5e-9,text_shift[1]*1.5e4,r'{\bf WISPLC}',fontsize=fs+1,color=col,rotation=-14,ha='left',va='top',clip_on=True)
        return

    def ORGAN(ax,col=[0.8, 0.0, 0.0],projection=False,fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1],lw=0.5):
        # ORGAN arXiv[1706.00209]
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 6
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = -2
        dat = loadtxt("limit_data/AxionPhoton/ORGAN.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=col,facecolor=col,zorder=zo,lw=1)

        dat2 = loadtxt("limit_data/AxionPhoton/ORGAN-1a.txt")
        plt.fill_between(dat2[:,0],dat2[:,1]/(rs1*2e-10*dat2[:,0]+rs2),y2=y2,edgecolor='k',facecolor=col,zorder=zo,lw=lw)

        dat2 = loadtxt("limit_data/AxionPhoton/ORGAN-1b.txt")
        plt.fill_between(dat2[:,0],dat2[:,1]/(rs1*2e-10*dat2[:,0]+rs2),y2=y2,edgecolor='k',facecolor=col,zorder=zo,lw=lw)

        dat2 = loadtxt("limit_data/AxionPhoton/ORGAN-Q.txt")
        plt.fill_between(dat2[:,0],dat2[:,1]/(rs1*2e-10*dat2[:,0]+rs2),y2=y2,edgecolor='k',facecolor=col,zorder=zo,lw=lw)

        if projection:
            dat = loadtxt("limit_data/AxionPhoton/Projections/ORGAN_Projected.txt")
            plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
            plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.2)
            if text_on:
                if rs1==0:
                    plt.text(text_shift[0]*5e-4,text_shift[1]*1.15e-15,r'{\bf ORGAN}',fontsize=18,color=col,rotation=0,ha='left',va='top',clip_on=True)
                    plt.plot([5e-4,1.5e-4],[1.3e-14,6e-13],'k-',lw=1.5)
                else:
                    plt.text(text_shift[0]*1.2e-4,text_shift[1]*1e3,r'{\bf ORGAN}',fontsize=18,color='darkred',rotation=-90,ha='left',va='top',clip_on=True)

        else:
            if RescaleByMass:
                plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color='k',lw=4,zorder=zo)
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=1,zorder=zo)
            if RescaleByMass:
                plt.plot(dat[0,0],dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)
            if text_on:
                if rs1==0:
                    plt.text(text_shift[0]*110e-6,text_shift[1]*1e-11,r'{\bf ORGAN}',fontsize=fs,color=col,rotation=-90,ha='left',va='top',clip_on=True)
                else:
                    plt.text(text_shift[0]*dat[0,0]*1.1,text_shift[1]*y2*1.2,r'{\bf ORGAN}',fontsize=fs-3,color=col,rotation=40,ha='left',rotation_mode='anchor')
                    plt.text(text_shift[0]*6e-5,text_shift[1]*1e2,r'{\bf ORGAN}',fontsize=fs-6,color=col,rotation=90,ha='left',rotation_mode='anchor')
        return

    def RADES(ax,col='blueviolet',fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        # RADES 2104.13798
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 6
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = 0
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/RADES.txt")
        dat2 = loadtxt("limit_data/AxionPhoton/RADES2.txt")

        if rs1==0:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=2,zorder=zo)
            plt.plot([dat2[0,0],dat2[0,0]],[dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),y2/(rs1*2e-10*dat2[0,0]+rs2)],color=col,lw=2,zorder=zo)
        else:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color='k',lw=4,zorder=zo)
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=3,zorder=zo)
            plt.plot([dat2[0,0],dat2[0,0]],[dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),y2/(rs1*2e-10*dat2[0,0]+rs2)],color=col,lw=3,zorder=zo)
            if text_on:
                plt.text(text_shift[0]*dat[0,0]*0.88,text_shift[1]*y2*1.2,r'{\bf RADES}',fontsize=fs,color=col,rotation=40,ha='left',rotation_mode='anchor')
            plt.plot(dat[0,0],dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)

        return

    def GrAHal(ax,col='#b53e5a',fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        # Grenoble haloscope  2110.14406
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 6
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = 0
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/GrAHal.txt")

        if rs1==0:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=2,zorder=zo)
        else:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color='k',lw=4,zorder=zo)
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=3,zorder=zo)
            if text_on:
                plt.text(text_shift[0]*dat[0,0]*0.88,text_shift[1]*y2*1.2,r'{\bf GrAHal}',fontsize=fs,color=col,rotation=40,ha='left',rotation_mode='anchor')
            plt.plot(dat[0,0],dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)

        return

    def MADMAX(ax,col='darkred',fs=18,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        # MADMAX arXiv[2003.10894]
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/MADMAX.txt")
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.2)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*1.5e-4,text_shift[1]*4.5e-15,r'{\bf MADMAX}',fontsize=18,color=col,rotation=0,ha='left',va='top',clip_on=True)
                plt.plot([3e-4,1.3e-4],[5.5e-15,2.6e-14],'k-',lw=1.5)
            else:
                plt.text(text_shift[0]*5e-5,text_shift[1]*3.5e0,r'{\bf MADMAX}',fontsize=14,color=col,rotation=0,ha='left',va='top',clip_on=True)

        return

    def DALI(ax,col='darkred',fs=18,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/DALI.txt")
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=2,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.2)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*1.0e-4,text_shift[1]*0.6e-15,r'{\bf DALI}',fontsize=18,color=col,rotation=0,ha='left',va='top',clip_on=True)
                plt.plot([0.9e-4,0.32e-4],[0.6e-15,0.4e-14],'k-',lw=1.5)
            else:
                plt.text(text_shift[0]*1.3e-4,text_shift[1]*6e-1,r'{\bf DALI}',fontsize=fs/1.3,color=col,rotation=20,ha='center',va='top',clip_on=True)
                #plt.text(2.3e-4,2e-1,r'{\bf haloscope}',fontsize=fs,color=col,rotation=0,ha='center',va='top')
        return

    def ALPHA(ax,col='darkred',fs=18,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        # Plasma Haloscope arXiv[1904.11872]
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/ALPHA.txt")
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=2,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.2)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*1.4e-4,text_shift[1]*1.6e-15,r'{\bf ALPHA}',fontsize=18,color=col,rotation=0,ha='left',va='top',clip_on=True)
                plt.plot([1.4e-4,0.6e-4],[1.6e-15,0.9e-14],'k-',lw=1.5)
            else:
                plt.text(text_shift[0]*2.3e-4,text_shift[1]*5e-1,r'{\bf ALPHA}',fontsize=fs,color=col,rotation=0,ha='center',va='top',clip_on=True)
                #plt.text(2.3e-4,2e-1,r'{\bf haloscope}',fontsize=fs,color=col,rotation=0,ha='center',va='top')
        return

    def FLASH(ax,col='darkred',fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        # FLASH https://indico.cern.ch/event/1115163/
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/FLASH.txt")
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,facecolor=col,zorder=0,alpha=0.3)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*2.5e-6,text_shift[1]*0.45e-16,r'{\bf FLASH}',fontsize=20,color=col,rotation=0,ha='left',va='top',clip_on=True)
                plt.plot([1.2e-6,2.5e-6],[5e-16,0.6e-16],'k-',lw=1.5)
            else:
                plt.text(text_shift[0]*3e-7,text_shift[1]*3e0,r'{\bf FLASH}',rotation=90,fontsize=fs,color=col,ha='left',va='top',rotation_mode='anchor',clip_on=True)
        return
    
    def BabyIAXO_RADES(ax,col='darkred',fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/BabyIAXO_RADES.txt")
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,facecolor=col,zorder=0,alpha=0.3)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*2.5e-6,text_shift[1]*0.45e-16,r'{\bf FLASH}',fontsize=20,color=col,rotation=0,ha='left',va='top',clip_on=True)
                plt.plot([1.2e-6,2.5e-6],[5e-16,0.6e-16],'k-',lw=1.5)
            else:
                plt.text(text_shift[0]*3e-7,text_shift[1]*3e0,r'{\bf FLASH}',rotation=90,fontsize=fs,color=col,ha='left',va='top',rotation_mode='anchor',clip_on=True)
        return

    def CADEx(ax,col='firebrick',fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/CADEx.txt")
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*1.1e-3,text_shift[1]*0.35e-13,r'{\bf CADEx}',fontsize=18,color=col,rotation=0,ha='left',va='top',clip_on=True)
                plt.plot([1.3e-3,0.4e-3],[0.45e-13,2e-12],'k-',lw=1.5)
            else:
                plt.text(text_shift[0]*5e-4,text_shift[1]*1e2,r'{\bf CADEx}',fontsize=fs,rotation=-90,color=col,clip_on=True)

        return

    def BRASS(ax,col='darkred',fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        # BRASS http://www.iexp.uni-hamburg.de/groups/astroparticle/brass/brassweb.htm
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/BRASS.txt")
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*2.4e-3,text_shift[1]*0.98e-13,r'{\bf BRASS}',fontsize=18,color=col,rotation=0,ha='left',va='top',clip_on=True)
                plt.plot([2.1e-3,0.7e-3],[0.95e-13,1.9e-12],'k-',lw=1.5)
            else:
                plt.text(text_shift[0]*0.45e-3,text_shift[1]*1e1,r'{\bf BRASS}',fontsize=20,rotation=9,color=col,clip_on=True)

        return

    def BREAD(ax,col='firebrick',fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/BREAD.txt")
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*7e-3,text_shift[1]*2.5e-13,r'{\bf BREAD}',fontsize=18,color=col,rotation=0,ha='left',va='top',clip_on=True)
                plt.plot([5.5e-3,3e-3],[1.9e-13,2.9e-13],'k-',lw=1.5)
            else:
                plt.text(text_shift[0]*2e-3,text_shift[1]*1e-1,r'{\bf BREAD}',fontsize=18,rotation=0,color=col,clip_on=True)

        return

    def TOORAD(ax,col=[0.8, 0.1, 0.2],fs=15,RescaleByMass=False,text_on=True,text_shift=[1,0.5]):
        # TOORAD arXiv[1807.08810]
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/TOORAD_2025.txt")
        dat[:,0] *= 1e-3
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*0.7e-2,text_shift[1]*3e-11,r'{\bf TOO}',fontsize=12,ha='center',color=col,clip_on=True)
                plt.text(text_shift[0]*0.7e-2,text_shift[1]*1.5e-11,r'{\bf RAD}',fontsize=12,ha='center',color=col,clip_on=True)
            else:
                #plt.text((1-0.05)*text_shift[0]*0.25e-2,(1+0.05)*text_shift[1]*0.3e2,r'{\bf TOORAD}',fontsize=18,rotation=-21,color='k',clip_on=True)
                plt.text(text_shift[0]*0.25e-2,text_shift[1]*0.3e2,r'{\bf TOORAD}',fontsize=18,rotation=-21,color=col,clip_on=True,path_effects=line_background(1,'k'))
        return

    def LAMPOST(ax,col=[0.8, 0.1, 0.2],fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1],rotation=55):
        # LAMPOST arXiv[1803.11455]
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/LAMPOST.txt",delimiter=',')
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*1.55e-1,text_shift[1]*3.5e-11,r'{\bf LAMPOST}',rotation=rotation,fontsize=fs,color=col,ha='left',va='top',clip_on=True)
            else:
                plt.text(text_shift[0]*0.9e-1,text_shift[1]*1.9e-1,r'{\bf LAMPOST}',rotation=0,fontsize=fs,color=col,ha='left',va='top',clip_on=True)

        return

    # Low mass ALP haloscopes
    def DANCE(ax,col=[0.8, 0.1, 0.2],fs=13,text_on=True,text_pos=[1.0e-12,3.7e-12],linestyle='-',rotation=50):
        # DANCE arXiv[1911.05196]
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/Projections/DANCE.txt")
        plt.plot(dat[:,0],dat[:,1],linestyle=linestyle,linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf DANCE}',rotation=rotation,fontsize=fs,color=col,ha='left',va='top',clip_on=True)
        return

    def aLIGO(ax,col=[0.8, 0.1, 0.2],fs=15,text_on=True,text_pos=[0.2e-9,0.35e-13],linestyle='-',rotation=0):
        # aLIGO arXiv[1903.02017]
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/Projections/aLIGO.txt")
        plt.plot(dat[:,0],dat[:,1],linestyle=linestyle,linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf aLIGO}',rotation=rotation,fontsize=fs,color=col,ha='left',va='top',clip_on=True)
        return

    def ADBC(ax,col=[0.8, 0.1, 0.2],fs=14,text_on=True,text_pos=[2e-11,0.6e-12],rotation=26):
        # ADBC arXiv[1809.01656]
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/Projections/ADBC.txt")
        plt.plot(dat[:,0],dat[:,1],'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf ADBC}',rotation=rotation,fontsize=fs,color=col,ha='left',va='top',clip_on=True)
        return
    
    def ADBC1(ax,col='red',fs=12,text_on=True,lw=1,text_pos=[0.3e-7,3e-8],rotation=90,zorder=0.8,edgealpha=1):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/ADBC.txt")
        n = shape(dat)[0]
        x = dat[arange(0,n,2),0]
        y = dat[arange(0,n,2),1]
        y[-1] = y2
        plt.plot(x,y,'k-',lw=lw,zorder=1.81,alpha=edgealpha)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf ADBC}',fontsize=fs,color='w',rotation=rotation,ha='center',va='top',clip_on=True,path_effects=line_background(1.5,'k'))
        return


    def SHAFT(ax,col='red',fs=16,text_on=True,lw=1,text_pos=[0.8e-10,3e-10],rotation=0,zorder=1.8,edgealpha=1):
        # SHAFT arXiv:[2003.03348]
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/SHAFT.txt")
        n = shape(dat)[0]
        x = dat[arange(0,n,2),0]
        y = dat[arange(0,n,2),1]
        y[-1] = y2
        plt.plot(x,y,'k-',lw=lw,zorder=1.81,alpha=edgealpha)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf SHAFT}',fontsize=fs,color='w',rotation=rotation,ha='center',va='top',clip_on=True,path_effects=line_background(1.5,'k'))
        return

    def UPLOAD(ax,col='tomato',fs=16,text_on=False):
        # UPLOAD arXiv:[1912.07751]
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/UPLOAD.txt")
        n = shape(dat)[0]
        x = dat[arange(0,n,2),0]
        y = dat[arange(0,n,2),1]
        y[-1] = y2
        plt.plot(x,y,'k-',lw=1,zorder=10,alpha=0.9)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=1.8)
        #if text_on:

        #    plt.text(0.8e-9,3e-8,r'{\bf UPLOAD}',fontsize=fs,color='w',rotation=-90,ha='center',va='top',zorder=9,clip_on=True)
        return


    def BASE(ax,col='crimson',fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1],zorder=1.9,lw=2.5,arrow_on=True):
        # BASE https://inspirehep.net/literature/1843024
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = zorder
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = zorder
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/BASE.txt")

        if arrow_on:
            fig = plt.gcf()
            plt.arrow(0.265, 0.535, 0, 0.035, transform=fig.transFigure,figure=fig,
              length_includes_head=True,lw=1,
              head_width=0.007, head_length=0.016, overhang=0.13,
              edgecolor='crimson',facecolor='crimson',clip_on=True)

        if rs1==0:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=lw,zorder=zo)
            if text_on:
                plt.text(text_shift[0]*3e-9,text_shift[1]*1.e-12,r'{\bf BASE}',fontsize=fs,color=col,rotation=90,ha='center',va='top',clip_on=True)
        else:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color='k',lw=lw+2,zorder=zo)
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=lw+1,zorder=zo)
            if text_on:
                plt.text(text_shift[0]*dat[0,0]*1.2,text_shift[1]*y2*1.2,r'{\bf BASE}',fontsize=fs,color=col,rotation=40,ha='left',rotation_mode='anchor')
            plt.plot(dat[0,0],dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)

        return

    def ADMX_SLIC(ax,col='crimson',fs=12,RescaleByMass=False,text_on=True,text_shift=[1,1],zorder=0.005):
        # ADMX SLIC https://arxiv.org/pdf/1911.05772.pdf
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = zorder
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = zorder
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/ADMX_SLIC.txt")
        x = mean(dat[:,0])
        y = amin(dat[:,1])
        if rs1==0:
            plt.plot([x,x],[y/(rs1*2e-10*x+rs2),y2/(rs1*2e-10*x+rs2)],color=col,lw=2,zorder=zorder)
            if text_on:
                plt.text(text_shift[0]*2.4e-7,text_shift[1]*0.2e-11,r'{\bf ADMX SLIC}',fontsize=fs,color=col,rotation=-90,ha='center',va='top',clip_on=True)
        else:
            plt.plot([x,x],[y/(rs1*2e-10*x+rs2),y2/(rs1*2e-10*x+rs2)],color='k',lw=4,zorder=zorder)
            plt.plot([x,x],[y/(rs1*2e-10*x+rs2),y2/(rs1*2e-10*x+rs2)],color=col,lw=3,zorder=zorder)
            if text_on:
                plt.text(text_shift[0]*x,text_shift[1]*y2*1.2,r'{\bf ADMX SLIC}',fontsize=fs,color=col,rotation=40,ha='left',rotation_mode='anchor')
            plt.plot(x,y/(rs1*2e-10*x+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zorder)

        return

    def ALPS(ax,projection=True,col=[0.8, 0.25, 0.33],fs=15,lw=1.5,RescaleByMass=False,text_on=True,lw_proj=1.5,lsty_proj='-',col_proj='k',text_shift_x=1,text_shift_y=1,block=True):
        # ALPS-I arXiv:[1004.1313]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0

        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/ALPS.txt")

        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=1.53,lw=0.01)
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'k-',lw=lw,zorder=1.53,alpha=1)
        if rs1==0:
            if text_on: plt.text(1e-5*text_shift_x,8e-8*text_shift_y,r'{\bf ALPS-I}',fontsize=20,color='w',clip_on=True,path_effects=line_background(1.5,'k'))
        if projection:
            dat = loadtxt("limit_data/AxionPhoton/Projections/ALPS-II.txt")
            if block:
                mask = dat[:,0]<0.85e-6
                dat[mask,0] = nan
            plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),linestyle=lsty_proj,lw=lw_proj,zorder=1.5,color=col_proj,alpha=0.5)
            if RescaleByMass:
                plt.text(9e-4*text_shift_x,2.5e3*text_shift_y,r'{\bf ALPS-II}',fontsize=20,color='k',rotation=20,alpha=0.5,clip_on=True)
            else:
                if text_on: plt.text(1.5e-3*text_shift_x,3e-9*text_shift_y,r'{\bf ALPS-II}',rotation=61,fontsize=18,color='w',zorder=10,clip_on=True,path_effects=line_background(1.5,'k'))
        return


    def Helioscopes(ax,col=[0.5, 0.0, 0.13],fs=25,projection=False,RescaleByMass=False,text_on=True):
        # CAST arXiv:[1705.02290]
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/CAST_highm.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor='k',facecolor=col,zorder=1.49,lw=0.1)
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'k-',lw=1.5,zorder=1.49,alpha=1)

        mf = dat[-3,0]
        gf = dat[-3,1]
        dat = loadtxt("limit_data/AxionPhoton/CAST.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor='none',facecolor=col,zorder=1.5,lw=0.1)
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'k-',lw=1.5,zorder=1.5,alpha=1)

        gi = 10.0**interp(log10(mf),log10(dat[:,0]),log10(dat[:,1]))/(rs1*2e-10*mf+rs2)
        plt.plot([mf,mf],[gf,gi],'k-',lw=1.5,zorder=1.5)
        if text_on==True:
            if rs1==0:
                plt.text(1e-1,1.5e-9,r'{\bf CAST}',fontsize=fs+4,color='w',rotation=0,ha='center',va='top',clip_on=True,path_effects=line_background(1.5,'k'))
            else:
                plt.text(4e-2,5e3,r'{\bf CAST}',fontsize=fs+4,color='w',rotation=0,ha='center',va='top',clip_on=True,path_effects=line_background(1.5,'k'))

        if projection:
            # IAXO arXiv[1212.4633]
            IAXO_col = 'purple'
            IAXO = loadtxt("limit_data/AxionPhoton/Projections/IAXO.txt")
            plt.plot(IAXO[:,0],IAXO[:,1]/(rs1*2e-10*IAXO[:,0]+rs2),'--',linewidth=2.5,color=IAXO_col,zorder=-1)
            plt.fill_between(IAXO[:,0],IAXO[:,1]/(rs1*2e-10*IAXO[:,0]+rs2),y2=y2,edgecolor=None,facecolor=IAXO_col,zorder=-1,alpha=0.3)
            if text_on==True:
                if rs1==0:
                    plt.text(0.5e-3,7.3e-12,r'{\bf IAXO}',fontsize=23,color='purple',rotation=0,clip_on=True)
                else:
                    plt.text(0.7e-2,0.12e1,r'{\bf IAXO}',fontsize=fs,color=IAXO_col,rotation=-18,clip_on=True)
        return

  
    import numpy as np

    def RedGiant(ax, text_label=r'\bf Red Giants', text_pos=[1e0, 5e-14], col='blue', text_col='b', fs=25, zorder=0.05, text_on=True, lw=1.5, edgealpha=1):
   
        y_limit = 2e-14

    
        x_min, x_max = ax.get_xlim()
    
        x_fill = np.linspace(x_min, x_max, 100)

        ax.fill_between(x_fill, y_limit, ax.get_ylim()[1], color=col, alpha=0.2, edgecolor='grey', zorder=zorder, linewidth=0)
        
        if text_on:
            ax.text(text_pos[0], text_pos[1], text_label, color=text_col, fontsize=fs, transform=ax.transData, ha='center', va='center', zorder=zorder+0.01)

        ax.plot([x_min, x_max], [y_limit, y_limit],
            color=col, lw=lw, alpha=edgealpha, zorder=zorder)

    def RadioPulsar(ax, rho=0.3, text_label=r'\bf Pulsars', text_pos=[5, 1e-8], col='red', text_col='r', fs=25, zorder=0.05, text_on=True, lw=1.5, edgealpha=1):

        x_min, x_max = ax.get_xlim()
        x = np.logspace(np.log10(x_min), np.log10(x_max), 300)
    
        y = (4e-9 * x) * np.sqrt(0.3 / rho)
    
   
        ax.fill_between(x, y, ax.get_ylim()[1], color=col, alpha=0.2, edgecolor='none', zorder=zorder, linewidth=0)
    
      
        ax.plot(x, y, color=col, lw=lw, alpha=edgealpha, zorder=zorder)
    
        if text_on:
            p1 = ax.transData.transform((x[0], y[0]))
            p2 = ax.transData.transform((x[-1], y[-1]))
            angle = np.degrees(np.arctan2(p2[1] - p1[1], p2[0] - p1[0]))
        
            y_text = max(text_pos[1], 1.15 * (4e-9 * text_pos[0]) * np.sqrt(0.3 / rho))
            ax.text(text_pos[0], y_text, text_label, color=text_col, fontsize=fs, ha='center', va='bottom', rotation=angle, rotation_mode='anchor', zorder=zorder + 0.01,)

    def ClusterMagneticFields(ax, text_label=r'\bf Cluster magnetic fields', text_pos=(5e4, 1e-18), col='grey', text_col='grey', fs=20, zorder=0.05,
        text_on=True, lw=1.5, edgealpha=1.0, alpha=0.2, prefactor=1e-14,):
        """
      
        """
        x_min, x_max = ax.get_xlim()
        x_vals = np.logspace(np.log10(x_min), np.log10(x_max), 300)
        y_vals = prefactor * 10e-9 * x_vals
        y_top = np.full_like(x_vals, ax.get_ylim()[1])
    
        ax.fill_between(x_vals, y_vals, y_top, color=col, alpha=alpha, edgecolor='none', linewidth=0, zorder=zorder,)
        ax.plot(x_vals, y_vals, color=col, lw=lw, alpha=edgealpha, zorder=zorder)
    
        if text_on:
            p1 = ax.transData.transform((x_vals[0], y_vals[0]))
            p2 = ax.transData.transform((x_vals[-1], y_vals[-1]))
            angle = np.degrees(np.arctan2(p2[1] - p1[1], p2[0] - p1[0]))
        
            y_text = max(text_pos[1], 1.15 * (prefactor * 10e-9 * text_pos[0]))
            ax.text(text_pos[0], y_text, text_label, color=text_col, fontsize=fs, ha='center', va='bottom', rotation=angle, rotation_mode='anchor', zorder=zorder + 0.01,)



    def ISMCoherentMagneticFields(ax, f_loc=1.0, text_label=r'\bf Large-Scale Coherent Magnetic Fields', text_pos=(5e3, 3e-19), col='dimgray', text_col='dimgray', fs=18, zorder=0.06, text_on=True, rotation = 45, lw=1.5, edgealpha=1.0, alpha=0.18, prefactor=3.5e-13, spinup_threshold=0.1, dashed_below_threshold=True,):

        x_min, x_max = ax.get_xlim()
        x_vals = np.logspace(np.log10(x_min), np.log10(x_max), 300)
    
        effective_fraction = max(f_loc, spinup_threshold)
        y_vals = prefactor * 10e-9 * x_vals / np.sqrt(effective_fraction)
    
        if f_loc >= spinup_threshold:
            y_top = np.full_like(x_vals, ax.get_ylim()[1])
            ax.fill_between(x_vals, y_vals, y_top, color=col, alpha=alpha, edgecolor='none', linewidth=0, zorder=zorder,)
            ax.plot(x_vals, y_vals, color=col, lw=lw, alpha=edgealpha, zorder=zorder)
            label = text_label
        else:
            if dashed_below_threshold:
                ax.plot(x_vals, y_vals, color=col, lw=lw, ls='--', alpha=edgealpha, zorder=zorder,)
            label = text_label + r' $({\rm spin\!-\!up\ regime})$'
    
        if text_on:
            p1 = ax.transData.transform((x_vals[0], y_vals[0]))
            p2 = ax.transData.transform((x_vals[-1], y_vals[-1]))
            angle = np.degrees(np.arctan2(p2[1] - p1[1], p2[0] - p1[0]))
        
            y_text = max(text_pos[1], 1.15 * (prefactor * 10e-9 * text_pos[0] / np.sqrt(effective_fraction)))
            ax.text(text_pos[0], y_text, label, color=text_col, fontsize=fs, ha='center', va='bottom', rotation=angle, rotation_mode='anchor', zorder=zorder + 0.01,)

    def Haloscopes(ax,projection=False,fs=20,text_on=True,BASE_arrow_on=True,Projection_color='crimson',alpha=0.1):


        if projection:
            AxionPhoton.ADMX(ax,fs=fs,text_on=False)
            AxionPhoton.HAYSTAC(ax,text_on=text_on)
            AxionPhoton.ABRACADABRA(ax,fs=fs,text_on=text_on)
            AxionPhoton.LIDA(ax,text_on=text_on)
            AxionPhoton.SHAFT(ax,text_on=text_on)
            AxionPhoton.ADBC1(ax,text_on=text_on)
            AxionPhoton.ORGAN(ax,text_on=False,lw=0)
            AxionPhoton.UPLOAD(ax,text_on=False)
            AxionPhoton.TASEH(ax,text_on=False)
            AxionPhoton.CASTCAPP(ax,text_on=False)
            AxionPhoton.CAPP(ax,fs=fs-4,text_on=False,col='darkred')
            AxionPhoton.RBF_UF(ax,fs=fs-2,text_on=False,col='darkred')
            AxionPhoton.ADMX(ax,text_on=False,col='darkred')
            AxionPhoton.CAPP(ax,text_on=False,col='darkred')
            AxionPhoton.ORGAN(ax,text_on=False,col='darkred',lw=0)
            AxionPhoton.HAYSTAC(ax,text_on=False,col='darkred')
            AxionPhoton.RBF_UF(ax,text_on=False,col='darkred')
            AxionPhoton.QUAX(ax,text_on=False,col='darkred')
            plt.text(0.5e-5,0.45e-12,r'{\bf Haloscopes}',color='w',rotation=90,fontsize=15)

            col = Projection_color
            dat = loadtxt("limit_data/AxionPhoton/Projections/HaloscopeProjections_Combined.txt")
            plt.fill_between(dat[:,0],dat[:,1],y2=1,lw=0,color=col,alpha=alpha,zorder=-10)
            plt.plot(dat[:,0],dat[:,1],'--',color=col,lw=1.5,zorder=-10)

            dat = loadtxt("limit_data/AxionPhoton/Projections/WISPLC.txt")
            plt.fill_between(dat[:,0],dat[:,1],y2=1,lw=0,color=col,alpha=alpha,zorder=-500)
            plt.plot(dat[:,0],dat[:,1],'--',color=col,lw=1.5,zorder=-500)

            dat = loadtxt("limit_data/AxionPhoton/Projections/ADBC.txt")
            plt.fill_between(dat[:,0],dat[:,1],y2=1,lw=0,color=col,alpha=alpha,zorder=-10)
            plt.plot(dat[:,0],dat[:,1],'--',color=col,lw=1.5,zorder=-10)

            dat = loadtxt("limit_data/AxionPhoton/Projections/DANCE.txt")
            plt.fill_between(dat[:,0],dat[:,1],y2=1,lw=0,color=col,alpha=alpha,zorder=-10)
            plt.plot(dat[:,0],dat[:,1],'--',color=col,lw=1.5,zorder=-10)

            dat = loadtxt("limit_data/AxionPhoton/Projections/aLIGO.txt")
            plt.fill_between(dat[:,0],dat[:,1],y2=1,lw=0,color=col,alpha=alpha,zorder=-10)
            plt.plot(dat[:,0],dat[:,1],'--',color=col,lw=1.5,zorder=-10)

            plt.text(1.8e-11,0.6e-12,r'{\bf ADBC}',rotation=26,fontsize=14,color=col,ha='left',va='top',clip_on=True)
            plt.text(0.2e-9,0.35e-13,r'{\bf aLIGO}',rotation=0,fontsize=15,color=col,ha='left',va='top',clip_on=True)
            plt.text(1.13e-12,6.2e-13,r'{\bf DANCE}',rotation=50,fontsize=11.5,color=col,ha='left',va='top',clip_on=True)
            plt.text(1.5e-11,0.7e-18,r'{\bf SRF-m$^3$}',color=col,fontsize=20,rotation=-40,clip_on=True)
            plt.text(2e-11,8e-16,r'{\bf WISPLC}',color=col,fontsize=15,rotation=14,clip_on=True)
            plt.text(3e-9,1.5e-19,r'{\bf DMRadio}',color=col,fontsize=18,rotation=46,clip_on=True)
            plt.text(2e-5,3.5e-16,r'{\bf QUAX}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(1e-5,1.5e-16,r'{\bf ADMX}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(0.5e-5,0.7e-16,r'{\bf BabyIAXO-RADES}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(0.3e-5,0.3e-16,r'{\bf FLASH}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(6e-5,9.5e-16,r'{\bf DALI}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(8e-5,2.0e-15,r'{\bf ALPHA}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(1.5e-4,4.3e-15,r'{\bf MADMAX}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(2.5e-4,8.3e-15,r'{\bf ORGAN}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(7.5e-4,5.0e-14,r'{\bf CADEx}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(5.5e-4,2.3e-14,r'{\bf EQC}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(1.4e-3,9.3e-14,r'{\bf BRASS}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(4.6e-3,3.9e-13,r'{\bf BREAD}',color=col,fontsize=15,rotation=56,clip_on=True)
            plt.text(4.2e-2,0.4e-12,r'{\bf LAMPOST}',rotation=0,fontsize=13,color=col,ha='left',va='top',clip_on=True)


        else:
            AxionPhoton.ADMX(ax,fs=fs,text_on=text_on)
            AxionPhoton.HAYSTAC(ax,text_on=text_on)
            AxionPhoton.ABRACADABRA(ax,fs=fs,text_on=text_on)
            AxionPhoton.LIDA(ax,text_on=text_on)
            AxionPhoton.SHAFT(ax,text_on=text_on)
            AxionPhoton.ADBC1(ax,text_on=text_on)
            AxionPhoton.ORGAN(ax,text_on=text_on,lw=0)
            AxionPhoton.UPLOAD(ax,text_on=text_on)
            AxionPhoton.TASEH(ax,text_on=False)
            AxionPhoton.CASTCAPP(ax,text_on=False)
            AxionPhoton.RBF_UF(ax,fs=fs-2,text_on=text_on)
            AxionPhoton.CAPP(ax,fs=fs-4,text_on=text_on)
            AxionPhoton.QUAX(ax,text_on=text_on)
            AxionPhoton.BASE(ax,text_on=text_on,arrow_on=BASE_arrow_on)
            AxionPhoton.ADMX_SLIC(ax,fs=fs-8,text_on=text_on)
            #AxionPhoton.RADES(ax,text_on=False)
            #AxionPhoton.GrAHal(ax,text_on=False)
        return


    def ORGAN_res(ax,col='purple',projection=False,fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1],lw=0.5):
        # ORGAN arXiv[1706.00209]
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 6
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = -2
        dat = loadtxt("limit_data/Rescale/ORGAN_rescaled.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=col,facecolor=col,zorder=zo,lw=1)

        dat2 = loadtxt("limit_data/Rescale/ORGAN-1a_rescaled.txt")
        plt.fill_between(dat2[:,0],dat2[:,1]/(rs1*2e-10*dat2[:,0]+rs2),y2=y2,edgecolor='k',facecolor=col,zorder=zo,lw=lw)

        dat2 = loadtxt("limit_data/Rescale/ORGAN-1b_rescaled.txt")
        plt.fill_between(dat2[:,0],dat2[:,1]/(rs1*2e-10*dat2[:,0]+rs2),y2=y2,edgecolor='k',facecolor=col,zorder=zo,lw=lw)


        if projection:
            dat = loadtxt("limit_data/Rescale/ORGAN_rescaled.txt")
            plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
            plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.2)
            if text_on:
                if rs1==0:
                    plt.text(text_shift[0]*5e-4,text_shift[1]*1.15e-15,r'{\bf ORGAN}',fontsize=18,color=col,rotation=0,ha='left',va='top',clip_on=True)
                    plt.plot([5e-4,1.5e-4],[1.3e-14,6e-13],'k-',lw=1.5)
                else:
                    plt.text(text_shift[0]*1.2e-4,text_shift[1]*1e3,r'{\bf ORGAN}',fontsize=18,color='darkred',rotation=-90,ha='left',va='top',clip_on=True)

        else:
            if RescaleByMass:
                plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color='k',lw=4,zorder=zo)
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=1,zorder=zo)
            if RescaleByMass:
                plt.plot(dat[0,0],dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)
            if text_on:
                if rs1==0:
                    plt.text(text_shift[0]*110e-6,text_shift[1]*1e-11,r'{\bf ORGAN}',fontsize=fs,color=col,rotation=-90,ha='left',va='top',clip_on=True)
                else:
                    plt.text(text_shift[0]*dat[0,0]*1.1,text_shift[1]*y2*1.2,r'{\bf ORGAN}',fontsize=fs-3,color=col,rotation=40,ha='left',rotation_mode='anchor')
                    plt.text(text_shift[0]*6e-5,text_shift[1]*1e2,r'{\bf ORGAN}',fontsize=fs-6,color=col,rotation=90,ha='left',rotation_mode='anchor')
        return


    def QUAX_res(ax, col="darkorange", fs=13, text_on=True, text_shift=(1.0, 1.0), data_dir="limit_data/Rescale",):
        y_top = ax.get_ylim()[1]
        files = [
            "QUAX_rescaled.txt",
            "QUAX2_rescaled.txt",
            "QUAX5_rescaled.txt",
        ]
    
        for filename in files:
            path = f"{data_dir}/{filename}"
    
            try:
                dat = np.loadtxt(path)
            except OSError:
                print(f"Skipping {path}: file not found")
                continue
    
            dat = np.atleast_2d(dat)
            x = dat[:, 0]
            y = dat[:, 1]
    
            if len(x) == 1:
                ax.plot([x[0], x[0]], [y[0], y_top], color=col, lw=2, zorder=-2)
                ax.plot(x[0], y[0], ".", markersize=10, color=col, zorder=-1)
            else:
                ax.fill_between(x, y, y2=y_top, color=col, alpha=0.25, zorder=-2)
                ax.plot(x, y, color=col, lw=2, zorder=-1)
    
        if text_on:
            ax.text(text_shift[0] * 5.0e-5, text_shift[1] * 0.50e-16, r"{\bf QUAX}", fontsize=fs, color=col, rotation=90, ha="center", va="top", clip_on=True,)
    
        return

    def CAPP_res(ax, col=[1, 0.1, 0.37], fs=15, RescaleByMass=False, text_on=True, text_shift=[1, 1]):
        
        y2 = ax.get_ylim()[1]
    
        if RescaleByMass:
            rs1, rs2, zo = 1.0, 0.0, 3
        else:
            rs1, rs2, zo = 0.0, 1.0, 0
    
        dat = loadtxt("limit_data/Rescale/CAPP-1_rescaled.txt")
        dat6 = loadtxt("limit_data/Rescale/CAPP-6_rescaled.txt")
        dat9 = loadtxt("limit_data/Rescale/CAPP-9_rescaled.txt")
        dat10 = loadtxt("limit_data/Rescale/CAPP-MAX_rescaled.txt")
    
        if rs1 == 0:
            plt.plot(
                [dat[0, 0], dat[0, 0]],
                [
                    dat[0, 1] / (rs1 * 2e-10 * dat[0, 0] + rs2),
                    y2 / (rs1 * 2e-10 * dat[0, 0] + rs2),
                ],
                color=col, zorder=zo, lw=3,)
    
            for dataset in (dat6, dat9, dat10):
                plt.fill_between(
                    dataset[:, 0],
                    dataset[:, 1] / (rs1 * 2e-10 * dataset[0, 0] + rs2),
                    y2=y2, color=col, zorder=zo,)
    
            if text_on:
                plt.text(
                    text_shift[0] * 5e-6,
                    text_shift[1] * 1e-19,
                    r'{\bf CAPP}',
                    fontsize=fs, color=col, rotation=90,
                    ha='center', va='top', clip_on=True,)
    
        else:
            denominator = rs1 * 2e-10 * dat[0, 0] + rs2
    
            plt.plot(
                [dat[0, 0], dat[0, 0]],
                [dat[0, 1] / denominator, y2 / denominator],
                color='k', zorder=zo, lw=4,)
            plt.plot(
                [dat[0, 0], dat[0, 0]],
                [dat[0, 1] / denominator, y2 / denominator],
                color=col, zorder=zo, lw=3,)
    
            if text_on:
                plt.text(
                    text_shift[0] * dat[0, 0] * 1.1,
                    text_shift[1] * y2 * 1.8,
                    r'{\bf CAPP}',
                    fontsize=fs, color=col, rotation=40,
                    ha='left', va='top', rotation_mode='anchor',)
    
            plt.plot(
                dat[0, 0],
                dat[0, 1] / denominator,
                '.',
                markersize=15, color=col,
                markeredgecolor='k', zorder=zo,)
    
            for dataset in (dat6, dat9, dat10):
                plt.fill_between(
                    dataset[:, 0],
                    dataset[:, 1] / (rs1 * 2e-10 * dataset[0, 0] + rs2),
                    y2=y2, color=col,)
        return


    def HAYSTAC_res(ax, col='deeppink', fs=13, RescaleByMass=False, projection=True, text_on=True, text_shift=[1, 1]):

        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 3
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = 0
    
        y2 = ax.get_ylim()[1]
    
        dat = loadtxt("limit_data/Rescale/HAYSTAC_PhaseI_rescaled.txt")
        dat2 = loadtxt("limit_data/Rescale/HAYSTAC_PhaseII_ab_rescaled.txt")
        dat3 = loadtxt("limit_data/Rescale/HAYSTAC_PhaseII_cd_rescaled.txt")

        if rs1 == 0:
            ax.plot(
                [dat[0, 0], dat[0, 0]],
                [dat[0, 1] / (rs1 * 2e-10 * dat[0, 0] + rs2), y2],
                color=col, zorder=zo, lw=2
            )
            ax.plot(
                [dat2[0, 0], dat2[0, 0]],
                [dat2[0, 1] / (rs1 * 2e-10 * dat2[0, 0] + rs2), y2],
                color=col, zorder=zo, lw=2
            )
            ax.fill_between(
                dat3[:, 0],
                dat3[:, 1] / (rs1 * 2e-10 * dat3[:, 0] + rs2),
                y2=y2,
                edgecolor=None,
                facecolor=col,
                zorder=zo
            )
    
            if text_on:
                ax.text(0.37 * text_shift[0], 0.25 * text_shift[1], r'{\bf HAYSTAC}', transform=ax.transAxes, fontsize=fs, color=col, rotation=90, ha='left', va='center', clip_on=False, zorder=100)
    
        else:
            denom = rs1 * 2e-10 * dat[0, 0] + rs2
            denom2 = rs1 * 2e-10 * dat2[0, 0] + rs2
    
            ax.plot([dat[0, 0], dat[0, 0]], [dat[0, 1] / denom, y2 / denom],
                    color='k', zorder=zo, lw=4)
            ax.plot([dat[0, 0], dat[0, 0]], [dat[0, 1] / denom, y2 / denom],
                    color=col, zorder=zo, lw=3)
            ax.plot(dat[0, 0], dat[0, 1] / denom, '.',
                    markersize=15, color=col, markeredgecolor='k', zorder=zo)
    
            ax.plot([dat2[0, 0], dat2[0, 0]], [dat2[0, 1] / denom2, y2 / denom2],
                    color='k', zorder=zo, lw=4)
            ax.plot([dat2[0, 0], dat2[0, 0]], [dat2[0, 1] / denom2, y2 / denom2],
                    color=col, zorder=zo, lw=3)
            ax.plot(dat2[0, 0], dat2[0, 1] / denom2, '.',
                    markersize=15, color=col, markeredgecolor='k', zorder=zo)
    
            if text_on:
                ax.text(0.85 * text_shift[0], 0.35 * text_shift[1], r'{\bf HAYSTAC}', transform=ax.transAxes, fontsize=fs, color=col, rotation=90, ha='left', va='center', clip_on=False, zorder=100)
    
        return


    def ADMX_res(ax, col='darkgreen', projection=False, fs=25,
             RescaleByMass=False, text_on=True,
             text_shift=[1, 1], zorder=0.1):
    
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
    
        y2 = ax.get_ylim()[1]
    
        files = [
            "ADMX_rescaled.txt",
            "ADMX2018_rescaled.txt",
            "ADMX2019_1_rescaled.txt",
            "ADMX2019_2_rescaled.txt",
            "ADMX2021_rescaled.txt",
            "ADMX2024_rescaled.txt",
            "ADMX2025_rescaled.txt",
            "ADMX_Sidecar_rescaled.txt",
        ]
    
        for fname in files:
            dat = loadtxt("limit_data/Rescale/" + fname)
            ax.fill_between(
                dat[:, 0],
                dat[:, 1] / (rs1 * 2e-10 * dat[:, 0] + rs2),
                y2=y2,
                edgecolor=None,
                facecolor=col,
                zorder=zorder
            )
    
        if text_on:
            ax.text(0.30 * text_shift[0], 0.42 * text_shift[1], r'{\bf ADMX}', transform=ax.transAxes, fontsize=fs, color=col, rotation=90, ha='left', va='center', clip_on=False, zorder=100)
            
            ax.text(0.35 * text_shift[0], 0.65 * text_shift[1], r'{\bf Sidecar}', transform=ax.transAxes, fontsize=18, color=col, rotation=90, ha='left', va='center', clip_on=False, zorder=100)
    
        return

    def CAPP_MAX_res(ax, col=[0.88, 0.07, 0.37], fs=13, RescaleByMass=False, projection=True, text_on=True, text_shift=[1, 1]):
            dat = loadtxt("limit_data/Rescale/CAPP-MAX_rescaled.txt")
            y2 = ax.get_ylim()[1]
            ax.fill_between(dat[:, 0], dat[:, 1], y2=y2, facecolor=col, zorder=0.1)
            
    
    def Haloscopes_res(ax,projection=False,fs=20,text_on=True,BASE_arrow_on=True,Projection_color='darkgreen',alpha=0.1):
        if projection:
            AxionPhoton.ADMX_res(ax,fs=fs,text_on=False)
            AxionPhoton.HAYSTAC_res(ax,text_on=False)
            AxionPhoton.ORGAN_res(ax,text_on=False,lw=0)
            AxionPhoton.UPLOAD_res(ax,text_on=False)
            AxionPhoton.CAPP_res(ax,fs=fs-4,text_on=False,col='darkred')
            AxionPhoton.ORGAN_res(ax,text_on=False,col='darkred',lw=0)
            AxionPhoton.QUAX_res(ax,text_on=False,col='darkred')
            plt.text(0.5e-5,0.45e-12,r'{\bf Haloscopes}',color='w',rotation=90,fontsize=15)

            col = Projection_color
            dat = loadtxt("limit_data/AxionPhoton/Projections/HaloscopeProjections_Combined.txt")
            plt.fill_between(dat[:,0],dat[:,1],y2=1,lw=0,color=col,alpha=alpha,zorder=-10)
            plt.plot(dat[:,0],dat[:,1],'--',color=col,lw=1.5,zorder=-10)

            dat = loadtxt("limit_data/AxionPhoton/Projections/WISPLC.txt")
            plt.fill_between(dat[:,0],dat[:,1],y2=1,lw=0,color=col,alpha=alpha,zorder=-500)
            plt.plot(dat[:,0],dat[:,1],'--',color=col,lw=1.5,zorder=-500)

            dat = loadtxt("limit_data/AxionPhoton/Projections/ADBC.txt")
            plt.fill_between(dat[:,0],dat[:,1],y2=1,lw=0,color=col,alpha=alpha,zorder=-10)
            plt.plot(dat[:,0],dat[:,1],'--',color=col,lw=1.5,zorder=-10)

            dat = loadtxt("limit_data/AxionPhoton/Projections/DANCE.txt")
            plt.fill_between(dat[:,0],dat[:,1],y2=1,lw=0,color=col,alpha=alpha,zorder=-10)
            plt.plot(dat[:,0],dat[:,1],'--',color=col,lw=1.5,zorder=-10)

            dat = loadtxt("limit_data/AxionPhoton/Projections/aLIGO.txt")
            plt.fill_between(dat[:,0],dat[:,1],y2=1,lw=0,color=col,alpha=alpha,zorder=-10)
            plt.plot(dat[:,0],dat[:,1],'--',color=col,lw=1.5,zorder=-10)

            plt.text(1.8e-11,0.6e-12,r'{\bf ADBC}',rotation=26,fontsize=14,color=col,ha='left',va='top',clip_on=True)
            plt.text(0.2e-9,0.35e-13,r'{\bf aLIGO}',rotation=0,fontsize=15,color=col,ha='left',va='top',clip_on=True)
            plt.text(1.13e-12,6.2e-13,r'{\bf DANCE}',rotation=50,fontsize=11.5,color=col,ha='left',va='top',clip_on=True)
            plt.text(1.5e-11,0.7e-18,r'{\bf SRF-m$^3$}',color=col,fontsize=20,rotation=-40,clip_on=True)
            plt.text(2e-11,8e-16,r'{\bf WISPLC}',color=col,fontsize=15,rotation=14,clip_on=True)
            plt.text(3e-9,1.5e-19,r'{\bf DMRadio}',color=col,fontsize=18,rotation=46,clip_on=True)
            plt.text(2e-5,3.5e-16,r'{\bf QUAX}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(1e-5,1.5e-16,r'{\bf ADMX}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(0.5e-5,0.7e-16,r'{\bf BabyIAXO-RADES}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(0.3e-5,0.3e-16,r'{\bf FLASH}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(6e-5,9.5e-16,r'{\bf DALI}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(8e-5,2.0e-15,r'{\bf ALPHA}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(1.5e-4,4.3e-15,r'{\bf MADMAX}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(2.5e-4,8.3e-15,r'{\bf ORGAN}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(7.5e-4,5.0e-14,r'{\bf CADEx}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(5.5e-4,2.3e-14,r'{\bf EQC}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(1.4e-3,9.3e-14,r'{\bf BRASS}',color=col,fontsize=15,rotation=0,clip_on=True)
            plt.text(4.6e-3,3.9e-13,r'{\bf BREAD}',color=col,fontsize=15,rotation=56,clip_on=True)
            plt.text(4.2e-2,0.4e-12,r'{\bf LAMPOST}',rotation=0,fontsize=13,color=col,ha='left',va='top',clip_on=True)


        else:
            AxionPhoton.ADMX_res(ax,fs=fs,text_on=text_on, col='darkgreen')
            AxionPhoton.HAYSTAC_res(ax,text_on=False)
            AxionPhoton.ABRACADABRA_res(ax,fs=fs,text_on=text_on)
            AxionPhoton.LIDA_res(ax,text_on=text_on)
            AxionPhoton.SHAFT_res(ax,text_on=text_on)
            AxionPhoton.ADBC_res(ax,text_on=text_on)
            AxionPhoton.ORGAN_res(ax,text_on=False,lw=0)
            AxionPhoton.UPLOAD_res(ax,text_on=False)
            AxionPhoton.TASEH_res(ax,text_on=False)
            AxionPhoton.CASTCAPP_res(ax,text_on=False)
            AxionPhoton.CAPP_res(ax,fs=fs-4,text_on=False,col='darkred')
            AxionPhoton.RBF_UF_res(ax,fs=fs-2,text_on=False,col='darkred')
            AxionPhoton.CAPP_res(ax,text_on=False,col='darkred')
            AxionPhoton.ORGAN_res(ax,text_on=False,col='darkred',lw=0)
            AxionPhoton.HAYSTAC_res(ax,text_on=False,col='darkred')
            AxionPhoton.RBF_UF_res(ax,text_on=False,col='darkred')
            AxionPhoton.QUAX_res(ax,text_on=False,col='darkred')
            plt.text(0.5e-5,0.45e-12,r'{\bf Haloscopes}',color='w',rotation=90,fontsize=15)

        return


    def GeomagneticDeflectionLowK(ax,m_min=None,m_max=None,n=300,delta_oplus=1.0,C_A=1.0,\
                              B_oplus_T=3.0e-5,R_oplus_m=6.371e6,v=1.0e-3,e_charge=0.303,\
                              edgecolor='dimgray',lw=2.0,edgealpha=1.0,zorder=5,\
                              label=r'Geomagnetic $kR_\oplus\ll1$',text_on=True,text_label=None,\
                              text_pos=None,ha='left',va='bottom',clip_on=True,fs=15,text_col=None,\
                              rotation=0,path_effects=None):
        T_to_eV2 = 195.0
        m_to_eVinverse = 5.0677e6
        B_oplus = B_oplus_T*T_to_eV2
        R_oplus = R_oplus_m*m_to_eVinverse
        m_transition = 1.0/(v*R_oplus)
    
        if m_min is None:
            m_min = ax.get_xlim()[0]
        if m_max is None:
            m_max = min(ax.get_xlim()[1],m_transition)
        else:
            m_max = min(m_max,m_transition)
        if m_min>=m_max:
            return None
    
        m_phi = logspace(log10(m_min),log10(m_max),n)
        eps_linear = delta_oplus/(4.0*pi*e_charge*v*m_phi*B_oplus*R_oplus**3)
        eps_quadratic = (1.0/(e_charge*B_oplus*R_oplus**2))*sqrt(delta_oplus/(pi*C_A))
        eps_oplus = minimum(eps_linear,eps_quadratic)
        line, = ax.plot(m_phi,eps_oplus,linestyle='--',color=edgecolor,lw=lw,\
                        alpha=edgealpha,zorder=zorder,label=label)
    
        if text_on:
            if text_label is None:
                text_label = label
            if text_col is None:
                text_col = edgecolor
            if text_pos is None:
                i = int(0.55*(n-1))
                text_pos = [m_phi[i],eps_oplus[i]]
            if path_effects is None:
                path_effects = line_background(3,'w')
            ax.text(text_pos[0],text_pos[1],text_label,fontsize=fs,color=text_col,\
                    ha=ha,va=va,clip_on=clip_on,rotation=rotation,rotation_mode='anchor',\
                    path_effects=path_effects,zorder=zorder+0.1)
        return line

    def GeomagneticDeflectionHighK(ax,m_min=None,m_max=None,n=300,delta_oplus=1.0,G_gt=1.0,\
                                   B_oplus_T=3.0e-5,R_oplus_m=6.371e6,v=1.0e-3,e_charge=0.303,\
                                   edgecolor='dimgray',lw=2.0,edgealpha=1.0,zorder=5,\
                                   label=r'Geomagnetic $kR_\oplus\gg1$',text_on=True,text_label=None,\
                                   text_pos=None,ha='left',va='bottom',clip_on=True,fs=15,text_col=None,\
                                   rotation=0,path_effects=None):
        T_to_eV2 = 195.0
        m_to_eVinverse = 5.0677e6
        B_oplus = B_oplus_T*T_to_eV2
        R_oplus = R_oplus_m*m_to_eVinverse
        m_transition = 1.0/(v*R_oplus)
    
        if m_min is None:
            m_min = max(ax.get_xlim()[0],m_transition)
        else:
            m_min = max(m_min,m_transition)
        if m_max is None:
            m_max = ax.get_xlim()[1]
        if m_min>=m_max:
            return None
    
        m_phi = logspace(log10(m_min),log10(m_max),n)
        eps_oplus = (delta_oplus/G_gt)*m_phi*v/(e_charge*B_oplus*R_oplus)
        line, = ax.plot(m_phi,eps_oplus,linestyle='--',color=edgecolor,lw=lw,\
                        alpha=edgealpha,zorder=zorder,label=label)
    
        if text_on:
            if text_label is None:
                text_label = label
            if text_col is None:
                text_col = edgecolor
            if text_pos is None:
                i = int(0.55*(n-1))
                text_pos = [m_phi[i],eps_oplus[i]]
            if path_effects is None:
                path_effects = line_background(3,'w')
            ax.text(text_pos[0],text_pos[1],text_label,fontsize=fs,color=text_col,\
                    ha=ha,va=va,clip_on=clip_on,rotation=rotation,rotation_mode='anchor',\
                    path_effects=path_effects,zorder=zorder+0.1)
        return line

#==============================================================================#



#==============================================================================#
def MySaveFig(fig,pltname,pngsave=True):
    fig.savefig(pltdir+pltname+'.pdf',bbox_inches='tight')
    if pngsave:
        fig.set_facecolor('w') # <- not sure what matplotlib fucked up in the new version but it seems impossible to set png files to be not transparent now
        fig.savefig(pltdir_png+pltname+'.png',bbox_inches='tight',transparent=False)

def cbar(mappable,extend='neither',minorticklength=8,majorticklength=10,\
            minortickwidth=2,majortickwidth=2.5,pad=0.2,side="right",orientation="vertical"):
    ax = mappable.axes
    fig = ax.figure
    divider = make_axes_locatable(ax)
    cax = divider.append_axes(side, size="5%", pad=pad)
    cbar = fig.colorbar(mappable, cax=cax,extend=extend,orientation=orientation)
    cbar.ax.tick_params(which='minor',length=minorticklength,width=minortickwidth)
    cbar.ax.tick_params(which='major',length=majorticklength,width=majortickwidth)
    cbar.solids.set_edgecolor("face")

    return cbar

def MySquarePlot(xlab='',ylab='',\
                 lw=2.5,lfs=45,tfs=25,size_x=13,size_y=12,Grid=False):
    plt.rcParams['axes.linewidth'] = lw
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=tfs)
    plt.rcParams.update({"text.usetex": True,"font.family": "serif","font.serif": ["Palatino"],})
    fig = plt.figure(figsize=(size_x,size_y))
    ax = fig.add_subplot(111)

    ax.set_xlabel(xlab,fontsize=lfs)
    ax.set_ylabel(ylab,fontsize=lfs)

    ax.tick_params(which='major',direction='in',width=2,length=13,right=True,top=True,pad=7)
    ax.tick_params(which='minor',direction='in',width=1,length=10,right=True,top=True)
    if Grid:
        ax.grid()
    return fig,ax

def MyDoublePlot(xlab1='',ylab1='',xlab2='',ylab2='',\
                 wspace=0.25,lw=2.5,lfs=45,tfs=25,size_x=20,size_y=11,Grid=False):
    plt.rcParams['axes.linewidth'] = lw
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=tfs)
    plt.rcParams.update({"text.usetex": True,"font.family": "serif","font.serif": ["Palatino"],})
    fig, axarr = plt.subplots(1, 2,figsize=(size_x,size_y))
    gs = gridspec.GridSpec(1, 2)
    gs.update(wspace=wspace)
    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1])
    ax1.tick_params(which='major',direction='in',width=2,length=13,right=True,top=True,pad=7)
    ax1.tick_params(which='minor',direction='in',width=1,length=10,right=True,top=True)
    ax2.tick_params(which='major',direction='in',width=2,length=13,right=True,top=True,pad=7)
    ax2.tick_params(which='minor',direction='in',width=1,length=10,right=True,top=True)

    ax1.set_xlabel(xlab1,fontsize=lfs)
    ax1.set_ylabel(ylab1,fontsize=lfs)

    ax2.set_xlabel(xlab2,fontsize=lfs)
    ax2.set_ylabel(ylab2,fontsize=lfs)

    if Grid:
        ax1.grid()
        ax2.grid()
    return fig,ax1,ax2


def MyDoublePlot_Vertical(xlab1='',ylab1='',xlab2='',ylab2='',\
                     hspace=0.05,lw=2.5,lfs=45,tfs=30,size_x=15,size_y=14,Grid=False,height_ratios=[2.5,1]):
    plt.rcParams['axes.linewidth'] = lw
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=tfs)
    plt.rcParams.update({"text.usetex": True,"font.family": "serif","font.serif": ["Palatino"],})


    fig, axarr = plt.subplots(2,1,figsize=(size_x,size_y))
    gs = gridspec.GridSpec(2, 1,height_ratios=height_ratios)
    gs.update(hspace=hspace)
    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1])

    ax1.tick_params(which='major',direction='in',width=2,length=13,right=False,top=True,pad=10)
    ax1.tick_params(which='minor',direction='in',width=1,length=10,right=False,top=True)

    ax2.tick_params(which='major',direction='in',width=2,length=13,right=False,top=True,pad=10)
    ax2.tick_params(which='minor',direction='in',width=1,length=10,right=False,top=True)

    ax1.set_xlabel(xlab1,fontsize=lfs)
    ax1.set_ylabel(ylab1,fontsize=lfs)

    ax2.set_xlabel(xlab2,fontsize=lfs)
    ax2.set_ylabel(ylab2,fontsize=lfs)


    if Grid:
        ax1.grid()
        ax2.grid()
    return fig,ax1,ax2



def MyTriplePlot(xlab1='',ylab1='',xlab2='',ylab2='',xlab3='',ylab3='',\
                 wspace=0.25,lw=2.5,lfs=45,tfs=25,size_x=20,size_y=7,Grid=False):
    plt.rcParams['axes.linewidth'] = lw
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=tfs)
    plt.rcParams.update({"text.usetex": True,"font.family": "serif","font.serif": ["Palatino"],})
    fig, axarr = plt.subplots(1, 3,figsize=(size_x,size_y))
    gs = gridspec.GridSpec(1, 3)
    gs.update(wspace=wspace)
    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1])
    ax3 = plt.subplot(gs[2])

    ax1.tick_params(which='major',direction='in',width=2,length=13,right=True,top=True,pad=7)
    ax1.tick_params(which='minor',direction='in',width=1,length=10,right=True,top=True)

    ax2.tick_params(which='major',direction='in',width=2,length=13,right=True,top=True,pad=7)
    ax2.tick_params(which='minor',direction='in',width=1,length=10,right=True,top=True)

    ax3.tick_params(which='major',direction='in',width=2,length=13,right=True,top=True,pad=7)
    ax3.tick_params(which='minor',direction='in',width=1,length=10,right=True,top=True)

    ax1.set_xlabel(xlab1,fontsize=lfs)
    ax1.set_ylabel(ylab1,fontsize=lfs)

    ax2.set_xlabel(xlab2,fontsize=lfs)
    ax2.set_ylabel(ylab2,fontsize=lfs)

    ax3.set_xlabel(xlab3,fontsize=lfs)
    ax3.set_ylabel(ylab3,fontsize=lfs)

    if Grid:
        ax1.grid()
        ax2.grid()
        ax3.grid()
    return fig,ax1,ax2,ax3
#==============================================================================#

#==============================================================================#
def reverse_colourmap(cmap, name = 'my_cmap_r'):
    reverse = []
    k = []

    for key in cmap._segmentdata:
        k.append(key)
        channel = cmap._segmentdata[key]
        data = []

        for t in channel:
            data.append((1-t[0],t[2],t[1]))
        reverse.append(sorted(data))

    LinearL = dict(zip(k,reverse))
    my_cmap_r = mpl.colors.LinearSegmentedColormap(name, LinearL)
    return my_cmap_r
#==============================================================================#




from matplotlib import patches
from matplotlib import text as mtext
import numpy as np
import math

class CurvedText(mtext.Text):
    """
    A text object that follows an arbitrary curve.
    """
    def __init__(self, x, y, text, axes, **kwargs):
        super(CurvedText, self).__init__(x[0],y[0],' ', **kwargs)

        axes.add_artist(self)

        ##saving the curve:
        self.__x = x
        self.__y = y
        self.__zorder = self.get_zorder()

        ##creating the text objects
        self.__Characters = []
        for c in text:
            if c == ' ':
                ##make this an invisible 'a':
                t = mtext.Text(0,0,'a')
                t.set_alpha(0.0)
            else:
                t = mtext.Text(0,0,c, **kwargs)

            #resetting unnecessary arguments
            t.set_ha('center')
            t.set_rotation(0)
            t.set_zorder(self.__zorder +1)

            self.__Characters.append((c,t))
            axes.add_artist(t)


    ##overloading some member functions, to assure correct functionality
    ##on update
    def set_zorder(self, zorder):
        super(CurvedText, self).set_zorder(zorder)
        self.__zorder = self.get_zorder()
        for c,t in self.__Characters:
            t.set_zorder(self.__zorder+1)

    def draw(self, renderer, *args, **kwargs):
        """
        Overload of the Text.draw() function. Do not do
        do any drawing, but update the positions and rotation
        angles of self.__Characters.
        """
        self.update_positions(renderer)

    def update_positions(self,renderer):
        """
        Update positions and rotations of the individual text elements.
        """

        #preparations

        ##determining the aspect ratio:
        ##from https://stackoverflow.com/a/42014041/2454357

        ##data limits
        xlim = self.axes.get_xlim()
        ylim = self.axes.get_ylim()
        ## Axis size on figure
        figW, figH = self.axes.get_figure().get_size_inches()
        ## Ratio of display units
        _, _, w, h = self.axes.get_position().bounds
        ##final aspect ratio
        aspect = ((figW * w)/(figH * h))*(ylim[1]-ylim[0])/(xlim[1]-xlim[0])

        #points of the curve in figure coordinates:
        x_fig,y_fig = (
            np.array(l) for l in zip(*self.axes.transData.transform([
            (i,j) for i,j in zip(self.__x,self.__y)
            ]))
        )

        #point distances in figure coordinates
        x_fig_dist = (x_fig[1:]-x_fig[:-1])
        y_fig_dist = (y_fig[1:]-y_fig[:-1])
        r_fig_dist = np.sqrt(x_fig_dist**2+y_fig_dist**2)

        #arc length in figure coordinates
        l_fig = np.insert(np.cumsum(r_fig_dist),0,0)

        #angles in figure coordinates
        rads = np.arctan2((y_fig[1:] - y_fig[:-1]),(x_fig[1:] - x_fig[:-1]))
        degs = np.rad2deg(rads)


        rel_pos = 10
        for c,t in self.__Characters:
            #finding the width of c:
            t.set_rotation(0)
            t.set_va('center')
            bbox1  = t.get_window_extent(renderer=renderer)
            w = bbox1.width
            h = bbox1.height

            #ignore all letters that don't fit:
            if rel_pos+w/2 > l_fig[-1]:
                t.set_alpha(0.0)
                rel_pos += w
                continue

            elif c != ' ':
                t.set_alpha(1.0)

            #finding the two data points between which the horizontal
            #center point of the character will be situated
            #left and right indices:
            il = np.where(rel_pos+w/2 >= l_fig)[0][-1]
            ir = np.where(rel_pos+w/2 <= l_fig)[0][0]

            #if we exactly hit a data point:
            if ir == il:
                ir += 1

            #how much of the letter width was needed to find il:
            used = l_fig[il]-rel_pos
            rel_pos = l_fig[il]

            #relative distance between il and ir where the center
            #of the character will be
            fraction = (w/2-used)/r_fig_dist[il]

            ##setting the character position in data coordinates:
            ##interpolate between the two points:
            x = self.__x[il]+fraction*(self.__x[ir]-self.__x[il])
            y = self.__y[il]+fraction*(self.__y[ir]-self.__y[il])

            #getting the offset when setting correct vertical alignment
            #in data coordinates
            t.set_va(self.get_va())
            bbox2  = t.get_window_extent(renderer=renderer)

            bbox1d = self.axes.transData.inverted().transform(bbox1)
            bbox2d = self.axes.transData.inverted().transform(bbox2)
            dr = np.array(bbox2d[0]-bbox1d[0])

            #the rotation/stretch matrix
            rad = rads[il]
            rot_mat = np.array([
                [math.cos(rad), math.sin(rad)*aspect],
                [-math.sin(rad)/aspect, math.cos(rad)]
            ])

            ##computing the offset vector of the rotated character
            drp = np.dot(dr,rot_mat)

            #setting final position and rotation:
            t.set_position(np.array([x,y])+drp)
            t.set_rotation(degs[il])

            t.set_va('center')
            t.set_ha('center')

            #updating rel_pos to right edge of character
            rel_pos += w-used
