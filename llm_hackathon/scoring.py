import pandas as pd
from sklearn.metrics import f1_score
import requests
from io import StringIO


def download_csv_from_sas(
    sas_url: str = "https://stllmchallenge2024.blob.core.windows.net/data/test_data.csv?sp=r&st=2024-09-08T13:25:41Z&se=2024-09-11T21:25:41Z&spr=https&sv=2022-11-02&sr=b&sig=XWxsQdUZEW5ygjAL6JbHNT%2FGOa6HKNHV3yu0dX8tH0w%3D"
):
    try:
        # Make an HTTP GET request to the SAS URL
        response = requests.get(sas_url)
        response.raise_for_status()  # Raise an exception if the request fails

        # Read the content of the response (CSV data)
        csv_content = response.content

        # Convert the CSV content to a Pandas DataFrame
        df = pd.read_csv(StringIO(csv_content.decode('utf-8')))

        return df
    except Exception as e:
        print(f"Error downloading CSV: {e}")
        return None


def score_solution(predictions: pd.DataFrame) -> pd.DataFrame:
    df = download_csv_from_sas()
    f1 = f1_score(predictions, df["cpv_code"].iloc[:predictions.shape[0]], average="weighted")
    df["accuracy"] = df["cpv_code"] == predictions["prediction"]
    weighted_acc = (df["accuracy"] * df["weight"]).sum() / df["weight"].sum()
    return {"f1-score": f1, "weighted accuracy": weighted_acc}
