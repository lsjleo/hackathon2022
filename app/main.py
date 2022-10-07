from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

class Teste(BaseModel):
    ids: list
    nomes: list
    prioridades: list

app = FastAPI()

@app.post("/teste/")
async def post_prioridades(p: Teste):
    df  = pd.DataFrame(
        data = {
            "nomes":p.nomes,
            "ids": p.ids,
            "prioridades": p.prioridades,
        }
    )

    return df.to_json()