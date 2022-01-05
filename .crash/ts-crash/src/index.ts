// Basic Types
let id: number = 5;
let company: string = "Dexter Co.";

let isPublished: boolean = true;

let x: any = "hello";
x = true;

let age: number;
age = 30;

// Array
let ids: number[] = [1, 2, 3, 4, 5];
let arr: any[] = [1, true, "Hello"];

// Tuple (must be in that particular order)
let person: [number, string, boolean] = [1, "Brad", true];

// Tuple Array
let employee: [number, string][];
employee = [
  [1, "Brad"],
  [2, "John"],
];

// Unions (for a variable to hold multiple types)
let pid: string | number = 22;
pid = "22";

// Enums (allow us to define a set of named constants, either numeric or string)
enum Direction1 {
  Up,
  Down,
  Left,
  Right,
}

console.log(Direction1.Up);

enum Direction2 {
  Up = "Up",
  Down = "Down",
  Left = "Left",
  Right = "Right",
}

// Objects ---------------------------------
const user: { id: number; name: string } = {
  id: 3,
  name: "John",
};

// Looks messy, this way!
type NewUser = {
  id: number;
  name: string;
};

const newUser: NewUser = {
  id: 1,
  name: "hehe",
};

// Type Assertions
let cid: any = 1;
// We want it to be of type 'number'
// let customerId = <number>cid; First waY
let customerId = cid as number;

// Functions ----------------------------------

function addNum(x: number, y: number): number {
  return x + y;
}

// void-return type
function log(message: string | number): void {
  console.log(message);
}
log("Hello, world!");

// Interfaces (custom types/ special structure for an object/ a function)
// similar to "type"
interface UserInterface {
  readonly id: number;
  name: string;
  age?: number;
}

const user5: UserInterface = {
  name: "Ram",
  id: 5,
};

// user5.id = 8;
// You can have "optional" && "readonly" props

// Differences between "type" && "interface"
// You cannot use "interface" with Primitives & Unions. Otherwise, use Interface as a preference.
// e.g.

type Point = number | string;
const p1: Point = 3;

// I cannot interface a union!
// But for objects, I prefer "interface"

// Interfaces with Functions ------------------------------
interface MathFunc {
  (x: number, y: number): number;
}

const add: MathFunc = (x: number, y: number): number => x + y;
const sub: MathFunc = (a, b) => a - b;

// Classes -------------------------------------------------

class Person {
  private id: number;
  name: string;

  constructor(id: number, name: string) {
    this.id = id;
    this.name = name;
  }
}

const satish = new Person(1, "Satish Adhikari");
const sandesh = new Person(2, "Sandesh Adhikari");

console.log(satish.id, sandesh);
