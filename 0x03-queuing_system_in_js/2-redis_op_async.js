import redis from "redis";
import { promisify } from "util";

const client = redis.createClient({ url: "redis://localhost:6379" });
client.on("error", (err) => {
  console.log("Redis client not connected to the server: " + err);
});
client.on("connect", () => {
  console.log("Redis client connected to the server");
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    redis.print(`Reply: ${reply}`);
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    console.log(reply);
  });
}

const displaySchoolValuePromise = promisify(displaySchoolValue);

displaySchoolValuePromise("ALX")
  .then((result) => {
    console.log(result);
  })
  .catch((err) => {
    console.log(err);
  });
setNewSchool("ALXSanFrancisco", "100");
displaySchoolValuePromise("ALXSanFrancisco")
  .then((result) => {
    console.log(result);
  })
  .catch((err) => {
    console.log(err);
  });
