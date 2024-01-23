import subprocess
import platform
import cpuinfo
import psutil
import numpy as np
import os
import shellingham
import time
import math
from screeninfo import get_monitors
import windows
import linux
import getpass
import distro


class Bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


vm_rounded = int(np.round(psutil.virtual_memory().total / 1024**3))


def get_gpu():
    line_as_bytes = subprocess.check_output("nvidia-smi -L", shell=True)
    line = line_as_bytes.decode("ascii")
    _, line = line.split(":", 1)
    line, _ = line.split("(")
    return line.strip()


def get_cpu_freq():
    freq_string = cpuinfo.get_cpu_info()["hz_actual_friendly"]
    num, unit = freq_string.split(" ")
    num = np.round(float(num), 1)
    return f"{num} {unit}"


def get_user_and_hostname():
    username = getpass.getuser()
    hostname = platform.node()
    return f"{username}@{hostname}"


def get_uptime():
    ut = time.time() - psutil.boot_time()
    uptime_min_working = math.floor(ut // 60)
    uptime_hours = math.floor(uptime_min_working // 60)
    uptime_min = uptime_min_working % 60
    return f"{uptime_hours} hours {uptime_min} minutes"


def real_windows_version(system, version):
    _, _, minor = version.split(".")
    if system == "Windows" and int(minor) >= 22000:
        return "Windows 11"
    else:
        return "Windows 10"


def get_os():
    sys = platform.system()
    if sys == "Windows":
        ver = platform.version()
        return real_windows_version(sys, ver), ver
    elif sys == "Linux":
        kernel = platform.release()
        dist = distro.name()
        ver = distro.version()
        d = f"{dist} {ver}"
        return d, kernel
    else:
        return sys


def get_shell():
    sh, _ = shellingham.detect_shell()
    return sh


def get_resolution():
    monitors = get_monitors()
    resolutions = []
    for i in range(len(monitors)):
        width = monitors[i].width
        height = monitors[i].height
        resolutions.append(f"{width}x{height}")

    return ", ".join(resolutions)


def get_terminal():
    return os.environ["TERM"]


user_hostname = get_user_and_hostname()
cpu = cpuinfo.get_cpu_info()["brand_raw"]
cpu_freq = get_cpu_freq()
cpu_arch = cpuinfo.get_cpu_info()["arch_string_raw"]
uptime = get_uptime()
op_sys, kernel = get_os()
shell = get_shell()
term = get_terminal()
resolution = get_resolution()


def print_logo():
    if op_sys.split(" ")[0] == "Ubuntu":
        return linux.ubuntu_logo_color
    elif op_sys.split(" ")[0] == "Windows":
        return windows.windows_logo_colorized
    elif op_sys.split(" ")[0] == "Pop!_OS":
        return linux.pop_os_logo_colored
    else:
        return linux.error_logo_colored


logo = print_logo()
logo_array = logo.split("\n")


def pyfetch():
    print("\n")
    info_labels = [
        "OS        ",
        "KERNEL    ",
        "UPTIME    ",
        "SHELL     ",
        "RESOLUTION",
        "TERMINAL  ",
        "CPU       ",
        "MEM       ",
        "DISK      ",
        "ARCH      ",
    ]
    info_data = [
        op_sys,
        kernel,
        uptime,
        shell,
        resolution,
        term,
        f"{cpu}@{cpu_freq}",
        f"{vm_rounded} GiB",
        "[insert disk data here]",
        cpu_arch,
    ]
    for i, line in enumerate(logo_array):
        if i == 0:
            print(f"{line}{Bcolors.WARNING} {user_hostname}{Bcolors.ENDC}")
        elif i == 1:
            print(
                line,
                f"{Bcolors.OKCYAN}----------------------------------------{Bcolors.ENDC}",
            )
        elif 2 <= i <= 11:
            label = info_labels[i - 2]
            data = info_data[i - 2]
            print(
                f"{line}  {Bcolors.OKCYAN}{Bcolors.BOLD}{Bcolors.UNDERLINE}{label}:{Bcolors.ENDC} {data}"
            )
        else:
            print(line)


pyfetch()
