import asyncio


async def greet(name: str):
    await asyncio.sleep(1)
    print(f"Hello, {name}!")


async def main():
    await asyncio.gather(greet("Alice"), greet("Bob"), greet("Charlie"))


asyncio.run(main())
