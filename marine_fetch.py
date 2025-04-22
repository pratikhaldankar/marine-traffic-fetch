import requests
import datetime
import os

url = "https://services.marinetraffic.com/api/exportvessels/8077da7303bee080d086ebf36be66074d8ec9a57?v=8&timespan=1440&msgtype=full&protocol=xml"

try:
    response = requests.get(url)
    if response.status_code == 200:
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"marine_traffic_{timestamp}.xml"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"✅ Saved: {filename}")
    else:
        print(f"❌ Failed to fetch data. Status: {response.status_code}")
except Exception as e:
    print(f"⚠️ Error: {str(e)}")
