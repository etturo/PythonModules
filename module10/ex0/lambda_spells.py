#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict],
                 min_power: int) -> list[dict]:
    return filter(lambda m: m['power'] >= min_power, mages)


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: "* " + s + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {'max_power': max(mages, key=lambda x: x['power'])['power'],
            'min_power': min(mages, key=lambda x: x['power'])['power'],
            'avarage_power': sum(map(lambda x: x['power'], mages))/len(mages)}


def main():
    artifacts = [{'name': 'Crystal Orb', 'power': 94, 'type': 'weapon'},
                 {'name': 'Wind Cloak', 'power': 90, 'type': 'accessory'},
                 {'name': 'Storm Crown', 'power': 117, 'type': 'relic'},
                 {'name': 'Shadow Blade', 'power': 76, 'type': 'armor'}]
    mages = [{'name': 'Nova', 'power': 56, 'element': 'fire'},
             {'name': 'Sage', 'power': 61, 'element': 'lightning'},
             {'name': 'Kai', 'power': 75, 'element': 'earth'},
             {'name': 'Jordan', 'power': 89, 'element': 'water'},
             {'name': 'Sage', 'power': 100, 'element': 'shadow'}]
    spells = ['tsunami', 'freeze', 'meteor', 'lightning']

    print()
    print("=" * 42)
    print()

    print("Artifatcs before sorting:")
    for artifact in artifacts:
        print(f"{artifact['name']} have {artifact['power']} power")

    print()

    print("Artifacts after sorting:")
    for artifact in artifact_sorter(artifacts):
        print(f"{artifact['name']} have {artifact['power']} power")

    print()
    print("=" * 42)
    print()

    print("Mages list:")
    for mage in mages:
        print(f"{mage['name']} have {mage['power']} power")

    print()

    print("Mage selection (only mage with 70 power):")
    for mage in power_filter(mages, 70):
        print(f"{mage['name']} with {mage['power']} power")

    print()
    print("=" * 42)
    print()

    print("All spells:")
    for spell in spells:
        print(spell)

    print()

    print("Transformed spells:")
    for spell in spell_transformer(spells):
        print(spell)

    print()
    print("=" * 42)
    print()

    print("Printing Stats:")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
