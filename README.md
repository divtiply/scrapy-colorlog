# scrapy-colorlog

Color log output support for [Scrapy][1].

## Installation

```sh
pip install scrapy-colorlog
```

## Configuration

Add the following to your Scrapy project settings module:

```python
import scrapy_colorlog

scrapy_colorlog.install()
```

## Settings

### COLORLOG_FORMAT

Default:

```python
(
    "%(light_black)s%(asctime)s%(reset)s "
    "%(light_black)s[%(name)s]%(reset)s "
    "%(log_color)s%(levelname)s%(reset)s%(light_black)s:%(reset)s "
    "%(message)s"
)
```

String for formatting log messages. Refer to the [colorlog][2] package
documentation for available escape codes and parameters to the format string.

See also:
[LOG_FORMAT](https://docs.scrapy.org/en/latest/topics/settings.html#log-format).

### COLORLOG_DATEFORMAT

Default: `"%Y-%m-%d %H:%M:%S"`

String for formatting date/time, expansion of the `%(asctime)s` placeholder in
[COLORLOG_FORMAT](#colorlog_format).

See also:
[LOG_DATEFORMAT](https://docs.scrapy.org/en/latest/topics/settings.html#log-dateformat).

### COLORLOG_COLORS

Default:

```python
{
    "DEBUG": "blue",
    "INFO": "cyan",
    "WARNING": "yellow",
    "ERROR": "red",
    "CRITICAL": "purple",
}
```

A mapping of record level names to color names. Refer to the [colorlog][2]
package documentation for details.

### COLORLOG_SECONDARY_COLORS

Default: `None`

A mapping of names to log_colors style mappings, defining additional colors that
can be used in format strings. Refer to the [colorlog][2] package documentation
for details.

### COLORLOG_RESET

Default: `True`

Implicitly adds a color reset code to the message output, unless the output
already ends with one.

### COLORLOG_NO_COLOR

Default: `False`

Disable color output.

See also: [NO_COLOR](#no_color) environment variable.

### COLORLOG_FORCE_COLOR

Default: `False`

Enable color output. Takes precedence over
[COLORLOG_NO_COLOR](#colorlog_no_color).

See also: [FORCE_COLOR](#force_color) environment variable.

## Environment variables

### NO_COLOR

Disable color output. See [NO_COLOR][3] for details.

### FORCE_COLOR

Enable color output. Takes precedence over [NO_COLOR](#no_color).

[1]: https://github.com/scrapy/scrapy
[2]: https://github.com/borntyping/python-colorlog
[3]: https://no-color.org/
