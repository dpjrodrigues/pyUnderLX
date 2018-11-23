import asyncio
import aiohttp

from pyUnderLX import Occurrences, UnderLX

async def main():
    async with aiohttp.ClientSession() as session:
        occurrences = await Occurrences.get(session)

        print("Occurrences:")
        for occurrence in await occurrences.full_list():
            print(occurrence)


        print("Occurrences per MetroLine:")
        for metroLine in await occurrences.split_per_metroLine():
            print(metroLine)

        print("Occurrences in Linha Azul:")
        metroLineOccurrences = await occurrences.occurrences_in_metroLine('pt-ml-azul')
        for metroLine_occurrences in metroLineOccurrences.occurrences:
            print(metroLine_occurrences)
        print("Number of occurrences in Linha Azul: ",await occurrences.number_of_occurrences('pt-ml-azul'))

        #print("Status of occurrence 9bdea6f4-6757-4999-9a57-25f9ee22e93a:")
        #occurrences_status = await occurrences.occurrence_status('9bdea6f4-6757-4999-9a57-25f9ee22e93a')
        #print(occurrences_status)

asyncio.get_event_loop().run_until_complete(main())


