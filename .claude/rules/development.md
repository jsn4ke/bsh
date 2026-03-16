# BSH 项目开发规则

## 项目概述
- **项目类型**: Python 项目
- **项目名称**: BSH (上海银行理财数据爬取)
- **当前版本**: 0.0.1

## 强制开发流程

### 每个功能开发周期（必须严格执行）

```
1. [Planning]  制定小功能点实现计划
2. [Branch]    创建新分支 (feat/xxx 或 fix/xxx)
3. [TDD]       写测试 → 实现代码 → 验证通过
4. [Commit]    提交到本地分支
5. [Push]      推送到远程分支
6. [Test]      严格测试（单元/集成）
7. [Merge]     合并到 main
8. [Push]      推送 main 到远程
```

### 关键约束（CRITICAL）

| 阶段 | 要求 |
|------|------|
| Python 操作 | **所有 Python 相关操作必须在 venv 虚拟环境下执行** |
| 开发前 | 制定计划，明确小功能点，更新 project-progress.md |
| 开发中 | TDD：先写测试，再写代码 |
| 提交前 | 测试必须通过，覆盖率 ≥80% |
| 合并前 | 所有测试通过 |
| 合并后 | 立即推送 main |

### 虚拟环境（CRITICAL）

**所有 Python 操作必须在 venv 虚拟环境下执行**

```bash
# 激活虚拟环境
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate        # Windows

# 安装依赖
pip install -r requirements.txt

# 运行测试
pytest

# 运行代码
python src/main.py
```

**禁止**:
- ❌ 在系统 Python 环境下安装依赖
- ❌ 直接运行 `python xxx.py` 而未激活 venv
- ❌ 在 venv 未激活时提交代码

## 开发原则

1. **按计划开发**: 严格按照 project-progress.md 中的版本计划执行
2. **小步迭代**: 每次只完成若干个小功能点
3. **测试驱动**: 必须先写测试，验证失败后再写代码
4. **严格测试**: 测试不通过绝不提交
5. **分支管理**: 每个开发任务创建独立分支
6. **版本管理**: 使用语义化版本号 (0.0.1 → 0.0.2 → 0.1.0)

## 分支命名规范

- `feat/xxx`: 新功能
- `fix/xxx`: Bug 修复
- `refactor/xxx`: 重构
- `test/xxx`: 测试相关

## Git 提交规范

```
<type>: <description>

类型: feat, fix, refactor, docs, test, chore

示例:
feat: 添加 API 客户端
fix: 修复分页逻辑错误
test: 添加 repository 测试
```

## 测试要求

1. **覆盖率**: ≥ 80%
2. **测试类型**: 单元测试 + 集成测试
3. **测试框架**: pytest
4. **测试顺序**: TDD - RED → GREEN → IMPROVE

## 架构约束

1. **Repository Pattern**: 数据存储必须通过抽象层实现
2. **不可变性**: 优先创建新对象，避免原地修改
3. **错误处理**: 完整的错误捕获和用户友好提示
4. **文件组织**: 高内聚低耦合，文件 ≤ 800 行

## 禁止事项

- ❌ 跳过测试直接提交
- ❌ 在 main 分支直接开发
- ❌ 测试未通过就合并
- ❌ 硬编码敏感信息
- ❌ 超过计划范围的开发

## 进度追踪

每次开发后更新 `memory/project-progress.md` 中的功能清单。

## 工具偏好

- **包管理**: uv (优先) 或 pip
- **代码格式化**: ruff
- **类型检查**: mypy
- **测试**: pytest + pytest-cov
- **数据模型**: pydantic
