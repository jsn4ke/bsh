# Task 6: 年化计算器实现计划

## 目标
实现 YieldCalculator 类，根据净值历史数据计算各种年化收益率。

## 小功能点清单

### 6.1 创建 YieldCalculator 基础结构
- 创建 `src/calculator/yield_calculator.py`
- 实现 YieldCalculator 类

### 6.2 实现基础年化计算方法
- 实现 `calculate_from_nav(initial_nav, current_nav, days)` - 从净值计算年化
- 应用公式：(当前净值 / 初始净值 - 1) × (365 / 天数) × 100%
- 处理除零错误
- 处理负天数错误
- 处理天数为0错误
- 保留2位小数

### 6.3 实现多日年化计算方法
- 实现 `calculate_7_day_yield(historical_navs)` - 计算7日年化
- 实现 `calculate_3_day_yield(historical_navs)` - 计算3日年化
- 实现通用方法 `calculate_n_day_yield(historical_navs, n)`
- 处理历史数据不足的情况
- 处理无效的净值数据

### 6.4 编写测试 (TDD - 先写测试)
- 创建 `tests/test_yield_calculator.py`
- 测试基础年化计算（正向情况）
- 测试边界值（天数为1、365等）
- 测试错误情况（天数为0、负数，除零）
- 测试精度（小数位数）
- 测试7日年化计算
- 测试3日年化计算
- 测试历史数据不足情况

## 开发顺序
1. 写测试 → 测试失败 (RED)
2. 写代码 → 测试通过 (GREEN)
3. 重构 → 代码优化 (IMPROVE)

## 验收标准
- [ ] 所有测试通过
- [ ] 测试覆盖率 ≥ 80%
- [ ] 计算公式正确
- [ ] 边界值处理正确
- [ ] 错误处理完善
