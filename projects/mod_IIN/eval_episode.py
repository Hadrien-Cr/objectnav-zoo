# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import habitat_extensions
from tqdm import tqdm
from mod_iin_agent import ModIINAgent
from config_utils import get_config
from habitat.core.env import Env

from objectnav_zoo.agent.imagenav_agent.visualizer import record_video
from objectnav_zoo.env.habitat_imagenav_env.habitat_imagenav_env import (
    HabitatImageNavEnv,
)

def episode_evaluation(env, agent, config, episode_name):
    env.reset()
    agent.reset()

    pbar = tqdm(total = config.habitat.environment.max_episode_steps)
    is_collision = []
    
    while not env.episode_over:
        obs = env.get_observation()
        action = agent.act(obs)
        env.apply_action(action)

        collision = obs.task_observations.get("collisions")
        is_collision.append(collision is not None and collision["is_collision"])
        if len(is_collision) > 10 and all(is_collision[-10:]):
            break

        pbar.update(1)

    metrics = {
        k: v
        for k, v in env.get_episode_metrics().items()
        if k not in ["top_down_map", "collisions"]
    }
    print(metrics)

    if agent.verbose:
        record_video(
            target_dir=f"{config.dump_location}/videos/{config.exp_name}",
            image_dir=f"{config.dump_location}/images/{config.exp_name}",
            episode_name=episode_name
        )


if __name__ == "__main__":
    config, config_str = get_config(
        "projects/mod_IIN/configs/instance_imagenav_hm3d.yaml"
    )
    print("Config:\n", config_str, "\n", "-" * 100)

    env = HabitatImageNavEnv(Env(config=config.habitat), config=config)
    agent = ModIINAgent(config=config)

    env.reset()
    agent.reset()

    for k in range(10):
        episode_evaluation(env, agent, config, episode_name=str(k))
