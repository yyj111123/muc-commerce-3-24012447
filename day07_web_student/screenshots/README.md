# 请把四张验收截图保存在这里

- `01_login.png`
- `02_dashboard.png`
- `03_interaction.png`
- `04_assistant.png`
# Day07 电商用户行为分析Flask实训
## 1. 环境启动
1. 安装依赖
pip install -r requirements.txt
2. 启动项目
python app.py
访问地址：http://127.0.0.1:5000

## 2. 核心功能介绍
1. 登录系统：Session登录拦截，未登录禁止访问看板
2. 数据看板：展示CSV统计指标、PNG分析图表，流失率百分比格式化
3. 品类筛选：下拉选择自动刷新表格数据，筛选生效
4. 智能离线问答：支持4类数据问题查询（总用户数、流失率、品类、生命周期、订单）

## 3. 拓展功能（拓展A：筛选结果导出）
访问接口：/download?category=品类名
示例：
/download?category=Fashion  导出时尚品类筛选数据
/download?category=All      导出全部数据
下载文件自动命名：{品类}_筛选数据.csv

## 4. 验收截图
截图存放于/screenshots目录：
01_login.png 登录页
02_dashboard.png 数据看板
03_interaction.png 筛选交互
04_assistant.png 智能问答