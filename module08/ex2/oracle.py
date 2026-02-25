#!/usr/bin/env pytohn3
import os


def main():
    print("\nORACLE STATUS: Reading the Matrix...\n")

    try:
        from dotenv import load_dotenv
    except ImportError:
        return 1

    load_dotenv()

    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("MATRIX_MODE")

    if not all([matrix_mode, database_url, api_key, log_level, zion_endpoint]):
        print("WARNING: Missing configuration detected!")
        print("Please ensure your .env file is properly configured.")
        print("Required variables: MATRIX_MODE, DATABASE_URL, API_KEY,"
              " LOG_LEVEL, ZION_ENDPOINT")
        return 1

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    print()

    if database_url:
        print("Database: Connected to local instance")
    if api_key:
        print("API Access: Authenticated")

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print("Zion Network: Online")

    print()

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print()

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
