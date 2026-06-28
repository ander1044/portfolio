import requests
import json
import os

# Replace this with your actual n8n Test Webhook URL
N8N_WEBHOOK_URL = "http://localhost:5678/webhook-test/meeting-ingestion"

def send_transcript_to_pipeline(filepath: str, title: str, host: str):
    if not os.path.exists(filepath):
        # Create a dummy transcript file if it doesn't exist for test purposes
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("Founder: Thanks everyone for joining. Today we need to align on Q3. "
                    "Sarah, please update the API Gateway routing tables by July 2nd. "
                    "John, I need you to review client retainer agreements by June 30th.")
        
    with open(filepath, 'r', encoding='utf-8') as f:
        raw_transcript = f.read()
        
    payload = {
        "metadata": {
            "title": title,
            "host": host,
            "date": "2026-06-27"
        },
        "transcript_raw": raw_transcript
    }
    
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(N8N_WEBHOOK_URL, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            print(f"[✓] Success: Payload delivered to pipeline.")
        else:
            print(f"[X] Failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[X] Error establishing connection: {e}")

if __name__ == "__main__":
    send_transcript_to_pipeline("transcript.txt", "Q3 Architecture Alignment", "Founder Direct")