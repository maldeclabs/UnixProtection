#pragma once

#include "compiler/compiler_attribute.h"

/**
 * @struct SCANNER_CONFIG
 * @brief Configuration structure for the file telekinesis driver.
 */
typedef struct packed(8) TELEKINESIS_CONFIG
{
  const char *driver_path; /**< Path to the driver telekinesis. */
  const char *driver_name; /**< Name to the driver*/
}
TELEKINESIS_CONFIG;