#include "logger/logger.h"
#include "err/err.h"
#include <stdlib.h>

int init_logger(LOGGER **logger, LOGGER_CONFIG logger_config)
{
    *logger = malloc(sizeof(struct LOGGER));

    ALLOC_ERR(*logger);

    (*logger)->config = logger_config;

    logger_initConsoleLogger(stdout);
    logger_setLevel((LogLevel)(*logger)->config.level);
    return (logger_initFileLogger((*logger)->config.filename,
                                  (*logger)->config.max_file_size,
                                  (*logger)->config.max_backup_files) == 0)
               ? ERROR
               : SUCCESS;
}

void exit_logger(LOGGER **logger)
{
    logger_exitFileLogger();
    free(*logger);
    NO_USE_AFTER_FREE(*logger);
}