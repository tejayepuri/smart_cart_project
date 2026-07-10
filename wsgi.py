import os
from app import app, initialize_database

# Run database initialization at startup
try:
    print("Running database initialization...")
    initialize_database()
    print("Database initialization complete.")
except Exception as e:
    print(f"Warning: Database initialization failed during startup. This is expected if database environment variables are not configured yet. Details: {e}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
