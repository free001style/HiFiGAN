import os

import gdown
import torch


def download():
    gdown.download(id="1icXuB7Y6b8IOgnoDuUEJidUywuDH9mkV")  # download model_best.pth
    ckpts = torch.load("model_best.pth", weights_only=False)["state_dict"]
    ckpts = {
        k[len("Generator") + 1 :]: v
        for k, v in ckpts.items()
        if k[: len("Generator") + 1] == "Generator" + "."
    }
    torch.save(ckpts, "model_best.pth")
    os.makedirs("data/other", exist_ok=True)
    os.rename("model_best.pth", "data/other/model_best.pth")


if __name__ == "__main__":
    download()
