import { json } from "express";
import redis from "redis";
import { promisify } from "util";

const client = redis.createClient({ url: "redis://localhost:6379" });
client.on("error", (err) => {
  console.log("Redis client not connected to the server: " + err);
});
client.on("connect", async () => {
  console.log("Redis client connected to the server");

  const delAsync = promisify(client.del).bind(client);
  const hgetallAsync = promisify(client.hgetall).bind(client);

  try {
    await delAsync("ALX");

    client.hset("ALX", "Portland", 50, redis.print);
    client.hset("ALX", "Seattle", 80, redis.print);
    client.hset("ALX", "New York", 20, redis.print);
    client.hset("ALX", "Bogota", 20, redis.print);
    client.hset("ALX", "Cali", 40, redis.print);
    client.hset("ALX", "Paris", 2, redis.print);

    const res = await hgetallAsync("ALX");
    console.log(res);
  } catch (err) {
    console.error(err);
  }
});
