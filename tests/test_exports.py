"""测试模块导出"""
import importlib


def test_bsh_module_imports():
    """测试可以导入 bsh 主模块"""
    import bsh

    assert hasattr(bsh, "__version__")
    assert bsh.__version__ == "0.0.2"


def test_bsh_all_exports():
    """测试 bsh.__all__ 包含所有导出"""
    import bsh

    expected_all = {
        "__version__",
        "ProductModel",
        "Settings",
        "ApiClient",
        "Parser",
        "BaseRepository",
        "CsvRepository",
        "RepositoryFactory",
        "YieldCalculator",
    }

    assert set(bsh.__all__) == expected_all


def test_bsh_exports_accessible():
    """测试所有导出的成员可以访问"""
    import bsh

    for name in bsh.__all__:
        assert hasattr(bsh, name), f"bsh.{name} not found"


def test_models_module_imports():
    """测试可以导入 models 模块"""
    from bsh.models import ProductModel

    assert ProductModel is not None


def test_models_all_exports():
    """测试 models.__all__ 包含 ProductModel"""
    import bsh.models

    assert bsh.models.__all__ == ["ProductModel"]


def test_config_module_imports():
    """测试可以导入 config 模块"""
    from bsh.config import Settings

    assert Settings is not None


def test_config_all_exports():
    """测试 config.__all__ 包含 Settings"""
    import bsh.config

    assert bsh.config.__all__ == ["Settings"]


def test_scraper_module_imports():
    """测试可以导入 scraper 模块"""
    from bsh.scraper import ApiClient, Parser

    assert ApiClient is not None
    assert Parser is not None


def test_scraper_all_exports():
    """测试 scraper.__all__ 包含 ApiClient 和 Parser"""
    import bsh.scraper

    assert set(bsh.scraper.__all__) == {"ApiClient", "Parser"}


def test_repository_module_imports():
    """测试可以导入 repository 模块"""
    from bsh.repository import BaseRepository, CsvRepository, RepositoryFactory

    assert BaseRepository is not None
    assert CsvRepository is not None
    assert RepositoryFactory is not None


def test_repository_all_exports():
    """测试 repository.__all__ 包含所有导出"""
    import bsh.repository

    expected = {"BaseRepository", "CsvRepository", "RepositoryFactory"}
    assert set(bsh.repository.__all__) == expected


def test_calculator_module_imports():
    """测试可以导入 calculator 模块"""
    from bsh.calculator import YieldCalculator

    assert YieldCalculator is not None


def test_calculator_all_exports():
    """测试 calculator.__all__ 包含 YieldCalculator"""
    import bsh.calculator

    assert bsh.calculator.__all__ == ["YieldCalculator"]
