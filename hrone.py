import requests
import datetime
import sys

# Replace with the actual login endpoint
LOGIN_URL = "https://gateway.hrone.cloud/oauth2/token"
API_URL = "https://app.hrone.cloud/api/timeoffice/mobile/checkin/Attendance/Request"

# Replace with your username and password
USERNAME = 
PASSWORD = 

# Get date from command-line arguments or default to today
if len(sys.argv) > 1:
    try:
        current_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD.")
        sys.exit(1)
else:
    current_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
print("----------------------------------------------------------------------------------------------------")
print(f"Using date: {current_date}")

# Define the request payload (adjust this according to your API)
payload = {
    "username": USERNAME,
    "password": PASSWORD,
    "grant_type":"password",
    "loginType":1,
    "companyDomainCode":"batonsystems",
    "isUpdated":0,
    "validSource":"Y",
    "deviceName":"Chrome-unknown"
}

# Make the login request
response = requests.post(LOGIN_URL, data=payload)

if response.status_code == 200:
    token = response.json().get("access_token")  # Adjust key based on API response
    if token:
        print(f"Bearer Token: {token}")

        # Step 2: Call API with Bearer token
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        # Define the payload with dynamic currentDate
        api_payload =  {
            "requestType": "A",
            "employeeId": 346,
            "latitude": "",
            "longitude": "",
            "geoAccuracy": "",
            "geoLocation": "",
            "punchTime": current_date,
            "remarks": "Kochi Office",
            "uploadedPhotoOneName": "",
            "uploadedPhotoOnePath": "",
            "uploadedPhotoTwoName": "",
            "uploadedPhotoTwoPath": "",
            "attendanceSource": "W",
            "attendanceType": "Online"
        }       

        # Make the API request
        api_response = requests.post(API_URL, json=api_payload, headers=headers)

        # Print API response
        print(f"API Response Status: {api_response.status_code}")
        print(f"API Response: {api_response.json()}")

    else:
        print("Token not found in response!")
else:
    print(f"Login failed! Status Code: {response.status_code}, Response: {response.text}")
