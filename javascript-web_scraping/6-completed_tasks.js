#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) throw error;
  const usercompleted = {};
  const tasks = JSON.parse(body);
  const completed = tasks.filter(Task => Task.completed === true);
  for (const task of completed) {
    if (task.completed && usercompleted[task.userId] === undefined) {
      usercompleted[`${task.userId}`] = 0;
    }
    usercompleted[`${task.userId}`]++;
  }
  console.log(usercompleted);
});
