/****************************************************************************************************************/
/* In-Class Exercises                                                                                           */
/****************************************************************************************************************/
/* 1. create an array called "fruits" and assign the values "Strawberry", "Raspberry", and "Apple" to it         */
// add code here
let fruits = ["Strawberry","Raspberry", "Apple"];
/* 2. add two more fruits to the "fruits" array using the correct array method                                   */
// add code here
fruits.push("Banana");
fruits.push("Kiwi");

/* 3. sort the fruits array alphabetically using the correct array method                                        */
// add code here
fruits.sort();
/* 4. create a function called printFruit that prints each item in the fruits array to the console              */
/*    and call the printFruit function                                                                          */
// add code here
function printFruit() {
    fruits.forEach((fruit) => console.log(fruit));
}
printFruit();
/* 5. create a fruit class that has three properties: name, color, and season and one method: printFruit()      */
/*    that prints all three properties of the fruit to the console. Then, create 3 fruit objects and print      */
/*    them using the printFruit() method                                                                        */
// add code here
class Fruit {
    constructor(newName, newColor, newSeason) {
        this.myName = newName;
        this.myColor = newColor;
        this.mySeason = newSeason; 
    }

    printFruit() {
        console.log(this.myName);
        console.log(this.myColor);
        console.log(this.mySeason);
    }
}

const apple = new Fruit("Apple", "Red", "Fall");
const banana = new Fruit("Banana", "Yellow", "Summer");
const orange = new Fruit("Orange", "Orange", "Spring");

apple.printFruit();
banana.printFruit();
orange.printFruit();
/****************************************************************************************************************/
/* In-Class Lab                                                                                                 */
/****************************************************************************************************************/
/* 1. Write a function that asks the user if they want to say hi. If the user selects "Okay" (true), then       */
/*    display a welcome message. If the user selects "Cancel" (false), then display a different message         */
function areYouSure() {
    let result = confirm("Do You Want to Say Hi?");
    let element = document.getElementById("welcome");

    if(result) {
        element.innerHTML = "HELLO :)"
    } else {
        element.innerHTML = "Damn :("
    }
}

/* 2. Write a function to change 3 styles on the webpage                                                        */
function changeStyle() {
    let welcomeElement = document.getElementById("welcome");
    let buttonElements = document.getElementsByTagName("button");
    let bodyElement = document.getElementsByTagName("body")[0];

    // update welcome text color
    welcomeElement.style.color = "blue";

    // update all button colors
    for (let i = 0; i < buttonElements.length; i++) {
        buttonElements[i].style.backgroundColor = "green";
    }

    // upd the body background
    bodyElement.style.backgroundColor = "black";
}
