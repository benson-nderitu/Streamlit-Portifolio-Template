import os
import sqlite3
from unittest import mock

import pandas as pd
import pytest
from alldata import update_services


@mock.patch("alldata.sqlite3.connect")
def test_update_services(mock_connect):
    # Create a mock DataFrame
    data = {
        "id": [1, 2],
        "title": ["Service 1", "Service 2"],
        "description": ["Description 1", "Description 2"],
        "icon": ["icon1.png", "icon2.png"],
    }
    df = pd.DataFrame(data)

    # Mock the database connection and cursor
    mock_conn = mock.Mock()
    mock_cursor = mock.Mock()
    mock_connect.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    # Call the function to test
    update_services(df)

    # Verify that the correct SQL commands were executed
    mock_cursor.execute.assert_any_call("DELETE FROM services")
    for _, row in df.iterrows():
        mock_cursor.execute.assert_any_call(
            "INSERT INTO services (id, title, description, icon) VALUES (?, ?, ?, ?)",
            (row["id"], row["title"], row["description"], row["icon"]),
        )

    # Verify that commit and close were called
    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()


# Debug unexpected behavior
if __name__ == "__main__":
    pytest.main(["-v", __file__])
