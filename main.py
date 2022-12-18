import requests


def detection(hero_1, hero_2, hero_3):
    response = requests.get(url)
    all_heroes = {}
    x = 0
    for x in range(len(response.json())):
        hero = response.json()[x]["name"]
        if hero == hero_1 or hero == hero_2 or hero == hero_3:
            intelligences = response.json()[x]["powerstats"]["intelligence"]
            all_heroes[hero] = intelligences
        x += 1
    max_value = max(all_heroes.values())
    best = {key: values for key, values in all_heroes.items() if values == max_value}
    answer = []
    for key, values in best.items():
        answer.append(f"Самый умный супергерой - {key}:{values}")
    return answer


if __name__ == "__main__":
    url = "https://akabab.github.io/superhero-api/api/all.json"
    print(detection(hero_1="Hulk", hero_2="Captain America", hero_3="Thanos"))
    