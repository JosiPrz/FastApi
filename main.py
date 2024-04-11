from fastapi import FastAPI

app = FastAPI(
    title="Deploy House Pricing",
    version="0.0.1"
)

app.post("/api/v1/predict-house-pricing", tag="House-Pricing")

async def predict(
        LotArea,
        age,
        1stFlrSF,
        2ndFlrSF,
        BedroomAbvGr,
        KitchenAbvGr,
        Fireplaces,
        GarageArea,
        Flat,
        Gable,
        Gambrel,
        Hip,
        Mansard,
        Shed,
        Ex,
        Fa,
        Gd,
        TA,
        Ex,
        Fa,
        Gd,
        Po,
        TA,
        Floor,
        GasA,
        GasW,
        Grav,
        OthW,
        Wall,
        Ex,
        Fa,
        Gd,
        Po,
        TA
):