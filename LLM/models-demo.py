# models-demo.py

import os
from langchain_openai import OpenAI  # DÙNG đúng gói mới
from apikey import OPENAI_API_KEY  # Đảm bảo chứa API key dạng 'sk-...'

# Đặt API key vào môi trường
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Khởi tạo model
llm = OpenAI(model="text-ada-001", n=2, best_of=2)

# Sinh nội dung
response = llm.generate(["Write a short title for the Viblo article about new framework Langchain"])

# Hiển thị kết quả
for i, gen in enumerate(response.generations[0]):
    print(f"Kết quả {i+1}: {gen.text.strip()}")
