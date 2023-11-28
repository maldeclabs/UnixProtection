#pragma once

#include <uthash.h>

struct skip_dirs {
    char *dir;
    UT_hash_handle hh;
};

void add_skip_dirs(struct skip_dirs **skip, const char *path[], size_t n);
void del_skip_dirs(struct skip_dirs **skip);
struct skip_dirs* get_skipped(struct skip_dirs *skip, const char *path);