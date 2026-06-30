from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_the_student_from_activity():
    activity_name = "Chess Club"
    participant = "michael@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/participants/{participant}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {participant} from {activity_name}"

    refreshed = client.get("/activities").json()
    assert participant not in refreshed[activity_name]["participants"]

    client.post(f"/activities/{activity_name}/signup?email={participant}")
