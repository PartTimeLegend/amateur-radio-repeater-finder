import csv


class CSVExporter:
    @staticmethod
    def save_to_chirp_csv(repeaters, filename):
        with open(filename, "w", newline="") as csvfile:
            fieldnames = [
                "Call",
                "Frequency",
                "Duplex",
                "Offset",
                "Tone",
                "rToneFreq",
                "cToneFreq",
                "DtcsCode",
                "DtcsPolarity",
                "Mode",
                "Name",
                "Comment",
                "URCALL",
                "RPT1CALL",
                "RPT2CALL",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for _mode, repeaters_list in repeaters.items():
                for repeater, _distance in repeaters_list:
                    writer.writerow(
                        {
                            "Call": repeater["callsign"],
                            "Frequency": repeater["frequency"],
                            "Duplex": (
                                repeater["offset"] if repeater["offset"] else "off"
                            ),
                            "Offset": (
                                repeater["offset_freq"]
                                if repeater["offset_freq"]
                                else "0.000000"
                            ),
                            "Tone": "Tone" if repeater["tone"] else "None",
                            "rToneFreq": (
                                repeater["tone"] if repeater["tone"] else "0.0"
                            ),
                            "cToneFreq": (
                                repeater["ctcss"] if repeater["ctcss"] else "0.0"
                            ),
                            "DtcsCode": "023",
                            "DtcsPolarity": "NN",
                            "Mode": repeater["mode"],
                            "Name": repeater["callsign"],
                            "Comment": "",
                            "URCALL": "",
                            "RPT1CALL": "",
                            "RPT2CALL": "",
                        }
                    )

    @staticmethod
    def save_to_icom_csv(repeaters, filename):
        with open(filename, "w", newline="") as csvfile:
            fieldnames = [
                "No",
                "Frequency",
                "Dup",
                "Offset",
                "Mode",
                "Tone",
                "ToneFreq",
                "Skip",
                "Step",
                "Name",
                "Comment",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for _mode, repeaters_list in repeaters.items():
                for index, (repeater, _distance) in enumerate(repeaters_list, start=1):
                    writer.writerow(
                        {
                            "No": index,
                            "Frequency": repeater["frequency"],
                            "Dup": "Split" if repeater["offset"] else "Simplex",
                            "Offset": (
                                repeater["offset_freq"]
                                if repeater["offset_freq"]
                                else "0.000000"
                            ),
                            "Mode": repeater["mode"],
                            "Tone": "Tone" if repeater["tone"] else "None",
                            "ToneFreq": (
                                repeater["ctcss"] if repeater["ctcss"] else "0.0"
                            ),
                            "Skip": "Off",
                            "Step": "5.00 kHz",
                            "Name": repeater["callsign"],
                            "Comment": "",
                        }
                    )

    @staticmethod
    def save_to_yaesu_csv(repeaters, filename):
        with open(filename, "w", newline="") as csvfile:
            fieldnames = [
                "Name",
                "Frequency",
                "Duplex",
                "Offset",
                "Tone",
                "rToneFreq",
                "cToneFreq",
                "DtcsCode",
                "DtcsPolarity",
                "MemoryMode",
                "Comment",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for _mode, repeaters_list in repeaters.items():
                for repeater, _distance in repeaters_list:
                    writer.writerow(
                        {
                            "Name": repeater["callsign"],
                            "Frequency": repeater["frequency"],
                            "Duplex": (
                                repeater["offset"] if repeater["offset"] else "off"
                            ),
                            "Offset": (
                                repeater["offset_freq"]
                                if repeater["offset_freq"]
                                else "0.000000"
                            ),
                            "Tone": "Tone" if repeater["tone"] else "None",
                            "rToneFreq": (
                                repeater["tone"] if repeater["tone"] else "0.0"
                            ),
                            "cToneFreq": (
                                repeater["ctcss"] if repeater["ctcss"] else "0.0"
                            ),
                            "DtcsCode": "023",
                            "DtcsPolarity": "NN",
                            "MemoryMode": "M",
                            "Comment": "",
                        }
                    )

    @staticmethod
    def export(repeaters, filename, export_choice):
        if export_choice == "c":
            CSVExporter.save_to_chirp_csv(repeaters, filename)
        elif export_choice == "i":
            CSVExporter.save_to_icom_csv(repeaters, filename)
        elif export_choice == "y":
            CSVExporter.save_to_yaesu_csv(repeaters, filename)
