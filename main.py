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
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


vm_rounded = int(np.round(psutil.virtual_memory().total / 1024 ** 3))

# For future logos: logo is 40 characters wide

logo = windows.windows_logo_colorized
windows_logo_array = logo.split("\n")


def get_gpu():
    line_as_bytes = subprocess.check_output("nvidia-smi -L", shell=True)
    line = line_as_bytes.decode("ascii")
    _, line = line.split(":", 1)
    line, _ = line.split("(")
    return line.strip()


def get_cpu_freq():
    freq_string = cpuinfo.get_cpu_info()['hz_actual_friendly']
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
cpu = cpuinfo.get_cpu_info()['brand_raw']
cpu_freq = get_cpu_freq()
cpu_arch = cpuinfo.get_cpu_info()['arch_string_raw']
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

print(op_sys)

# TODO: Test to see if running all fetches before rendering feels faster than
#       fetching between lines (It doesn't really)
#       FOREACH??


logo = print_logo()


def pyfetch():
    print("\n")
    for i in range(len(windows_logo_array)):
        if i == 0:
            # USERNAME@MACHINE
            print(
                f"{windows_logo_array[i]}{Bcolors.WARNING} {user_hostname}{Bcolors.ENDC}")

        elif i == 1:
            # SEPARATOR
            print(windows_logo_array[i],
                  f"{Bcolors.OKCYAN}----------------------------------------{Bcolors.ENDC}")

        elif i == 2:
            # OS
            print(windows_logo_array[i], f"  {Bcolors.OKCYAN}{Bcolors.BOLD}{Bcolors.UNDERLINE}OS        :{Bcolors.ENDC}",
                  op_sys)

        elif i == 3:
            # KERNEL
            print(
                windows_logo_array[i], f"  {Bcolors.OKCYAN}{Bcolors.BOLD}{Bcolors.UNDERLINE}KERNEL    :{Bcolors.ENDC}", kernel)

        elif i == 4:
            # UPTIME
            print(
                windows_logo_array[i], f"  {Bcolors.OKCYAN}{Bcolors.BOLD}{Bcolors.UNDERLINE}UPTIME    :{Bcolors.ENDC}", uptime)

        elif i == 5:
            # SHELL
            print(windows_logo_array[i],
                  f"  {Bcolors.OKCYAN}{Bcolors.BOLD}{Bcolors.UNDERLINE}SHELL     :{Bcolors.ENDC}", shell)

        elif i == 6:
            # RESOLUTION
            print(windows_logo_array[i],
                  f"  {Bcolors.OKCYAN}{Bcolors.BOLD}{Bcolors.UNDERLINE}RESOLUTION:{Bcolors.ENDC}", resolution)

        elif i == 7:
            # TERMINAL
            print(windows_logo_array[i],
                  f"  {Bcolors.OKCYAN}{Bcolors.BOLD}{Bcolors.UNDERLINE}TERMINAL  :{Bcolors.ENDC}", term)

        elif i == 8:
            # CPU
            print(windows_logo_array[i], f"  {Bcolors.OKCYAN}{Bcolors.BOLD}{Bcolors.UNDERLINE}CPU       :{Bcolors.ENDC}",
                  f"{cpu}@{cpu_freq}")

        elif i == 9:
            # MEMORY
            print(
                windows_logo_array[i], f"  {Bcolors.OKCYAN}{Bcolors.BOLD}{Bcolors.UNDERLINE}MEM       :{Bcolors.ENDC}", vm_rounded, "GiB")

        elif i == 10:
            # DISK
            print(windows_logo_array[i], f"  {Bcolors.OKCYAN}{Bcolors.BOLD}{Bcolors.UNDERLINE}DISK      :{Bcolors.ENDC}",
                  "[insert disk data here]")

        elif i == 11:
            # ARCH
            print(
                windows_logo_array[i], f"  {Bcolors.OKCYAN}{Bcolors.BOLD}{Bcolors.UNDERLINE}ARCH      :{Bcolors.ENDC}", cpu_arch)

        else:
            print(windows_logo_array[i])


pyfetch()
