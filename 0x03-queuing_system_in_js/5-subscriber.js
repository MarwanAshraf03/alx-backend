import redis from "redis";
const client = redis.createClient({ url: "redis://localhost:6379" });
client.on("error", (err) => {
  console.log("Redis client not connected to the server: " + err);
});
client.on("connect", async () => {
  console.log("Redis client connected to the server");
});
client.subscribe("ALXchannel");
client.on("message", (channel, message) => {
  if (channel === "ALXchannel") {
    console.log(message);
    if (message === "KILL_SERVER") {
      client.unsubscribe();
      client.quit();
    }
  }
});
