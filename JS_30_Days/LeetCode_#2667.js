var createHelloWorld = function() {
  // Return a function that returns "Hello World"
  return function() {
      return "Hello World";
  };
};

// Create a new function using createHelloWorld
const helloWorld = createHelloWorld();

// Call the returned function
console.log(helloWorld()); // Output: "Hello World"
