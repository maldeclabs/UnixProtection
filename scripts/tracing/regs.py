from ctypes import Structure, c_ulong

class user_regs_struct(Structure):
    _fields_ = [
        ("r15", c_ulong),
        ("r14", c_ulong),
        ("r13", c_ulong),
        ("r12", c_ulong),
        ("rbp", c_ulong),
        ("rbx", c_ulong),
        ("r11", c_ulong),
        ("r10", c_ulong),
        ("r9", c_ulong),
        ("r8", c_ulong),
        ("rax", c_ulong),
        ("rcx", c_ulong),
        ("rdx", c_ulong),
        ("rsi", c_ulong),
        ("rdi", c_ulong),
        ("orig_rax", c_ulong),
        ("rip", c_ulong),
        ("cs", c_ulong),
        ("eflags", c_ulong),
        ("rsp", c_ulong),
        ("ss", c_ulong),
        ("fs_base", c_ulong),
        ("gs_base", c_ulong),
        ("ds", c_ulong),
        ("es", c_ulong),
        ("fs", c_ulong),
        ("gs", c_ulong),
    ]