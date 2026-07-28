programming_dictionary = {
    "variable": "A storage location identified by a name that holds data.",
    "function": "A block of code that performs a specific task and can be called upon when needed.",
    "loop": "A control structure that repeats a block of code as long as a specified condition is true.",
    "conditional": "A statement that allows the program to make decisions based on certain conditions, typically using if, else, and elif statements.",
    "class": "A blueprint for creating objects that encapsulates data and behavior, allowing for object-oriented programming.",
    "inheritance": "A mechanism in object-oriented programming that allows a class to inherit properties and methods from another class, promoting code reuse and establishing a hierarchy.",
    "encapsulation": "The bundling of data and methods that operate on that data within a single unit, typically a class, to restrict direct access to some of the object's components and promote modularity."
}

print(programming_dictionary["class"]);

programming_dictionary["bug"]= "An error or flaw in a program that causes it to produce incorrect or unexpected results."
print(programming_dictionary);

programming_dictionary["bug"] = "A mistake in the code that prevents the program from running as expected."
print(programming_dictionary);

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])