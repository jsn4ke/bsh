# BSH - 上海银行理财数据爬取

爬取上海银行理财页面数据，提取产品信息并计算各种年化收益率。

## 功能特性

- 爬取上海银行理财产品数据
- 提取产品基本信息（名称、收益率、风险等级等）
- 计算年化收益率（净值转年化）
- 数据存储为 CSV（支持扩展其他存储方式）

## 安装

### 创建虚拟环境

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

```bash
python src/main.py
```

数据将保存到 `data/products.csv`。

## 项目结构

```
bsh/
├── src/
│   ├── config/          # 配置管理
│   ├── models/          # Pydantic 数据模型
│   ├── repository/      # 数据存储抽象层
│   ├── scraper/         # API 客户端和解析
│   ├── calculator/      # 年化计算
│   └── main.py          # 主入口
├── tests/               # 测试
├── data/                # 数据存储
├── doc/                 # 文档和计划
└── pyproject.toml       # 项目配置
```

## 开发

### 运行测试

```bash
pytest
```

### 代码格式化

```bash
ruff format .
ruff check .
```

### 类型检查

```bash
mypy src/
```

## 版本

当前版本: 0.0.1

详见 [doc/v0.0.1-plan.md](doc/v0.0.1-plan.md)

## License

MIT
