import requests

# Function to fetch and display users
def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(url, timeout=10)  # network request
        response.raise_for_status()  # raise error for non-200 status
        users = response.json()  # parse JSON
        
        # Limit to num_users
        for i, user in enumerate(users[:num_users]):
            try:
                name = user["name"]
                email = user["email"]
                city = user["address"]["city"]
                print(f"{i+1}. Name: {name}, Email: {email}, City: {city}")
            except KeyError as e:
                print(f"Missing expected key: {e}")
                
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return None

# Example calls
if __name__ == "__main__":
    print("Fetching 3 users:")
    fetch_and_display_users(3)
    print("\nFetching 15 users (more than available):")
    fetch_and_display_users(15)
