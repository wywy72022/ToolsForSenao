# ToolsForSenao

## 系統概述：
原基於 Google Cloud Platform (GCP)建構AI Agent，採用Google較新發布的模型Gemini 1.5 Flash，並包含三個主要工具：
1. 播放聲音：接受用戶語音命令，觸發音效播放。
2. 語音轉文字 (STT)：將用戶的語音轉換為文字並保存至文本檔案。
3. 鏡頭中人數檢測：通過 GCP 的影像處理能力識別畫面中的人數。

![image](https://github.com/user-attachments/assets/118c6feb-95fc-4e9c-9d6b-9ef2894ce585)
1. 使用者鍵入或說出任務；
2. 以 Dialogflow 將使用者表達與意圖進行匹配並提取參數；
3. 由 Dialogflow 將 Webhook 請求的訊息傳送到 Webhook 服務。此訊息包含有關匹配的意圖、操作、參數以及為意圖定義的回應的資訊。您的服務根據需要執行操作，例如資料庫查詢或外部 API 呼叫；
4. 接下來，向 Dialogflow 發送 Webhook 回應的訊息，包含應發送給使用者的回應；
5. Dialogflow 將回應傳送給最終使用者；
6. 最終用戶看到或聽到回應。

## 主要使用的GCP服務：
Google Cloud Speech-to-Text API
Google Cloud Text-to-Speech API
Google Cloud Vision API
Google Cloud Functions
Google Cloud Storage
