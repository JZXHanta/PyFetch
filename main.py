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


class bcolors:
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
    username = os.getlogin()
    hostname = platform.node()
    return f"{username}@{hostname}"


def get_uptime():
    uptime = time.time() - psutil.boot_time()
    uptime_min_working = math.floor(uptime // 60)
    uptime_hours = math.floor(uptime_min_working // 60)
    uptime_min = uptime_min_working % 60
    return f"{uptime_hours} hours {uptime_min} minutes"


def real_windows_version(system, version):
    maj, _, min = version.split(".")
    if system == "Windows" and int(min) >= 22000:
        return "Windows 11"
    else:
        return "Windows 10"


def get_os():
    sys = platform.system()
    if sys == "Windows":
        ver = platform.version()
        return real_windows_version(sys, ver)
    else:
        return sys


def get_shell():
    shell , _ = shellingham.detect_shell()
    return shell


def get_resolution():
    pass


def get_terminal():
    pass


user_hostname = get_user_and_hostname()
plat_version = platform.version()
cpu = cpuinfo.get_cpu_info()['brand_raw']
cpu_freq = get_cpu_freq()
cpu_arch = cpuinfo.get_cpu_info()['arch_string_raw']
uptime = get_uptime()
op_sys = get_os()
shell = get_shell()


# TODO: Test to see if running all fetches before rendering feels faster than
#       fetching between lines (It doesn't really)
#       FOREACH??


def pyfetch():
    print("\n")
    for i in range(len(windows_logo_array)):
        if i == 0:
            # USERNAME@MACHINE
            print(
                f"{windows_logo_array[i]}{bcolors.WARNING} {user_hostname}{bcolors.ENDC}")

        elif i == 1:
            # SEPARATOR
            print(windows_logo_array[i],
                  f"{bcolors.OKCYAN}----------------------------------------{bcolors.ENDC}")

        elif i == 2:
            # OS
            print(windows_logo_array[i], f"  {bcolors.OKCYAN}{bcolors.BOLD}{bcolors.UNDERLINE}OS        :{bcolors.ENDC}",
                  op_sys)

        elif i == 3:
            # KERNEL
            print(
                windows_logo_array[i], f"  {bcolors.OKCYAN}{bcolors.BOLD}{bcolors.UNDERLINE}KERNEL    :{bcolors.ENDC}", plat_version)

        elif i == 4:
            # UPTIME
            print(
                windows_logo_array[i], f"  {bcolors.OKCYAN}{bcolors.BOLD}{bcolors.UNDERLINE}UPTIME    :{bcolors.ENDC}", uptime)

        elif i == 5:
            # SHELL
            print(windows_logo_array[i],
                  f"  {bcolors.OKCYAN}{bcolors.BOLD}{bcolors.UNDERLINE}SHELL     :{bcolors.ENDC}", shell)

        elif i == 6:
            # RESOLUTION
            print(windows_logo_array[i],
                  f"  {bcolors.OKCYAN}{bcolors.BOLD}{bcolors.UNDERLINE}RESOLUTION:{bcolors.ENDC}", "[insert resolution here]")

        elif i == 7:
            # TERMINAL
            print(windows_logo_array[i],
                  f"  {bcolors.OKCYAN}{bcolors.BOLD}{bcolors.UNDERLINE}TERMINAL  :{bcolors.ENDC}", "[insert terminal here]")

        elif i == 8:
            # CPU
            print(windows_logo_array[i], f"  {bcolors.OKCYAN}{bcolors.BOLD}{bcolors.UNDERLINE}CPU       :{bcolors.ENDC}",
                  f"{cpu}@{cpu_freq}")

        elif i == 9:
            # MEMORY
            print(
                windows_logo_array[i], f"  {bcolors.OKCYAN}{bcolors.BOLD}{bcolors.UNDERLINE}MEM       :{bcolors.ENDC}", vm_rounded, "GiB")

        elif i == 10:
            # DISK
            print(windows_logo_array[i], f"  {bcolors.OKCYAN}{bcolors.BOLD}{bcolors.UNDERLINE}DISK      :{bcolors.ENDC}",
                  "[insert disk data here]")

        elif i == 11:
            # ARCH
            print(
                windows_logo_array[i], f"  {bcolors.OKCYAN}{bcolors.BOLD}{bcolors.UNDERLINE}ARCH      :{bcolors.ENDC}", cpu_arch)

        else:
            print(windows_logo_array[i])


get_shell()
pyfetch()
