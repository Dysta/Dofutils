from enum import IntEnum


class Race(IntEnum):
    FECA = 1
    OSAMODAS = 2
    ENUTROF = 3
    SRAM = 4
    XELOR = 5
    ECAFLIP = 6
    ENIRIPSA = 7
    IOP = 8
    CRA = 9
    SADIDA = 10
    SACRIEUR = 11
    PANDAWA = 12

    @staticmethod
    def by_id(race_id: int) -> "Race":
        """
        Get the character race by its id

        :param race_id: The race id
        :return: The race object
        :rtype: Race
        """
        if not race_id in list(map(int, Race)):
            raise ValueError(f"Incorrect parameter {race_id}, must be between 1 and 12")

        return Race(race_id)
