"""BSH - 上海银行理财数据爬取库"""

__version__ = "0.0.2"

from bsh.models import ProductModel
from bsh.config import Settings
from bsh.scraper import ApiClient, Parser
from bsh.repository import BaseRepository, CsvRepository, RepositoryFactory
from bsh.calculator import YieldCalculator

__all__ = [
    "__version__",
    "ProductModel",
    "Settings",
    "ApiClient",
    "Parser",
    "BaseRepository",
    "CsvRepository",
    "RepositoryFactory",
    "YieldCalculator",
]
