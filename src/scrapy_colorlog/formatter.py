import colorlog
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from typing_extensions import Self

DEFAULT_FORMAT = (
    "%(light_black)s%(asctime)s%(reset)s "
    "%(light_black)s[%(name)s]%(reset)s "
    "%(log_color)s%(levelname)s%(reset)s%(light_black)s:%(reset)s "
    "%(message)s"
)

DEFAULT_DATEFORMAT = "%Y-%m-%d %H:%M:%S"

DEFAULT_COLORS = {
    "DEBUG": "blue",
    "INFO": "cyan",
    "WARNING": "yellow",
    "ERROR": "red",
    "CRITICAL": "purple",
}


class ColoredFormatter(colorlog.ColoredFormatter):
    @classmethod
    def from_crawler(cls, crawler: Crawler) -> Self:
        return cls.from_settings(crawler.settings)

    @classmethod
    def from_settings(cls, settings: Settings) -> Self:
        return cls(
            fmt=settings.get("COLORLOG_FORMAT", DEFAULT_FORMAT),
            datefmt=settings.get("COLORLOG_DATEFORMAT", DEFAULT_DATEFORMAT),
            log_colors=settings.getdict("COLORLOG_COLORS", DEFAULT_COLORS),
            secondary_log_colors=settings.getdict("COLORLOG_SECONDARY_COLORS"),
            reset=settings.getbool("COLORLOG_RESET", True),
            no_color=settings.getbool("COLORLOG_NO_COLOR", False),
            force_color=settings.getbool("COLORLOG_FORCE_COLOR", False),
        )
