# __enter__() - start or open
#
# __exit__() - end or exception
import asyncio

v1 = [1, 2, 3]
v2 = [2, 3, 1]

class VectorChanger:
    def __init__(self, vector):
        self.__vector = vector

    def __enter__(self):
        self.__temp = self.__vector
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__vector[:] = self.__temp

        return False

with VectorChanger(v1) as dv:
    for i, a in enumerate(dv):
        dv[i] += v2[i]
    print(v1)


class AsyncVectorChanger:
    def __init__(self, vector):
        self.__vector = vector

    async def __aenter__(self):
        self.__temp = self.__vector
        return await self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__vector[:] = self.__temp

        return False
