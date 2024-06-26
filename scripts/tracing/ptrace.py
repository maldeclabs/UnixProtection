from regs import *
import ctypes
import os
from syscall_table import *

PTRACE_GETREGS = 12
PTRACE_SYSCALL = 24
PTRACE_ATTACH = 16
PTRACE_DETACH = 17
PTRACE_SETOPTIONS = 0x4200
PTRACE_O_TRACEFORK = 0x00000002
PTRACE_O_TRACECLONE = 0x00000008
PTRACE_O_TRACEVFORK = 0x00000004

def ptrace_syscalls(pid, syscalls_list):
    libc = ctypes.CDLL('libc.so.6')
    ptrace = libc.ptrace
    ptrace.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
    ptrace.restype = ctypes.c_long

    if ptrace(PTRACE_ATTACH, pid, 0, 0) < 0:
        print("Error in ptrace PTRACE_ATTACH")
        return -1
    
    status = ctypes.c_int(0)
    libc.waitpid(pid, ctypes.byref(status), 0)
    
    regs = user_regs_struct()

    while os.WIFSTOPPED(status.value):
        libc.ptrace(PTRACE_GETREGS, pid, 0, ctypes.byref(regs))

        syscall_name = syscall_table.get(regs.orig_rax)
        if syscall_name is not None:
            syscalls_list.append(syscall_name)
                
        libc.ptrace(PTRACE_SYSCALL, pid, 0, 0)
        libc.waitpid(pid, ctypes.byref(status), 0)

    libc.ptrace(PTRACE_DETACH, pid, 0, 0)
    print("Detached from process")