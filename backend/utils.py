
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_with_gpt(df):
    content = df.head(30).to_csv(index=False)
    prompt = f"""Analyze the following spreadsheet data and provide:
- Forecast of future trends
- Reorder quantity if stock level is low
- Any key anomalies

Data:
{content}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )

    return response['choices'][0]['message']['content']
