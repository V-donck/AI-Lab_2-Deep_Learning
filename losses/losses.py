import torch

import utilities.utils as utils


def mse(input_tensor: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
    """TODO: implement this method"""
    difference = input_tensor-target
    power = torch.pow(difference,2)
    MeSqEr = torch.sum(power)/torch.numel(difference)
    print(MeSqEr)
    return MeSqEr
