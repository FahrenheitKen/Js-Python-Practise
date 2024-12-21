/*
const cityYouGrewIn = prompt("What's the name of the city you grew in?");
const nameOfYourPet = prompt("Whats the name of your pet ?");

const bandName = `Your Band Name could be ${cityYouGrewIn} ${nameOfYourPet}`;
console.log(bandName);



// Write a program in js that prints the number of characters in a user's name.

let username = prompt("Please enter your name :");
let nameLength = username.length;
console.log(nameLength);

 */
//
// Write a program that adds the digits in a 2 digit number. e.g.
// if the input was 35, then the output should be 3 + 5 = 8

// Warning. Do not change the code on lines 1-3.
// Your program should work for different inputs. e.g. any two-digit number.

//🚨 Don't change the code below 👇
const two_digit_number = prompt("Type a two digit number: ")
// 🚨 Don't change the code above 👆


/// Use "parseInt" is an inbuilt function that converts string representation of number to Interger
const firstInt = parseInt(two_digit_number[0]);
const secondInt = parseInt(two_digit_number[1]);

const output = firstInt + secondInt;
console.log(output);
