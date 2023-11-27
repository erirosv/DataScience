import torch
import pandas as pd
import numpy as np

def get_result_to_csv(model, loader, test_ids, device):
    all_preds = []
    model.eval()
    with torch.no_grad():
        for x,y in loader:
            x = x.to(device)
            score = model(x)
            prediction = score.float()
            all_preds += prediction.tolist()
    model.train()
    df = pd.DataFrame({
        "ID_code" : test_ids.values,
        "target" : np.array(all_preds)
    })

    df.to_csv("sub.csv", index=False)
    print('Result CSV created')