from http.server import HTTPServer, BaseHTTPRequestHandler
import mysql.connector
import json
from datetime import date, datetime

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "wastemanagement"
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        return super().default(obj)

class WasteManagementHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            response_data = {}

            if self.path == "/schedules":
                cursor.execute("SELECT * FROM schedules")
                response_data = cursor.fetchall()

            elif self.path == "/collections":
                cursor.execute("""
                    SELECT C.*, S.area_id, S.collection_date
                    FROM collections C
                    INNER JOIN schedules S ON C.schedule_id = S.schedule_id
                """)
                response_data = cursor.fetchall()

            elif self.path == "/disposal-sites":
                cursor.execute("SELECT * FROM disposalsites")
                response_data = cursor.fetchall()

            else:
                self.send_error(404, "Endpoint not found")
                return

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response_data, cls=CustomJSONEncoder).encode())

        except Exception as e:
            self.send_error(500, str(e))
        finally:
            cursor.close()
            conn.close()

    def do_POST(self):
        try:
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data)

            conn = get_db_connection()
            cursor = conn.cursor()

            if self.path == "/add-schedule":
                area_id = post_data["area_id"]
                collection_date = post_data["collection_date"]
                cursor.execute(
                    "INSERT INTO schedules (area_id, collection_date) VALUES (%s, %s)",
                    (area_id, collection_date)
                )
                conn.commit()
                response = {"message": "Schedule added successfully"}

            elif self.path == "/log-collection":
                schedule_id = post_data["schedule_id"]
                status = post_data["status"]
                collection_time = datetime.now()
                cursor.execute(
                    "INSERT INTO collections (schedule_id, status, collection_time) VALUES (%s, %s, %s)",
                    (schedule_id, status, collection_time)
                )
                conn.commit()
                response = {"message": "Collection logged successfully"}

            elif self.path == "/update-disposal":
                site_id = post_data["site_id"]
                additional_utilization = post_data["additional_utilization"]
                cursor.execute(
                    "UPDATE disposalsites SET current_utilization = current_utilization + %s WHERE site_id = %s",
                    (additional_utilization, site_id)
                )
                conn.commit()
                response = {"message": "Disposal site updated successfully"}

            else:
                self.send_error(404, "Endpoint not found")
                return

            self.send_response(201)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        except Exception as e:
            self.send_error(500, str(e))

        finally:
            cursor.close()
            conn.close()

def run_server(port=8000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, WasteManagementHandler)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
