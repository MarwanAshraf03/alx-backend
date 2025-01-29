import kue from "kue";

const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
}
queue.process("push_notification_code", (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
//   const obj = {
//     phoneNumber,
//     message,
//   };
//   const push_notification_code = queue.create("push_notification_code", obj);
//   push_notification_code.save((err) => {
//     if (!err)
//       console.log(`Notification job created: ${push_notification_code.id}`);
//   });
//   push_notification_code.on("complete", () => {
//     console.log("Notification job completed");
//   });
//   push_notification_code.on("failed", () => {
//     console.log("Notification job failed");
//   });
// }

// const obj = {
//   phoneNumber: String,
//   message: String,
// };
// const push_notification_code = queue.create("push_notification_code", obj);
// push_notification_code.save((err) => {
//   if (!err)
//     console.log(`Notification job created: ${push_notification_code.id}`);
// });
// push_notification_code.on("complete", () => {
//   console.log("Notification job completed");
// });
// push_notification_code.on("failed", () => {
//   console.log("Notification job failed");
// });
