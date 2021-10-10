"use strict";
// Basic Types
let id = 5;
let company = "Dexter Co.";
let isPublished = true;
let x = "hello";
x = true;
let age;
age = 30;
// Array
let ids = [1, 2, 3, 4, 5];
let arr = [1, true, "Hello"];
// Tuple (must be in that particular order)
let person = [1, "Brad", true];
// Tuple Array
let employee;
employee = [
    [1, "Brad"],
    [2, "John"],
];
// Unions (for a variable to hold multiple types)
let pid = 22;
pid = "22";
// Enums (allow us to define a set of named constants, either numeric or string)
var Direction1;
(function (Direction1) {
    Direction1[Direction1["Up"] = 0] = "Up";
    Direction1[Direction1["Down"] = 1] = "Down";
    Direction1[Direction1["Left"] = 2] = "Left";
    Direction1[Direction1["Right"] = 3] = "Right";
})(Direction1 || (Direction1 = {}));
console.log(Direction1.Up);
var Direction2;
(function (Direction2) {
    Direction2["Up"] = "Up";
    Direction2["Down"] = "Down";
    Direction2["Left"] = "Left";
    Direction2["Right"] = "Right";
})(Direction2 || (Direction2 = {}));
// Objects ---------------------------------
const user = {
    id: 3,
    name: "John",
};
const newUser = {
    id: 1,
    name: "hehe",
};
// Type Assertions
let cid = 1;
// We want it to be of type 'number'
// let customerId = <number>cid; First waY
let customerId = cid;
// Functions ----------------------------------
function addNum(x, y) {
    return x + y;
}
// void-return type
function log(message) {
    console.log(message);
}
log("Hello, world!");
const user5 = {
    name: "Ram",
    id: 5,
};
const p1 = 3;
const add = (x, y) => x + y;
const sub = (a, b) => a - b;
// Classes -------------------------------------------------
class Person {
    constructor(id, name) {
        this.id = id;
        this.name = name;
    }
}
const satish = new Person(1, "Satish Adhikari");
const sandesh = new Person(2, "Sandesh Adhikari");
console.log(satish, sandesh);
