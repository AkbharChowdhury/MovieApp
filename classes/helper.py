class Helper:
    @staticmethod
    def calc_duration(minutes):
        h = minutes // 60
        m = minutes % 60
        return f"{h:01d}:{m:02d}"
