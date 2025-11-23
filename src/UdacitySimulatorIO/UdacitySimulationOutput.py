from pydantic.dataclasses import dataclass
from typing import List, Tuple
import json
from pathlib import Path
from dataclasses import field
import json_numpy as jnp

@dataclass
class UdacitySimulationOutput():
    """A class to sequentially store the outputs of a simulation

    Arguments:
        elapsedTime (float): The elapsed time of the simulation in seconds
        iterations (int): The number of iterations completed in the simulation
        positions (List[Tuple[float, float, float]]): The list of positions recorded during the simulation
        speeds (List[float]): The list of speeds recorded during the simulation
        xtes (List[float]): The list of cross-track errors recorded during the simulation
        steerings (List[float]): The list of steerings recorded during the simulation
        throttles (List[float]): The list of throttles recorded during the simulation
        road (List[Tuple]): The list of road information recorded during the simulation

    Returns:
        _type_: _description_
    """
    elapsedTime: float = -1
    iterations: int = -1
    positions: List[Tuple[float, float, float]
                    ] = field(default_factory=lambda: [])
    speeds: List[float] = field(default_factory=lambda: [])
    xtes: List[float] = field(default_factory=lambda: [])
    steerings: List[float] = field(default_factory=lambda: [])
    throttles: List[float] = field(default_factory=lambda: [])
    road: List[Tuple[float]] = field(default_factory=lambda: [])

    # def to_json(self):
    #     return json.dumps(self.__dict__)

    def addStats(
            self,
            position: Tuple[float, float, float],
            speed: float,
            xte: float,
            steering: float,
            throttle: float) -> None:
        self.positions.append(position)
        self.speeds.append(speed)
        self.xtes.append(xte)
        self.steerings.append(steering)
        self.throttles.append(throttle)

    @classmethod
    def from_json(cls, json_str: str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
    
    def to_json(self) -> str:
        return jnp.dumps(self.__dict__)