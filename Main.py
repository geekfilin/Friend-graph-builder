import yaml
from social_mapper import TwitterHarvester, VKHarvester, build_graph

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    config = load_config()
    
    target_user = input("Введите username или ID цели: ")
    platform = input("Платформа (twitter/vk): ").strip().lower()
    
    if platform == "twitter":
        harvester = TwitterHarvester(config['twitter'])
        user_data = harvester.get_user_connections(target_user)
    elif platform == "vk":
        harvester = VKHarvester(config['vk'])
        user_data = harvester.get_user_connections(target_user)
    else:
        raise ValueError("Неподдерживаемая платформа")
    
    graph = build_graph(
        user_data, 
        max_users=config['settings']['max_users'],
        edge_threshold=config['settings']['edge_threshold']
    )
    
    graph.export_gexf(f"outputs/{target_user}_network.gexf")
    print(f"Граф сохранён в outputs/{target_user}_network.gexf")
