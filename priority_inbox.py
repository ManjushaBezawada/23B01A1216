import requests

BEARER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJtYW5qdXNoYWJlemF3YWRhMTY1QGdtYWlsLmNvbSIsImV4cCI6MTc4MjM3NTc5OSwiaWF0IjoxNzgyMzc0ODk5LCJpc3MiOiJBZmZvcmQgTWVkaWNhbCBUZWNobm9sb2dpZXMgUHJpdmF0ZSBMaW1pdGVkIiwianRpIjoiMWRkYTIzZDgtODJhYi00YjlhLTlmZDMtMzAyZTM2Yzc2YWFlIiwibG9jYWxlIjoiZW4tSU4iLCJuYW1lIjoiYmV6YXdhZGEgbWFuanVzaGEiLCJzdWIiOiIzNGQwYzI4NS0wNWYwLTRkMmMtYTQzOC1kNTU5M2QzNDM0ZjAifSwiZW1haWwiOiJtYW5qdXNoYWJlemF3YWRhMTY1QGdtYWlsLmNvbSIsIm5hbWUiOiJiZXphd2FkYSBtYW5qdXNoYSIsInJvbGxObyI6IjIzYjAxYTEyMTYiLCJhY2Nlc3NDb2RlIjoiYWhYanZwIiwiY2xpZW50SUQiOiIzNGQwYzI4NS0wNWYwLTRkMmMtYTQzOC1kNTU5M2QzNDM0ZjAiLCJjbGllbnRTZWNyZXQiOiJrQW1iSkFhVWt6WUFSeGNCIn0.g8aMBMWp0-Kg1vqfZC0T7jdNCnhd3lrvWCplN5X4q9k"

url = "http://20.244.56.144/evaluation-service/notifications"
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)

if response.status_code == 200:

    notifications = response.json()["notifications"]

    placement = []
    result = []
    event = []

    for notification in notifications:

        if notification["Type"] == "Placement":
            placement.append(notification)

        elif notification["Type"] == "Result":
            result.append(notification)

        else:
            event.append(notification)

    final_list = placement + result + event

    print("Priority Notifications\n")

    for notification in final_list:

        print("Type :", notification["Type"])
        print("Message :", notification["Message"])
        print("Time :", notification["Timestamp"])
        print("------------------------")

else:
    print("Failed to fetch notifications")