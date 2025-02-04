def longest_repeating_substring(s: str) -> str:
    def has_duplicate_substring(length: int) -> str:
        """ Helper function to check if a substring of given length has duplicates. """
        seen = set()
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring in seen:
                return substring
            seen.add(substring)
        return ""

    # Binary search for the longest length
    left, right = 1, len(s)
    result = ""
    
    while left <= right:
        mid = (left + right) // 2
        substring = has_duplicate_substring(mid)
        
        if substring:
            result = substring  # Found a longer repeated substring, store it
            left = mid + 1  # Try to find a longer one
        else:
            right = mid - 1  # Try shorter lengths
    
    return result






from flask import Flask, request, render_template

app = Flask(__name__)

# Route for the homepage (HTML page)
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the form submission
@app.route('/process', methods=['POST'])
def process():
    # Get the input value from the form
    user_input = request.form.get('user_input')
    


    if user_input:
        result = longest_repeating_substring(user_input)
    else:
        result = 'No input provided'
    
    # Return the result to the HTML page
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
