from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Placeholder for events
events = []

# Routes for rendering HTML templates and handling AJAX requests
@app.route("/", methods=["GET", "POST", "DELETE"])
def index():
    global events
    try:
        if request.method == "GET":
            return render_template("index.html", events=events)
        
        elif request.method == "POST":
            title = request.form.get("title")
            description = request.form.get("description")
            date = request.form.get("date")
            time = request.form.get("time")
            # Add your logic to add the event
            events.append({"title": title, "description": description, "date": date, "time": time})
            return jsonify({"message": "Event added successfully"})
        
        elif request.method == "DELETE":
            title = request.args.get("title")
            # Add your logic to delete the event
            events = [event for event in events if event["title"] != title]
            return jsonify({"message": "Event deleted successfully"})
    
    except KeyError as ke:
        return jsonify({"error": f"KeyError: {ke}"}), 400
    
    except ValueError as ve:
        return jsonify({"error": f"ValueError: {ve}"}), 400
    
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

