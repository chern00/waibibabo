import schedule
import time
import yaml
import os
from connectors import DataAggregator
from agents import ReportAgent

def run_daily_task():
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 🚀 開始執行自動化日報生成...")
    
    aggregator = DataAggregator()
    raw_data = aggregator.aggregate_all()
    
    agent = ReportAgent()
    draft = agent.generate_draft(raw_data)
    
    report_filename = f"Daily_Report_{time.strftime('%Y%m%d')}.md"
    with open(report_filename, "w", encoding="utf-8") as f:
        f.write(draft)
    
    print("\n" + "="*30)
    print("✨ 今日日報草稿已生成 ✨")
    print(draft)
    print("="*30)
    print(f"📄 文件已保存至: {report_filename}")

if __name__ == "__main__":
    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    print(f"🤖 個人日報自動生成器已啟動...")
    
    # 為了演示，運行時立即執行一次
    run_daily_task()

    schedule.every().day.at(config.get("trigger_time", "17:50")).do(run_daily_task)
    
    while True:
        schedule.run_pending()
        time.sleep(60)
