import redis from "redis";
const client = redis.createClient({ url: "redis://localhost:6379" });
client.on("error", (err) => {
  console.log("Redis client not connected to the server: " + err);
});
client.on("connect", async () => {
  console.log("Redis client connected to the server");
});
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish("ALXchannel", message);
  }, time);
}
publishMessage("ALX Student #1 starts course", 100);
publishMessage("ALX Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("ALX Student #3 starts course", 400);
