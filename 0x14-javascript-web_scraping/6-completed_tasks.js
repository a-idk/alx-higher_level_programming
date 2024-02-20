#!/usr/bin/node
// script that computes the number of tasks completed by user id
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error) {
    const taskList = JSON.parse(body);
    const compTask = {};
    taskList.forEach((todo) => {
      if (todo.completed && compTask[todo.userId] === undefined) {
        compTask[todo.userId] = 1;
      } else if (todo.completed) {
        compTask[todo.userId] = compTask[todo.userId] + 1;
      }
    });
    console.log(compTask);
  }
});
