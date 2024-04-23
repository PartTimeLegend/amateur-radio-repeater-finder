class SortRepeaters:
    @staticmethod
    def sort_repeaters_by_mode_and_distance(repeaters):
        sorted_repeaters = {}
        for repeater in repeaters:
            mode = repeater['mode']
            distance = repeater['distance']
            if mode not in sorted_repeaters:
                sorted_repeaters[mode] = []
            sorted_repeaters[mode].append((repeater, distance))

        for mode, repeaters in sorted_repeaters.items():
            sorted_repeaters[mode] = sorted(repeaters, key=lambda x: x[1])

        return sorted_repeaters
