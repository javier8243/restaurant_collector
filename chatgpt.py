import openai


def summary(name, message, api_key, focus_point):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"你現在是一個美食資料分析師，以下是關於這間餐廳的評論。做一個表格產出這家餐廳最常見的缺點和優點。我在乎的是{focus_point}，根據我在乎的是告訴我這家餐廳推薦我去嗎？ 回傳都用marksown格式",
            }
        ]
        + message,
    )

    with open("output.txt", "a", encoding="utf-8") as output_file:
        print(response["choices"][0]["message"]["content"])
        output_file.write(f"\n# {name}\n\n")
        output_file.write(response["choices"][0]["message"]["content"])
        output_file.write("\n")
