from __future__ import annotations

import logging

import scrapy.utils.log
from scrapy.settings import Settings
from scrapy.utils.log import get_scrapy_root_handler

from .formatter import ColoredFormatter


def install() -> None:
    from scrapy import crawler

    crawler.configure_logging = configure_logging
    crawler.install_scrapy_root_handler = install_scrapy_root_handler


def configure_logging(
    settings: Settings | dict | None = None, install_root_handler: bool = True
) -> None:
    if isinstance(settings, dict) or settings is None:
        settings = Settings(settings)
    scrapy.utils.log.configure_logging(settings, install_root_handler)
    replace_scrapy_root_handler_formatter(settings)


def install_scrapy_root_handler(settings: Settings) -> None:
    scrapy.utils.log.install_scrapy_root_handler(settings)
    replace_scrapy_root_handler_formatter(settings)


def replace_scrapy_root_handler_formatter(settings: Settings) -> None:
    handler = get_scrapy_root_handler()
    if (
        handler
        and isinstance(handler, logging.StreamHandler)
        and not isinstance(handler.formatter, ColoredFormatter)
    ):
        formatter = ColoredFormatter.from_settings(settings)
        formatter.stream = handler.stream
        handler.setFormatter(formatter)
