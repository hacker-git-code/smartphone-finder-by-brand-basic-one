# import requests
# from flask import Flask, render_template, request

# app = Flask(__name__)

# def fetch_smartphone_prices(search_query, budget):
#     """
#     Fetches smartphones and their prices from e-commerce platforms.
    
#     Args:
#         search_query (str): The smartphone brand or type.
#         budget (int): The maximum budget of the user.

#     Returns:
#         list: A list of smartphones with prices and purchase links.
#     """
#     # Example API or scraping implementation (replace this with actual API details)
#     api_url = "https://api.example.com/search"  # Replace with a real API endpoint
#     params = {
#         "query": search_query,
#         "max_price": budget,
#         "currency": "USD"
#     }

#     try:
#         # Replace the following line with actual API requests for real-world use
#         # response = requests.get(api_url, params=params)
#         # Mock data for testing
#         response = {
#             "status_code": 200,
#             "data": [
#                 {"name": "Smartphone A", "price": 199, "url": "http://example.com/a"},
#                 {"name": "Smartphone B", "price": 299, "url": "http://example.com/b"},
#                 {"name": "Smartphone C", "price": 399, "url": "http://example.com/c"}
#             ]
#         }

#         # Simulate the response structure
#         if response["status_code"] == 200:
#             products = response["data"]
#             return [
#                 {
#                     "name": product["name"],
#                     "price": product["price"],
#                     "link": product["url"]
#                 }
#                 for product in products if product["price"] <= budget
#             ]
#         else:
#             print(f"Error: Unable to fetch data (Status Code: {response['status_code']})")
#             return []
#     except Exception as e:
#         print(f"Error fetching smartphone prices: {e}")
#         return []

# @app.route('/')
# def home():
#     return render_template('templates/index.html')

# @app.route('/search', methods=['POST'])
# def search():
#     search_query = request.form.get('search_query', '').strip()
#     budget = request.form.get('budget', '').strip()

#     if not search_query:
#         return "Error: Please provide a search query."

#     try:
#         budget = int(budget)
#         if budget <= 0:
#             return "Error: Please provide a valid positive budget."

#         smartphones = fetch_smartphone_prices(search_query, budget)

#         return render_template('templates/results.html', smartphones=smartphones, search_query=search_query, budget=budget)
#     except ValueError:
#         return "Error: Please enter a numeric value for the budget."
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#         return "An unexpected error occurred. Please try again later."

# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import Flask, render_template

# app = Flask(__name__, template_folder='path/to/your/templates')

# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)






from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
