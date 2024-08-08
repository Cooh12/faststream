import asyncio
import multiprocessing

from faststream import FastStream
from faststream.rabbit import RabbitBroker


broker = RabbitBroker("amqp://admin:password@localhost:5672/")
app = FastStream(broker)


@broker.subscriber("queue")
async def handler(msg: str) -> None:
    print("Worker function is running in process:", multiprocessing.current_process())
    print(msg)


if __name__ == "__main__":
    asyncio.run(app.run(workers=2))
