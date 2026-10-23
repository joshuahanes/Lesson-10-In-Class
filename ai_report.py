
from groq import Groq
import os

def make_report(weather_data):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY")
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a weather reporter. "
                    "Write a short but witty report about "
                    "the provided weather data. "
                    "Do not make weather stuff up."
                )
            },
            {
                "role": "user",
                "content":weather_data.to_string(index=False)}
        ],
        reasoning_effort="low"
    )

    report = response.choices[0].message.content
    usage = response.usage

    return report, usage


if __name__ == "__main__":
    report, usage = make_report("25 degrees and snow")
    print(report)
    print(usage)
