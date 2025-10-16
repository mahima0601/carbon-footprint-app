import os
from flask import Flask, render_template, request, send_from_directory
from assessment3_backend import calculate_footprint, save_progress, get_last_results
from assessment3_visualization import create_chart

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # Show form + recent history
    history = get_last_results()
    # Convert to records for easy templating
    history_records = history.to_dict(orient="records") if not history.empty else []
    return render_template("index.html", history=history_records)

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        transport_km = float(request.form.get("transport_km", 0) or 0)
        electricity_kwh = float(request.form.get("electricity_kwh", 0) or 0)
        flight_hours = float(request.form.get("flight_hours", 0) or 0)
    except ValueError:
        return render_template("result.html", error="Please enter valid numbers only.", result=None, chart_url=None)

    result = calculate_footprint(transport_km, electricity_kwh, flight_hours)
    # Save to CSV
    save_progress(result)
    # Build chart into static folder
    chart_path = os.path.join("static", "chart.png")
    create_chart(result, filename=chart_path)
    return render_template("result.html", error=None, result=result, chart_url="/static/chart.png")

# Health check (useful for Render)
@app.route("/healthz")
def healthz():
    return {"status": "ok"}

if __name__ == "__main__":
    # Local dev run
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
