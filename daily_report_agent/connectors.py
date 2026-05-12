import datetime

class DataAggregator:
    """
    多源數據聚合器 MVP 版本
    在實際生產中，這裡應替換為真實的 API 調用
    """
    def get_git_commits(self):
        # 模擬數據：獲取今日代碼提交
        return [
            "feat: 實作 Agent 長鏈推理核心邏輯",
            "fix: 修復多源數據去重時的 Key 錯誤",
            "docs: 更新 MVP 部署文檔"
        ]

    def get_im_discussions(self):
        # 模擬數據：從通訊軟體提取的關鍵討論
        return [
            "10:30 與產品經理確認了日報自動生成的視覺樣式",
            "14:15 討論了關於 Git 權限驗證的安全方案",
            "16:40 團隊達成一致：優先保證輕量化，不引入重型數據庫"
        ]

    def get_doc_updates(self):
        # 模擬數據：文檔編輯記錄
        return [
            "編輯了《個人日報 Agent 技術架構圖》",
            "新建了《API 安全調用規範.md》"
        ]

    def aggregate_all(self):
        return {
            "git": self.get_git_commits(),
            "im": self.get_im_discussions(),
            "docs": self.get_doc_updates(),
            "date": str(datetime.date.today())
        }
