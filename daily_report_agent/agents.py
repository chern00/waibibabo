from openai import OpenAI
import yaml

class ReportAgent:
    def __init__(self, config_path="config.yaml"):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        
        self.client = OpenAI(
            api_key=self.config['api_key'],
            base_url=self.config.get('base_url', 'https://api.openai.com/v1')
        )

    def generate_draft(self, raw_data):
        prompt = f"""
        你是一個高效的個人辦公助手。請根據以下碎片化的工作軌跡，進行語義提煉與長鏈推理，生成一份專業的日報。
        
        【要求】：
        1. 語義提煉：不要簡單羅列，要將相關聯的活動合併。
        2. 推理邏輯：根據今日產出推理出「關鍵結論」以及對明日的「待辦風險」。
        3. 結構化輸出：分為【今日主要產出】、【關鍵結論】、【待辦風險】和【明日計劃】。

        【原始軌跡數據】：
        {raw_data}
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.config['model_name'],
                messages=[{"role": "system", "content": "你是一個資深的職場專家，善於歸納總結工作成果。"},
                          {"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"生成失敗，請檢查 API Key 或網絡配置。錯誤：{str(e)}"
