from pathlib import Path
import pandas as pd

def answer_question(base_dir: Path, question: str) -> str:
    data_dir = base_dir / "data"
    metrics_df = pd.read_csv(data_dir / "overall_metrics.csv", encoding="utf-8")
    metrics = dict(zip(metrics_df["指标"], metrics_df["数值"]))
    normalized = question.replace(" ", "").lower()

    # 1、总用户数（原有保留）
    if any(word in normalized for word in ["多少用户", "用户数", "总用户"]):
        return f"数据集中共有{int(metrics['用户数'])}名用户。"

    # 2、流失率类问答
    elif any(word in normalized for word in ["流失率", "流失多少", "流失比例"]):
        loss_rate = metrics["流失率"] * 100
        return f"平台整体用户流失率为{loss_rate:.2f}%。"

    # 3、偏好品类 / 品类流失问答
    elif any(word in normalized for word in ["品类", "时尚", "电子", "商品类别"]):
        return f"时尚类商品用户流失率最高，整体平均品类流失率{metrics['品类平均流失率']*100:.2f}%。"

    # 4、生命周期风险问答
    elif any(word in normalized for word in ["生命周期", "阶段", "新手", "老用户"]):
        return f"新注册新手用户生命周期流失风险最高，流失占比{metrics['新手流失占比']*100:.2f}%。"

    # 5、订单相关问答
    elif any(word in normalized for word in ["订单", "下单", "平均订单"]):
        return f"用户平均订单数量为{metrics['平均订单数']:.2f}单。"

    # 无法识别问题默认返回
    return "暂时无法解答该问题，请更换问题（可询问总用户数、流失率、商品品类、用户生命周期、订单相关问题）。"