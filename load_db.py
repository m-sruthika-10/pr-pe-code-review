import psycopg2
from psycopg2 import sql

def create_leaderboard_score_table(host, user, password, port, dbname):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            dbname=dbname,
            sslmode="require"  # remove if not using SSL
        )
        cursor = conn.cursor()

        # Ensure schema exists
        cursor.execute(sql.SQL("CREATE SCHEMA IF NOT EXISTS syscoscore"))

        # Create the Leaderboard_score table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS syscoscore.Leaderboard_score (
                id SERIAL PRIMARY KEY,
                delivery_velocity NUMERIC,
                quality_reliability NUMERIC,
                code_process_health NUMERIC,
                operational_excellence NUMERIC,
                cloud_score_health NUMERIC,
                collaboration_team_dynamics NUMERIC,
                total NUMERIC,
                repository TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()
        print("✅ Table syscoscore.Leaderboard_score created successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    # Example usage (replace with your .env values or inputs)
    create_leaderboard_score_table(
        host="localhost",
        user="user",
        password="password",
        port="5432",
        dbname="name"
    )
