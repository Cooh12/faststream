import asyncio

from faststream.rabbit import RabbitBroker


async def main():
    async with RabbitBroker("amqp://admin:password@localhost:5672/") as broker:
        await broker.publish("message", "queue")

asyncio.run(main())
