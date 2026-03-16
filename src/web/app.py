"""Streamlit Web 应用"""
import pandas as pd

from bsh.repository import RepositoryFactory
from bsh.models.product import ProductModel


@st.cache_data
def load_products(filepath: str = "data/products.csv") -> list[ProductModel]:
    """加载产品数据（带缓存）"""
    repository = RepositoryFactory.create_repository(None, "csv", filepath=filepath)
    return repository.find_all()


def main() -> None:
    """主函数"""
    st.set_page_config(
        page_title="BSH - 上海银行理财产品查询",
        page_icon="🏦",
        layout="wide",
    )

    st.title("🏦 上海银行理财产品查询")
    st.markdown("---")

    # 加载数据
    products = load_products()

    if not products:
        st.warning("暂无产品数据，请先运行 `bsh-fetch` 获取数据")
        return

    # 数据转换为 DataFrame
    df = pd.DataFrame([p.model_dump() for p in products])

    # 侧边栏筛选器
    st.sidebar.header("筛选条件")

    # 按产品代码筛选
    code_filter = st.sidebar.text_input("产品代码（模糊搜索）")

    # 按产品名称筛选
    name_filter = st.sidebar.text_input("产品名称（模糊搜索）")

    # 按风险等级筛选
    risk_levels = ["全部"] + sorted(df["risk_level"].dropna().astype(int).astype(str).unique().tolist())
    risk_filter = st.sidebar.selectbox("风险等级", risk_levels)

    # 按币种筛选
    currencies = ["全部"] + sorted(df["curr_type"].dropna().unique().tolist())
    currency_filter = st.sidebar.selectbox("币种", currencies)

    # 应用筛选
    filtered_df = df.copy()

    if code_filter:
        filtered_df = filtered_df[filtered_df["prd_code"].str.contains(code_filter, case=False, na=False)]

    if name_filter:
        filtered_df = filtered_df[filtered_df["prd_name"].str.contains(name_filter, case=False, na=False)]

    if risk_filter != "全部":
        filtered_df = filtered_df[filtered_df["risk_level"].astype(str) == risk_filter]

    if currency_filter != "全部":
        filtered_df = filtered_df[filtered_df["curr_type"] == currency_filter]

    # 显示结果
    st.subheader(f"查询结果: {len(filtered_df)} 条")

    if len(filtered_df) > 0:
        st.dataframe(
            filtered_df,
            column_config={
                "prd_code": st.column_config.TextColumn("产品代码", width=150),
                "prd_name": st.column_config.TextColumn("产品名称", width=300),
                "rate": st.column_config.NumberColumn("年化收益率(%)", format="%.2f"),
                "risk_level": st.column_config.TextColumn("风险等级", width=100),
                "curr_type": st.column_config.TextColumn("币种", width=80),
                "pfirst_amt": st.column_config.NumberColumn("起售金额", format="%.0f"),
                "sold_out": st.column_config.CheckboxColumn("是否售罄"),
            },
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("没有匹配的产品")


if __name__ == "__main__":
    main()
